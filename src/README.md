# Multi-Agent LLM Puzzle Solvers

Multi-agent LLM-based solvers for classic puzzles using voting algorithms.

## Project Structure

```
src/
├── utils/
│   ├── __init__.py
│   └── llm.py              # Shared LLM interface for both puzzles
│
├── tower_of_hanoi/
│   ├── __init__.py
│   ├── enviroment.py       # Tower of Hanoi environment
│   ├── parser.py           # LLM output parser
│   ├── decomposer.py       # Agent with prompts
│   └── main.py             # Multi-agent orchestration
│
├── sliding_puzzle/
│   ├── __init__.py
│   ├── enviroment.py       # Sliding Puzzle environment (generic for NxN)
│   ├── parser.py           # LLM output parser
│   ├── decomposer.py       # Agent with prompts
│   └── main.py             # Multi-agent orchestration
│
├── run_tower_of_hanoi.py   # Entry point for Tower of Hanoi
└── run_sliding_puzzle.py   # Entry point for Sliding Puzzle
```

## Quick Start

### Run Tower of Hanoi Solver
```bash
cd src
uv run run_tower_of_hanoi.py
```

### Run Sliding Puzzle Solver
```bash
cd src
uv run run_sliding_puzzle.py
```

## Shared Components

### `utils/llm.py`
- Shared LLM interface used by both puzzle solvers
- Wraps HuggingFace transformers pipeline
- Auto-detects device (CUDA > MPS > CPU)
- Generates text completions for puzzle-solving agents

## Tower of Hanoi

Classic disk-stacking puzzle with rule-based alternating strategy.

**Key Features:**
- Rule-based prompting (disk 1 alternates clockwise/counter-clockwise)
- Deterministic solution length: 2^n - 1 moves
- Works with any number of disks

**State Format:** `[[3, 2, 1], [], []]` (3 towers)
**Move Format:** `[disk, from_tower, to_tower]`

## Sliding Puzzle

Classic tile-sliding puzzle with heuristic-guided strategy.

**Key Features:**
- **Generic NxN support**: Works with 2×2, 3×3, 4×4, 5×5, etc.
- Solvability validation (inversion parity checking)
- Heuristic-based prompting (prioritize misplaced tiles)
- Visual grid representation in prompts

**State Format:** `[1, 2, 3, 4, 5, 6, 7, 8, 0]` (flat list, 0 = empty)
**Move Format:** `[tile, direction]` where direction ∈ {up, down, left, right}

**Supported Sizes:**
- 2×2 (3-puzzle): 4 tiles
- 3×3 (8-puzzle): 9 tiles
- 4×4 (15-puzzle): 16 tiles
- 5×5 (24-puzzle): 25 tiles
- Any perfect square size

## Multi-Agent Voting

Both solvers use the same voting mechanism:

1. **Multiple agents** propose moves independently
2. **Votes aggregated** using margin-k algorithm
3. **Best action** selected when vote margin exceeds threshold
4. **Configurable parameters:**
   - `margin_k`: Vote margin threshold (default: 2)
   - `max_number_agents_per_step`: Max agents per step (15-20)
   - `max_steps`: Maximum solving steps (200-1000)

## Output

### Console Output
- Step-by-step state visualization
- Agent predictions and voting distribution
- Final solution or timeout message

### CSV Logs
File: `output/log.csv` (created in working directory)

Columns:
- `step`: Step number
- `number_agent`: Agent ID
- `response`: Full LLM response
- `predicted_action`: Parsed action
- `predicted_state`: Parsed next state
- `error_message`: Any parsing errors

### Visualizations
- Vote distribution charts: `output/step_N_distribution.png`
- Bar charts showing action voting patterns per step

## Configuration

Edit `main.py` in each puzzle folder to customize:

```python
# Tower of Hanoi
num_disks = 3
margin_k = 2
max_number_agents_per_step = 15
max_steps = 1000

# Sliding Puzzle
initial_state = [1, 2, 3, 4, 5, 6, 7, 0, 8]  # Must be solvable
margin_k = 2
max_number_agents_per_step = 20
max_steps = 200
```

## Dependencies

- Python 3.8+
- transformers
- torch
- matplotlib
- python-dotenv

Install via the project's main requirements.

## Architecture Pattern

Both implementations follow the same architectural pattern:

1. **Environment**: State management and move validation
2. **Parser**: Extract structured data from LLM text output
3. **Agent**: System/user prompts and LLM interaction
4. **Main**: Multi-agent voting orchestration

This pattern makes it easy to add new puzzles by following the same structure.
