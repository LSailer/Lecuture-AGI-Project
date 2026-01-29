import torch
from .parser import Parser
from utils.llm import LLM
from .enviroment import SlidingPuzzle
import csv
import os


class Agent:
    def __init__(self, environment: SlidingPuzzle, device="cpu"):
        self.SYSTEM_PROMPT = """
You are a helpful assistant solving a sliding puzzle (8-puzzle).

The puzzle is a 3x3 grid with tiles numbered 1-8 and one empty space (0).
Goal: Arrange tiles in order [1, 2, 3, 4, 5, 6, 7, 8, 0]

Visual goal state:
1 2 3
4 5 6
7 8 0

Rules:
1. Only tiles adjacent to empty space (0) can move
2. A tile moves INTO the empty space by sliding up/down/left/right
3. Each move: select a tile and direction

Example:
State: [1, 2, 3, 4, 0, 5, 7, 8, 6]
Visual:
1 2 3
4 0 5
7 8 6

Valid moves:
- move = [2, "down"] → tile 2 slides down
- move = [4, "right"] → tile 4 slides right
- move = [5, "left"] → tile 5 slides left
- move = [8, "up"] → tile 8 slides up

After move [5, "left"]:
next_state = [1, 2, 3, 4, 5, 0, 7, 8, 6]

Output format (EXACT):
move = [tile_number, "direction"]
next_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
"""
        self.llm = LLM(device=device)
        self.output_parser = Parser(environment)

    def visualize_state(self, state):
        return f"{state[0]} {state[1]} {state[2]}\n{state[3]} {state[4]} {state[5]}\n{state[6]} {state[7]} {state[8]}"

    def execute_decompose_prompt(
        self, previous_move: str, current_state: list, step: int = 0, agent_num: int = 0
    ):
        state_visual = self.visualize_state(current_state)

        USER_TEMPLATE = f"""
Current State: {current_state}

Visual:
{state_visual}

Goal State:
1 2 3
4 5 6
7 8 0

Decision Process:
1. Find the empty space (0) position
2. List tiles adjacent to empty (up/down/left/right neighbors)
3. For each valid move, consider:
   - Does it move a misplaced tile closer to goal position?
   - Does it avoid undoing the previous move?
   - Prioritize establishing top-left tiles first (1, 2, 3, 4, 5)

4. Select best move based on:
   Priority 1: Move tiles far from goal positions
   Priority 2: Avoid reversing previous move
   Priority 3: Work on upper/left tiles first

Previous move: {previous_move}

Think step-by-step:
1. Where is empty space (0)?
2. What tiles can move? (List tile numbers and directions)
3. Which move brings a tile closer to its goal?
4. Does this reverse previous move? If yes, choose different move
5. Output move and resulting next_state
"""
        response = self.llm.generate(self.SYSTEM_PROMPT, USER_TEMPLATE)
        content = response[-1]["content"]

        action = "None"
        parsed_state = "None"
        error_message = "None"

        try:
            action, parsed_state = self.output_parser.parse_action_state(content)
        except Exception as e:
            error_message = str(e)

        log_file = "output/log.csv"
        os.makedirs("output", exist_ok=True)
        file_exists = os.path.isfile(log_file)

        with open(log_file, mode="a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(
                    [
                        "step",
                        "number_agent",
                        "response",
                        "predicted_action",
                        "predicted_state",
                        "error_message",
                    ]
                )
            writer.writerow(
                [step, agent_num, content, action, parsed_state, error_message]
            )

        if error_message != "None":
            raise ValueError(error_message)

        return action, parsed_state


if __name__ == "__main__":
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    agent = Agent(SlidingPuzzle(), device=device)
