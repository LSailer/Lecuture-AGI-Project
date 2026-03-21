import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import argparse
import copy
import subprocess
from pathlib import Path
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
    elif game_name == "rubiks_cube":
        from rubiks_cube.enviroment import RubiksCube

        return RubiksCube.from_config(
            scramble=config.get("scramble"),
            forbid_undo=config.get("forbid_undo", True),
            max_score_drop=config.get("max_score_drop", 3),
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
    elif game_name == "rubiks_cube":
        from rubiks_cube import prompts
    else:
        raise ValueError(f"Unknown game: {game_name}")
    model_path = config.get("model_path", "LLM/model")
    prompt_variant = config.get("prompt_variant", "base")
    return Agent(environment=game, prompts_module=prompts, device=device, model_path=model_path, prompt_variant=prompt_variant)


def _cancel_sibling_jobs() -> None:
    """Read active experiment job IDs and scancel them all."""
    repo_root = Path(__file__).resolve().parent.parent
    ids_file = repo_root / "logs" / "active_experiment_ids.txt"
    if not ids_file.exists():
        print("No active_experiment_ids.txt found, skipping scancel (likely local dev).")
        return
    job_ids = [line.strip() for line in ids_file.read_text().splitlines() if line.strip()]
    print(f"Cancelling {len(job_ids)} sibling jobs: {job_ids}")
    for jid in job_ids:
        subprocess.run(["scancel", jid], check=False)


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
    if args.temperature is not None:
        config["temperature"] = args.temperature
    if args.num_disks is not None:
        config["num_disks"] = args.num_disks
    if args.max_state_revisits is not None:
        config["max_state_revisits"] = args.max_state_revisits
    if args.temp_escalation:
        config["temp_escalation"] = True
    if args.model_path is not None:
        config["model_path"] = args.model_path
    if args.prompt_variant is not None:
        config["prompt_variant"] = args.prompt_variant

    # Defaults
    config.setdefault("temp_escalation", False)
    config.setdefault("max_state_revisits", 3)
    config.setdefault("max_fallback_retries", 3)
    config.setdefault("model_path", "LLM/model")
    config.setdefault("prompt_variant", "base")
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
    Voting is over full candidates: (action, next_state).
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


class SafeFormatDict(dict):
    """Leave unknown placeholders unchanged instead of failing formatting."""

    def __missing__(self, key: str) -> str:
        return "{" + key + "}"


def log_actual_llm_prompt(
    step: int,
    system_prompt: str,
    user_prompt: str,
    mode: str,
) -> None:
    """Log the actual prompt sent to the LLM once per step and mode."""
    os.makedirs("output", exist_ok=True)
    debug_path = os.path.join("output", "debug_prompts.md")

    with open(debug_path, "a", encoding="utf-8") as f:
        f.write(f"\n## Actual LLM Prompt at Step {step} ({mode})\n\n")
        f.write("### System Prompt\n")
        f.write(system_prompt)
        f.write("\n\n### User Prompt\n")
        f.write(user_prompt)
        f.write("\n\n---\n")


@weave.op()
def _build_batch_messages(
    agent: Agent,
    previous_move: str,
    current_state: Any,
    current_step: int,
    count: int,
    system_prompt_override: str | None = None,
    user_prompt_override: str | None = None,
) -> list:
    """Build `count` prompt message lists for batch inference."""
    state_visual = str(current_state)
    if hasattr(agent.prompts, "_visualize_state"):
        state_visual = agent.prompts._visualize_state(current_state)
    elif hasattr(agent.environment, "visualize"):
        state_visual = agent.environment.visualize()

    batch_messages = []
    logged_this_step = False

    for _ in range(count):
        messages, _user_prompt = agent.build_prompt(
            previous_move, current_state, current_step
        )

        if system_prompt_override:
            messages[0]["content"] = system_prompt_override
        if user_prompt_override:
            if "{" in user_prompt_override:
                try:
                    format_values: dict[str, Any] = {
                        "current_state": current_state,
                        "previous_move": previous_move,
                        "state_visual": state_visual,
                        "current_step": current_step,
                    }

                    if hasattr(agent.environment, "row_hints"):
                        format_values["row_hints"] = agent.environment.row_hints
                    if hasattr(agent.environment, "col_hints"):
                        format_values["col_hints"] = agent.environment.col_hints
                        format_values["column_hints"] = agent.environment.col_hints
                    if hasattr(agent.environment, "n_rows"):
                        format_values["n_rows"] = agent.environment.n_rows
                    if hasattr(agent.environment, "n_cols"):
                        format_values["n_cols"] = agent.environment.n_cols
                    if hasattr(agent.environment, "row_hints"):
                        allowed_cells = [
                            (r, c)
                            for r, row in enumerate(current_state)
                            for c, v in enumerate(row)
                            if v == -1
                        ]
                        format_values["allowed_cells"] = (
                            allowed_cells
                            if len(allowed_cells) <= 80
                            else allowed_cells[:80] + ["..."]
                        )

                    formatted_prompt = user_prompt_override.format_map(
                        SafeFormatDict(format_values)
                    )
                    messages[1]["content"] = formatted_prompt
                except Exception as e:
                    print(f"Warning: Failed to format fallback prompt: {e}")
                    messages[1]["content"] = (
                        user_prompt_override + "\n\n" + messages[1]["content"]
                    )
            else:
                messages[1]["content"] = (
                    user_prompt_override + "\n\n" + messages[1]["content"]
                )

        if not logged_this_step:
            mode = "fallback" if (system_prompt_override or user_prompt_override) else "default"
            log_actual_llm_prompt(
                step=current_step,
                system_prompt=messages[0]["content"],
                user_prompt=messages[1]["content"],
                mode=mode,
            )
            logged_this_step = True

        batch_messages.append(messages)
    return batch_messages

    return batch_messages


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
) -> tuple[dict[str, int], dict[str, Any] | None, list[FailedPrediction], bool]:
    """
    Run agents, vote over full candidates (action + next_state),
    and only return a best prediction if margin_k is actually met.
    """
    candidate_voting: dict[Any, int] = {}
    candidate_lookup: dict[Any, dict[str, Any]] = {}
    failed_predictions: list[FailedPrediction] = []

    agents_so_far = 0
    max_agents_total = batch_size * 3

    def process_response(response_content: str, agent_num: int) -> None:
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
                current_step, agent_num, str(current_state),
                str(action), str(parsed_state), error,
            )

    # Initial batch
    batch_messages = _build_batch_messages(
        agent,
        previous_move,
        current_state,
        current_step,
        batch_size,
        system_prompt_override,
        user_prompt_override,
    )

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

    for i, response in enumerate(responses):
        agent_num = i + 1
        content = response[-1]["content"]
        process_response(content, agent_num)

    agents_so_far = batch_size

    # Additional agents until consensus or cap
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


