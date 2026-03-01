import pytest
from src.tower_of_hanoi.enviroment import TowerOfHanoi
from src.tower_of_hanoi.prompts import parse_move, parse_state, MOVE_PATTERN, STATE_PATTERN


# --- TowerOfHanoi.__init__ ---

def test_init_three_disks():
    env = TowerOfHanoi(3)
    assert env.towers == [[3, 2, 1], [], []]
    assert env.num_disks == 3

def test_init_one_disk():
    env = TowerOfHanoi(1)
    assert env.towers == [[1], [], []]

def test_init_zero_disks():
    env = TowerOfHanoi(0)
    assert env.towers == [[], [], []]


# --- TowerOfHanoi.validate_move ---

def test_validate_move_legal():
    env = TowerOfHanoi(3)
    result = env.validate_move((1, 0, 2))
    assert result == (1, 0, 2)

def test_validate_move_disk_not_on_top():
    env = TowerOfHanoi(3)
    with pytest.raises(ValueError, match="Disk not on top"):
        env.validate_move((2, 0, 2))

def test_validate_move_from_empty_tower():
    env = TowerOfHanoi(3)
    with pytest.raises(ValueError, match="Disk not on top"):
        env.validate_move((1, 1, 2))

def test_validate_move_larger_on_smaller():
    env = TowerOfHanoi(3)
    env.towers = [[3, 2], [1], []]
    with pytest.raises(ValueError, match="Cannot place larger disk on smaller disk"):
        env.validate_move((2, 0, 1))

def test_validate_move_same_size_blocked():
    # Disk 1 on top of tower 0, disk 1 doesn't exist twice but test wrong disk id
    env = TowerOfHanoi(3)
    env.towers = [[3], [2], [1]]
    with pytest.raises(ValueError):
        env.validate_move((3, 0, 1))  # 3 is not on top of tower 1


# --- TowerOfHanoi.move_disk ---

def test_move_disk_updates_state():
    env = TowerOfHanoi(3)
    env.move_disk(1, 0, 2)
    assert env.towers == [[3, 2], [], [1]]

def test_move_disk_chain():
    env = TowerOfHanoi(2)
    env.move_disk(1, 0, 1)
    env.move_disk(2, 0, 2)
    env.move_disk(1, 1, 2)
    assert env.towers == [[], [], [2, 1]]

def test_move_disk_invalid_raises():
    env = TowerOfHanoi(3)
    with pytest.raises(ValueError):
        env.move_disk(3, 0, 2)  # 3 is not on top (1 is)

def test_move_disk_returns_towers():
    env = TowerOfHanoi(3)
    result = env.move_disk(1, 0, 2)
    assert result == env.towers


# --- TowerOfHanoi.is_valid_state ---

def test_is_valid_state_valid():
    env = TowerOfHanoi(3)
    state = [[3, 2], [1], []]
    assert env.is_valid_state(state) == state

def test_is_valid_state_solved():
    env = TowerOfHanoi(3)
    state = [[], [], [3, 2, 1]]
    assert env.is_valid_state(state) == state

def test_is_valid_state_missing_disk():
    env = TowerOfHanoi(3)
    with pytest.raises(ValueError, match="missing or duplicated"):
        env.is_valid_state([[3, 2], [], []])

def test_is_valid_state_duplicate_disk():
    env = TowerOfHanoi(3)
    with pytest.raises(ValueError, match="missing or duplicated"):
        env.is_valid_state([[3, 2, 1], [1], []])

def test_is_valid_state_wrong_order():
    env = TowerOfHanoi(3)
    with pytest.raises(ValueError, match="Larger disk on top"):
        env.is_valid_state([[1, 2, 3], [], []])  # ascending = larger on top


# --- TowerOfHanoi.is_solved ---

def test_is_solved_false_initial():
    env = TowerOfHanoi(3)
    assert not env.is_solved()

def test_is_solved_true():
    env = TowerOfHanoi(3)
    env.towers = [[], [], [3, 2, 1]]
    assert env.is_solved()

def test_is_solved_partial():
    env = TowerOfHanoi(3)
    env.towers = [[], [3], [2, 1]]
    assert not env.is_solved()

def test_is_solved_one_disk():
    env = TowerOfHanoi(1)
    env.move_disk(1, 0, 2)
    assert env.is_solved()


