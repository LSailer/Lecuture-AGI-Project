# Tower of Hanoi

Classic disk-stacking puzzle with 3 pegs and N disks.

## Environment (`enviroment.py`)

**Class:** `TowerOfHanoi(num_disks)`

**State format:** List of 3 lists (one per peg), each containing disk numbers sorted largest-to-smallest from bottom to top.
```python
# 3 disks, all on peg 0:
[[3, 2, 1], [], []]
```

**Move format:** `(disk, from_peg, to_peg)`
```python
game = TowerOfHanoi(3)
game.move_disk(1, 0, 2)  # Move disk 1 from peg 0 to peg 2
```

**Validation rules:**
- Only the top disk on a peg can be moved
- A larger disk cannot be placed on a smaller disk

**Goal:** All disks on peg 2. Optimal solution length is 2^n - 1 moves.

**Interface:**
- `get_state()` - returns current tower state
- `apply_move(action)` - applies a `(disk, from, to)` move
- `validate_move(move)` - raises `ValueError` on illegal moves
- `is_valid_state(state)` - validates a proposed state
- `is_solved()` - checks if all disks are on peg 2
- `reset()` - resets to initial state

## Prompts (`prompts.py`)

The LLM prompt uses a parity-aware alternating strategy:
- **Even N:** Disk 1 moves clockwise (0 -> 1 -> 2 -> 0)
- **Odd N:** Disk 1 moves counter-clockwise (0 -> 2 -> 1 -> 0)

Decision rules in the user prompt:
- **Rule A:** If previous move was not Disk 1, move Disk 1 in its direction sequence.
- **Rule B:** If previous move was Disk 1, make the only legal move between the other two pegs.

**LLM output patterns:**
```
move = [disk_id, from_peg, to_peg]
next_state = [[...], [...], [...]]
```
