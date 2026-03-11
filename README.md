# MAKER Framework - Multi-Agent LLM Puzzle Solvers

Reimplementation and extension of the MAKER framework (Massively decomposed Agentic processes) from Meyerson et al. (2025). Multi-agent LLM systems solve puzzle problems via single-step decomposition, parallel agent voting with "first-to-ahead-by-k" consensus, and error filtering.

Currently implements **Tower of Hanoi** and **Sliding Puzzle** domains.

## Prerequisites

- **Python** >= 3.13
- **Package manager**: `uv`
- **Hugging Face Account**: A valid token to download the LLM model (only needed for HuggingFace backend)
- **Ollama** (recommended for Apple Silicon): [ollama.com](https://ollama.com)

## Installation

```bash
uv sync
```

## Configuration

1. Create a `.env` file in the project root.
2. Add your Hugging Face token:

   ```env
   HF_TOKEN=hf_...
   ```

## Usage

### 1. Download the LLM

**Option A — Ollama (recommended for Apple Silicon):**

```bash
ollama pull qwen3:8b
```

Ensure `llm_backend: ollama` is set in `src/config/*.yaml` (default).

**Option B — HuggingFace:**

```bash
uv run LLM/download.py
```

Downloads the model to `LLM/model/`. Set `llm_backend: huggingface` in the config.

### 2. Run Solvers

```bash
uv run src/main.py --game tower_of_hanoi
uv run src/main.py --game sliding_puzzle
uv run src/main.py --game nonogram
```

**CLI overrides:**

| Flag | Description |
|------|-------------|
| `--config path/to/config.yaml` | Custom YAML config file |
| `--margin_k N` | Vote margin for consensus (default: from config) |
| `--max_steps N` | Maximum solver steps |
| `--max_agents_per_step N` | Cap on agents queried per step |

### 3. Run on HPC Cluster (SLURM)

```bash
sbatch scripts/run.sh
```

Submits to `gpu_h100_il` partition with 1x H100 GPU, 127 GB RAM.

### 4. Cancel All SLURM Jobs (Remote)

```bash
gh workflow run cancel-jobs.yml --ref dev
```

Triggers the self-hosted runner to `scancel --user=$USER` on the cluster. No SSH required.

### 5. Run Tests

```bash
cd src
uv run sliding_puzzle/test_simple.py
uv run sliding_puzzle/test_generic.py
```

## Project Structure

```
Lecuture-AGI-Project/
├── LLM/
│   ├── download.py               # Model download script
│   └── model/                    # Downloaded model weights
├── src/
│   ├── main.py                   # Unified orchestration + voting loop
│   ├── config/
│   │   ├── tower_of_hanoi.yaml   # ToH config (num_disks, voting params)
│   │   └── sliding_puzzle.yaml   # SP config (initial_state, voting params)
│   ├── utils/
│   │   ├── llm.py                # Shared LLM interface (HuggingFace pipeline)
│   │   ├── decomposer.py         # Unified Agent class
│   │   └── parser.py             # Unified Parser class
│   ├── tower_of_hanoi/
│   │   ├── enviroment.py         # Game state, move validation, goal checking
│   │   └── prompts.py            # System/user prompts, regex patterns, parse fns
│   └── sliding_puzzle/
│       ├── enviroment.py         # Game state, move validation, goal checking
│       ├── prompts.py            # System/user prompts, regex patterns, parse fns
│       ├── test_simple.py        # Basic environment tests
│       └── test_generic.py       # Generic NxN tests
├── output/                       # Generated logs and plots
├── scripts/
│   └── run.sh                    # SLURM job script
└── .env                          # HF_TOKEN (not committed)
```

## Architecture

### Composition pattern

Game-specific behavior is isolated in per-game `prompts.py` modules. The unified `Agent` and `Parser` in `utils/` delegate to these modules at runtime:

```
src/main.py
  -> load YAML config + CLI overrides
  -> factory creates game environment + agent (with game's prompts module)
  -> voting loop:
       prompts.build_user_prompt(current_state, ...)
       -> LLM.generate(system_prompt, user_prompt)
       -> Parser extracts (action, state) using prompts.MOVE_PATTERN / STATE_PATTERN
       -> action added to vote tally
       -> repeat until margin_k consensus or agent limit
  -> game.apply_move(winning_action)
```

### Per-game prompts module interface

Each `prompts.py` exports:
- `get_system_prompt(environment)` - returns system prompt string
- `build_user_prompt(current_state, previous_move, environment, step)` - returns user prompt string
- `MOVE_PATTERN` - compiled regex for extracting moves from LLM output
- `STATE_PATTERN` - compiled regex for extracting states from LLM output
- `parse_move(match)` - converts regex match to a move value
- `parse_state(match)` - converts regex match to a state value

### Key parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `margin_k` | Required vote lead for consensus | 2 |
| `max_agents_per_step` | Cap on agents queried per step | 15 (ToH) / 20 (SP) |
| `max_steps` | Maximum solver steps | 1000 (ToH) / 200 (SP) |
| `num_disks` | Tower of Hanoi disk count | 3 |
| `initial_state` | Sliding Puzzle starting configuration | `[1,2,3,4,5,6,7,0,8]` |

Configuration lives in `src/config/*.yaml` and can be overridden via CLI.

## Output

- `output/log.csv` - Per-agent responses with columns: `step`, `number_agent`, `response`, `predicted_action`, `predicted_state`, `error_message`
- `output/step_N_distribution.png` - Vote distribution bar charts per step
