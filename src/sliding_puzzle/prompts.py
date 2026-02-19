import ast
import re


MOVE_PATTERN = re.compile(r"(?is)\bmove\b\s*=\s*\[(\d+),\s*[\"'](\w+)[\"']\]")
STATE_PATTERN = re.compile(r"(?is)\bnext_state\b\s*=\s*(\[[^\[\]]+\])")


def get_system_prompt(environment):
    return """
You are a micro-agent solving an 8-puzzle using a prioritized heuristic.
Goal State: [1, 2, 3, 4, 5, 6, 7, 8, 0]

Micro-Agent Priority Rules (Strict Order):
1. **Identify Target:** Find the first number $N$ (1-8) that is NOT in its correct sorted position. This is your TARGET.
2. **Move Logic:**
   - If 0 is adjacent to TARGET and in the direction of TARGET's goal: **Move TARGET towards goal.**
   - Else: **Move 0 closer to TARGET** (to "pick it up").
   - EXCEPTION: Do not move a tile that is already correctly placed (lower than TARGET) unless absolutely necessary.
3. **Safety:** Never reverse the immediately previous move.

Output Format (STRICT):
Target: <number>
Reasoning: <briefly justify based on Rule 2>
move = [tile_number, "direction"]
next_state = [resulting_list]

Example:
State: [1, 2, 0, 4, 5, 3, 7, 8, 6]
Target: 3 (1, 2 are correct. 3 is at index 5, goal is 2)
Reasoning: 0 is at index 2 (Goal of 3). 3 is at index 5 (below 0). Move 3 up into 0.
move = [3, "up"]
next_state = [1, 2, 3, 4, 5, 0, 7, 8, 6]
"""


def _visualize_state(state):
    return f"{state[0]} {state[1]} {state[2]}\n{state[3]} {state[4]} {state[5]}\n{state[6]} {state[7]} {state[8]}"


def build_user_prompt(current_state, previous_move, environment, step):
    return f"""
Current State: {current_state}
Previous move: {previous_move}

Task:
1. Scan for the first misplaced number (1 -> 8). This is your Target.
2. Apply Move Logic to help Target reach its goal.

Provide Target, Reasoning, and Move:
"""


def parse_move(match):
    tile = int(match.group(1))
    direction = match.group(2)
    return (tile, direction)


def parse_state(match):
    return ast.literal_eval(match.group(1))
