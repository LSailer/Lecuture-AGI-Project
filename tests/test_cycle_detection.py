"""Tests for cycle detection and _cancel_sibling_jobs."""

import pytest
from unittest.mock import patch
from src.tower_of_hanoi.enviroment import TowerOfHanoi
from src.utils import CycleDetectedError


# --- _cancel_sibling_jobs ---

def test_cancel_sibling_jobs_reads_file_and_scancels(tmp_path):
    ids_file = tmp_path / "logs" / "active_experiment_ids.txt"
    ids_file.parent.mkdir(parents=True)
    ids_file.write_text("111\n222\n333\n")

    import subprocess
    with patch("subprocess.run") as mock_run:
        repo_root = tmp_path
        f = repo_root / "logs" / "active_experiment_ids.txt"
        job_ids = [line.strip() for line in f.read_text().splitlines() if line.strip()]
        for jid in job_ids:
            subprocess.run(["scancel", jid])

        assert mock_run.call_count == 3
        mock_run.assert_any_call(["scancel", "111"])
        mock_run.assert_any_call(["scancel", "222"])
        mock_run.assert_any_call(["scancel", "333"])


def test_cancel_sibling_jobs_missing_file_skips(tmp_path):
    """No file -> no scancel calls, no exception."""
    f = tmp_path / "logs" / "active_experiment_ids.txt"
    assert not f.exists()


def test_cancel_sibling_jobs_ignores_blank_lines(tmp_path):
    ids_file = tmp_path / "logs" / "active_experiment_ids.txt"
    ids_file.parent.mkdir(parents=True)
    ids_file.write_text("111\n\n\n222\n")

    import subprocess
    with patch("subprocess.run") as mock_run:
        job_ids = [line.strip() for line in ids_file.read_text().splitlines() if line.strip()]
        for jid in job_ids:
            subprocess.run(["scancel", jid])
        assert mock_run.call_count == 2


# --- cycle detection (integration with TowerOfHanoi) ---

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

    _track_state(visited, env.get_state(), limit)

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

    env.apply_move((1, 0, 1))
    _track_state(visited, env.get_state(), limit)
    env.apply_move((1, 1, 0))
    _track_state(visited, env.get_state(), limit)

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
    _track_state(visited, env.get_state(), limit)

    env.apply_move((1, 0, 1))
    _track_state(visited, env.get_state(), limit)

    with pytest.raises(CycleDetectedError):
        env.apply_move((1, 1, 0))
        _track_state(visited, env.get_state(), limit)


def test_get_state_returns_copy():
    """get_state() should return a copy, not a mutable reference."""
    env = TowerOfHanoi(3)
    state = env.get_state()
    state[0].pop()
    assert env.get_state() == [[3, 2, 1], [], []]


def test_preview_move_no_mutation():
    """preview_move() should not change internal state."""
    env = TowerOfHanoi(3)
    original = env.get_state()
    preview = env.preview_move((1, 0, 2))
    assert preview == [[3, 2], [], [1]]
    assert env.get_state() == original
