"""Unified entry point for all puzzle solvers."""

import sys
import os
import argparse
import heapq
from typing import Any

import yaml
import torch
from utils.decomposer import Agent
from utils.fallback import FailedPrediction
import wandb
import weave
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
    else:
        raise ValueError(f"Unknown game: {game_name}")
    return Agent(environment=game, prompts_module=prompts, device=device, config=config)


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


@weave.op()
def run_voting_batch(
    agent: Agent,
    previous_move: str,
    current_state: Any,
    current_step: int,
    batch_size: int,
    margin_k: int,
    system_prompt_override: str | None = None,
    user_prompt_override: str | None = None,
    predictions_table: wandb.Table | None = None,
) -> tuple[dict[Any, int], Any | None, list[FailedPrediction]]:
    """Run a batch of agents and tally votes. Returns (action_voting, best_action, failed_predictions)."""
    action_voting: dict[Any, int] = {}
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
            # Check if override is a template with placeholders
            if "{current_state}" in user_prompt_override:
                try:
                    formatted_prompt = user_prompt_override.format(
                        current_state=current_state,
                        previous_move=previous_move,
                        state_visual=state_visual,
                    )
                    messages[1]["content"] = formatted_prompt
                except KeyError as e:
                    print(f"Warning: Failed to format fallback prompt: {e}")
                    # Fallback to prepending if formatting fails
                    messages[1]["content"] = (
                        user_prompt_override + "\n\n" + messages[1]["content"]
                    )
            else:
                # Prepend fallback guidance to the state-specific user prompt
                messages[1]["content"] = (
                    user_prompt_override + "\n\n" + messages[1]["content"]
                )
        batch_messages.append(messages)

    # Batch inference
    responses = agent.llm.generate_batch(batch_messages)

    # Parse each response and tally votes
    for i, response in enumerate(responses):
        agent_num = i + 1
        content = response[-1]["content"]
        action = "None"
        parsed_state = "None"
        error = "None"

        try:
            action, parsed_state = agent.parse_response(
                content, current_state, current_step, agent_num
            )
            if isinstance(action, list):
                action = tuple(action)
            print(
                f"Agent {agent_num} predicted move: {action}, resulting state: {parsed_state}"
            )
            action_voting[action] = action_voting.get(action, 0) + 1
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

        # Log to WandB predictions table
        if predictions_table is not None:
            predictions_table.add_data(
                current_step,
                agent_num,
                str(current_state),
                str(action),
                str(parsed_state),
                error,
            )

    best_action = None
    if action_voting:
        top_two = heapq.nlargest(2, action_voting.items(), key=lambda x: x[1])
        best_action = top_two[0][0]
        best_value = top_two[0][1]
        second_best_value = top_two[1][1] if len(top_two) > 1 else 0

        # If margin not met, run additional single agents until it is
        agents_so_far = batch_size
        while (
            best_value < second_best_value + margin_k
            and agents_so_far < batch_size * 3  # cap additional agents
        ):
            agents_so_far += 1
            try:
                action, state = agent.execute_decompose_prompt(
                    previous_move,
                    current_state,
                    step=current_step,
                    agent_num=agents_so_far,
                )
                if isinstance(action, list):
                    action = tuple(action)
                print(
                    f"Agent {agents_so_far} predicted move: {action}, resulting state: {state}"
                )
                action_voting[action] = action_voting.get(action, 0) + 1

                top_two = heapq.nlargest(2, action_voting.items(), key=lambda x: x[1])
                best_action, best_value = top_two[0]
                second_best_value = top_two[1][1] if len(top_two) > 1 else 0

                if predictions_table is not None:
                    predictions_table.add_data(
                        current_step,
                        agents_so_far,
                        str(current_state),
                        str(action),
                        str(state),
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
                continue

    return action_voting, best_action, failed_predictions


def main() -> None:
    parser = argparse.ArgumentParser(description="MAKER framework puzzle solver")
    parser.add_argument(
        "--game",
        required=True,
        choices=["tower_of_hanoi", "sliding_puzzle"],
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

    # Initialize WandB + Weave
    wandb.init(project="lecture-agi", config=config)
    weave.init("lecture-agi")

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

    if config.get("llm_backend") == "ollama":
        device = "cpu"
    elif torch.cuda.is_available():
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
        current_state = game.get_state()
        current_step += 1

        # Batch voting: run max_agents_per_step agents in one batch
        action_voting, best_action, failed_predictions = run_voting_batch(
            agent,
            previous_move,
            current_state,
            current_step,
            batch_size=max_number_agents_per_step,
            margin_k=margin_k,
            predictions_table=predictions_table,
        )

        step_data = {
            "step": current_step,
            "current_state": str(current_state),
            "processed_state": str(game.get_state())
            if hasattr(game, "get_state")
            else str(current_state),
            "agent_votes": {str(k): v for k, v in action_voting.items()},
            "best_action": str(best_action),
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

        if action_voting:
            game.apply_move(best_action)
        else:
            # MASTER FALLBACK: all agents failed
            print(f"All agents failed at step {current_step}. Engaging fallback...")
            fallback_retry = 0
            while fallback_retry < max_fallback_retries and not action_voting:
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

                # Retry voting with updated prompts
                action_voting, best_action, failed_predictions = run_voting_batch(
                    agent,
                    previous_move,
                    current_state,
                    current_step,
                    batch_size=max_number_agents_per_step,
                    margin_k=margin_k,
                    system_prompt_override=new_sys,
                    user_prompt_override=new_usr,
                    predictions_table=predictions_table,
                )

            if action_voting:
                game.apply_move(best_action)
            else:
                print("Fallback exhausted. No valid move found.")
                break

        previous_move = str(best_action)
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
    experiment_data = {
        "game_type": config['game'],
        "steps": game_history
    }

    with open(json_path, "w") as f:
        json.dump(experiment_data, f, indent=2)

    print(f"Experiment log saved to: {json_path}")

    wandb.finish()


if __name__ == "__main__":
    main()
