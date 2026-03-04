"""Unified entry point for all puzzle solvers."""

import sys
import os
import argparse
import copy
from typing import Any

import yaml
import torch
from utils.decomposer import Agent
from utils.fallback import FailedPrediction
import wandb
import matplotlib.pyplot as plt  # noqa: F401
import json
from datetime import datetime

# Add src to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def create_game(config: dict[str, Any]) -> Any:
    """Factory: instantiate the right game environment from config."""
    game_name = config["game"]
    if game_name == "tower_of_hanoi":
        from tower_of_hanoi.enviroment import TowerOfHanoi

        return TowerOfHanoi(num_disks=config["num_disks"])
    elif game_name == "sliding_puzzle":
        from sliding_puzzle.enviroment import SlidingPuzzle

        return SlidingPuzzle(initial_state=config["initial_state"])
    elif game_name == "nonogram":
        from nonogram.enviroment import Nonogram

        return Nonogram.from_config(
            row_hints=config["row_hints"],
            col_hints=config["col_hints"],
            initial_state=config.get("initial_state"),
        )
    else:
        raise ValueError(f"Unknown game: {game_name}")


def create_agent(config: dict[str, Any], game: Any, device: str) -> Agent:
    """Factory: instantiate the right agent from config."""
    from utils.decomposer import Agent

    game_name = config["game"]
    if game_name == "tower_of_hanoi":
        from tower_of_hanoi import prompts
    elif game_name == "sliding_puzzle":
        from sliding_puzzle import prompts
    elif game_name == "nonogram":
        from nonogram import prompts
    else:
        raise ValueError(f"Unknown game: {game_name}")
    return Agent(environment=game, prompts_module=prompts, device=device)


def load_config(args: argparse.Namespace) -> dict[str, Any]:
    """Load YAML config, then apply CLI overrides."""
    config_path = args.config
    if config_path is None:
        config_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "config", f"{args.game}.yaml"
        )

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    # CLI overrides
    if args.margin_k is not None:
        config["margin_k"] = args.margin_k
    if args.max_steps is not None:
        config["max_steps"] = args.max_steps
    if args.max_agents_per_step is not None:
        config["max_agents_per_step"] = args.max_agents_per_step

    # Defaults for fallback config keys
    config.setdefault("max_fallback_retries", 3)
    config.setdefault("fallback_api", "gemini")
    config.setdefault("gemini_model", "gemini-2.5-flash")

    return config


def freeze_for_vote(value: Any) -> Any:
    """Convert nested lists/dicts into hashable structures for voting keys."""
    if isinstance(value, list):
        return tuple(freeze_for_vote(v) for v in value)
    if isinstance(value, tuple):
        return tuple(freeze_for_vote(v) for v in value)
    if isinstance(value, dict):
        return tuple(sorted((k, freeze_for_vote(v)) for k, v in value.items()))
    return value


def validate_prediction_consistency(
    agent: Agent,
    current_state: Any,
    action: Any,
    predicted_state: Any,
) -> None:
    """
    Enforce MAKER-style consistency:
    the returned next_state must exactly match the state obtained
    by applying the returned action to the current state.
    """
    temp_env = copy.deepcopy(agent.environment)
    expected_current_state = temp_env.get_state()

    if expected_current_state != current_state:
        raise ValueError(
            "Internal state mismatch: copied environment state differs from current_state."
        )

    temp_env.apply_move(action)
    expected_next_state = temp_env.get_state()

    if expected_next_state != predicted_state:
        raise ValueError(
            "Inconsistent prediction: next_state does not match current_state + move."
        )


def get_top_two_counts(vote_counts: dict[Any, int]) -> tuple[int, int]:
    """Return (best_count, second_best_count)."""
    counts = sorted(vote_counts.values(), reverse=True)
    best = counts[0] if counts else 0
    second = counts[1] if len(counts) > 1 else 0
    return best, second


def has_consensus(vote_counts: dict[Any, int], margin_k: int) -> bool:
    """
    True iff the top candidate is ahead by at least margin_k votes.
    MAKER-style rule: do not accept a candidate before the margin is met.
    """
    if not vote_counts:
        return False
    best, second = get_top_two_counts(vote_counts)
    return (best - second) >= margin_k


