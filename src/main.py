"""Unified entry point for all puzzle solvers."""
import sys
import os
import argparse
import heapq

import yaml
import torch
import matplotlib.pyplot as plt

# Add src to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def create_game(config):
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


def create_agent(config, game, device):
    """Factory: instantiate the right agent from config."""
    from utils.decomposer import Agent

    game_name = config["game"]
    if game_name == "tower_of_hanoi":
        from tower_of_hanoi import prompts
    elif game_name == "sliding_puzzle":
        from sliding_puzzle import prompts
    else:
        raise ValueError(f"Unknown game: {game_name}")
    return Agent(environment=game, prompts_module=prompts, device=device)


def load_config(args):
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

    return config


def main():
    parser = argparse.ArgumentParser(description="MAKER framework puzzle solver")
    parser.add_argument(
        "--game",
        required=True,
        choices=["tower_of_hanoi", "sliding_puzzle"],
        help="Which puzzle to solve",
    )
    parser.add_argument("--config", default=None, help="Path to YAML config file")
    parser.add_argument("--margin_k", type=int, default=None, help="Vote margin for consensus")
    parser.add_argument("--max_steps", type=int, default=None, help="Maximum solver steps")
    parser.add_argument("--max_agents_per_step", type=int, default=None, help="Max agents per step")
    args = parser.parse_args()

    config = load_config(args)

    margin_k = config["margin_k"]
    max_steps = config["max_steps"]
    max_number_agents_per_step = config["max_agents_per_step"]
    output_dir = config.get("output_dir", "output")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    log_path = os.path.join(output_dir, "log.csv")
    if os.path.exists(log_path):
        os.remove(log_path)

    if torch.cuda.is_available():
        device = "cuda"
    elif torch.backends.mps.is_available():
        device = "mps"
    else:
        device = "cpu"

    game = create_game(config)
    agent = create_agent(config, game, device)

    print("Initial State:", game.get_state())
    if hasattr(game, "visualize"):
        print("Visual:")
        print(game.visualize())

    previous_move = "None"
    current_step = 0

    while not game.is_solved() and current_step < max_steps:
        current_state = game.get_state()
        action_voting = {}
        best_value = 0
        second_best_value = 0
        number_agents_per_step = 0
        current_step += 1

        while (
            best_value < second_best_value + margin_k
            and number_agents_per_step < max_number_agents_per_step
        ):
            number_agents_per_step += 1
            try:
                action, state = agent.execute_decompose_prompt(
                    previous_move,
                    current_state,
                    step=current_step,
                    agent_num=number_agents_per_step,
                )
                if isinstance(action, list):
                    action = tuple(action)
                print(
                    f"Agent {number_agents_per_step} predicted move: {action}, resulting state: {state}"
                )
                action_voting[action] = action_voting.get(action, 0) + 1

                top_two = heapq.nlargest(2, action_voting.items(), key=lambda x: x[1])

                if top_two:
                    best_action, best_value = top_two[0]
                    second_best_value = top_two[1][1] if len(top_two) > 1 else 0
            except ValueError as e:
                print("Error parsing LLM response:", e)
                continue

        if action_voting:
            game.apply_move(best_action)
        else:
            print("No valid move found.")
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


if __name__ == "__main__":
    main()
