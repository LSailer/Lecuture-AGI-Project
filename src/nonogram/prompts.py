import ast
import re


# move = [row, col, "filled"|"empty"]
MOVE_PATTERN = re.compile(r'(?is)\bmove\b\s*=\s*\[(\d+)\s*,\s*(\d+)\s*,\s*[\"\'](filled|empty)[\"\']\s*\]')
# next_state = [[...], [...], ...]
STATE_PATTERN = re.compile(r"(?is)\bnext_state\b\s*=\s*(\[\s*\[[\s\d,-]+\](?:\s*,\s*\[[\s\d,-]+\])+\s*\])")


def get_system_prompt(environment):
    rows = environment.n_rows
    cols = environment.n_cols
    return f"""
You are a helpful assistant solving a Nonogram (Picross).

Nonogram rules:
- You have a {rows}x{cols} grid.
- Each row has hints (a list of positive integers) describing the lengths of consecutive FILLED blocks (#) in that row, in order, separated by at least one EMPTY cell (x).
- Same for each column.
- A single number means there is exactly one consecutive FILLED block of that length in the line.
- Each cell is one of:
  - unknown: -1 (.)
  - empty: 0 (x)
  - filled: 1 (#)

Examples:
- Hint [3] means exactly one block of 3 consecutive FILLED cells in that row/column.
- Hint [1, 1] means exactly two FILLED single cells, separated by at least one EMPTY cell.
- Hint [2, 1] means one block of 2 consecutive FILLED cells, then at least one EMPTY cell, then one block of 1 FILLED cell.

Goal:
- Decide every cell so that ALL row hints and column hints are satisfied exactly.

VERY IMPORTANT:
- You must propose exactly ONE cell decision per step (Maximal Agentic Decomposition).
- Your answer MUST be in the EXACT format:

move = [row, col, "filled"]
next_state = [[...], [...], ...]

or

move = [row, col, "empty"]
next_state = [[...], [...], ...]

Where:
- row and col are 0-indexed integers.
- next_state is the full grid as a nested list of ints using only -1, 0, 1.
- next_state MUST be the result of applying the move to the current_state (only that single cell changes).
Do NOT add extra text after the two lines.
""".strip()

def _visualize_state(state):
    mapping = {-1: ".", 0: "x", 1: "#"}
    return "\n".join("".join(mapping[v] for v in row) for row in state)


def build_user_prompt(current_state, previous_move, environment, step):
    state_visual = _visualize_state(current_state)
    allowed = [(r, c) for r, row in enumerate(current_state) for c, v in enumerate(row) if v == -1]
    # Keep prompt compact for larger puzzles
    allowed_preview = allowed if len(allowed) <= 80 else allowed[:80] + ["..."]
    return f"""
Current step: {step}
Previous move: {previous_move}

Row hints (0..{environment.n_rows-1}):
{environment.row_hints}

Column hints (0..{environment.n_cols-1}):
{environment.col_hints}

Current_state (nested list):
{current_state}

Visual (.:unknown, x:empty, #:filled):
{state_visual}

Allowed cells (must choose one of these coordinates; 0-indexed):
{allowed_preview}

Decision guidance:
1) Prefer a move that is logically forced (no guessing) using the hints.
2) Only decide an UNKNOWN cell (value -1).
3) After choosing the cell, update exactly that cell in next_state; all others must stay identical.
4) Keep the move consistent with feasibility: it should not make the affected row or column impossible.

Now output ONLY:
move = [row, col, "filled"|"empty"]
next_state = [...]
""".strip()


def parse_move(match):
    r = int(match.group(1))
    c = int(match.group(2))
    val_str = match.group(3).lower()
    v = 1 if val_str == "filled" else 0
    return (r, c, v)


def parse_state(match):
    return ast.literal_eval(match.group(1))
