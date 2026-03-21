import ast
import os
import re

import yaml


# move = [row, col, "filled"|"empty"]
MOVE_PATTERN = re.compile(r'(?is)\bmove\b\s*=\s*\[(\d+)\s*,\s*(\d+)\s*,\s*[\"\'](filled|empty)[\"\']\s*\]')
# next_state = [[...], [...], ...]
STATE_PATTERN = re.compile(r"(?is)\bnext_state\b\s*=\s*(\[\s*\[[\s\d,-]+\](?:\s*,\s*\[[\s\d,-]+\])+\s*\])")

_PROMPTS_DIR = os.path.join(os.path.dirname(__file__), "prompts")
_prompt_cache: dict[str, dict[str, str]] = {}


def _load_variant(variant: str) -> dict[str, str]:
    if variant not in _prompt_cache:
        path = os.path.join(_PROMPTS_DIR, f"{variant}.yaml")
        with open(path) as f:
            _prompt_cache[variant] = yaml.safe_load(f)
    return _prompt_cache[variant]


def _visualize_state(state):
    mapping = {-1: ".", 0: "x", 1: "#"}
    return "\n".join("".join(mapping[v] for v in row) for row in state)


def get_system_prompt(environment, variant: str = "base"):
    templates = _load_variant(variant)
    return templates["system_prompt"].format(
        n_rows=environment.n_rows,
        n_cols=environment.n_cols,
    )


def build_user_prompt(current_state, previous_move, environment, step, variant: str = "base"):
    templates = _load_variant(variant)
    state_visual = _visualize_state(current_state)
    allowed = [(r, c) for r, row in enumerate(current_state) for c, v in enumerate(row) if v == -1]
    # Keep prompt compact for larger puzzles
    allowed_preview = allowed if len(allowed) <= 80 else allowed[:80] + ["..."]
    return templates["user_prompt"].format(
        step=step,
        previous_move=previous_move,
        n_rows=environment.n_rows,
        n_cols=environment.n_cols,
        n_rows_minus1=environment.n_rows - 1,
        n_cols_minus1=environment.n_cols - 1,
        row_hints=environment.row_hints,
        col_hints=environment.col_hints,
        current_state=current_state,
        state_visual=state_visual,
        allowed_cells=allowed_preview,
    )


def parse_move(match):
    r = int(match.group(1))
    c = int(match.group(2))
    val_str = match.group(3).lower()
    v = 1 if val_str == "filled" else 0
    return (r, c, v)


def parse_state(match):
    return ast.literal_eval(match.group(1))
