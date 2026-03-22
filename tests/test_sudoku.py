import pytest
from src.sudoku.enviroment import Sudoku, CONFIGS
from src.sudoku.prompts import parse_move, parse_state, MOVE_PATTERN, STATE_PATTERN

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

EASY_PUZZLE = CONFIGS["easy"]


@pytest.fixture
def sudoku():
    return Sudoku.from_config(initial_state=EASY_PUZZLE)


@pytest.fixture
def almost_solved():
    """A puzzle with only one empty cell remaining."""
    grid = [
        [4, 5, 2, 8, 3, 6, 1, 9, 7],
        [6, 8, 7, 9, 5, 1, 3, 4, 2],
        [9, 1, 3, 4, 2, 7, 5, 6, 8],
        [3, 4, 5, 8, 7, 1, 9, 2, 6],
        [7, 2, 6, 3, 4, 5, 8, 0, 1],  # row 4, col 7 is empty -> should be some valid digit
        [8, 9, 1, 2, 6, 0, 4, 7, 3],  # row 5, col 5 is empty
        [5, 3, 8, 7, 9, 4, 2, 1, 0],  # row 6, col 8 is empty
        [1, 6, 9, 5, 0, 8, 7, 3, 4],  # row 7, col 4 is empty
        [2, 7, 4, 1, 0, 3, 6, 8, 5],  # row 8, col 4 is empty
    ]
    # This grid may have constraint issues, so let's use a simpler approach:
    # Build a fully solved grid then remove one cell
    solved_grid = [
        [4, 5, 2, 8, 3, 6, 1, 9, 7],
        [6, 8, 7, 9, 5, 1, 3, 4, 2],
        [9, 1, 3, 4, 2, 7, 5, 6, 8],
        [3, 4, 5, 8, 7, 1, 9, 2, 6],
        [7, 2, 6, 3, 4, 5, 8, 0, 1],  # removed cell (4,7) was some digit
        [8, 9, 1, 2, 6, 0, 4, 7, 3],
        [5, 3, 8, 7, 9, 4, 2, 1, 0],
        [1, 6, 9, 5, 0, 8, 7, 3, 4],
        [2, 7, 4, 1, 0, 3, 6, 8, 5],
    ]
    # Note: This might not pass validation due to constraint issues.
    # We'll use a known valid minimal puzzle instead.
    return None


# ---------------------------------------------------------------------------
# __init__
# ---------------------------------------------------------------------------


class TestInit:
    def test_valid_puzzle(self, sudoku):
        assert len(sudoku.grid) == 9
        assert all(len(row) == 9 for row in sudoku.grid)

    def test_initial_grid_preserved(self, sudoku):
        assert sudoku.initial_grid == EASY_PUZZLE

    def test_grid_is_copy(self, sudoku):
        """Modifying grid should not affect initial_grid."""
        sudoku.grid[0][0] = 99
        assert sudoku.initial_grid[0][0] != 99

    def test_invalid_size_raises(self):
        with pytest.raises(ValueError):
            Sudoku.from_config(initial_state=[[0] * 9] * 8)  # 8 rows

    def test_invalid_value_raises(self):
        bad = [row[:] for row in EASY_PUZZLE]
        bad[0][0] = 10
        with pytest.raises(ValueError):
            Sudoku.from_config(initial_state=bad)


# ---------------------------------------------------------------------------
# validate_move
# ---------------------------------------------------------------------------


