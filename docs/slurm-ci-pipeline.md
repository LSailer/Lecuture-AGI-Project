# SLURM CI Pipeline — Dev & Prod Jobs

## Overview

Push to `dev` branch triggers a GitHub Actions workflow that submits **two SLURM jobs** from a single script (`scripts/run.sh`). A short dev job validates on a fast GPU, and a long prod job runs the full experiment. If dev fails, prod is automatically cancelled.

## How It Works

```
push to dev
    │
    ▼
GitHub Actions (self-hosted runner)
    │
    ├─► sbatch --partition=dev_gpu_h100 --time=00:30:00 scripts/run.sh   (dev)
    ├─► sbatch --partition=gpu_h100_il  --time=42:00:00 scripts/run.sh   (prod)
    │
    ▼
Wait for dev job
    │
    ├─ dev passes → prod continues running
    └─ dev fails  → scancel prod job, workflow fails
```

## Single Script, Two Partitions

Both jobs use `scripts/run.sh`. The game and params are defined once:

```bash
uv run src/main.py --game sliding_puzzle --margin_k 3
```

Partition and time are overridden via `sbatch` CLI flags (CLI flags override `#SBATCH` directives). Change the game/params in one place — both jobs always run the same thing.

## Failure Handling

1. Workflow waits for the dev job (polls `squeue` every 5 min)
2. Checks exit code via `sacct`
3. If non-zero → `scancel $PROD_ID` and `exit 1`
4. Safety net step (`if: failure()`) cancels prod on any unexpected workflow failure

## Manual Usage

```bash
# Dev (quick validation)
sbatch --partition=dev_gpu_h100 --time=00:30:00 scripts/run.sh

# Prod (full run)
sbatch --partition=gpu_h100_il --time=42:00:00 scripts/run.sh
```
