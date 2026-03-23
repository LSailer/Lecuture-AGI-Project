#!/bin/sh
#SBATCH --job-name=autoresearch-dev
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

# Critical: load CUDA runtime so torch.cuda.is_available() works (see docs/gpu_debugging.md)
module load devel/cuda/12.8

GAME=${GAME:-rubiks_cube}
MAX_ITER=2
ITER=0

echo "=== DEV Autoresearch: game=$GAME, max_iter=$MAX_ITER ==="
echo "GPU: $(nvidia-smi --query-gpu=name --format=csv,noheader 2>/dev/null || echo 'none')"

while [ $ITER -lt $MAX_ITER ]; do
  ITER=$((ITER + 1))
  echo ""
  echo "=== Iteration $ITER/$MAX_ITER ==="

  claude -p "read program.md, game=$GAME, iteration $ITER of $MAX_ITER. IMPORTANT: use config src/config/${GAME}_dev.yaml (3 disks, max_steps=100). Pass --config src/config/${GAME}_dev.yaml to main.py. This is a DEV validation run." \
    --dangerously-skip-permissions \
    --model sonnet \
    --max-budget-usd 1
done

echo "=== Dev experiments done after $ITER iterations ==="

# --- Wrap-up: analysis + PR ---
echo "=== Wrap-up ==="
git add results.tsv findings.md && git commit -m "dev: autoresearch smoke test results" || true

uv run jupyter nbconvert --to notebook --execute --inplace notebooks/analyze_autoresearch.ipynb
git add notebooks/analyze_autoresearch.ipynb && git commit -m "dev: analysis notebook" || true

git push -u origin HEAD
gh pr create --title "dev: autoresearch smoke test ($GAME)" \
  --body "$(cat results.tsv 2>/dev/null || echo 'no results')" || true

echo "=== Dev autoresearch complete ==="
