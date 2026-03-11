import re
from typing import Any

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


def get_system_prompt(environment: Any) -> str:
    return f"""
You are a Rubik's Cube solver assistant.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8
- IMPORTANT invariant: each letter W,R,G,Y,O,B must appear EXACTLY 9 times.

Moves:
- Allowed moves are EXACTLY: {", ".join(_ALLOWED)}.
- U means rotate the U face 90° clockwise when looking at the U face from outside.
- U' is counter-clockwise, U2 is 180°. Same for R,F,D,L,B.

Reference solved state:
{_SOLVED}

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
""".strip()


def build_user_prompt(current_state: str, previous_move: str, environment: Any, step: int) -> str:
    score = environment.score(current_state)
    phase = environment.phase
    phase_goal = (
        "Solve the WHITE CROSS on the U face (white)."
        if phase == "white_cross"
        else "Continue toward the full solve."
    )

    return f"""
Step: {step}
Phase: {phase}
Goal: {phase_goal}
Current score: {score}
Previous move: {previous_move}
Allowed moves: {", ".join(_ALLOWED)}

Current state:
{current_state}

Remember: output EXACTLY TWO LINES:
move = <...>
next_state = <...>
""".strip()


def parse_move(match: re.Match):
    mv = match.group(1).strip()
    if mv not in _ALLOWED:
        raise ValueError("Move not in allowed set.")
    return mv


def parse_state(match: re.Match):
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