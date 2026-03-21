from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple, Optional


Cell = int  # -1 unknown, 0 empty, 1 filled
Move = Tuple[int, int, int]  # row, col, value (0 empty, 1 filled)

CONFIGS = {
    "5x5 (diamond)": {
        "row_hints": [[1], [3], [5], [3], [1]],
        "col_hints": [[1], [3], [5], [3], [1]],
    },
    "5x5 (cross)": {
        "row_hints": [[1, 1], [5], [1, 1], [5], [1, 1]],
        "col_hints": [[1, 1], [5], [1, 1], [5], [1, 1]],
    },
    "5x5 (arrow)": {
        "row_hints": [[1], [2], [5], [2], [1]],
        "col_hints": [[1], [1], [5], [1, 1], [1]],
    },
    "5x5 (checkerboard)": {
        "row_hints": [[1, 1, 1], [1, 1], [1, 1, 1], [1, 1], [1, 1, 1]],
        "col_hints": [[1, 1, 1], [1, 1], [1, 1, 1], [1, 1], [1, 1, 1]],
    },
    "7x7 (heart)": {
        "row_hints": [[2, 2], [5], [7], [7], [5], [3], [1]],
        "col_hints": [[2], [4], [6], [5], [6], [4], [2]],
    },
    "10x10 (oval)": {
        "row_hints": [[4], [6], [8], [10], [10], [10], [10], [8], [6], [4]],
        "col_hints": [[4], [6], [8], [10], [10], [10], [10], [8], [6], [4]],
    },
    "10x10 (star)": {
        "row_hints": [[2], [4], [10], [4], [6], [6], [4], [10], [4], [2]],
        "col_hints": [[2], [4], [10], [4], [6], [6], [4], [10], [4], [2]],
    },
}


def _line_feasible(cells: List[Cell], hints: List[int]) -> bool:
    """
    Return True iff there exists a completion of `cells` (with -1 as unknown)
    that matches `hints` exactly (standard Nonogram line feasibility).
    Uses DP over positions and hint index.
    """
    n = len(cells)
    m = len(hints)

    if m == 0:
        return all(c != 1 for c in cells)
    min_len = sum(hints) + (m - 1)
    if min_len > n:
        return False

    from functools import lru_cache

    @lru_cache(None)
    def dp(pos: int, h: int, run: int) -> bool:
        if pos == n:
            if run > 0:
                return h < m and run == hints[h] and h == m - 1
            return h == m

        cell = cells[pos]

        def can_be_empty() -> bool:
            return cell in (-1, 0)

        def can_be_filled() -> bool:
            return cell in (-1, 1)

        if can_be_empty():
            if run > 0:
                if h < m and run == hints[h]:
                    if dp(pos + 1, h + 1, 0):
                        return True
            else:
                if dp(pos + 1, h, 0):
                    return True

        if can_be_filled():
            if h >= m:
                return False
            new_run = run + 1
            if new_run <= hints[h]:
                if dp(pos + 1, h, new_run):
                    return True

        return False

    return dp(0, 0, 0)


def _line_satisfied(cells: List[Cell], hints: List[int]) -> bool:
    """Exact satisfaction (no unknowns) for solved check."""
    if any(c == -1 for c in cells):
        return False
    groups: List[int] = []
    run = 0
    for c in cells:
        if c == 1:
            run += 1
        else:
            if run > 0:
                groups.append(run)
                run = 0
    if run > 0:
        groups.append(run)
    return groups == hints


@dataclass
class Nonogram:
    row_hints: List[List[int]]
    col_hints: List[List[int]]
    grid: List[List[Cell]]

    @classmethod
    def from_config(
        cls,
        row_hints: List[List[int]],
        col_hints: List[List[int]],
        initial_state: Optional[List[List[int]]] = None,
    ) -> "Nonogram":
        rows = len(row_hints)
        cols = len(col_hints)
        if initial_state is None:
            grid = [[-1 for _ in range(cols)] for _ in range(rows)]
        else:
            grid = initial_state
        env = cls(row_hints=row_hints, col_hints=col_hints, grid=grid)
        env.is_valid_state(env.grid)
        return env

    @property
    def n_rows(self) -> int:
        return len(self.row_hints)

    @property
    def n_cols(self) -> int:
        return len(self.col_hints)

    def get_state(self):
        return [row[:] for row in self.grid]

    def preview_move(self, action) -> list:
        """Return resulting state after action WITHOUT mutating self."""
        r, c, v = action
        grid = [row[:] for row in self.grid]
        grid[r][c] = v
        return grid

    def reset(self):
        self.grid = [[-1 for _ in range(self.n_cols)] for _ in range(self.n_rows)]

    def visualize(self) -> str:
        mapping = {-1: ".", 0: "x", 1: "#"}
        lines = []
        for r in range(self.n_rows):
            lines.append("".join(mapping[self.grid[r][c]] for c in range(self.n_cols)))
        return "\n".join(lines)

    def validate_move(self, move: Move) -> Move:
        r, c, v = move
        if not (0 <= r < self.n_rows and 0 <= c < self.n_cols):
            raise ValueError("Invalid move: row/col out of bounds.")
        if v not in (0, 1):
            raise ValueError("Invalid move: value must be 0 (empty) or 1 (filled).")
        if self.grid[r][c] != -1:
            raise ValueError("Invalid move: cell already decided.")

        test_grid = [row[:] for row in self.grid]
        test_grid[r][c] = v
        row = test_grid[r]
        col = [test_grid[i][c] for i in range(self.n_rows)]

        if not _line_feasible(row, self.row_hints[r]):
            raise ValueError("Invalid move: makes row impossible.")
        if not _line_feasible(col, self.col_hints[c]):
            raise ValueError("Invalid move: makes column impossible.")
        return move

    def is_valid_state(self, state):
        if not isinstance(state, list) or len(state) != self.n_rows:
            raise ValueError("Invalid state: wrong number of rows.")
        for r in range(self.n_rows):
            if not isinstance(state[r], list) or len(state[r]) != self.n_cols:
                raise ValueError("Invalid state: wrong number of cols in a row.")
            for c in range(self.n_cols):
                if state[r][c] not in (-1, 0, 1):
                    raise ValueError("Invalid state: cell values must be -1/0/1.")

        for r in range(self.n_rows):
            if not _line_feasible(list(state[r]), self.row_hints[r]):
                raise ValueError(f"Invalid state: row {r} impossible.")
        for c in range(self.n_cols):
            col = [state[r][c] for r in range(self.n_rows)]
            if not _line_feasible(col, self.col_hints[c]):
                raise ValueError(f"Invalid state: col {c} impossible.")
        return state

    def apply_move(self, action):
        r, c, v = action
        self.validate_move((r, c, v))
        self.grid[r][c] = v

    def is_solved(self) -> bool:
        for r in range(self.n_rows):
            if not _line_satisfied(self.grid[r], self.row_hints[r]):
                return False
        for c in range(self.n_cols):
            col = [self.grid[r][c] for r in range(self.n_rows)]
            if not _line_satisfied(col, self.col_hints[c]):
                return False
        return True

    def compute_progress(self) -> float:
        total = self.n_rows * self.n_cols
        decided = sum(1 for row in self.grid for c in row if c != -1)
        return decided / total