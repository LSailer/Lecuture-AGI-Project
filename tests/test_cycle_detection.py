import pytest
from src.tower_of_hanoi.enviroment import TowerOfHanoi
from src.utils import CycleDetectedError


def _track_state(visited, state, limit):
    """Simulate the cycle detection logic from main.py."""
    key = str(state)
    visited[key] = visited.get(key, 0) + 1
    if visited[key] > limit:
        raise CycleDetectedError(
            f"State visited {visited[key]} times (limit {limit}): {key}"
        )


def test_cycle_detected_on_oscillation():
    """Moves that return to the same state should trigger CycleDetectedError."""
    env = TowerOfHanoi(3)
    visited: dict[str, int] = {}
    limit = 3

    # Count initial state
    _track_state(visited, env.get_state(), limit)

    # Oscillate: move disk 1 back and forth (visits initial state repeatedly)
    with pytest.raises(CycleDetectedError):
        for _ in range(10):
            env.apply_move((1, 0, 1))
            _track_state(visited, env.get_state(), limit)
            env.apply_move((1, 1, 0))
            _track_state(visited, env.get_state(), limit)


def test_no_error_within_limit():
    """Revisiting a state within the limit should NOT raise."""
    env = TowerOfHanoi(3)
    visited: dict[str, int] = {}
    limit = 3

    _track_state(visited, env.get_state(), limit)

    # Visit initial state 2 more times (total 3 = limit, should be fine)
    env.apply_move((1, 0, 1))
    _track_state(visited, env.get_state(), limit)
    env.apply_move((1, 1, 0))
    _track_state(visited, env.get_state(), limit)  # 2nd visit

    env.apply_move((1, 0, 1))
    _track_state(visited, env.get_state(), limit)
    env.apply_move((1, 1, 0))
    _track_state(visited, env.get_state(), limit)  # 3rd visit = limit, still ok


def test_error_on_exceeding_limit():
    """One visit beyond the limit should raise."""
    env = TowerOfHanoi(3)
    visited: dict[str, int] = {}
    limit = 2

    _track_state(visited, env.get_state(), limit)

    env.apply_move((1, 0, 1))
    _track_state(visited, env.get_state(), limit)
    env.apply_move((1, 1, 0))
    _track_state(visited, env.get_state(), limit)  # 2nd = limit

    env.apply_move((1, 0, 1))
    _track_state(visited, env.get_state(), limit)

    with pytest.raises(CycleDetectedError):
        env.apply_move((1, 1, 0))
        _track_state(visited, env.get_state(), limit)  # 3rd > limit


def test_get_state_returns_copy():
    """get_state() should return a copy, not a mutable reference."""
    env = TowerOfHanoi(3)
    state = env.get_state()
    state[0].pop()  # mutate the returned copy
    assert env.get_state() == [[3, 2, 1], [], []]  # original unchanged


def test_preview_move_no_mutation():
    """preview_move() should not change internal state."""
    env = TowerOfHanoi(3)
    original = env.get_state()
    preview = env.preview_move((1, 0, 2))
    assert preview == [[3, 2], [], [1]]
    assert env.get_state() == original
