from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple, Optional


Cell = int  # 0 empty, 1-9 digits
Move = Tuple[int, int, int]  # row, col, value

CONFIGS = {
    "easy": [
        [0, 5, 0, 0, 0, 0, 1, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 2],
        [9, 1, 0, 0, 2, 7, 5, 6, 8],
        [3, 4, 5, 0, 0, 1, 9, 0, 6],
        [7, 0, 0, 3, 4, 0, 0, 0, 0],
        [8, 9, 0, 2, 0, 6, 0, 0, 3],
        [0, 0, 8, 7, 0, 0, 2, 1, 0],
        [1, 6, 0, 0, 0, 8, 0, 0, 4],
        [0, 0, 0, 1, 0, 0, 6, 8, 5],
    ],
    "medium": [
        [2, 0, 3, 4, 0, 0, 0, 0, 5],
        [8, 0, 9, 1, 6, 0, 7, 0, 4],
        [0, 0, 6, 0, 3, 0, 0, 1, 9],
        [7, 0, 2, 0, 0, 3, 0, 6, 0],
        [0, 0, 8, 2, 5, 0, 0, 0, 0],
        [0, 0, 1, 6, 0, 7, 0, 0, 2],
        [0, 0, 7, 0, 0, 5, 9, 2, 6],
        [9, 3, 0, 7, 2, 0, 0, 0, 0],
        [6, 0, 0, 0, 9, 0, 4, 7, 0],
    ],
    "hard": [
        [1, 0, 0, 0, 3, 4, 0, 0, 8],
        [0, 7, 0, 6, 8, 0, 0, 3, 0],
        [0, 0, 8, 2, 1, 0, 7, 0, 4],
        [0, 5, 4, 0, 9, 0, 6, 8, 0],
        [9, 1, 0, 5, 0, 8, 0, 2, 0],
        [0, 8, 0, 3, 0, 0, 0, 0, 5],
        [3, 0, 5, 9, 0, 6, 8, 7, 1],
        [0, 0, 6, 0, 0, 0, 0, 4, 0],
        [0, 0, 1, 0, 7, 0, 2, 0, 0],
    ],
    "expert": [
        [1, 5, 0, 0, 8, 2, 0, 0, 0],
        [3, 0, 0, 0, 7, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 7, 5, 3],
        [0, 0, 0, 5, 2, 7, 6, 0, 9],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 4, 0, 0, 6, 3, 8, 0, 7],
        [4, 0, 0, 0, 0, 8, 0, 0, 0],
        [7, 0, 3, 0, 4, 0, 1, 0, 0],
        [0, 0, 8, 6, 0, 0, 3, 0, 0],
    ],
    "master": [
        [0, 0, 9, 5, 8, 6, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 6, 8, 3],
        [9, 0, 0, 6, 5, 0, 0, 3, 2],
        [0, 6, 0, 7, 0, 0, 0, 9, 8],
        [0, 3, 0, 2, 0, 0, 7, 0, 4],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [6, 2, 0, 0, 1, 5, 0, 4, 0],
        [0, 0, 0, 4, 0, 0, 0, 5, 0],
    ],
}

@dataclass
class Sudoku:
    grid: List[List[Cell]]
    initial_grid: List[List[Cell]] = field(repr=False)

    @classmethod
    def from_config(
        cls,
        initial_state: List[List[int]],
    ) -> "Sudoku":
        grid = [row[:] for row in initial_state]
        env = cls(grid=grid, initial_grid=[row[:] for row in initial_state])
        env.is_valid_state(env.grid)
        return env

    def get_state(self):
        return [row[:] for row in self.grid]

    def preview_move(self, action) -> list:
        r, c, v = action
        grid = [row[:] for row in self.grid]
        grid[r][c] = v
        return grid

    def reset(self):
        self.grid = [row[:] for row in self.initial_grid]

    def visualize(self) -> str:
        lines = []
        for r in range(9):
            parts = []
            for c in range(9):
                v = self.grid[r][c]
                parts.append(str(v) if v != 0 else ".")
            row_str = " ".join(parts[:3]) + " | " + " ".join(parts[3:6]) + " | " + " ".join(parts[6:])
            lines.append(row_str)
            if r in (2, 5):
                lines.append("------+-------+------")
        return "\n".join(lines)

    def validate_move(self, move: Move) -> Move:
        r, c, v = move
        if not (0 <= r <= 8 and 0 <= c <= 8):
            raise ValueError("Invalid move: row/col out of bounds (must be 0-8).")
        if not (1 <= v <= 9):
            raise ValueError("Invalid move: value must be 1-9.")
        if self.initial_grid[r][c] != 0:
            raise ValueError("Invalid move: cannot modify initial given cell.")
        if self.grid[r][c] != 0:
            raise ValueError("Invalid move: cell already filled.")
        # Row check
        if v in self.grid[r]:
            raise ValueError(f"Invalid move: value {v} already in row {r}.")
        # Column check
        if v in [self.grid[i][c] for i in range(9)]:
            raise ValueError(f"Invalid move: value {v} already in column {c}.")
        # Box check
        br, bc = 3 * (r // 3), 3 * (c // 3)
        if v in [self.grid[br + i][bc + j] for i in range(3) for j in range(3)]:
            raise ValueError(f"Invalid move: value {v} already in 3x3 box.")
        return move

    def is_valid_state(self, state):
        if not isinstance(state, list) or len(state) != 9:
            raise ValueError("Invalid state: must be 9 rows.")
        for r in range(9):
            if not isinstance(state[r], list) or len(state[r]) != 9:
                raise ValueError(f"Invalid state: row {r} must have 9 columns.")
            for c in range(9):
                v = state[r][c]
                if not isinstance(v, int) or v < 0 or v > 9:
                    raise ValueError(f"Invalid state: cell ({r},{c}) must be 0-9.")

        # Check initial cells preserved
        for r in range(9):
            for c in range(9):
                if self.initial_grid[r][c] != 0 and state[r][c] != self.initial_grid[r][c]:
                    raise ValueError(f"Invalid state: initial cell ({r},{c}) was changed.")

        # Check no duplicate non-zero values in rows, cols, boxes
        for r in range(9):
            seen = []
            for c in range(9):
                v = state[r][c]
                if v != 0:
                    if v in seen:
                        raise ValueError(f"Invalid state: duplicate {v} in row {r}.")
                    seen.append(v)

        for c in range(9):
            seen = []
            for r in range(9):
                v = state[r][c]
                if v != 0:
                    if v in seen:
                        raise ValueError(f"Invalid state: duplicate {v} in column {c}.")
                    seen.append(v)

        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                seen = []
                for i in range(3):
                    for j in range(3):
                        v = state[br + i][bc + j]
                        if v != 0:
                            if v in seen:
                                raise ValueError(f"Invalid state: duplicate {v} in box ({br},{bc}).")
                            seen.append(v)

        return state

    def apply_move(self, action):
        r, c, v = action
        self.validate_move((r, c, v))
        self.grid[r][c] = v

    def is_solved(self) -> bool:
        for r in range(9):
            for c in range(9):
                if self.grid[r][c] == 0:
                    return False
        # All cells filled — check constraints
        try:
            self.is_valid_state(self.grid)
        except ValueError:
            return False
        return True

    def compute_progress(self) -> float:
        total_empty = sum(1 for r in range(9) for c in range(9) if self.initial_grid[r][c] == 0)
        if total_empty == 0:
            return 1.0
        filled = sum(
            1 for r in range(9) for c in range(9)
            if self.initial_grid[r][c] == 0 and self.grid[r][c] != 0
        )
        return filled / total_empty