def get_best_candidate(
    vote_counts: dict[Any, int],
    candidate_lookup: dict[Any, dict[str, Any]],
) -> dict[str, Any] | None:
    """Return the currently leading candidate, if any."""
    if not vote_counts:
        return None
    best_key = max(vote_counts.items(), key=lambda x: x[1])[0]
    return candidate_lookup[best_key]


def run_voting_batch(
    agent: Agent,
    previous_move: str,
    current_state: Any,
    current_step: int,
    batch_size: int,
    margin_k: int,
    max_agents_total: int,
    system_prompt_override: str | None = None,
    user_prompt_override: str | None = None,
    predictions_table: wandb.Table | None = None,
) -> tuple[dict[str, int], dict[str, Any] | None, list[FailedPrediction], bool]:
    """
    Run a batch of agents and tally votes.

    Returns:
        (
            candidate_voting_as_strings,
            best_prediction_or_none,
            failed_predictions,
            consensus_reached,
        )

    Voting is done over the full (action, next_state) candidate,
    not just over the action alone.
    """
    candidate_voting: dict[Any, int] = {}
    candidate_lookup: dict[Any, dict[str, Any]] = {}
    failed_predictions: list[FailedPrediction] = []

    # Build batch prompts — always include current game state via build_prompt()
    batch_messages = []

    # Pre-calculate visual state if needed for formatting
    state_visual = str(current_state)
    if hasattr(agent.prompts, "_visualize_state"):
        state_visual = agent.prompts._visualize_state(current_state)
    elif hasattr(agent.environment, "visualize"):
        state_visual = agent.environment.visualize()

    for _ in range(batch_size):
        messages, _user_prompt = agent.build_prompt(
            previous_move, current_state, current_step
        )
        if system_prompt_override:
            messages[0]["content"] = system_prompt_override

        if user_prompt_override:
            if "{current_state}" in user_prompt_override:
                try:
                    formatted_prompt = user_prompt_override.format(
                    current_state=current_state,
                    previous_move=previous_move,
                    state_visual=state_visual,
                    current_step=current_step,
                    )
                    messages[1]["content"] = formatted_prompt
                except KeyError as e:
                    print(f"Warning: Failed to format fallback prompt: {e}")
                    messages[1]["content"] = (
                        user_prompt_override + "\n\n" + messages[1]["content"]
                    )
            else:
                messages[1]["content"] = (
                    user_prompt_override + "\n\n" + messages[1]["content"]
                )
        batch_messages.append(messages)

    # Batch inference (MAKER-style): first vote deterministic (tau=0), remaining votes sampled (tau=0.1)
    responses = []
    first_messages = batch_messages[:1]
    rest_messages = batch_messages[1:]
    if first_messages:
        responses.extend(
            agent.llm.generate_batch(first_messages, do_sample=False, temperature=0.0)
        )
    if rest_messages:
        responses.extend(
            agent.llm.generate_batch(
                rest_messages, do_sample=True, temperature=0.1, top_p=0.95
            )
        )

    def process_prediction(
        response_content: str, agent_num: int
    ) -> None:
        action: Any = "None"
        parsed_state: Any = "None"
        error = "None"

        try:
            action, parsed_state = agent.parse_response(
                response_content, current_state, current_step, agent_num
            )

            if isinstance(action, list):
                action = tuple(action)

            validate_prediction_consistency(
                agent=agent,
                current_state=current_state,
                action=action,
                predicted_state=parsed_state,
            )

            candidate_key = (
                freeze_for_vote(action),
                freeze_for_vote(parsed_state),
            )
            candidate_voting[candidate_key] = candidate_voting.get(candidate_key, 0) + 1
            candidate_lookup[candidate_key] = {
                "action": action,
                "state": parsed_state,
            }

            print(
                f"Agent {agent_num} predicted move: {action}, resulting state: {parsed_state}"
            )
        except ValueError as e:
            error = str(e)
            print(f"Agent {agent_num} error: {e}")
            failed_predictions.append(
                {
                    "agent_id": f"{current_step}:{agent_num}",
                    "action": action,
                    "state": parsed_state,
                    "error": error,
                }
            )

        if predictions_table is not None:
            predictions_table.add_data(
                current_step,
                agent_num,
                str(current_state),
                str(action),
                str(parsed_state),
                error,
            )

    # Parse each response and tally votes
    for i, response in enumerate(responses):
        agent_num = i + 1
        content = response[-1]["content"]
        process_prediction(content, agent_num)

    agents_so_far = batch_size

    # If margin not met, run additional single agents until it is or until max_agents_total is reached
    while (
        candidate_voting
        and not has_consensus(candidate_voting, margin_k)
        and agents_so_far < max_agents_total
    ):
        agents_so_far += 1
        try:
            action, parsed_state = agent.execute_decompose_prompt(
                previous_move,
                current_state,
                step=current_step,
                agent_num=agents_so_far,
                temperature=0.1,
                do_sample=True,
                top_p=0.95,
            )

            if isinstance(action, list):
                action = tuple(action)

            validate_prediction_consistency(
                agent=agent,
                current_state=current_state,
                action=action,
                predicted_state=parsed_state,
            )

            candidate_key = (
                freeze_for_vote(action),
                freeze_for_vote(parsed_state),
            )
            candidate_voting[candidate_key] = candidate_voting.get(candidate_key, 0) + 1
            candidate_lookup[candidate_key] = {
                "action": action,
                "state": parsed_state,
            }

            print(
                f"Agent {agents_so_far} predicted move: {action}, resulting state: {parsed_state}"
            )

            if predictions_table is not None:
                predictions_table.add_data(
                    current_step,
                    agents_so_far,
                    str(current_state),
                    str(action),
                    str(parsed_state),
                    "None",
                )
        except ValueError as e:
            print(f"Agent {agents_so_far} error: {e}")
            failed_predictions.append(
                {
                    "agent_id": f"{current_step}:{agents_so_far}",
                    "action": "None",
                    "state": "None",
                    "error": str(e),
                }
            )
            if predictions_table is not None:
                predictions_table.add_data(
                    current_step,
                    agents_so_far,
                    str(current_state),
                    "None",
                    "None",
                    str(e),
                )
            continue

    consensus_reached = has_consensus(candidate_voting, margin_k)
    best_prediction = (
        get_best_candidate(candidate_voting, candidate_lookup)
        if consensus_reached
        else None
    )

    candidate_voting_as_strings = {
        str(candidate_lookup[key]): count for key, count in candidate_voting.items()
    }

    return (
        candidate_voting_as_strings,
        best_prediction,
        failed_predictions,
        consensus_reached,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="MAKER framework puzzle solver")
    parser.add_argument(
        "--game",
        required=True,
        choices=["tower_of_hanoi", "sliding_puzzle", "nonogram"],
        help="Which puzzle to solve",
    )
    parser.add_argument("--config", default=None, help="Path to YAML config file")
    parser.add_argument(
        "--margin_k", type=int, default=None, help="Vote margin for consensus"
    )
    parser.add_argument(
        "--max_steps", type=int, default=None, help="Maximum solver steps"
    )
    parser.add_argument(
        "--max_agents_per_step", type=int, default=None, help="Max agents per step"
    )
    args = parser.parse_args()

    config = load_config(args)

    # Initialize WandB
    wandb.init(project="lecture-agi", config=config)

    margin_k = config["margin_k"]
    max_steps = config["max_steps"]
    max_number_agents_per_step = config["max_agents_per_step"]
    max_fallback_retries = config["max_fallback_retries"]
    output_dir = config.get("output_dir", "output")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Clean up old logs
    for filename in ["failures.csv", "debug_prompts.md", "log.csv"]:
        path = os.path.join(output_dir, filename)
        if os.path.exists(path):
            os.remove(path)

    if torch.cuda.is_available():
        device = "cuda"
    elif torch.backends.mps.is_available():
        device = "mps"
    else:
        device = "cpu"

    game = create_game(config)
    agent = create_agent(config, game, device)

    # Initialize fallback model (lazy — won't load weights until needed)
    from utils.fallback import FallbackModel

    fallback: FallbackModel = FallbackModel(config, device=device)

    # WandB predictions table
    predictions_table = wandb.Table(
        columns=[
            "step",
            "agent_num",
            "current_state",
            "predicted_action",
            "predicted_state",
            "error",
        ]
    )

    print("Initial State:", game.get_state())
    wandb.log({"initial_state": str(game.get_state())})

    if hasattr(game, "visualize"):
        print("Visual:")
        print(game.visualize())

    previous_move = "None"
    current_step = 0
    game_history = []

    while not game.is_solved() and current_step < max_steps:
        current_state = copy.deepcopy(game.get_state())
        current_step += 1

        candidate_voting, best_prediction, failed_predictions, consensus_reached = (
            run_voting_batch(
                agent,
                previous_move,
                current_state,
                current_step,
                batch_size=max_number_agents_per_step,
                margin_k=margin_k,
                max_agents_total=max_number_agents_per_step,
                predictions_table=predictions_table,
            )
        )

        step_data = {
            "step": current_step,
            "current_state": str(current_state),
            "processed_state": str(game.get_state())
            if hasattr(game, "get_state")
            else str(current_state),
            "candidate_votes": candidate_voting,
            "best_action": str(best_prediction["action"]) if best_prediction else "None",
            "best_state": str(best_prediction["state"]) if best_prediction else "None",
            "consensus_reached": consensus_reached,
            "failed_predictions": [
                {
                    "agent_id": f.get("agent_id"),
                    "action": str(f.get("action")),
                    "state": str(f.get("state")),
                    "error": f.get("error"),
                }
                for f in failed_predictions
            ],
        }
        game_history.append(step_data)

        if consensus_reached and best_prediction is not None:
            game.apply_move(best_prediction["action"])
        else:
            print(
                f"No valid consensus at step {current_step}. Engaging fallback..."
            )
            fallback_retry = 0

            while (
                fallback_retry < max_fallback_retries
                and not (consensus_reached and best_prediction is not None)
            ):
                fallback_retry += 1
                print(f"Fallback retry {fallback_retry}/{max_fallback_retries}")

                _messages, user_prompt = agent.build_prompt(
                    previous_move, current_state, current_step
                )
                new_sys, new_usr = fallback.update_compose(
                    agent.system_prompt,
                    user_prompt,
                    failed_predictions,
                    step=current_step,
                    retry=fallback_retry,
                )

                candidate_voting, best_prediction, failed_predictions, consensus_reached = (
                    run_voting_batch(
                        agent,
                        previous_move,
                        current_state,
                        current_step,
                        batch_size=max_number_agents_per_step,
                        margin_k=margin_k,
                        max_agents_total=max_number_agents_per_step,
                        system_prompt_override=new_sys,
                        user_prompt_override=new_usr,
                        predictions_table=predictions_table,
                    )
                )

            if consensus_reached and best_prediction is not None:
                game.apply_move(best_prediction["action"])
            else:
                print("Fallback exhausted. No valid consensus move found.")
                break

        previous_move = (
            str(best_prediction["action"]) if best_prediction is not None else "None"
        )

        print(f"\nStep {current_step} - Current State:", game.get_state())
        if hasattr(game, "visualize"):
            print("Visual:")
            print(game.visualize())
        print()

    if game.is_solved():
        print(f"\nPuzzle solved in {current_step} steps!")
    else:
        print(f"\nMax steps ({max_steps}) reached without solving.")

    # Log final metrics to WandB
    wandb.log({"predictions": predictions_table})
    wandb.log({"total_steps": current_step, "solved": game.is_solved()})

    # Save custom log files
    wandb.save(os.path.join(output_dir, "failures.csv"))
    wandb.save(os.path.join(output_dir, "debug_prompts.md"))

    # Save detailed JSON log for visualization
    experiments_dir = os.path.join(output_dir, "experiments")
    if not os.path.exists(experiments_dir):
        os.makedirs(experiments_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_filename = f"experiment_{timestamp}_{config['game']}.json"
    json_path = os.path.join(experiments_dir, json_filename)

    # Wrap game_history with metadata for webapp
    experiment_data = {"game_type": config["game"], "steps": game_history}

    with open(json_path, "w") as f:
        json.dump(experiment_data, f, indent=2)

    print(f"Experiment log saved to: {json_path}")

    wandb.finish()


if __name__ == "__main__":
    main()



"""
- Fix: margin_k is now enforced strictly, so no move is applied before real consensus is reached.
- Fix: The LLM-provided next_state is now actually validated and must match the state resulting from applying the predicted move; it is no longer just parsed and ignored
- Fix: Fix: The fallback is now triggered not only when all predictions fail, but also when valid candidates exist without reaching consensus.

"""