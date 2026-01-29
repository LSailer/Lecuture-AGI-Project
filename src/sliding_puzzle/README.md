# Sliding Puzzle (8-Puzzle) Implementation

Multi-agent LLM-based solver for the classic 8-puzzle using the Tower of Hanoi architectural pattern.

## Overview

The sliding puzzle consists of a 3×3 grid with tiles numbered 1-8 and one empty space (0). The goal is to arrange the tiles in order by sliding adjacent tiles into the empty space.

**Goal State:**
```
1 2 3
4 5 6
7 8 0
```

## File Structure

```
sliding_puzzle/
├── enviroment.py      # SlidingPuzzle environment class
├── parser.py          # Parser for LLM output extraction
├── decomposer.py      # Agent class with prompts
├── main.py            # Multi-agent orchestration
├── llm.py             # LLM interface
└── test_simple.py     # Basic tests
```

## Quick Start

### Run Tests
```bash
cd sliding_puzzle
uv run test_simple.py
```

### Run Main Solver
```bash
cd sliding_puzzle
uv run main.py
```

## Implementation Details

### State Representation
- **Format**: 1D list of 9 integers (0-8)
- **Empty space**: Represented by 0
- **Example**: `[1, 2, 3, 4, 5, 6, 7, 0, 8]`

### Move Format
- **Format**: `(tile_number, direction)`
- **Directions**: `"up"`, `"down"`, `"left"`, `"right"`
- **Example**: `(8, "left")` moves tile 8 left into empty space

### LLM Output Format
```python
move = [tile_number, "direction"]
next_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
```

## Key Features

### Solvability Check
- Validates initial states using parity of inversions
- Only even-inversion states are solvable

### Move Validation
- Checks tile adjacency to empty space
- Validates bounds (3×3 grid)
- Ensures tile exists in puzzle

### Multi-Agent Voting
- Multiple LLM agents propose moves
- Votes aggregated using margin-k algorithm
- Configurable parameters:
  - `margin_k=2`: Vote margin threshold
  - `max_number_agents_per_step=20`: Max agents per step
  - `max_steps=200`: Maximum solving steps

## Configuration

Edit `main.py` to customize:

```python
# Initial puzzle state (must be solvable)
initial_state = [1, 2, 3, 4, 5, 6, 7, 0, 8]

# Voting parameters
margin_k = 2
max_number_agents_per_step = 20
max_steps = 200

# Device selection (automatic)
# cuda > mps > cpu
```

## Testing Examples

### Simple Puzzles

**One-move puzzle:**
```python
puzzle = SlidingPuzzle(initial_state=[1, 2, 3, 4, 5, 6, 7, 0, 8])
puzzle.move_tile(8, "left")
# Solved!
```

**Two-move puzzle:**
```python
puzzle = SlidingPuzzle(initial_state=[1, 2, 3, 4, 5, 6, 0, 7, 8])
puzzle.move_tile(7, "left")
puzzle.move_tile(8, "left")
# Solved!
```

## Output

### Console Output
- Step-by-step state visualization
- Agent predictions and voting
- Final solution or timeout message

### CSV Log
File: `output/log.csv`

Columns:
- `step`: Step number
- `number_agent`: Agent ID
- `response`: Full LLM response
- `predicted_action`: Parsed action
- `predicted_state`: Parsed state
- `error_message`: Any parsing errors

### Visualizations
- Vote distribution charts: `output/step_N_distribution.png`
- Shows action voting patterns per step

## Comparison with Tower of Hanoi

| Aspect | Tower of Hanoi | Sliding Puzzle |
|--------|---------------|----------------|
| State | List of 3 lists | Flat list of 9 ints |
| Move | `[disk, from, to]` | `[tile, direction]` |
| Validation | Tower tops + size rule | Adjacency to empty |
| Strategy | Rule-based alternating | Heuristic-guided |
| Solution length | 2^n - 1 (predictable) | Variable (15-100+) |

## Known Limitations

- Solution quality depends on LLM heuristics
- May exceed optimal solution length
- Performance varies with initial state complexity
- No A* or BFS guarantee of shortest path

## Dependencies

- Python 3.8+
- transformers
- torch
- matplotlib
- python-dotenv

Install via the project's main requirements.
