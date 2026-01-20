import torch
from parser import Parser
from llm import LLM
from enviroment import TowerOfHanoi
import csv
import os


class Agent:
    def __init__(self, environment: TowerOfHanoi, device="cpu"):
        self.SYSTEM_PROMPT = f"""
        You are a helpful assistant. Solve this puzzle for me.
        There are three pegs and {environment.num_disks} disks of different sizes stacked on the first peg. The disks are
        numbered from 1 (smallest) to {environment.num_disks} (largest). Disk moves in this puzzle should follow:
        1. Only one disk can be moved at a time.
        2. Each move consists of taking the upper disk from one stack and placing it on top of
        another stack.
        3. A larger disk may not be placed on top of a smaller disk.
        The goal is to move the entire stack to the third peg.
        Example: With 3 disks numbered 1 (smallest), 2, and 3 (largest), the initial state is [[3, 2,
        1], [], []], and a solution might be:
        moves = [[1, 0, 2], [2, 0, 1], [1, 2, 1], [3, 0, 2], [1, 1, 0], [2, 1, 2], [1, 0, 2]]
        This means: Move disk 1 from peg 0 to peg 2, then move disk 2 from peg 0 to peg 1, and so on.
        Requirements:
        - The positions are 0-indexed (the leftmost peg is 0).
        - Ensure your answer includes a single next move in this EXACT FORMAT:
        ‘‘‘move = [disk id, from peg, to peg]‘‘‘
        - Ensure your answer includes the next state resulting from applying the move to the current
        state in this EXACT FORMAT:
        ‘‘‘next_state = [[...], [...], [...]]‘‘‘
        """
        self.llm = LLM(device=device)
        self.output_parser = Parser(environment)
        self.num_disks = environment.num_disks

    def execute_decompose_prompt(
        self, previous_move: str, current_state: str, step: int = 0, agent_num: int = 0
    ):
        # Determine direction based on number of disks (parity)
        # If N is EVEN: Clockwise (0 -> 1 -> 2 -> 0)
        # If N is ODD: Counter-clockwise (0 -> 2 -> 1 -> 0)
        if self.num_disks % 2 == 0:
            direction_string = "0 -> 1 -> 2 -> 0"
        else:
            direction_string = "0 -> 2 -> 1 -> 0"

        USER_TEMPLATE = f"""
        Current State Analysis:
        1. Identify the TOP disk on each peg (the last number in each list).
        2. Identify where Disk 1 is located.

        Decision Rules:
        - Rule A: If the 'Previous move' was NOT Disk 1 (or was 'None'), you MUST move Disk 1.
          -> Direction: Move Disk 1 to the next peg in sequence {direction_string}.
             (Sequence: {direction_string})

        - Rule B: If the 'Previous move' WAS Disk 1, you MUST move a different disk (NOT Disk 1).
          -> Look at the top disks of the two pegs that do NOT have Disk 1.
          -> Make the only legal move between those two pegs (remember: smaller disk on larger only).

        Task:
        Previous move: {previous_move}
        Current state: {current_state}

        Think step-by-step:
        1. Which rule applies (A or B)?
        2. If Rule B: What are the top disks on the other pegs? Which move is legal?
        3. Output the move and next state.
        """
        response = self.llm.generate(self.SYSTEM_PROMPT, USER_TEMPLATE)
        content = response[-1]["content"]  # type: ignore

        action = "None"
        parsed_state = "None"
        error_message = "None"

        try:
            action, parsed_state = self.output_parser.parse_action_state(content)
        except Exception as e:
            error_message = str(e)

        # Log to CSV
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
    agent = Agent(TowerOfHanoi(3), device=device)
