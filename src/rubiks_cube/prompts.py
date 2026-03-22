import os
import re

import yaml


# Robust patterns (safety net) – find fields anywhere even if model adds extra text.
MOVE_PATTERN = re.compile(r"(?is)\bmove\b\s*[:=]\s*([URFDLB](?:2|')?)\b")
STATE_PATTERN = re.compile(r"(?is)\bnext_state\b\s*[:=]\s*([WRGYOB]{54})\b")

_ALLOWED = [
    "U", "U'", "U2",
    "R", "R'", "R2",
    "F", "F'", "F2",
    "D", "D'", "D2",
    "L", "L'", "L2",
    "B", "B'", "B2",
]

_SOLVED = "W" * 9 + "R" * 9 + "G" * 9 + "Y" * 9 + "O" * 9 + "B" * 9

_PROMPTS_DIR = os.path.join(os.path.dirname(__file__), "prompts")
_prompt_cache: dict[str, dict[str, str]] = {}


def _load_variant(variant: str) -> dict[str, str]:
    if variant not in _prompt_cache:
        path = os.path.join(_PROMPTS_DIR, f"{variant}.yaml")
        with open(path) as f:
            _prompt_cache[variant] = yaml.safe_load(f)
    return _prompt_cache[variant]


def get_system_prompt(environment, variant: str = "base"):
    templates = _load_variant(variant)
    return templates["system_prompt"].format(
        allowed_moves=", ".join(_ALLOWED),
        solved_state=_SOLVED,
    )


def _compute_move_lookup(current_state: str, environment) -> str:
    """Pre-compute next_state for every valid move and return a formatted lookup table."""
    import copy
    lines = []
    for mv in _ALLOWED:
        try:
            temp = copy.deepcopy(environment)
            temp.apply_move(mv, validate=True)
            lines.append(f"  {mv:<3}: {temp.state}")
        except ValueError:
            pass  # skip forbidden moves (undo, score drop)
    return "\n".join(lines)


def build_user_prompt(current_state, previous_move, environment, step, variant: str = "base"):
    score = environment.score(current_state)
    phase = environment.phase
    phase_goal = (
        "Solve the WHITE CROSS on the U face (white)."
        if phase == "white_cross"
        else "Continue toward the full solve."
    )

    templates = _load_variant(variant)
    template = templates["user_prompt"]

    extra = {}
    if "{move_lookup}" in template:
        extra["move_lookup"] = _compute_move_lookup(current_state, environment)

    return template.format(
        step=step,
        phase=phase,
        phase_goal=phase_goal,
        score=score,
        previous_move=previous_move,
        allowed_moves=", ".join(_ALLOWED),
        current_state=current_state,
        **extra,
    )


def parse_move(match):
    mv = match.group(1).strip()
    if mv not in _ALLOWED:
        raise ValueError("Move not in allowed set.")
    return mv


def parse_state(match):
    st = match.group(1).strip()
    if len(st) != 54:
        raise ValueError("State must be a 54-character string.")
    allowed = set("WRGYOB")
    if any(ch not in allowed for ch in st):
        raise ValueError("State contains invalid color letters.")
    for c in "WRGYOB":
        if st.count(c) != 9:
            raise ValueError("Invalid state: each color must appear exactly 9 times.")
    return st
