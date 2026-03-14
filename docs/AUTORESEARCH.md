# Autoresearch Guide

Automated hyperparameter search for Tower of Hanoi and Sliding Puzzle.
Inspired by [karpathy/autoresearch](https://github.com/karpathy/autoresearch).

## How it works

The script iterates over combinations of:
- **Models**: Qwen3-32B, Devstral-24B, DeepSeek-R1-32B
- **Temperature**: 0.0, 0.1, 0.3, 0.5, 0.7, 1.0
- **Prompt variants**: base, cot_detailed, minimal
- **Agents per step**: 1, 3, 5
- **Margin k**: 1, 2, 3

Each experiment: modify config → git commit → run main.py → parse SR/steps → keep or discard.

Stages auto-advance when SR=100% for 2 consecutive experiments:
- **Tower of Hanoi**: 3 disks → 4 → 5 → ...
- **Sliding Puzzle**: 2x2 → 3x3 (easiest) → 3x3 (hardest) → 4x4 (easiest) → 4x4 (hardest)

## Prerequisites

- SSH access to bwunicluster
- HuggingFace token in `.env` (`HUGGING_FACE_HUB_TOKEN`)
- GitHub CLI (`gh`) configured for PR creation

## Step 1: Download models (one-time)

```bash
# On cluster:
sbatch --partition=dev_gpu_h100 --time=02:00:00 --wrap="uv run LLM/download_all.py"

# Verify:
ls LLM/models/
# → qwen3-32b/  devstral-24b/  deepseek-r1-32b/
```

## Step 2: Run test notebook (verify setup)

```bash
uv run jupyter nbconvert --to notebook --execute --inplace notebooks/test_autoresearch.ipynb
```

All 5 tests should pass (prompt loading, configs, SR, dry-run).

## Step 3: Start autoresearch

Two separate jobs — one per game:

```bash
# Tower of Hanoi
git checkout -b autoresearch/toh-$(date +%b%d | tr '[:upper:]' '[:lower:]')
GAME=tower_of_hanoi sbatch --job-name=ar-toh scripts/run_autoresearch.sh

# Sliding Puzzle
git checkout -b autoresearch/sp-$(date +%b%d | tr '[:upper:]' '[:lower:]')
GAME=sliding_puzzle sbatch --job-name=ar-sp scripts/run_autoresearch.sh
```

## Step 4: Monitor

```bash
squeue -u $USER                          # job status
tail -f logs/autoresearch-<jobid>.out    # live output
cat results.tsv                          # experiment summary
cat output/autoresearch_results.csv      # full CSV for analysis
```

## Step 5: Analyze results (locally)

```bash
# Copy CSV from cluster
scp cluster:~/path/to/Project/output/autoresearch_results.csv output/

# Open analysis notebook
jupyter notebook notebooks/analyze_autoresearch.ipynb
```

Charts include: model comparison, temperature heatmap, prompt variant comparison, stage progression, SR vs steps Pareto front.

## Step 6: Review PR

The autoresearch script auto-creates a PR with the best config before the time budget runs out. Review on GitHub and merge if results look good.

## Dry run (no GPU needed)

```bash
uv run scripts/autoresearch.py --game tower_of_hanoi --dry-run
uv run scripts/autoresearch.py --game sliding_puzzle --dry-run
```

## Configuration

Edit `scripts/autoresearch.py` constants to change search space:
- `MODELS` — model name → path mapping
- `TEMPERATURES` — temperature values to try
- `PROMPT_VARIANTS` — prompt variant names (must match YAML files)
- `AGENT_COUNTS` — max_agents_per_step values
- `MARGIN_KS` — margin_k values
- `EXPERIMENT_TIMEOUT` — per-experiment timeout in seconds
