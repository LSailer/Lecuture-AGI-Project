from __future__ import annotations

from typing import Any, Callable
import copy
import re


class Parser:
    def __init__(
        self,
        environment: Any,
        move_pattern: re.Pattern[str],
        state_pattern: re.Pattern[str],
        parse_move_fn: Callable[[re.Match[str]], Any],
        parse_state_fn: Callable[[re.Match[str]], Any],
    ) -> None:
        self.environment = environment
        self.move_pattern = move_pattern
        self.state_pattern = state_pattern
        self.parse_move_fn = parse_move_fn
        self.parse_state_fn = parse_state_fn

    def _extract_single_match(
        self,
        pattern: re.Pattern[str],
        response: str,
        label: str,
    ) -> re.Match[str]:
        matches = list(pattern.finditer(response))

        if not matches:
            raise ValueError(f"Could not find {label} in the response.")
        if len(matches) > 1:
            raise ValueError(f"Invalid response: expected exactly one {label}.")

        return matches[0]

    def _ensure_strict_two_line_format(
        self,
        response: str,
        move_match: re.Match[str],
        state_match: re.Match[str],
    ) -> None:
        if move_match.start() > state_match.start():
            raise ValueError("Invalid response: move must appear before next_state.")

        prefix = response[: move_match.start()]
        between = response[move_match.end() : state_match.start()]
        suffix = response[state_match.end() :]

        if prefix.strip():
            raise ValueError("Invalid response: extra text before move.")
        if between.strip():
            raise ValueError(
                "Invalid response: only whitespace is allowed between move and next_state."
            )
        if suffix.strip():
            raise ValueError("Invalid response: extra text after next_state.")

    def _validate_transition_consistency(
        self,
        current_state: Any,
        move: Any,
        state: Any,
    ) -> None:
        """
        Enforce MAKER-style consistency:
        next_state must be exactly the result of applying move to current_state.
        """
        temp_env = copy.deepcopy(self.environment)

        if hasattr(temp_env, "get_state"):
            env_state = temp_env.get_state()
            if env_state != current_state:
                raise ValueError(
                    "Internal state mismatch: environment state differs from current_state."
                )

        if not hasattr(temp_env, "apply_move") or not hasattr(temp_env, "get_state"):
            return

        temp_env.apply_move(move)
        expected_state = temp_env.get_state()

        if expected_state != state:
            raise ValueError(
                "Inconsistent prediction: next_state does not match current_state + move."
            )

    def parse_action_state(
        self,
        response: str,
        current_state: Any | None = None,
    ) -> tuple[Any, Any]:
        if not isinstance(response, str) or not response.strip():
            raise ValueError("Empty response.")

        move_match = self._extract_single_match(self.move_pattern, response, "move")
        state_match = self._extract_single_match(
            self.state_pattern, response, "next_state"
        )

        self._ensure_strict_two_line_format(response, move_match, state_match)

        try:
            move = self.parse_move_fn(move_match)
        except Exception as e:
            raise ValueError("Error parsing move.") from e

        try:
            state = self.parse_state_fn(state_match)
        except Exception as e:
            raise ValueError("Error parsing next_state.") from e

        try:
            validated_move = self.environment.validate_move(move)
        except Exception as e:
            raise ValueError(str(e)) from e

        try:
            validated_state = self.environment.is_valid_state(state)
        except Exception as e:
            raise ValueError(str(e)) from e

        if current_state is not None:
            self._validate_transition_consistency(
                current_state=current_state,
                move=validated_move,
                state=validated_state,
            )

        return validated_move, validated_state
    


"""
- Fix: parser accepts now exactly one move and one state.
- Fix: Checks if next_state is consistent with current_state + move.
"""