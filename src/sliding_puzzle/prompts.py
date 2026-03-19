import ast
import os
import re

import yaml


MOVE_PATTERN = re.compile(r"(?is)\bmove\b\s*=\s*(UP|DOWN|LEFT|RIGHT)")
STATE_PATTERN = re.compile(r"(?is)\bnext_state\b\s*=\s*(\[[^\[\]]+\])")

_PROMPTS_DIR = os.path.join(os.path.dirname(__file__), "prompts")
_prompt_cache: dict[str, dict[str, str]] = {}


def _load_variant(variant: str) -> dict[str, str]:
    if variant not in _prompt_cache:
        path = os.path.join(_PROMPTS_DIR, f"{variant}.yaml")
        with open(path) as f:
            _prompt_cache[variant] = yaml.safe_load(f)
    return _prompt_cache[variant]


def _visualize_state(state):
    n = int(len(state) ** 0.5)
    lines = []
    for r in range(n):
        lines.append(" ".join(f"{state[r * n + c]:>2}" for c in range(n)))
    return "\n".join(lines)


def _goal_state(size):
    return list(range(size))


def _build_index_map(n, goal):
    index_lines = []
    for r in range(n):
        for c in range(n):
            idx = r * n + c
            pos_label = ["top", "mid", "bot"][min(r, 2)] if n <= 3 else f"row{r}"
            col_label = ["left", "center", "right"][min(c, 2)] if n <= 3 else f"col{c}"
            index_lines.append(f"  Index {idx} = {pos_label}-{col_label} (tile {goal[idx]})")
    return "\n".join(index_lines)


def get_system_prompt(environment, variant: str = "base"):
    size = environment.size
    n = environment.grid_size
    goal = _goal_state(size)
    max_tile = size - 1

    templates = _load_variant(variant)
    return templates["system_prompt"].format(
        puzzle_name=f"{n * n - 1}",
        n=n,
        goal_list=str(goal),
        goal_viz=_visualize_state(goal),
        index_map=_build_index_map(n, goal),
        max_tile=max_tile,
        size=size,
    )


def build_user_prompt(current_state, previous_move, environment, step, variant: str = "base"):
    prev = previous_move if previous_move else "None (first move)"
    max_tile = environment.size - 1

    templates = _load_variant(variant)
    return templates["user_prompt"].format(
        step=step,
        current_state=current_state,
        previous_move=prev,
        state_visual=_visualize_state(state=current_state),
        max_tile=max_tile,
    )


def parse_move(match):
    return match.group(1).lower()


def parse_state(match):
    return ast.literal_eval(match.group(1))