def _run_fallback_loop(
    agent: Any,
    fallback: Any,
    previous_move: str,
    current_state: Any,
    current_step: int,
    max_fallback_retries: int,
    max_number_agents_per_step: int,
    margin_k: int,
    failed_predictions: list[dict[str, str]],
    predictions_table: Any,
) -> tuple[dict[Any, int], dict[str, Any] | None, list[dict[str, str]], bool, int]:
    """Run fallback retry loop. Returns (candidate_voting, best_prediction, failed_predictions, consensus_reached, fallback_retries_used)."""
    candidate_voting: dict[Any, int] = {}
    best_prediction: dict[str, Any] | None = None
    consensus_reached = False
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
        state_visual = str(current_state)
        if hasattr(agent.prompts, "_visualize_state"):
            state_visual = agent.prompts._visualize_state(current_state)
        elif hasattr(agent.environment, "visualize"):
            state_visual = agent.environment.visualize()

        prompt_context: dict[str, Any] = {
            "current_state": current_state,
            "previous_move": previous_move,
            "state_visual": state_visual,
            "current_step": current_step,
        }

        if hasattr(agent.environment, "row_hints"):
            prompt_context["row_hints"] = agent.environment.row_hints
        if hasattr(agent.environment, "col_hints"):
            prompt_context["col_hints"] = agent.environment.col_hints
            prompt_context["column_hints"] = agent.environment.col_hints
        if hasattr(agent.environment, "n_rows"):
            prompt_context["n_rows"] = agent.environment.n_rows
        if hasattr(agent.environment, "n_cols"):
            prompt_context["n_cols"] = agent.environment.n_cols
        if hasattr(agent.environment, "row_hints"):
            allowed_cells = [
                (r, c)
                for r, row in enumerate(current_state)
                for c, v in enumerate(row)
                if v == -1
            ]
            prompt_context["allowed_cells"] = (
                allowed_cells if len(allowed_cells) <= 80 else allowed_cells[:80] + ["..."]
            )

        new_sys, new_usr = fallback.update_compose(
            agent.system_prompt,
            user_prompt,
            failed_predictions,
            step=current_step,
            retry=fallback_retry,
            prompt_context=prompt_context,
        )
        candidate_voting, best_prediction, failed_predictions, consensus_reached = (
            run_voting_batch(
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
        )

    return candidate_voting, best_prediction, failed_predictions, consensus_reached, fallback_retry


def main() -> None:
    parser = argparse.ArgumentParser(description="MAKER framework puzzle solver")
    parser.add_argument(
        "--game",
        required=True,
        choices=["tower_of_hanoi", "sliding_puzzle", "nonogram", "rubiks_cube"],
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
    parser.add_argument(
        "--temperature", type=float, default=None, help="LLM sampling temperature"
    )
    parser.add_argument(
        "--num_disks", type=int, default=None, help="Number of disks (tower_of_hanoi)"
    )
    parser.add_argument(
        "--temp_escalation",
        action="store_true",
        default=False,
        help="Escalate temperature per agent (0.1, 0.2, ...)",
    )
    parser.add_argument(
        "--model_path", type=str, default=None, help="Path to local model directory"
    )
    parser.add_argument(
        "--prompt_variant", type=str, default=None, help="Prompt variant name (e.g., base, cot_detailed, minimal)"
    )
    parser.add_argument(
        "--max_state_revisits",
        type=int,
        default=None,
        help="Cancel all jobs after a state is seen this many times (cycle detection)",
    )
    args = parser.parse_args()

    config = load_config(args)

    # Initialize WandB + Weave
    game_type = config["game"]

    if game_type == "tower_of_hanoi":
        size_str = f"d{config.get('num_disks', '?')}"
    elif game_type == "nonogram":
        size_str = f"{len(config.get('row_hints', []))}x{len(config.get('col_hints', []))}"
    elif game_type == "rubiks_cube":
        size_str = f"s{len(config.get('scramble', []))}"
    else:
        n = len(config.get("initial_state", []))
        side = int(n ** 0.5)
        size_str = f"{side}x{side}"

    timestamp = datetime.now().strftime("%m%d_%H%M")
    run_name = f"{game_type}_{size_str}_k{config['margin_k']}_a{config['max_agents_per_step']}_{timestamp}"
    tags = [game_type]

    wandb.init(
        project="lecture-agi",
        config=config,
        group=game_type,
        name=run_name,
        tags=tags,
    )
    try:
        weave.init("lecture-agi")
    except Exception as e:
        print(f"Warning: Weave disabled: {e}")

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

    # Initialize fallback model
    from utils.fallback import FallbackModel

    fallback: FallbackModel = FallbackModel(config, device=device)

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
    visited_states: dict[str, int] = {}
    max_state_revisits = config.get("max_state_revisits", 3)
    cycle_detected = False

    while not game.is_solved() and current_step < max_steps:
        current_state = copy.deepcopy(game.get_state())
        current_step += 1

        # Cycle detection before step
        state_key = str(current_state)
        visited_states[state_key] = visited_states.get(state_key, 0) + 1
        cycle_hit = visited_states[state_key] > max_state_revisits

        fallback_retries_used = 0

        if not cycle_hit:
            # Normal path: voting → consensus check → fallback if needed
            candidate_voting, best_prediction, failed_predictions, consensus_reached = (
                run_voting_batch(
                    agent,
                    previous_move,
                    current_state,
                    current_step,
                    batch_size=max_number_agents_per_step,
                    margin_k=margin_k,
                    predictions_table=predictions_table,
                )
            )

            if not (consensus_reached and best_prediction is not None):
                print(f"No valid consensus at step {current_step}. Engaging fallback...")
                candidate_voting, best_prediction, failed_predictions, consensus_reached, fallback_retries_used = (
                    _run_fallback_loop(
                        agent, fallback, previous_move, current_state, current_step,
                        max_fallback_retries, max_number_agents_per_step, margin_k,
                        failed_predictions, predictions_table,
                    )
                )

            if consensus_reached and best_prediction is not None:
                game.apply_move(best_prediction["action"])
            else:
                print("Fallback exhausted. No valid consensus move found.")
                break
        else:
            # Cycle path: skip voting, go directly to fallback with cycle context
            print(f"Cycle detected: state seen {visited_states[state_key]} times. Trying fallback to escape cycle...")
            failed_predictions = [
                {
                    "agent_id": "cycle_detector",
                    "action": "N/A",
                    "state": state_key,
                    "error": f"Cycle detected: state visited {visited_states[state_key]} times (limit {max_state_revisits}). The agent is stuck in a loop. You MUST choose a completely different move.",
                }
            ]
            candidate_voting, best_prediction, _, consensus_reached, fallback_retries_used = (
                _run_fallback_loop(
                    agent, fallback, previous_move, current_state, current_step,
                    max_fallback_retries, max_number_agents_per_step, margin_k,
                    failed_predictions, predictions_table,
                )
            )

            if consensus_reached and best_prediction is not None:
                game.apply_move(best_prediction["action"])
            else:
                print(f"Cycle detected and fallback exhausted. Cancelling all jobs.")
                wandb.log(
                    {
                        "early_stop": "cycle_detected",
                        "cycle_state": state_key,
                        "cycle_step": current_step,
                    }
                )
                _cancel_sibling_jobs()
                cycle_detected = True
                break

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
            "fallback_retries": fallback_retries_used,
            "num_agents_queried": len(failed_predictions) + sum(candidate_voting.values()),
        }
        game_history.append(step_data)

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

    success_rate = game.compute_progress()
    print(f"Success Rate: {success_rate:.1%}")

    wandb.log({"predictions": predictions_table})
    wandb.log(
        {
            "total_steps": current_step,
            "solved": game.is_solved(),
            "cycle_detected": cycle_detected,
            "success_rate": success_rate,
        }
    )

    wandb.save(os.path.join(output_dir, "failures.csv"))
    wandb.save(os.path.join(output_dir, "debug_prompts.md"))

    experiments_dir = os.path.join(output_dir, "experiments")
    if not os.path.exists(experiments_dir):
        os.makedirs(experiments_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    num_disks_str = f"_{config['num_disks']}d" if game_type == "tower_of_hanoi" else ""
    json_filename = f"{game_type}{num_disks_str}_{config['max_agents_per_step']}a_{timestamp}.json"
    json_path = os.path.join(experiments_dir, json_filename)

    experiment_data = {"game_type": config["game"], "success_rate": success_rate, "steps": game_history}

    with open(json_path, "w") as f:
        json.dump(experiment_data, f, indent=2)

    print(f"Experiment log saved to: {json_path}")

    wandb.finish()


if __name__ == "__main__":
    main()
