#!/bin/sh
#SBATCH --job-name=autoresearch
#SBATCH --output=logs/autoresearch-%j.out
#SBATCH --error=logs/autoresearch-%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=190G
#SBATCH --gres=gpu:1
#SBATCH --time=24:00:00
#SBATCH --partition=gpu_h100_il

cd "${SLURM_SUBMIT_DIR:-$(dirname "$(readlink -f "$0")")/..}"
mkdir -p logs output


GAME=${GAME:-tower_of_hanoi}
MAX_ITER=${MAX_ITER:-50}
ITER=0

echo "=== Autoresearch: game=$GAME, max_iter=$MAX_ITER ==="
echo "GPU: $(nvidia-smi --query-gpu=name --format=csv,noheader 2>/dev/null || echo 'none')"

while [ $ITER -lt $MAX_ITER ]; do
  ITER=$((ITER + 1))
  echo ""
  echo "=== Iteration $ITER/$MAX_ITER ==="

  claude -p "read program.md, game=$GAME, iteration $ITER of $MAX_ITER" \
    --dangerously-skip-permissions \
    --model sonnet \
    --max-budget-usd 2

done

echo "=== Experiments done after $ITER iterations ==="

# --- Wrap-up: analysis + PR ---
echo "=== Wrap-up ==="
git add results.tsv findings.md && git commit -m "autoresearch results" || true

uv run jupyter nbconvert --to notebook --execute --inplace notebooks/analyze_autoresearch.ipynb
git add notebooks/analyze_autoresearch.ipynb && git commit -m "analysis" || true

git push -u origin HEAD
gh pr create --title "autoresearch: $GAME results" --body "$(cat results.tsv)" || true

echo "=== Autoresearch complete ==="
