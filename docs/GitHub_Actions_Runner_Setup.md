# GitHub Actions Self-Hosted Runner — Setup Guide

> Run SLURM cluster jobs automatically on every push or merge.

---

## Overview

This guide explains how to attach a self-hosted GitHub Actions runner to any repository so that pushes and merges to a chosen branch automatically submit a SLURM job on your HPC cluster. The runner lives inside the cluster, so no VPN or one-time token is needed for day-to-day use after the initial setup.

---

## Prerequisites

- A GitHub repository (public or private)
- SSH access to the HPC cluster (VPN + OTP for first-time setup only)
- SLURM installed on the cluster with `sbatch` available
- A job script at `scripts/<branch>.sh` in your repo with the following SBATCH directives:

```bash
#SBATCH --output=logs/slurm-%j.out
#SBATCH --error=logs/slurm-%j.err
```

> `%j` is replaced by SLURM with the job number at runtime. The workflow reads these files using `${JOB_ID}` to display output directly in the GitHub Actions log.

---

## Step 1 — Install the Runner on the Cluster

Log in to your cluster once (VPN + OTP). Then run:

```bash
# Create a dedicated directory (outside your repo)
mkdir -p ~/actions-runner && cd ~/actions-runner

# Download the latest runner binary
curl -o actions-runner-linux-x64.tar.gz -L \
  https://github.com/actions/runner/releases/download/v2.322.0/actions-runner-linux-x64-2.322.0.tar.gz

tar xzf ./actions-runner-linux-x64.tar.gz
```

Get your registration token from GitHub:

1. Go to your repository → **Settings → Actions → Runners → New self-hosted runner**
2. Copy the token from the `./config.sh` command shown (expires after 1 hour)

```bash
# Register the runner with your repo
./config.sh --url https://github.com/YOUR_USER/YOUR_REPO --token YOUR_TOKEN
```

---

## Step 2 — Keep the Runner Alive

Start the runner inside a tmux session so it persists after you disconnect:

```bash
tmux new -s runner
cd ~/actions-runner && ./run.sh
# Press Ctrl+B then D to detach — the runner stays active
```

> **Note:** If your cluster supports systemd user services, run `./svc.sh install && ./svc.sh start` for a setup that survives reboots automatically.

---

## Step 3 — Add the Workflow File

Create `.github/workflows/cluster-dev.yml` in your repository. Adjust the branch name and script path as needed.

```yaml
name: Run Dev on BVUni Cluster

on:
  push:
    branches: [dev]
  pull_request:
    branches: [dev]
    types: [closed]

jobs:
  submit-slurm-job:
    runs-on: self-hosted
    if: github.event_name == 'push' || github.event.pull_request.merged == true

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Submit SLURM job
        id: sbatch
        run: |
          job_id=$(sbatch --parsable scripts/dev.sh)
          echo "Submitted SLURM job: $job_id"
          echo "JOB_ID=$job_id" >> $GITHUB_ENV

      - name: Wait for job and report
        run: |
          echo "Waiting for SLURM job $JOB_ID to finish..."

          while squeue -j $JOB_ID -h 2>/dev/null | grep -q "$JOB_ID"; do
            echo "Job $JOB_ID still running — checking again in 30s..."
            sleep 30
          done

          echo "Job $JOB_ID finished."

          # Print SLURM output and error logs if they exist
          OUT_FILE="logs/slurm-${JOB_ID}.out"
          ERR_FILE="logs/slurm-${JOB_ID}.err"

          if [ -f "$OUT_FILE" ]; then
            echo "--- SLURM Output (slurm-${JOB_ID}.out) ---"
            cat "$OUT_FILE"
          else
            echo "No output file found at $OUT_FILE"
          fi

          if [ -f "$ERR_FILE" ]; then
            echo "--- SLURM Errors (slurm-${JOB_ID}.err) ---"
            cat "$ERR_FILE"
          else
            echo "No error file found at $ERR_FILE"
          fi

          # Check exit code from SLURM job
          EXIT_CODE=$(sacct -j $JOB_ID --format=ExitCode --noheader | head -1 | cut -d':' -f1 | tr -d ' ')
          echo "Job exit code: $EXIT_CODE"

          if [ "$EXIT_CODE" != "0" ] && [ -n "$EXIT_CODE" ]; then
            echo "Job failed with exit code $EXIT_CODE"
            exit 1
          else
            echo "Job completed successfully."
          fi
```

The GitHub Actions log will show the output and error sections separately, like this:

```
--- SLURM Output (slurm-48291.out) ---
[your job stdout here]

--- SLURM Errors (slurm-48291.err) ---
[your job stderr here]

Job exit code: 0
Job completed successfully.
```

---

## Reusing on Another Project

For each new repository, repeat only these steps:

1. Generate a new token: **GitHub → New Repo → Settings → Actions → Runners → New self-hosted runner**
2. Re-run `./config.sh` on the cluster with the new repo URL and token (the binary is already installed)
3. Copy the workflow file into the new repo and adjust the branch name and script path
4. Make sure your job script includes `#SBATCH --output=logs/slurm-%j.out` and `#SBATCH --error=logs/slurm-%j.err`
5. Commit and push

> **Note:** The runner token is one-time only. After registration you will not need it again unless you reinstall the runner.

---

## Quick Reference

| Setting | Value |
|---|---|
| Runner directory | `~/actions-runner/` |
| Token location | GitHub → Repo → Settings → Actions → Runners |
| Start runner | `tmux new -s runner` then `./run.sh` |
| Workflow file | `.github/workflows/cluster-<branch>.yml` |
| SLURM output log | `logs/slurm-<job_id>.out` |
| SLURM error log | `logs/slurm-<job_id>.err` |
| Trigger | Push or merged PR to the watched branch |
| Output visible | Inline in the GitHub Actions log |

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Workflow stuck on "Waiting for a runner" | The runner is not running. SSH in and restart: `tmux attach -t runner` then `./run.sh` |
| `sbatch: command not found` | Add `module load slurm` (or the cluster equivalent) to the top of your job script |
| Token expired during `config.sh` | Generate a new token from GitHub Settings — tokens are valid for 1 hour only |
| No `.out` or `.err` file found | Check your job script has `#SBATCH --output=logs/slurm-%j.out` and that the `logs/` directory exists on the cluster |
