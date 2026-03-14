# Autoresearch Guide

Autonomous research for Tower of Hanoi and Sliding Puzzle.
Inspired by [karpathy/autoresearch](https://github.com/karpathy/autoresearch).

## How it works

Claude Code IS the researcher, driven by a **Ralph Loop**. Each iteration:
1. Claude reads `results.tsv` + git history (previous experiments)
2. Decides what to try next (model, temperature, prompt, agents)
3. Modifies config/prompt YAML, commits
4. Runs experiment via `srun` on GPU (dev_gpu_h100, 20 min)
5. Parses results, keeps or discards
6. Exits → Ralph Loop feeds same prompt again → next iteration

No context bloat — each iteration gets fresh context, reads state from files.

## Prerequisites

- SSH access to bwunicluster login node
- Claude Code installed
- HuggingFace token in `.env`
- Models pre-downloaded (`uv run LLM/download_all.py`)
- Ralph Loop plugin installed

## Quick start

```bash
# SSH to cluster login node
cd ~/Lecuture-AGI-Project
git checkout -b autoresearch/toh-mar14

# Start Ralph Loop
/ralph-loop "read program.md, game=tower_of_hanoi" \
  --completion-promise "DONE" \
  --max-iterations 50
```

For sliding puzzle (separate session):
```bash
git checkout -b autoresearch/sp-mar14
/ralph-loop "read program.md, game=sliding_puzzle" \
  --completion-promise "DONE" \
  --max-iterations 50
```

## What happens

- Each iteration: ~20 min (GPU experiment) + ~1 min (Claude reasoning)
- 50 iterations ≈ ~17 hours
- Wrap-up: analysis notebook + PR created automatically on last iteration
- Stop early: `/cancel-ralph`

## Monitor

```bash
cat results.tsv              # experiment log
git log --oneline            # kept experiments
tail -f run.log              # live experiment output (during srun)
```

## Key files

| File | Role |
|------|------|
| `program.md` | Instructions for Claude Code (read each iteration) |
| `src/config/<game>.yaml` | Config Claude modifies |
| `src/<game>/prompts/*.yaml` | Prompt templates Claude modifies |
| `results.tsv` | Experiment log (untracked, persists across iterations) |
| `run.log` | Latest experiment output |
| `LLM/download_all.py` | One-time model download |

## Download models (one-time)

```bash
srun --partition=dev_gpu_h100 --time=02:00:00 --gres=gpu:1 --mem=127G \
  uv run LLM/download_all.py
```
