import sys
import unittest
from pathlib import Path

# Make src importable when running from project root
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from nonogram.enviroment import Nonogram, _line_feasible  # noqa: E402


class TestNonogramEnvironment(unittest.TestCase):
    def setUp(self) -> None:
        # 5x5 diamond puzzle from config
        self.row_hints = [[1], [3], [5], [3], [1]]
        self.col_hints = [[1], [3], [5], [3], [1]]
        self.env = Nonogram.from_config(
            row_hints=self.row_hints,
            col_hints=self.col_hints,
        )

    def test_line_feasible_accepts_valid_partial_line(self) -> None:
        self.assertTrue(_line_feasible([-1, -1, -1, -1, -1], [3]))
        self.assertTrue(_line_feasible([0, 1, 1, -1, 0], [3]))
        self.assertTrue(_line_feasible([1, -1, -1, 0, -1], [1, 1]))

    def test_line_feasible_rejects_impossible_line(self) -> None:
        self.assertFalse(_line_feasible([1, 1, 0], [1]))
        self.assertFalse(_line_feasible([1, 0, 1], [2]))
        self.assertFalse(_line_feasible([1, 1, 1], [1, 1]))

    def test_validate_move_accepts_forced_safe_move(self) -> None:
        move = self.env.validate_move((2, 2, 1))
        self.assertEqual(move, (2, 2, 1))

    def test_validate_move_rejects_out_of_bounds(self) -> None:
        with self.assertRaisesRegex(ValueError, "out of bounds"):
            self.env.validate_move((10, 0, 1))

    def test_validate_move_rejects_invalid_cell_value(self) -> None:
        with self.assertRaisesRegex(ValueError, "value must be 0"):
            self.env.validate_move((0, 0, 7))

    def test_validate_move_rejects_already_decided_cell(self) -> None:
        self.env.apply_move((2, 2, 1))
        with self.assertRaisesRegex(ValueError, "cell already decided"):
            self.env.validate_move((2, 2, 0))

    def test_validate_move_rejects_row_that_becomes_impossible(self) -> None:
        # Row 0 has hint [1]. After placing one filled cell there,
        # a second filled cell in that row must be rejected.
        self.env.apply_move((0, 0, 1))
        with self.assertRaisesRegex(ValueError, "row impossible"):
            self.env.validate_move((0, 1, 1))

    def test_is_valid_state_rejects_wrong_row_count(self) -> None:
        bad_state = [
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
        ]
        with self.assertRaisesRegex(ValueError, "wrong number of rows"):
            self.env.is_valid_state(bad_state)

    def test_is_valid_state_rejects_wrong_column_count(self) -> None:
        bad_state = [
            [-1, -1, -1, -1],
            [-1, -1, -1, -1],
            [-1, -1, -1, -1],
            [-1, -1, -1, -1],
            [-1, -1, -1, -1],
        ]
        with self.assertRaisesRegex(ValueError, "wrong number of cols"):
            self.env.is_valid_state(bad_state)

    def test_is_valid_state_rejects_impossible_row(self) -> None:
        bad_state = [
            [1, 1, 0, 0, 0],   # row hint is [1], so this row is impossible
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
        ]
        with self.assertRaisesRegex(ValueError, "row 0 impossible"):
            self.env.is_valid_state(bad_state)

    def test_is_valid_state_rejects_impossible_column(self) -> None:
        bad_state = [
            [1, -1, -1, -1, -1],
            [0, -1, -1, -1, -1],
            [1, -1, -1, -1, -1],
            [0, -1, -1, -1, -1],
            [1, -1, -1, -1, -1],
        ]
        # Column 0 becomes [1,0,1,0,1] which cannot satisfy hint [1]
        with self.assertRaisesRegex(ValueError, "col 0 impossible"):
            self.env.is_valid_state(bad_state)

    def test_apply_move_updates_grid(self) -> None:
        self.env.apply_move((2, 2, 1))
        self.assertEqual(self.env.get_state()[2][2], 1)

    def test_is_solved_true_for_correct_solution(self) -> None:
        solved = [
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0],
        ]
        env = Nonogram.from_config(
            row_hints=self.row_hints,
            col_hints=self.col_hints,
            initial_state=solved,
        )
        self.assertTrue(env.is_solved())

    def test_is_solved_false_for_incomplete_state(self) -> None:
        self.assertFalse(self.env.is_solved())


if __name__ == "__main__":
    unittest.main()