import ast
import os
import re

import yaml


# move = [row, col, value]  (3 integers)
MOVE_PATTERN = re.compile(r'(?is)\bmove\b\s*=\s*\[(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\]')
# next_state = [[...], [...], ...]  (9x9 nested list)
STATE_PATTERN = re.compile(r"(?is)\bnext_state\b\s*=\s*(\[\s*\[[\s\d,]+\](?:\s*,\s*\[[\s\d,]+\]){8}\s*\])")

_PROMPTS_DIR = os.path.join(os.path.dirname(__file__), "prompts")
_prompt_cache: dict[str, dict[str, str]] = {}


def _load_variant(variant: str) -> dict[str, str]:
    if variant not in _prompt_cache:
        path = os.path.join(_PROMPTS_DIR, f"{variant}.yaml")
        with open(path) as f:
            _prompt_cache[variant] = yaml.safe_load(f)
    return _prompt_cache[variant]


def _visualize_state(state):
    lines = []
    for r in range(9):
        parts = []
        for c in range(9):
            v = state[r][c]
            parts.append(str(v) if v != 0 else ".")
        row_str = " ".join(parts[:3]) + " | " + " ".join(parts[3:6]) + " | " + " ".join(parts[6:])
        lines.append(row_str)
        if r in (2, 5):
            lines.append("------+-------+------")
    return "\n".join(lines)


def get_system_prompt(environment, variant: str = "base"):
    templates = _load_variant(variant)
    return templates["system_prompt"]


def build_user_prompt(current_state, previous_move, environment, step, variant: str = "base"):
    templates = _load_variant(variant)
    state_visual = _visualize_state(current_state)
    empty_cells = [(r, c) for r in range(9) for c in range(9) if current_state[r][c] == 0]
    empty_preview = empty_cells if len(empty_cells) <= 81 else empty_cells[:81]
    return templates["user_prompt"].format(
        step=step,
        previous_move=previous_move,
        current_state=current_state,
        state_visual=state_visual,
        empty_cells=empty_preview,
    )


def parse_move(match):
    r = int(match.group(1))
    c = int(match.group(2))
    v = int(match.group(3))
    return (r, c, v)


def parse_state(match):
    return ast.literal_eval(match.group(1))
