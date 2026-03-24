#!/bin/sh
# Submit dev dry run + all 3 full game jobs with dependency.
# Usage: bash scripts/run_autoresearch_run3_full.sh
#
# The full jobs only start if the dev job succeeds (exit 0).
# If the dev job fails, SLURM automatically cancels the dependents.

set -e
cd "$(dirname "$(readlink -f "$0")")/.."

echo "=== Submitting Autoresearch Run 3 ==="

# 1. Dev dry run (30min, sudoku)
DEV_JOB=$(cd worktrees/run3_sudoku && sbatch --parsable ../../scripts/run_autoresearch_run3_dev.sh)
echo "Dev job submitted: $DEV_JOB (30min dry run)"

# 2. Full 24h jobs — depend on dev success
SUDOKU_JOB=$(cd worktrees/run3_sudoku && GAME=sudoku sbatch --parsable --dependency=afterok:$DEV_JOB ../../scripts/run_autoresearch_run3.sh)
echo "Sudoku job submitted: $SUDOKU_JOB (depends on $DEV_JOB)"

NONOGRAM_JOB=$(cd worktrees/run3_nonogram && GAME=nonogram sbatch --parsable --dependency=afterok:$DEV_JOB ../../scripts/run_autoresearch_run3.sh)
echo "Nonogram job submitted: $NONOGRAM_JOB (depends on $DEV_JOB)"

CUBE_JOB=$(cd worktrees/run3_cube && GAME=rubiks_cube sbatch --parsable --dependency=afterok:$DEV_JOB ../../scripts/run_autoresearch_run3.sh)
echo "Cube job submitted: $CUBE_JOB (depends on $DEV_JOB)"

echo ""
echo "=== All jobs submitted ==="
echo "Dev:      $DEV_JOB (30min, dev_gpu_h100)"
echo "Sudoku:   $SUDOKU_JOB (24h, gpu_h100_il, after dev)"
echo "Nonogram: $NONOGRAM_JOB (24h, gpu_h100_il, after dev)"
echo "Cube:     $CUBE_JOB (24h, gpu_h100_il, after dev)"
echo ""
echo "If dev fails: scancel $SUDOKU_JOB $NONOGRAM_JOB $CUBE_JOB"
