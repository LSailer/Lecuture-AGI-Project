# Sliding Puzzle

Classic tile-sliding puzzle on an NxN grid (supports 2x2, 3x3, 4x4, etc.).

## Environment (`enviroment.py`)

**Class:** `SlidingPuzzle(initial_state)`

`initial_state` is required and must be a flat list whose length is a perfect square.

**State format:** Flat list of integers where `0` represents the empty space.
```python
# 3x3 puzzle (8-puzzle):
[1, 2, 3, 4, 5, 6, 7, 0, 8]

# Visualized:
# [1, 2, 3]
# [4, 5, 6]
# [7, 0, 8]
```

**Goal state:** Tiles in order 1..N with 0 at the end: `[1, 2, 3, 4, 5, 6, 7, 8, 0]`

**Move format:** `(tile, direction)` where direction is `"up"`, `"down"`, `"left"`, or `"right"`.
```python
puzzle = SlidingPuzzle(initial_state=[1, 2, 3, 4, 5, 6, 7, 0, 8])
puzzle.move_tile(8, "left")  # Slide tile 8 left into the empty space
```

**Validation rules:**
- Tile must exist in the puzzle
- Cannot move the empty space (0) directly
- Tile must be adjacent to the empty space in the given direction
- Target position must be within grid bounds

**Solvability:** The constructor rejects unsolvable states using inversion parity (only even-inversion states are solvable).

**Interface:**
- `get_state()` - returns current state as a flat list
- `apply_move(action)` - applies a `(tile, direction)` move
- `validate_move(move)` - raises `ValueError` on illegal moves
- `is_valid_state(state)` - validates a proposed state
- `is_solved()` - checks if tiles are in goal order
- `visualize()` - returns a grid string representation
- `reset()` - resets to goal state

## Prompts (`prompts.py`)

The LLM prompt uses heuristic-guided strategy:
- Prioritize moving misplaced tiles closer to their goal positions
- Avoid reversing the previous move
- Work on upper/left tiles first (1, 2, 3, 4, 5)

**LLM output patterns:**
```
move = [tile_number, "direction"]
next_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
```
