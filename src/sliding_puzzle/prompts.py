import ast
import re


MOVE_PATTERN = re.compile(r"(?is)\bmove\b\s*=\s*\[(\d+),\s*[\"'](\w+)[\"']\]")
STATE_PATTERN = re.compile(r"(?is)\bnext_state\b\s*=\s*(\[[^\[\]]+\])")


def get_system_prompt(environment):
    return """
You are a concise solver for an 8-puzzle (3x3 grid, tiles 1-8, empty space 0).
Goal State: [1, 2, 3, 4, 5, 6, 7, 8, 0]

Rules:
- Move a tile adjacent to 0 INTO the empty space.
- Directions: "up", "down", "left", "right".

Output Format (STRICT):
Reasoning: <briefly justify move>
move = [tile_number, "direction"]
next_state = [resulting_list]

Example:
State: [1, 2, 3, 4, 0, 5, 7, 8, 6]
Reasoning: Tile 5 is right of 0, move it left to reach goal position.
move = [5, "left"]
next_state = [1, 2, 3, 4, 5, 0, 7, 8, 6]

No conversational filler. No redundant visualizations. Just reasoning and the exact move/state lines.
"""


def _visualize_state(state):
    return f"{state[0]} {state[1]} {state[2]}\n{state[3]} {state[4]} {state[5]}\n{state[6]} {state[7]} {state[8]}"


def build_user_prompt(current_state, previous_move, environment, step):
    state_visual = _visualize_state(current_state)

    return f"""
Current State: {current_state}
Visual:
{state_visual}

Previous move: {previous_move}

Guidelines:
1. Identify 0's position and neighbors.
2. Choose move that progresses misplaced tiles (especially 1-5).
3. Do NOT reverse the previous move.

Provide reasoning and move:
"""


def parse_move(match):
    tile = int(match.group(1))
    direction = match.group(2)
    return (tile, direction)


def parse_state(match):
    return ast.literal_eval(match.group(1))
