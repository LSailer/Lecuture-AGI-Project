import ast
import re
from .enviroment import SlidingPuzzle


class Parser:
    def __init__(self, environment: SlidingPuzzle) -> None:
        self.environment = environment

    def parse_action_state(self, response: str):
        move_pat = re.compile(r"(?is)\bmove\b\s*=\s*\[(\d+),\s*[\"'](\w+)[\"']\]")
        state_pat = re.compile(r"(?is)\bnext_state\b\s*=\s*(\[[^\[\]]+\])")

        move_matches = list(move_pat.finditer(response))
        state_matches = list(state_pat.finditer(response))

        move_str = move_matches[-1].groups() if move_matches else None
        state_str = state_matches[-1].group(1) if state_matches else None

        if not move_str or not state_str:
            raise ValueError("Could not find move or next_state in the response.")

        try:
            tile = int(move_str[0])
            direction = move_str[1]
            move = (tile, direction)

            state = ast.literal_eval(state_str)

        except Exception as e:
            raise ValueError(f"Error parsing move or next_state") from e

        return self.environment.validate_move(move), self.environment.is_valid_state(
            state
        )


if __name__ == "__main__":
    environment = SlidingPuzzle(initial_state=[1, 2, 3, 4, 5, 6, 7, 0, 8])
    parser = Parser(environment)
    test_response = """
    To solve this, I need to move tile 8 left into the empty space.

    move = [8, "left"]
    next_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    This will solve the puzzle.
    """
    action, state = parser.parse_action_state(test_response)
    print("Parsed Action:", action)
    print("Parsed State:", state)
