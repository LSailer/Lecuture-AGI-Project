# Autoresearch Guide

Autonomous research for Tower of Hanoi and Sliding Puzzle.
Inspired by [karpathy/autoresearch](https://github.com/karpathy/autoresearch).

## How it works

Claude Code IS the researcher. A shell loop invokes Claude repeatedly with the same prompt. Each iteration Claude reads `results.tsv` + git history, runs one experiment, keeps or discards, then exits. The loop restarts it with fresh context.

## Two modes

### Mode A: sbatch (preferred)

Claude Code runs inside a sbatch job on a GPU node. Experiments run directly with `uv run`. Submit and walk away.

Uses `program.md`.

```bash
cd ~/Lecuture-AGI-Project
git checkout -b autoresearch/toh-mar14

# Submit (24h, H100)
GAME=tower_of_hanoi sbatch scripts/run_autoresearch.sh

# For sliding puzzle
GAME=sliding_puzzle sbatch scripts/run_autoresearch.sh
```

Monitor from anywhere:
```bash
ssh cluster
cat ~/Lecuture-AGI-Project/results.tsv
tail -f ~/Lecuture-AGI-Project/logs/autoresearch-*.out
```

### Mode B: tmux fallback

If Claude Code can't run on GPU nodes, use this. Claude runs on login node inside tmux, experiments via `srun`.

Uses `program_fallback.md`.

```bash
ssh cluster

# Start tmux (survives SSH disconnect)
tmux new -s autoresearch

cd ~/Lecuture-AGI-Project
git checkout -b autoresearch/toh-mar14
claude
# Inside Claude Code:
/ralph-loop "read program_fallback.md, game=tower_of_hanoi" \
  --completion-promise "DONE" \
  --max-iterations 50
```

Detach: `Ctrl+b` then `d`. Reattach: `tmux attach -t autoresearch`.

## Test which mode works

Run this on the cluster to check if Claude Code works on a GPU node:

```bash
srun --partition=dev_gpu_h100 --time=00:10:00 --gres=gpu:1 --mem=64G \
  uv run jupyter nbconvert --to notebook --execute --inplace notebooks/test_cluster_claude.ipynb
```

If test passes → use Mode A. If Claude Code fails on GPU node → use Mode B.

## What happens

- Each iteration: ~20 min (experiment) + ~1 min (Claude reasoning)
- 50 iterations ≈ ~17 hours
- Last 2 iterations: analysis notebook + PR created automatically
- Mode A: stops via `claude_done.flag`
- Mode B: stops via `<promise>DONE</promise>` or `/cancel-ralph`

## Prerequisites

- SSH access to bwunicluster
- Claude Code installed
- HuggingFace token in `.env`
- Models pre-downloaded
- Mode B only: Ralph Loop plugin installed

## Download models (one-time)

```bash
srun --partition=dev_gpu_h100 --time=02:00:00 --gres=gpu:1 --mem=127G \
  uv run LLM/download_all.py
```

## Key files

| File | Role |
|------|------|
| `program.md` | Mode A — Claude on GPU node, direct `uv run` |
| `program_fallback.md` | Mode B — Claude on login node, `srun` to GPU |
| `scripts/run_autoresearch.sh` | Mode A sbatch wrapper (shell loop) |
| `src/config/<game>.yaml` | Config Claude modifies |
| `src/<game>/prompts/*.yaml` | Prompt templates Claude modifies |
| `results.tsv` | Experiment log (persists across iterations) |
| `run.log` | Latest experiment output |
