import heapq
from llm import LLM
from enviroment import TowerOfHanoi
from decomposer import Agent
import torch
import matplotlib.pyplot as plt
import os


def main(margin_k=2):
    if not os.path.exists("output"):
        os.makedirs("output")
    if os.path.exists("output/log.csv"):
        os.remove("output/log.csv")

    if torch.cuda.is_available():
        device = "cuda"
    elif torch.backends.mps.is_available():
        device = "mps"
    else:
        device = "cpu"

    game = TowerOfHanoi(num_disks=20)
    agent = Agent(environment=game, device=device)

    print("Initial State:", game.get_state())
    previous_move = "None"
    max_steps = 1048575 
    current_step = 0
    while not game.is_solved() and current_step < max_steps:
        current_state = str(game.get_state())
        action_voting = {}
        best_value = 0
        second_best_value = 0
        number_agents_per_step = 0
        max_number_agents_per_step = 15
        current_step += 1
        while (
            best_value <= second_best_value + margin_k
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

                # Update best and second best values
                top_two = heapq.nlargest(2, action_voting.items(), key=lambda x: x[1])

                if top_two:
                    best_action, best_value = top_two[0]
                    second_best_value = top_two[1][1] if len(top_two) > 1 else 0
            except ValueError as e:
                print("Error parsing LLM response:", e)
                continue

        # Save Plot distribution of action_voting here with the current step number
        if action_voting:
            # plt.figure()
            # actions_str = [str(k) for k in action_voting.keys()]
            # counts = list(action_voting.values())
            # plt.bar(actions_str, counts)
            # plt.title(f"Action Distribution Step {current_step}")
            # plt.xlabel("Actions")
            # plt.xticks(rotation=45)
            # plt.ylabel("Votes")
            # plt.tight_layout()
            # plt.savefig(f"output/step_{current_step}_distribution.png")
            # plt.close()

            game.move_disk(best_action[0], best_action[1], best_action[2])
        else:
            print("No valid move found.")
            break
        previous_move = str(best_action)
        print("Current State:", game.get_state())


if __name__ == "__main__":
    main()
