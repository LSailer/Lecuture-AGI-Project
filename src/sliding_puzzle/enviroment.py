CONFIGS = {
    "2x2": [2, 1, 3, 0],
    "3x3 (easiest)": [1, 2, 5, 6, 3, 4, 7, 8, 0],
    "3x3 (hardest)": [8, 6, 7, 2, 5, 4, 3, 1, 0],
    "4x4 (easiest)": [1, 2, 3, 7, 8, 4, 5, 6, 9, 10, 11, 15, 0, 12, 13, 14],
    "4x4 (hardest)": [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
}


class SlidingPuzzle:
    def __init__(self, initial_state):
        if initial_state is None:
            raise ValueError(
                "initial_state is required. Please provide a valid puzzle configuration."
            )

        self.size = len(initial_state)
        if self.size**0.5 != int(self.size**0.5):
            raise ValueError("Number should squared")
        self.grid_size = int(self.size**0.5)

        self.goal_state = list(range(self.size))
        if not self._is_solvable(initial_state):
            raise ValueError("Initial state is not solvable.")
        self.state = initial_state.copy()

    def _is_solvable(self, state):
        inversions = 0
        flat = [t for t in state if t != 0]
        for i in range(len(flat)):
            for j in range(i + 1, len(flat)):
                if flat[i] > flat[j]:
                    inversions += 1
        if self.grid_size % 2 == 1:
            return inversions % 2 == 0
        blank_row = state.index(0) // self.grid_size
        goal_blank_row = 0
        return (inversions + abs(blank_row - goal_blank_row)) % 2 == 0

    def _get_position(self, tile):
        index = self.state.index(tile)
        row = index // self.grid_size
        col = index % self.grid_size
        return row, col

    def move_tile(self, tile: int, direction: str):
        if not self.validate_move((tile, direction)):
            raise ValueError("Invalid move attempted.")

        tile_row, tile_col = self._get_position(tile)
        empty_row, empty_col = self._get_position(0)

        tile_index = tile_row * self.grid_size + tile_col
        empty_index = empty_row * self.grid_size + empty_col

        self.state[tile_index], self.state[empty_index] = (
            self.state[empty_index],
            self.state[tile_index],
        )

        return self.state

    _OPPOSITE = {"up": "down", "down": "up", "left": "right", "right": "left"}
    _BLANK_OFFSETS = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

    def validate_move(self, move):
        if isinstance(move, str):
            blank_dir = move.lower()
            empty_row, empty_col = self._get_position(0)
            dr, dc = self._BLANK_OFFSETS[blank_dir]
            tile_row, tile_col = empty_row + dr, empty_col + dc
            if not (0 <= tile_row < self.grid_size and 0 <= tile_col < self.grid_size):
                raise ValueError("Invalid move: No tile in that direction.")
            tile = self.state[tile_row * self.grid_size + tile_col]
            return (tile, self._OPPOSITE[blank_dir])
        tile, direction = move

        if tile not in self.state:
            raise ValueError(f"Invalid move: Tile {tile} not in puzzle.")

        if tile == 0:
            raise ValueError("Invalid move: Cannot move empty space directly.")

        tile_row, tile_col = self._get_position(tile)
        empty_row, empty_col = self._get_position(0)

        target_row, target_col = tile_row, tile_col

        if direction == "up":
            target_row -= 1
        elif direction == "down":
            target_row += 1
        elif direction == "left":
            target_col -= 1
        elif direction == "right":
            target_col += 1
        else:
            raise ValueError(f"Invalid direction: {direction}")

        max_index = self.grid_size - 1
        if (
            target_row < 0
            or target_row > max_index
            or target_col < 0
            or target_col > max_index
        ):
            raise ValueError("Invalid move: Target position out of bounds.")

        if target_row != empty_row or target_col != empty_col:
            raise ValueError("Invalid move: Tile not adjacent to empty space.")

        return move

    def is_valid_state(self, state):
        if len(state) != self.size:
            raise ValueError(f"Invalid state: Must have exactly {self.size} tiles.")

        sorted_state = sorted(state)
        if sorted_state != list(range(self.size)):
            raise ValueError(
                f"Invalid state: Must contain tiles 0-{self.size - 1} exactly once."
            )

        return state

    def is_solved(self):
        return self.state == self.goal_state

    def compute_progress(self) -> float:
        correct = sum(1 for i, tile in enumerate(self.state) if tile == self.goal_state[i])
        return correct / len(self.state)

    def get_state(self):
        return self.state[:]

    def preview_move(self, action) -> list:
        """Return resulting state after action WITHOUT mutating self."""
        tile, direction = action
        state = self.state[:]
        tile_index = state.index(tile)
        empty_index = state.index(0)
        state[tile_index], state[empty_index] = state[empty_index], state[tile_index]
        return state

    def apply_move(self, action):
        self.move_tile(action[0], action[1])

    def reset(self):
        self.state = self.goal_state.copy()

    def visualize(self):
        """Return a string representation of the puzzle grid"""
        lines = []
        for i in range(0, self.size, self.grid_size):
            lines.append(str(self.state[i : i + self.grid_size]))
        return "\n".join(lines)


if __name__ == "__main__":
    print("=== 3x3 Puzzle (8-puzzle) ===")
    puzzle = SlidingPuzzle(initial_state=[1, 2, 3, 6, 4, 5, 7, 8, 0])
    print("Initial State:", puzzle.get_state())
    print("Goal State:", puzzle.goal_state)
    print("Visual:")
    print(puzzle.visualize())

    print("\n=== 4x4 Puzzle (15-puzzle) ===")
    puzzle_4x4 = SlidingPuzzle(
        initial_state=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    )
    print("Initial State:", puzzle_4x4.get_state())
    print("Goal State:", puzzle_4x4.goal_state)
    print("Visual:")
    print(puzzle_4x4.visualize())