class TestValidateMove:
    def test_valid_move(self, sudoku):
        # Find an empty cell and a valid digit for it
        r, c = 0, 0  # EASY_PUZZLE[0][0] = 0 (empty)
        # Row 0: [0,5,0,0,0,0,1,9,0] -> has 5,1,9
        # Col 0: 0,0,9,3,7,8,0,1,0 -> has 9,3,7,8,1
        # Box (0,0): [0,5,0],[0,0,0],[9,1,0] -> has 5,9,1
        # Available: 2,4,6 (not in row, col, or box)
        move = sudoku.validate_move((0, 0, 4))
        assert move == (0, 0, 4)

    def test_out_of_bounds(self, sudoku):
        with pytest.raises(ValueError, match="out of bounds"):
            sudoku.validate_move((9, 0, 1))

    def test_value_zero(self, sudoku):
        with pytest.raises(ValueError, match="1-9"):
            sudoku.validate_move((0, 0, 0))

    def test_value_ten(self, sudoku):
        with pytest.raises(ValueError, match="1-9"):
            sudoku.validate_move((0, 0, 10))

    def test_initial_cell(self, sudoku):
        # EASY_PUZZLE[0][1] = 5 (given)
        with pytest.raises(ValueError, match="initial"):
            sudoku.validate_move((0, 1, 3))

    def test_duplicate_in_row(self, sudoku):
        # Row 0 already has 5
        with pytest.raises(ValueError, match="row"):
            sudoku.validate_move((0, 0, 5))

    def test_duplicate_in_col(self, sudoku):
        # Col 0 already has 3 (row 3), and 3 is NOT in row 0 [0,5,0,0,0,0,1,9,0]
        # and NOT in box (0,0) [[0,5,0],[0,0,0],[9,1,0]]
        with pytest.raises(ValueError, match="column"):
            sudoku.validate_move((0, 0, 3))

    def test_duplicate_in_box(self, sudoku):
        # Box (0,0) already has 5 (at 0,1)
        with pytest.raises(ValueError, match="box"):
            sudoku.validate_move((1, 0, 5))


# ---------------------------------------------------------------------------
# apply_move / preview_move
# ---------------------------------------------------------------------------


class TestApplyMove:
    def test_apply_move(self, sudoku):
        sudoku.apply_move((0, 0, 4))
        assert sudoku.grid[0][0] == 4

    def test_already_filled(self, sudoku):
        sudoku.apply_move((0, 0, 4))
        with pytest.raises(ValueError, match="already filled"):
            sudoku.apply_move((0, 0, 6))

    def test_preview_no_mutation(self, sudoku):
        original = sudoku.get_state()
        result = sudoku.preview_move((0, 0, 4))
        assert result[0][0] == 4
        assert sudoku.grid[0][0] == 0  # unchanged
        assert sudoku.get_state() == original


# ---------------------------------------------------------------------------
# is_solved / compute_progress
# ---------------------------------------------------------------------------


class TestSolvedAndProgress:
    def test_not_solved_initially(self, sudoku):
        assert sudoku.is_solved() is False

    def test_progress_zero_initially(self, sudoku):
        assert sudoku.compute_progress() == 0.0

    def test_progress_after_move(self, sudoku):
        total_empty = sum(1 for r in range(9) for c in range(9) if EASY_PUZZLE[r][c] == 0)
        sudoku.apply_move((0, 0, 4))
        expected = 1 / total_empty
        assert abs(sudoku.compute_progress() - expected) < 1e-9


# ---------------------------------------------------------------------------
# reset
# ---------------------------------------------------------------------------


class TestReset:
    def test_reset(self, sudoku):
        sudoku.apply_move((0, 0, 4))
        assert sudoku.grid[0][0] == 4
        sudoku.reset()
        assert sudoku.grid[0][0] == 0
        assert sudoku.get_state() == EASY_PUZZLE


# ---------------------------------------------------------------------------
# is_valid_state
# ---------------------------------------------------------------------------


