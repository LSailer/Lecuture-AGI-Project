import ast
import re


MOVE_PATTERN = re.compile(r"(?is)\bmove\b\s*=\s*(UP|DOWN|LEFT|RIGHT)")
STATE_PATTERN = re.compile(r"(?is)\bnext_state\b\s*=\s*(\[[^\[\]]+\])")


def get_system_prompt(environment):
    return f"""
You are a micro-agent solving an 8-puzzle (sliding puzzle) on a 3×3 grid.

Goal State: [1, 2, 3, 4, 5, 6, 7, 8, 0]
Visualized:
1 2 3
4 5 6
7 8 0

The state is a flat list in row-major order:
  Index 1 = top-left, index 2 = top-center, index 3 = top-right
  Index 4 = mid-left,  index 5 = mid-center, index 6 = mid-right
  Index 7= bot-left,  index 8 = bot-center, index 0 = bot-right


Directions (the direction the BLANK moves):
  UP, DOWN, LEFT, RIGHT

A move is legal only if the blank (0) has an adjacent tile in the given direction.

Micro-Agent Priority Rules (Strict Order):

1. **Identify Target:**
   Scan tiles 1 through 8 in order. The first tile whose current index
   does NOT equal its goal index (goal index of tile N is N-1) is your TARGET.

2. **Move Logic:**
   a) If the blank (0) is adjacent to TARGET on the grid, AND swapping them
      would reduce TARGET's Manhattan distance to its goal index:
      → Move TARGET into the blank's position.
   b) Otherwise: Move the blank one step closer to TARGET by Manhattan distance.
      Prefer moves that do NOT displace any tile that is already at its goal index.
   c) CONSTRAINT: Do not displace a correctly-placed tile (index < TARGET's index)
      unless the blank cannot reach TARGET by any other path.

3. **Safety:**
   Never reverse the immediately previous move.
   If all candidate moves would reverse the previous move, choose the move
   that displaces the fewest correctly-placed tiles.

Output Format (STRICT — follow exactly):
Target: <tile_number>
Reasoning: <1-2 sentences: which rule from Step 2 applies, why this move helps>
move = <DIRECTION>
next_state = [<resulting 9-element list>]

Where <DIRECTION> is one of: UP, DOWN, LEFT, RIGHT (direction the blank moves).

Verify before answering:
- The blank (0) has an adjacent tile in the chosen direction.
- next_state contains each number 0-8 exactly once.
- next_state matches the board after legally applying your move.

Example:
State: [1, 2, 0, 4, 5, 3, 7, 8, 6]
Grid:
1 2 0
4 5 3
7 8 6

Target: 3 (tiles 1, 2 are at their goal indices. Tile 3 is at index 5, its goal index is 2.)
Reasoning: Blank is at index 2. Tile 3 is directly below (index 5). Moving blank DOWN swaps them, placing tile 3 at its goal index. Rule 2a applies.
move = DOWN
next_state = [1, 2, 3, 4, 5, 0, 7, 8, 6]
"""

def _visualize_state(state):
    return f"{state[0]} {state[1]} {state[2]}\n{state[3]} {state[4]} {state[5]}\n{state[6]} {state[7]} {state[8]}"


def build_user_prompt(current_state, previous_move, environment, step):
    prev = previous_move if previous_move else "None (first move)"
    return f"""
Step: {step}
Current State: {current_state}
Previous Move: {prev}

Grid:
{_visualize_state(state=current_state)}

Task:
1. Scan tiles 1→8. Find the first tile not at its goal index. That is your Target.
2. Apply Move Logic (Rule 2) to move Target closer to its goal.
3. Verify your move is legal and next_state is correct.

Provide Target, Reasoning, move, and next_state:
"""

def parse_move(match):
    return match.group(1).lower()


def parse_state(match):
    return ast.literal_eval(match.group(1))
