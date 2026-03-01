import pytest
from src.sliding_puzzle.enviroment import SlidingPuzzle
from src.sliding_puzzle.prompts import parse_move, parse_state, MOVE_PATTERN, STATE_PATTERN

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

SOLVED_3x3 = [1, 2, 3, 4, 5, 6, 7, 8, 0]
# One move from solved: tile 8 is at index 7, blank at index 8 -> move tile 8 right
ONE_AWAY_3x3 = [1, 2, 3, 4, 5, 6, 7, 0, 8]  # blank col=1, tile 8 col=2
SOLVED_4x4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]


@pytest.fixture
def puzzle_3x3():
    return SlidingPuzzle(ONE_AWAY_3x3)


@pytest.fixture
def puzzle_solved():
    return SlidingPuzzle(SOLVED_3x3)


# ---------------------------------------------------------------------------
# __init__
# ---------------------------------------------------------------------------


class TestInit:
    def test_valid_3x3(self):
        p = SlidingPuzzle(ONE_AWAY_3x3)
        assert p.size == 9
        assert p.grid_size == 3
        assert p.state == ONE_AWAY_3x3

    def test_valid_4x4(self):
        p = SlidingPuzzle(SOLVED_4x4)
        assert p.size == 16
        assert p.grid_size == 4

    def test_goal_state_3x3(self):
        p = SlidingPuzzle(ONE_AWAY_3x3)
        assert p.goal_state == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def test_none_raises(self):
        with pytest.raises((ValueError, TypeError)):
            SlidingPuzzle(None)

    def test_non_square_raises(self):
        with pytest.raises(ValueError):
            SlidingPuzzle([1, 2, 3, 4, 5, 0])  # 6 tiles, not square

    def test_unsolvable_raises(self):
        # Swap tiles 1 and 2 in solved state -> odd inversions -> unsolvable
        with pytest.raises(ValueError):
            SlidingPuzzle([2, 1, 3, 4, 5, 6, 7, 8, 0])

    def test_state_is_copy(self):
        original = list(ONE_AWAY_3x3)
        p = SlidingPuzzle(original)
        original[0] = 99
        assert p.state[0] != 99


# ---------------------------------------------------------------------------
# _is_solvable
# ---------------------------------------------------------------------------


class TestIsSolvable:
    def test_solved_state_solvable(self):
        p = SlidingPuzzle(SOLVED_3x3)
        assert p._is_solvable(SOLVED_3x3) is True

    def test_one_away_solvable(self):
        p = SlidingPuzzle(SOLVED_3x3)
        assert p._is_solvable(ONE_AWAY_3x3) is True

    def test_unsolvable_state(self):
        p = SlidingPuzzle(SOLVED_3x3)
        # Adjacent swap of two non-zero tiles = odd inversions
        assert p._is_solvable([2, 1, 3, 4, 5, 6, 7, 8, 0]) is False

    def test_two_swaps_solvable(self):
        p = SlidingPuzzle(SOLVED_3x3)
        # Two swaps = even inversions -> solvable
        assert p._is_solvable([2, 1, 4, 3, 5, 6, 7, 8, 0]) is True


# ---------------------------------------------------------------------------
# validate_move (tuple form)
# ---------------------------------------------------------------------------


class TestValidateMoveTuple:
    def test_valid_move_returns_move(self, puzzle_3x3):
        # State: [1,2,3,4,5,6,7,0,8], blank at (2,1), tile 8 at (2,2)
        # tile 8 moving left -> blank is to the left of tile 8
        result = puzzle_3x3.validate_move((8, "left"))
        assert result == (8, "left")

    def test_invalid_tile_raises(self, puzzle_3x3):
        with pytest.raises(ValueError, match="not in puzzle"):
            puzzle_3x3.validate_move((99, "left"))

    def test_tile_zero_raises(self, puzzle_3x3):
        with pytest.raises(ValueError, match="Cannot move empty space"):
            puzzle_3x3.validate_move((0, "up"))

    def test_out_of_bounds_raises(self, puzzle_solved):
        # Solved state: blank at (2,2), tile 3 at (0,2) -> moving tile 3 up is out of bounds
        with pytest.raises(ValueError):
            puzzle_solved.validate_move((3, "up"))

    def test_not_adjacent_raises(self, puzzle_3x3):
        # tile 1 is at (0,0), blank at (2,1) -> not adjacent
        with pytest.raises(ValueError, match="not adjacent"):
            puzzle_3x3.validate_move((1, "down"))

    def test_invalid_direction_raises(self, puzzle_3x3):
        with pytest.raises(ValueError, match="Invalid direction"):
            puzzle_3x3.validate_move((8, "diagonal"))


