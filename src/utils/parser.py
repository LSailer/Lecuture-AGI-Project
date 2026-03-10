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

    def _coerce_to_reference_shape(self, value: Any, reference: Any) -> Any:
        """
        Normalize parsed states to the container structure of current_state.
        This keeps one parser compatible with games that use lists vs tuples.
        """
        if isinstance(reference, list):
            if isinstance(value, (list, tuple)):
                if reference:
                    return [self._coerce_to_reference_shape(v, reference[0]) for v in value]
                return list(value)
            return value

        if isinstance(reference, tuple):
            if isinstance(value, (list, tuple)):
                if reference:
                    return tuple(self._coerce_to_reference_shape(v, reference[0]) for v in value)
                return tuple(value)
            return value

        return value

    def _validate_transition_consistency(
        self,
        current_state: Any,
        move: Any,
        state: Any,
    ) -> None:
        """
        Check that next_state exactly matches the result of applying move
        to current_state in the environment.
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

        normalized_state = self._coerce_to_reference_shape(state, expected_state)

        if expected_state != normalized_state:
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

        move_matches = list(self.move_pattern.finditer(response))
        state_matches = list(self.state_pattern.finditer(response))

        if not move_matches or not state_matches:
            raise ValueError("Could not find move or next_state in the response.")

        try:
            move = self.parse_move_fn(move_matches[-1])
        except Exception as e:
            raise ValueError("Error parsing move.") from e

        try:
            state = self.parse_state_fn(state_matches[-1])
        except Exception as e:
            raise ValueError("Error parsing next_state.") from e

        if current_state is not None:
            state = self._coerce_to_reference_shape(state, current_state)

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
    Ursprünglicher Parser, nur wird jetzt zusätzlich noch geprüft ob der move tatsächlich zum state führt.
    Vorher nur ist move gültig + ist state gültig!

    """