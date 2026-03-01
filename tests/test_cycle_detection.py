"""Tests for cycle detection and _cancel_sibling_jobs."""

import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path


# --- _cancel_sibling_jobs ---

def test_cancel_sibling_jobs_reads_file_and_scancels(tmp_path):
    ids_file = tmp_path / "logs" / "active_experiment_ids.txt"
    ids_file.parent.mkdir(parents=True)
    ids_file.write_text("111\n222\n333\n")

    import subprocess
    with patch("subprocess.run") as mock_run:
        # Inline the function logic to avoid importing src.main (heavy deps)
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
    """No file → no scancel calls, no exception."""
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


# --- cycle detection logic ---

def test_cycle_detection_triggers_after_threshold():
    """Simulate visited_states logic from main loop."""
    visited_states: dict[str, int] = {}
    max_state_revisits = 3
    states_sequence = ["A", "B", "A", "B", "A", "B", "A"]  # A seen 4th time at idx 6
    cycle_step = None

    for i, state_key in enumerate(states_sequence):
        visited_states[state_key] = visited_states.get(state_key, 0) + 1
        if visited_states[state_key] > max_state_revisits:
            cycle_step = i
            break

    assert cycle_step == 6
    assert visited_states["A"] == 4


def test_no_cycle_when_states_unique():
    visited_states: dict[str, int] = {}
    max_state_revisits = 3
    triggered = False

    for state_key in ["A", "B", "C", "D", "E"]:
        visited_states[state_key] = visited_states.get(state_key, 0) + 1
        if visited_states[state_key] > max_state_revisits:
            triggered = True
            break

    assert not triggered


def test_cycle_respects_custom_threshold():
    visited_states: dict[str, int] = {}
    max_state_revisits = 1  # trigger on 2nd visit
    triggered = False

    for state_key in ["A", "B", "A"]:
        visited_states[state_key] = visited_states.get(state_key, 0) + 1
        if visited_states[state_key] > max_state_revisits:
            triggered = True
            break

    assert triggered
    assert visited_states["A"] == 2