# ---------------------------------------------------------------------------
# validate_move (string form)
# ---------------------------------------------------------------------------


class TestValidateMoveString:
    def test_string_right_returns_tile_and_opposite(self, puzzle_3x3):
        # State [1,2,3,4,5,6,7,0,8]: blank at (2,1), moving blank RIGHT -> tile at (2,2)=8
        tile, direction = puzzle_3x3.validate_move("right")
        assert tile == 8
        assert direction == "left"

    def test_string_left_blank_at_left_edge_raises(self, puzzle_solved):
        # Solved: blank at (2,2). Moving blank LEFT -> tile at (2,1)=8
        tile, direction = puzzle_solved.validate_move("left")
        assert tile == 8
        assert direction == "right"

    def test_string_out_of_bounds_raises(self, puzzle_solved):
        # Solved: blank at (2,2). Moving blank RIGHT is out of bounds
        with pytest.raises(ValueError, match="No tile in that direction"):
            puzzle_solved.validate_move("right")

    def test_string_up_returns_correct_tile(self, puzzle_solved):
        # Solved: blank at (2,2). Tile above is at (1,2)=6
        tile, direction = puzzle_solved.validate_move("up")
        assert tile == 6
        assert direction == "down"


# ---------------------------------------------------------------------------
# move_tile
# ---------------------------------------------------------------------------


class TestMoveTile:
    def test_move_swaps_tile_and_blank(self, puzzle_3x3):
        # [1,2,3,4,5,6,7,0,8]: move tile 8 left
        state = puzzle_3x3.move_tile(8, "left")
        assert state == SOLVED_3x3

    def test_move_returns_state(self, puzzle_3x3):
        result = puzzle_3x3.move_tile(8, "left")
        assert result is puzzle_3x3.state

    def test_move_updates_internal_state(self, puzzle_3x3):
        puzzle_3x3.move_tile(8, "left")
        assert puzzle_3x3.get_state() == SOLVED_3x3

    def test_invalid_move_raises(self, puzzle_3x3):
        with pytest.raises(ValueError):
            puzzle_3x3.move_tile(1, "down")


# ---------------------------------------------------------------------------
# is_valid_state
# ---------------------------------------------------------------------------


