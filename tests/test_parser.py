import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from nonogram.enviroment import Nonogram  # noqa: E402
from nonogram import prompts  # noqa: E402
from utils.parser import Parser  # noqa: E402


def build_response(move_row: int, move_col: int, label: str, next_state: list[list[int]]) -> str:
    return f'move = [{move_row}, {move_col}, "{label}"]\nnext_state = {next_state}'


class TestParser(unittest.TestCase):
    def setUp(self) -> None:
        self.row_hints = [[1], [3], [5], [3], [1]]
        self.col_hints = [[1], [3], [5], [3], [1]]
        self.env = Nonogram.from_config(
            row_hints=self.row_hints,
            col_hints=self.col_hints,
        )
        self.parser = Parser(
            environment=self.env,
            move_pattern=prompts.MOVE_PATTERN,
            state_pattern=prompts.STATE_PATTERN,
            parse_move_fn=prompts.parse_move,
            parse_state_fn=prompts.parse_state,
        )

    def test_parse_action_state_accepts_valid_response(self) -> None:
        current_state = [[-1] * 5 for _ in range(5)]
        next_state = [[-1] * 5 for _ in range(5)]
        next_state[2][2] = 1

        response = build_response(2, 2, "filled", next_state)
        move, state = self.parser.parse_action_state(response, current_state=current_state)

        self.assertEqual(move, (2, 2, 1))
        self.assertEqual(state, next_state)

    def test_parse_action_state_rejects_missing_move_or_state(self) -> None:
        with self.assertRaisesRegex(ValueError, "Could not find"):
            self.parser.parse_action_state('move = [2, 2, "filled"]', current_state=self.env.get_state())

    def test_parse_action_state_rejects_multiple_moves(self) -> None:
        current_state = self.env.get_state()
        next_state = [[-1] * 5 for _ in range(5)]
        next_state[2][2] = 1

        response = (
            'move = [2, 2, "filled"]\n'
            'move = [2, 3, "filled"]\n'
            f'next_state = {next_state}'
        )
        with self.assertRaisesRegex(ValueError, "exactly one move"):
            self.parser.parse_action_state(response, current_state=current_state)

    def test_parse_action_state_allows_reasoning_before_move(self) -> None:
        current_state = self.env.get_state()
        next_state = [[-1] * 5 for _ in range(5)]
        next_state[2][2] = 1

        response = (
            "Here is my reasoning:\n"
            "I will choose the center cell.\n"
            + build_response(2, 2, "filled", next_state)
        )

        move, state = self.parser.parse_action_state(
            response,
            current_state=current_state,
        )

        self.assertEqual(move, (2, 2, 1))
        self.assertEqual(state, next_state)

    def test_parse_action_state_rejects_extra_text_after_state(self) -> None:
        current_state = self.env.get_state()
        next_state = [[-1] * 5 for _ in range(5)]
        next_state[2][2] = 1

        response = build_response(2, 2, "filled", next_state) + "\nthanks"
        with self.assertRaisesRegex(ValueError, "extra text after next_state"):
            self.parser.parse_action_state(response, current_state=current_state)

    def test_parse_action_state_rejects_wrong_order(self) -> None:
        current_state = self.env.get_state()
        next_state = [[-1] * 5 for _ in range(5)]
        next_state[2][2] = 1

        response = f"next_state = {next_state}\nmove = [2, 2, \"filled\"]"
        with self.assertRaisesRegex(ValueError, "move must appear before next_state"):
            self.parser.parse_action_state(response, current_state=current_state)

    def test_parse_action_state_rejects_inconsistent_next_state(self) -> None:
        current_state = [[-1] * 5 for _ in range(5)]
        wrong_next_state = [[-1] * 5 for _ in range(5)]
        wrong_next_state[2][3] = 1  # falsche Zelle geändert

        response = build_response(2, 2, "filled", wrong_next_state)
        with self.assertRaisesRegex(ValueError, "Inconsistent prediction"):
            self.parser.parse_action_state(response, current_state=current_state)

    def test_parse_action_state_rejects_move_to_already_decided_cell(self) -> None:
        current_state = [[-1] * 5 for _ in range(5)]
        current_state[2][2] = 1
        self.env.grid = [row[:] for row in current_state]

        next_state = [[row for row in current_state]][0]
        next_state = [row[:] for row in current_state]
        next_state[2][2] = 0

        response = build_response(2, 2, "empty", next_state)
        with self.assertRaisesRegex(ValueError, "cell already decided"):
            self.parser.parse_action_state(response, current_state=current_state)


if __name__ == "__main__":
    unittest.main()
