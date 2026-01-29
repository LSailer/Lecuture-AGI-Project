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

        self.goal_state = list(range(1, self.size)) + [0]
        if not self._is_solvable(initial_state):
            raise ValueError("Initial state is not solvable.")
        self.state = initial_state.copy()

    def _is_solvable(self, state):
        inversions = 0
        flat_state = [tile for tile in state if tile != 0]
        for i in range(len(flat_state)):
            for j in range(i + 1, len(flat_state)):
                if flat_state[i] > flat_state[j]:
                    inversions += 1

        return inversions % 2 == 0

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

    def validate_move(self, move: tuple):
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

    def get_state(self):
        return self.state

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
    puzzle = SlidingPuzzle(initial_state=[1, 2, 3, 4, 5, 6, 7, 0, 8])
    print("Initial State:", puzzle.get_state())
    print("Visual:")
    print(puzzle.visualize())

    puzzle.move_tile(8, "left")
    print("\nAfter moving tile 8 left:")
    print(puzzle.get_state())
    print("Visual:")
    print(puzzle.visualize())
    print("Is solved?", puzzle.is_solved())

    print("\n=== 4x4 Puzzle (15-puzzle) ===")
    puzzle_4x4 = SlidingPuzzle(
        initial_state=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15]
    )
    print("Initial State:", puzzle_4x4.get_state())
    print("Visual:")
    print(puzzle_4x4.visualize())
    print("Goal State:", puzzle_4x4.goal_state)