class TestIsValidState:
    def test_valid_state(self, puzzle_3x3):
        result = puzzle_3x3.is_valid_state(list(range(9)))
        assert result == list(range(9))

    def test_wrong_length_raises(self, puzzle_3x3):
        with pytest.raises(ValueError, match="exactly"):
            puzzle_3x3.is_valid_state([1, 2, 3])

    def test_duplicates_raises(self, puzzle_3x3):
        with pytest.raises(ValueError):
            puzzle_3x3.is_valid_state([1, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_missing_tile_raises(self, puzzle_3x3):
        with pytest.raises(ValueError):
            puzzle_3x3.is_valid_state([0, 1, 2, 3, 4, 5, 6, 7, 9])


# ---------------------------------------------------------------------------
# is_solved
# ---------------------------------------------------------------------------


class TestIsSolved:
    def test_solved_state(self, puzzle_solved):
        assert puzzle_solved.is_solved() is True

    def test_unsolved_state(self, puzzle_3x3):
        assert puzzle_3x3.is_solved() is False

    def test_becomes_solved_after_move(self, puzzle_3x3):
        puzzle_3x3.move_tile(8, "left")
        assert puzzle_3x3.is_solved() is True


# ---------------------------------------------------------------------------
# apply_move
# ---------------------------------------------------------------------------


class TestApplyMove:
    def test_apply_move_delegates_to_move_tile(self, puzzle_3x3):
        puzzle_3x3.apply_move((8, "left"))
        assert puzzle_3x3.get_state() == SOLVED_3x3

    def test_apply_invalid_move_raises(self, puzzle_3x3):
        with pytest.raises(ValueError):
            puzzle_3x3.apply_move((1, "down"))


# ---------------------------------------------------------------------------
# reset
# ---------------------------------------------------------------------------


class TestReset:
    def test_reset_restores_goal_state(self, puzzle_3x3):
        puzzle_3x3.reset()
        assert puzzle_3x3.get_state() == puzzle_3x3.goal_state

    def test_reset_after_moves(self, puzzle_3x3):
        puzzle_3x3.move_tile(8, "left")
        puzzle_3x3.reset()
        assert puzzle_3x3.is_solved() is True

    def test_reset_state_is_copy(self, puzzle_3x3):
        puzzle_3x3.reset()
        puzzle_3x3.state[0] = 99
        assert puzzle_3x3.goal_state[0] != 99


# ---------------------------------------------------------------------------
# visualize
# ---------------------------------------------------------------------------


class TestVisualize:
    def test_visualize_returns_string(self, puzzle_3x3):
        assert isinstance(puzzle_3x3.visualize(), str)

    def test_visualize_line_count(self, puzzle_3x3):
        lines = puzzle_3x3.visualize().split("\n")
        assert len(lines) == puzzle_3x3.grid_size

    def test_visualize_solved(self, puzzle_solved):
        viz = puzzle_solved.visualize()
        assert "[1, 2, 3]" in viz
        assert "[7, 8, 0]" in viz

    def test_visualize_4x4_line_count(self):
        p = SlidingPuzzle(SOLVED_4x4)
        lines = p.visualize().split("\n")
        assert len(lines) == 4


# ---------------------------------------------------------------------------
# parse_move / parse_state
# ---------------------------------------------------------------------------


class TestParseMove:
    def test_extracts_down_lowercase(self):
        m = MOVE_PATTERN.search("move = DOWN")
        assert parse_move(m) == "down"

    def test_extracts_up_lowercase(self):
        m = MOVE_PATTERN.search("move = UP")
        assert parse_move(m) == "up"

    def test_extracts_left_lowercase(self):
        m = MOVE_PATTERN.search("move = LEFT")
        assert parse_move(m) == "left"

    def test_extracts_right_lowercase(self):
        m = MOVE_PATTERN.search("move = RIGHT")
        assert parse_move(m) == "right"

    def test_case_insensitive_match(self):
        m = MOVE_PATTERN.search("Move = DOWN")
        assert m is not None
        assert parse_move(m) == "down"


class TestParseState:
    def test_extracts_list(self):
        m = STATE_PATTERN.search("next_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]")
        result = parse_state(m)
        assert result == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def test_returns_python_list(self):
        m = STATE_PATTERN.search("next_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]")
        assert isinstance(parse_state(m), list)

    def test_multiline_context(self):
        text = "move = RIGHT\nnext_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]"
        m = STATE_PATTERN.search(text)
        assert parse_state(m) == [1, 2, 3, 4, 5, 6, 7, 8, 0]


# ---------------------------------------------------------------------------
# MOVE_PATTERN / STATE_PATTERN regex
# ---------------------------------------------------------------------------


class TestPatterns:
    def test_move_pattern_matches_all_directions(self):
        for direction in ("UP", "DOWN", "LEFT", "RIGHT"):
            assert MOVE_PATTERN.search(f"move = {direction}") is not None

    def test_move_pattern_no_match_garbage(self):
        assert MOVE_PATTERN.search("move = DIAGONAL") is None

    def test_move_pattern_no_match_partial_word(self):
        assert MOVE_PATTERN.search("movement = UP") is None

    def test_state_pattern_matches(self):
        assert STATE_PATTERN.search("next_state = [1, 2, 3]") is not None

    def test_state_pattern_no_match_wrong_key(self):
        assert STATE_PATTERN.search("state = [1, 2, 3]") is None

    def test_state_pattern_no_match_nested_brackets(self):
        # nested brackets not matched by [^\[\]]+
        assert STATE_PATTERN.search("next_state = [[1, 2], [3]]") is None

    def test_move_pattern_case_insensitive_keyword(self):
        assert MOVE_PATTERN.search("MOVE = UP") is not None

    def test_state_pattern_case_insensitive_keyword(self):
        assert STATE_PATTERN.search("NEXT_STATE = [1, 2, 3]") is not None
