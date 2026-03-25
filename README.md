# Closing the Loop: Extending MAKER with Autoresearch for Autonomous LLM Puzzle Solving

Reimplementation and extension of the MAKER framework (Massively decomposed Agentic processes) from Meyerson et al. (2025). Multi-agent LLM systems solve puzzle problems via single-step decomposition, parallel agent voting with "first-to-ahead-by-k" consensus, and error filtering.

## Prerequisites

- **Python** >= 3.13
- **Package manager**: `uv`
- **Hugging Face Account**: A valid token to download the LLM model (only needed for HuggingFace backend)


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

### 1. Download the LLMs

```bash
uv run LLM/download_all.py
```

Downloads all models (Qwen3-32B, Devstral-24B, DeepSeek-R1-32B) to `LLM/models/`:

```bash
uv run LLM/download_all.py
```

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

### 4. Autoresearch (Autonomous Experiment Loop)

Inspired by [karpathy/autoresearch](https://github.com/karpathy/autoresearch). Autoresearch runs Claude Code in a loop on the cluster. Each iteration, Claude reads prior results (`results.tsv`), designs and runs an experiment, evaluates the outcome, and commits findings. See [docs/AUTORESEARCH.md](docs/AUTORESEARCH.md) for full details.

**Dev (smoke test):**

```bash
# Quick validation — 2 iterations, 30 min, dev config (3 disks, max_steps=100)
GAME=tower_of_hanoi sbatch scripts/run_autoresearch_dev.sh
```

- Partition: `dev_gpu_h100`
- Timeout: 30 minutes
- Iterations: 2 (hardcoded)
- Config: `src/config/<game>_dev.yaml`
- Claude budget: $1/iteration

**Prod (full research run):**

```bash
# Full campaign — up to 50 iterations, 24h, prod config (7 disks)
GAME=tower_of_hanoi sbatch scripts/run_autoresearch.sh

# Override iteration count
MAX_ITER=20 GAME=sliding_puzzle sbatch scripts/run_autoresearch.sh
```

- Partition: `gpu_h100_il`
- Timeout: 24 hours
- Iterations: 50 (default, configurable via `MAX_ITER`)
- Config: `src/config/<game>.yaml`


**Monitor a running job:**

```bash
tail -f logs/autoresearch-*.out    # live output
cat results.tsv                    # experiment log
squeue -u $USER                    # SLURM job status
```

Both scripts automatically commit results, run the analysis notebook, push to the branch, and create a PR when finished.





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


