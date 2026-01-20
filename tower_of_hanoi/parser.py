import ast
import re
from enviroment import TowerOfHanoi


class Parser:
    def __init__(self, environment: TowerOfHanoi) -> None:
        self.environment = environment

    def parse_action_state(self, response: str):
        move_pat = re.compile(r"(?is)\bmove\b\s*=\s*(\[[^\[\]]*\])")
        state_pat = re.compile(
            r"(?is)\bnext_state\b\s*=\s*(\[\s*\[[^\[\]]*\]\s*,\s*\[[^\[\]]*\]\s*,\s*\[[^\[\]]*\]\s*\])"
        )

        move_matches = list(move_pat.finditer(response))
        state_matches = list(state_pat.finditer(response))

        move_str = move_matches[-1].group(1) if move_matches else None
        state_str = state_matches[-1].group(1) if state_matches else None

        if not move_str or not state_str:
            raise ValueError("Could not find move or next_state in the response.")
        try:
            move = ast.literal_eval(move_str)
            state = ast.literal_eval(state_str)
            move = tuple(move)
            state = tuple(tuple(tower) for tower in state)

        except Exception as e:
            raise ValueError(f"Error parsing move or next_state") from e

        return self.environment.validate_move(move), self.environment.is_valid_state(
            state
        )


if __name__ == "__main__":
    environment = TowerOfHanoi(num_disks=3)
    parser = Parser(environment)
    test_response = """
    To find the next move, we need to follow the standard Tower of Hanoi procedure.\n\nSince the previous move was None, we need to move disk 1 clockwise one peg. The current state has disk 1 on peg 0, so we need to move it to peg 1.\n\nThe only legal move that does not involve moving disk 1 is to move disk 2 from peg 0 to peg 2.\n\nSo, the next move is:\n```\nmove = [2, 0, 2]\n```\nNow, let's apply this move to the current state to get the next state:\n```\nnext_state = [[3, 2, 1], [2], []]\n```\nThe next state is [[3, 2, 1], [2], []].
    """
    action, state = parser.parse_action_state(test_response)
    print("Parsed Action:", action)
    print("Parsed State:", state)