# --- TowerOfHanoi.apply_move ---

def test_apply_move_delegates_to_move_disk():
    env = TowerOfHanoi(3)
    env.apply_move((1, 0, 2))
    assert env.towers == [[3, 2], [], [1]]

def test_apply_move_invalid_raises():
    env = TowerOfHanoi(3)
    with pytest.raises(ValueError):
        env.apply_move((3, 0, 1))


# --- TowerOfHanoi.reset ---

def test_reset_restores_initial_state():
    env = TowerOfHanoi(3)
    env.move_disk(1, 0, 2)
    env.reset()
    assert env.towers == [[3, 2, 1], [], []]

def test_reset_idempotent():
    env = TowerOfHanoi(3)
    env.reset()
    env.reset()
    assert env.towers == [[3, 2, 1], [], []]


# --- TowerOfHanoi.get_state ---

def test_get_state_returns_towers():
    env = TowerOfHanoi(3)
    assert env.get_state() == [[3, 2, 1], [], []]

def test_get_state_after_move():
    env = TowerOfHanoi(3)
    env.move_disk(1, 0, 1)
    assert env.get_state() == [[3, 2], [1], []]


# --- MOVE_PATTERN ---

def test_move_pattern_matches_basic():
    text = "move = [1, 0, 2]"
    assert MOVE_PATTERN.search(text) is not None

def test_move_pattern_case_insensitive():
    assert MOVE_PATTERN.search("MOVE = [2, 0, 1]") is not None

def test_move_pattern_no_match_missing_keyword():
    assert MOVE_PATTERN.search("[1, 0, 2]") is None

def test_move_pattern_no_match_nested():
    # Nested brackets should not match (pattern excludes inner brackets)
    assert MOVE_PATTERN.search("move = [[1, 0], 2]") is None

def test_move_pattern_captures_list():
    m = MOVE_PATTERN.search("move = [1, 0, 2]")
    assert m.group(1) == "[1, 0, 2]"


# --- STATE_PATTERN ---

def test_state_pattern_matches_basic():
    text = "next_state = [[3, 2], [1], []]"
    assert STATE_PATTERN.search(text) is not None

def test_state_pattern_case_insensitive():
    assert STATE_PATTERN.search("NEXT_STATE = [[3], [2], [1]]") is not None

def test_state_pattern_no_match_missing_keyword():
    assert STATE_PATTERN.search("[[3, 2], [1], []]") is None

def test_state_pattern_captures_list():
    text = "next_state = [[3, 2], [1], []]"
    m = STATE_PATTERN.search(text)
    assert m.group(1).strip() == "[[3, 2], [1], []]"

def test_state_pattern_requires_three_sublists():
    # Only two sublists — should not match
    assert STATE_PATTERN.search("next_state = [[3, 2], [1]]") is None


# --- parse_move ---

def test_parse_move_basic():
    text = "move = [1, 0, 2]"
    m = MOVE_PATTERN.search(text)
    assert parse_move(m) == (1, 0, 2)

def test_parse_move_returns_tuple():
    m = MOVE_PATTERN.search("move = [2, 1, 2]")
    result = parse_move(m)
    assert isinstance(result, tuple)

def test_parse_move_with_surrounding_text():
    text = "I will make the move = [1, 0, 2] now."
    m = MOVE_PATTERN.search(text)
    assert parse_move(m) == (1, 0, 2)


# --- parse_state ---

def test_parse_state_basic():
    text = "next_state = [[3, 2], [1], []]"
    m = STATE_PATTERN.search(text)
    assert parse_state(m) == ((3, 2), (1,), ())

def test_parse_state_returns_nested_tuples():
    m = STATE_PATTERN.search("next_state = [[3], [2], [1]]")
    result = parse_state(m)
    assert isinstance(result, tuple)
    assert all(isinstance(t, tuple) for t in result)

def test_parse_state_solved_position():
    text = "next_state = [[], [], [3, 2, 1]]"
    m = STATE_PATTERN.search(text)
    assert parse_state(m) == ((), (), (3, 2, 1))

def test_parse_state_with_surrounding_text():
    text = "After thinking, next_state = [[3, 2], [], [1]] is correct."
    m = STATE_PATTERN.search(text)
    assert parse_state(m) == ((3, 2), (), (1,))
