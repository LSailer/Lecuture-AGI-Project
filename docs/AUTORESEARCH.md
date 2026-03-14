# Autoresearch Guide

Autonomous research for Tower of Hanoi and Sliding Puzzle.
Inspired by [karpathy/autoresearch](https://github.com/karpathy/autoresearch).

## How it works

Claude Code IS the researcher. You give it `program.md` and it runs experiments autonomously — modifying configs/prompts, running `main.py`, evaluating SR/steps, keeping or discarding changes. No Python script orchestrating — Claude Code itself is the loop.

One game per Claude Code session. It runs until you stop it.

## Prerequisites

- SSH access to bwunicluster
- Claude Code installed on cluster nodes
- HuggingFace token in `.env`
- Models pre-downloaded (see step 1)

## Step 1: Download models (one-time)

```bash
sbatch --partition=dev_gpu_h100 --time=02:00:00 --wrap="uv run LLM/download_all.py"

# Verify:
ls LLM/models/
# → qwen3-32b/  devstral-24b/  deepseek-r1-32b/
```

## Step 2: Run test notebook (verify setup)

```bash
uv run jupyter nbconvert --to notebook --execute --inplace notebooks/test_autoresearch.ipynb
```

## Step 3: Start autoresearch

```bash
# Tower of Hanoi
git checkout -b autoresearch/toh-$(date +%b%d | tr '[:upper:]' '[:lower:]')
claude --print "read program.md, game=tower_of_hanoi, start experimenting"

# Sliding Puzzle (separate session)
git checkout -b autoresearch/sp-$(date +%b%d | tr '[:upper:]' '[:lower:]')
claude --print "read program.md, game=sliding_puzzle, start experimenting"
```

Or wrap in sbatch for unattended runs:

```bash
sbatch --partition=gpu_h100_il --time=24:00:00 --gres=gpu:1 --mem=127G \
  --wrap="claude --print 'read program.md, game=tower_of_hanoi, start experimenting'"
```

## Step 4: Monitor

```bash
cat results.tsv                    # experiment log
git log --oneline                  # kept experiments
```

## Step 5: Analyze results (locally)

```bash
# Copy results from cluster
scp cluster:~/path/to/Project/results.tsv .

# Open analysis notebook
jupyter notebook notebooks/analyze_autoresearch.ipynb
```

## Key files

| File | Role |
|------|------|
| `program.md` | Instructions for Claude Code (the "skill") |
| `src/config/<game>.yaml` | Config Claude Code modifies |
| `src/<game>/prompts/*.yaml` | Prompt templates Claude Code modifies |
| `results.tsv` | Experiment log (untracked) |
| `LLM/download_all.py` | One-time model download |
