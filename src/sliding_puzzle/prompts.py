import ast
import re


MOVE_PATTERN = re.compile(r"(?is)\bmove\b\s*=\s*\[(\d+),\s*[\"'](\w+)[\"']\]")
STATE_PATTERN = re.compile(r"(?is)\bnext_state\b\s*=\s*(\[[^\[\]]+\])")


def get_system_prompt(environment):
    return """
You are a helpful assistant solving a sliding puzzle (8-puzzle).
Be concise. No unnecessary explanation. Output only what is required.

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
- move = [2, "down"] \u2192 tile 2 slides down
- move = [4, "right"] \u2192 tile 4 slides right
- move = [5, "left"] \u2192 tile 5 slides left
- move = [8, "up"] \u2192 tile 8 slides up

After move [5, "left"]:
next_state = [1, 2, 3, 4, 5, 0, 7, 8, 6]

Output format (EXACT):
move = [tile_number, "direction"]
next_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
"""


def _visualize_state(state):
    return f"{state[0]} {state[1]} {state[2]}\n{state[3]} {state[4]} {state[5]}\n{state[6]} {state[7]} {state[8]}"


def build_user_prompt(current_state, previous_move, environment, step):
    state_visual = _visualize_state(current_state)

    return f"""
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


def parse_move(match):
    tile = int(match.group(1))
    direction = match.group(2)
    return (tile, direction)


def parse_state(match):
    return ast.literal_eval(match.group(1))
