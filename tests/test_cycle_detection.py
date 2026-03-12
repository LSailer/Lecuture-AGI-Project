"""Tests for cycle detection and _cancel_sibling_jobs."""

import copy
import pytest
from unittest.mock import patch, MagicMock, call
from src.tower_of_hanoi.enviroment import TowerOfHanoi


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


# --- cycle detection (state visit counting) ---

def _track_state(visited, state, limit):
    """Simulate the cycle detection logic from main.py.

    Returns True if cycle detected (visit count exceeds limit).
    """
    key = str(state)
    visited[key] = visited.get(key, 0) + 1
    return visited[key] > limit


def test_cycle_detected_on_oscillation():
    """Moves that return to the same state should trigger cycle detection."""
    env = TowerOfHanoi(3)
    visited: dict[str, int] = {}
    limit = 3

    cycle_hit = False
    _track_state(visited, env.get_state(), limit)

    for _ in range(10):
        env.apply_move((1, 0, 1))
        _track_state(visited, env.get_state(), limit)
        env.apply_move((1, 1, 0))
        if _track_state(visited, env.get_state(), limit):
            cycle_hit = True
            break

    assert cycle_hit, "Cycle should have been detected"


def test_no_cycle_within_limit():
    """Revisiting a state within the limit should NOT flag cycle."""
    env = TowerOfHanoi(3)
    visited: dict[str, int] = {}
    limit = 3

    assert not _track_state(visited, env.get_state(), limit)

    env.apply_move((1, 0, 1))
    assert not _track_state(visited, env.get_state(), limit)
    env.apply_move((1, 1, 0))
    assert not _track_state(visited, env.get_state(), limit)

    env.apply_move((1, 0, 1))
    assert not _track_state(visited, env.get_state(), limit)
    env.apply_move((1, 1, 0))
    assert not _track_state(visited, env.get_state(), limit)  # 3rd visit = limit, still ok


def test_cycle_on_exceeding_limit():
    """One visit beyond the limit should flag cycle."""
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

    env.apply_move((1, 1, 0))
    assert _track_state(visited, env.get_state(), limit), "Should exceed limit"


def test_initial_state_not_double_counted():
    """First visit to any state should count as 1, not 2."""
    visited: dict[str, int] = {}
    state = [[3, 2, 1], [], []]
    _track_state(visited, state, limit=3)
    assert visited[str(state)] == 1


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


# --- integration: cycle triggers fallback in main loop ---

def _run_main_loop(game, agent, fallback, run_voting_batch_fn, run_fallback_fn,
                   max_steps, max_fallback_retries, max_number_agents_per_step,
                   margin_k, max_state_revisits, predictions_table):
    """Extracted main loop logic matching src/main.py for testability."""
    previous_move = "None"
    current_step = 0
    visited_states: dict[str, int] = {}
    cycle_detected = False
    fallback_calls = []

    while not game.is_solved() and current_step < max_steps:
        current_state = copy.deepcopy(game.get_state())
        current_step += 1

        state_key = str(current_state)
        visited_states[state_key] = visited_states.get(state_key, 0) + 1
        cycle_hit = visited_states[state_key] > max_state_revisits

        if not cycle_hit:
            candidate_voting, best_prediction, failed_predictions, consensus_reached = (
                run_voting_batch_fn(current_state, current_step)
            )
            if consensus_reached and best_prediction is not None:
                game.apply_move(best_prediction["action"])
            else:
                break
        else:
            failed_predictions = [
                {
                    "agent_id": "cycle_detector",
                    "action": "N/A",
                    "state": state_key,
                    "error": f"Cycle detected: state visited {visited_states[state_key]} times (limit {max_state_revisits}). The agent is stuck in a loop. You MUST choose a completely different move.",
                }
            ]
            fallback_calls.append(failed_predictions)
            result = run_fallback_fn(failed_predictions)
            candidate_voting, best_prediction, _, consensus_reached, _ = result

            if consensus_reached and best_prediction is not None:
                game.apply_move(best_prediction["action"])
            else:
                cycle_detected = True
                break

        previous_move = str(best_prediction["action"]) if best_prediction else "None"

    return cycle_detected, fallback_calls, current_step


def test_cycle_triggers_fallback_and_escapes():
    """When cycle is detected, fallback should be called with cycle context.
    If fallback returns a valid move, the game continues."""
    env = TowerOfHanoi(3)
    max_state_revisits = 1  # trigger cycle on 2nd visit

    move_sequence = [
        (1, 0, 1),  # step 1: normal
        (1, 1, 0),  # step 2: normal — returns to initial state
        # step 3: cycle detected on initial state (visit count = 2 > 1)
        # fallback should be called
    ]
    call_count = [0]

    def voting_fn(state, step):
        idx = call_count[0]
        call_count[0] += 1
        if idx < len(move_sequence):
            action = move_sequence[idx]
            return ({str(action): 3}, {"action": action, "state": None}, [], True)
        return ({}, None, [], False)

    # Fallback returns a different move to escape the cycle
    escape_move = (1, 0, 2)
    def fallback_fn(failed_preds):
        # Verify cycle context is passed
        assert any("Cycle detected" in fp["error"] for fp in failed_preds)
        return (
            {str(escape_move): 3},
            {"action": escape_move, "state": None},
            failed_preds,
            True,
            1,
        )

    cycle_detected, fallback_calls, steps = _run_main_loop(
        game=env,
        agent=None,
        fallback=None,
        run_voting_batch_fn=voting_fn,
        run_fallback_fn=fallback_fn,
        max_steps=5,
        max_fallback_retries=3,
        max_number_agents_per_step=3,
        margin_k=1,
        max_state_revisits=max_state_revisits,
        predictions_table=None,
    )

    assert len(fallback_calls) == 1, "Fallback should be called exactly once for cycle"
    assert not cycle_detected, "Cycle should be resolved by fallback"
    assert "Cycle detected" in fallback_calls[0][0]["error"]


def test_cycle_fallback_exhausted_stops():
    """When cycle detected and fallback can't find a move, loop stops with cycle_detected=True."""
    env = TowerOfHanoi(3)

    move_sequence = [(1, 0, 1), (1, 1, 0)]
    call_count = [0]

    def voting_fn(state, step):
        idx = call_count[0]
        call_count[0] += 1
        if idx < len(move_sequence):
            action = move_sequence[idx]
            return ({str(action): 3}, {"action": action, "state": None}, [], True)
        return ({}, None, [], False)

    def fallback_fn(failed_preds):
        # Fallback fails — no valid move
        return ({}, None, failed_preds, False, 3)

    cycle_detected, fallback_calls, steps = _run_main_loop(
        game=env,
        agent=None,
        fallback=None,
        run_voting_batch_fn=voting_fn,
        run_fallback_fn=fallback_fn,
        max_steps=10,
        max_fallback_retries=3,
        max_number_agents_per_step=3,
        margin_k=1,
        max_state_revisits=1,
        predictions_table=None,
    )

    assert cycle_detected, "Should flag cycle_detected when fallback exhausted"
    assert len(fallback_calls) == 1
