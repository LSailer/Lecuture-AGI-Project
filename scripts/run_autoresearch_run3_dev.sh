#!/bin/sh
#SBATCH --job-name=autoresearch_run3_dev
#SBATCH --output=logs/autoresearch-dev-%j.out
#SBATCH --error=logs/autoresearch-dev-%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=127G
#SBATCH --gres=gpu:1
#SBATCH --time=00:30:00
#SBATCH --partition=dev_gpu_h100

cd "${SLURM_SUBMIT_DIR:-$(dirname "$(readlink -f "$0")")/..}"
mkdir -p logs output
export WANDB_MODE=disabled

# Critical: load CUDA runtime so torch.cuda.is_available() works
module load devel/cuda/12.8

GAME=${GAME:-sudoku}
MAX_ITER=2
ITER=0

echo "=== DEV Autoresearch Run 3: game=$GAME, max_iter=$MAX_ITER ==="
echo "GPU: $(nvidia-smi --query-gpu=name --format=csv,noheader 2>/dev/null || echo 'none')"

while [ $ITER -lt $MAX_ITER ]; do
  ITER=$((ITER + 1))
  echo ""
  echo "=== Iteration $ITER/$MAX_ITER ==="

  claude -p "read program_run3.md, game=$GAME, iteration $ITER of $MAX_ITER. IMPORTANT: This is a DEV validation run — use easy difficulty, max_steps=50." \
    --dangerously-skip-permissions \
    --model sonnet \
    --max-budget-usd 1
done

echo "=== Dev experiments done after $ITER iterations ==="
