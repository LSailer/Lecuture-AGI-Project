import ast
import os
import re

import yaml


MOVE_PATTERN = re.compile(r"(?is)\bmove\b\s*=\s*(\[[^\[\]]*\])")
STATE_PATTERN = re.compile(
    r"(?is)\bnext_state\b\s*=\s*(\[\s*\[[^\[\]]*\]\s*,\s*\[[^\[\]]*\]\s*,\s*\[[^\[\]]*\]\s*\])"
)

_PROMPTS_DIR = os.path.join(os.path.dirname(__file__), "prompts")
_prompt_cache: dict[str, dict[str, str]] = {}


def _load_variant(variant: str) -> dict[str, str]:
    if variant not in _prompt_cache:
        path = os.path.join(_PROMPTS_DIR, f"{variant}.yaml")
        with open(path) as f:
            _prompt_cache[variant] = yaml.safe_load(f)
    return _prompt_cache[variant]


def _direction_string(num_disks: int) -> str:
    if num_disks % 2 == 0:
        return "0 -> 1 -> 2 -> 0"
    return "0 -> 2 -> 1 -> 0"


def get_system_prompt(environment, variant: str = "base"):
    templates = _load_variant(variant)
    return templates["system_prompt"].format(
        num_disks=environment.num_disks,
        direction_string=_direction_string(environment.num_disks),
    )


def build_user_prompt(current_state, previous_move, environment, step, variant: str = "base"):
    templates = _load_variant(variant)
    return templates["user_prompt"].format(
        current_state=current_state,
        previous_move=previous_move,
        direction_string=_direction_string(environment.num_disks),
    )


def parse_move(match):
    move = ast.literal_eval(match.group(1))
    return tuple(move)


def parse_state(match):
    state = ast.literal_eval(match.group(1))
    return tuple(tuple(tower) for tower in state)
