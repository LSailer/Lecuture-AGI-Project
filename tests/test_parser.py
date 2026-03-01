import pytest

from src.utils.parser import Parser
from src.sliding_puzzle.enviroment import SlidingPuzzle
from src.sliding_puzzle.prompts import MOVE_PATTERN, STATE_PATTERN, parse_move, parse_state

# A solvable 3x3 state with blank at index 7 (bottom-center)
# Goal: [1,2,3,4,5,6,7,8,0]  — moving blank RIGHT reaches goal
INITIAL_STATE = [1, 2, 3, 4, 5, 6, 7, 0, 8]


@pytest.fixture
def puzzle():
    return SlidingPuzzle(INITIAL_STATE)


@pytest.fixture
def parser(puzzle):
    return Parser(puzzle, MOVE_PATTERN, STATE_PATTERN, parse_move, parse_state)


# move=RIGHT is valid: blank at index 7, tile 8 is at index 8, moving blank RIGHT swaps them
VALID_RESPONSE = "move = RIGHT\nnext_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]"


def test_valid_response(parser):
    move, state = parser.parse_action_state(VALID_RESPONSE)
    assert move == (8, "left")  # validate_move returns (tile, opposite_dir)
    assert state == [1, 2, 3, 4, 5, 6, 7, 8, 0]


def test_missing_move_raises(parser):
    response = "next_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]"
    with pytest.raises(ValueError, match="Could not find move or next_state"):
        parser.parse_action_state(response)


def test_missing_state_raises(parser):
    response = "move = RIGHT"
    with pytest.raises(ValueError, match="Could not find move or next_state"):
        parser.parse_action_state(response)


def test_uses_last_match(parser):
    # First match is UP (would be invalid anyway, but last match RIGHT is used)
    response = (
        "move = UP\n"
        "Some reasoning here...\n"
        "move = RIGHT\n"
        "next_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]"
    )
    move, state = parser.parse_action_state(response)
    # If first match (UP) were used it would raise; RIGHT succeeds
    assert move == (8, "left")
    assert state == [1, 2, 3, 4, 5, 6, 7, 8, 0]