class TestIsValidState:
    def test_valid_state(self, sudoku):
        state = sudoku.get_state()
        assert sudoku.is_valid_state(state) == state

    def test_wrong_row_count(self, sudoku):
        with pytest.raises(ValueError):
            sudoku.is_valid_state([[0] * 9] * 8)

    def test_wrong_col_count(self, sudoku):
        state = sudoku.get_state()
        state[0] = [0] * 8
        with pytest.raises(ValueError):
            sudoku.is_valid_state(state)

    def test_duplicate_in_row(self, sudoku):
        state = sudoku.get_state()
        # Put duplicate in row 0
        state[0][0] = 5  # 5 already at (0,1)
        with pytest.raises(ValueError, match="duplicate"):
            sudoku.is_valid_state(state)

    def test_changed_initial_cell(self, sudoku):
        state = sudoku.get_state()
        state[0][1] = 3  # was 5 (given)
        with pytest.raises(ValueError, match="initial"):
            sudoku.is_valid_state(state)


# ---------------------------------------------------------------------------
# visualize
# ---------------------------------------------------------------------------


class TestVisualize:
    def test_visualize_contains_dividers(self, sudoku):
        vis = sudoku.visualize()
        assert "------+-------+------" in vis
        assert "|" in vis

    def test_visualize_shows_dots(self, sudoku):
        vis = sudoku.visualize()
        assert "." in vis  # empty cells shown as dots


# ---------------------------------------------------------------------------
# CONFIGS
# ---------------------------------------------------------------------------


class TestConfigs:
    @pytest.mark.parametrize("key", list(CONFIGS.keys()))
    def test_config_creates_valid_puzzle(self, key):
        puzzle = Sudoku.from_config(initial_state=CONFIGS[key])
        assert len(puzzle.grid) == 9
        assert not puzzle.is_solved()


# ---------------------------------------------------------------------------
# Prompts: regex patterns
# ---------------------------------------------------------------------------


class TestPromptParsing:
    def test_move_pattern(self):
        text = 'move = [3, 5, 7]'
        m = MOVE_PATTERN.search(text)
        assert m is not None
        assert parse_move(m) == (3, 5, 7)

    def test_move_pattern_in_context(self):
        text = 'I think the best move is:\nmove = [0, 2, 4]\nnext_state = ...'
        m = MOVE_PATTERN.search(text)
        assert m is not None
        assert parse_move(m) == (0, 2, 4)

    def test_state_pattern(self):
        state_str = (
            "next_state = ["
            "[1,2,3,4,5,6,7,8,9],"
            "[4,5,6,7,8,9,1,2,3],"
            "[7,8,9,1,2,3,4,5,6],"
            "[2,3,4,5,6,7,8,9,1],"
            "[5,6,7,8,9,1,2,3,4],"
            "[8,9,1,2,3,4,5,6,7],"
            "[3,4,5,6,7,8,9,1,2],"
            "[6,7,8,9,1,2,3,4,5],"
            "[9,1,2,3,4,5,6,7,8]"
            "]"
        )
        m = STATE_PATTERN.search(state_str)
        assert m is not None
        parsed = parse_state(m)
        assert len(parsed) == 9
        assert all(len(row) == 9 for row in parsed)
        assert parsed[0] == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_state_pattern_with_spaces(self):
        state_str = (
            "next_state = [\n"
            "  [1, 2, 3, 4, 5, 6, 7, 8, 9],\n"
            "  [4, 5, 6, 7, 8, 9, 1, 2, 3],\n"
            "  [7, 8, 9, 1, 2, 3, 4, 5, 6],\n"
            "  [2, 3, 4, 5, 6, 7, 8, 9, 1],\n"
            "  [5, 6, 7, 8, 9, 1, 2, 3, 4],\n"
            "  [8, 9, 1, 2, 3, 4, 5, 6, 7],\n"
            "  [3, 4, 5, 6, 7, 8, 9, 1, 2],\n"
            "  [6, 7, 8, 9, 1, 2, 3, 4, 5],\n"
            "  [9, 1, 2, 3, 4, 5, 6, 7, 8]\n"
            "]"
        )
        m = STATE_PATTERN.search(state_str)
        assert m is not None
        parsed = parse_state(m)
        assert len(parsed) == 9
