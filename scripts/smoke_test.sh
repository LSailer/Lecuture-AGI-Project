#!/bin/sh
#SBATCH --job-name=rubiks-smoke
#SBATCH --output=logs/rubiks-smoke-%j.out
#SBATCH --error=logs/rubiks-smoke-%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=127G
#SBATCH --gres=gpu:1
#SBATCH --time=00:15:00
#SBATCH --partition=dev_gpu_h100

cd "${SLURM_SUBMIT_DIR:-$(dirname "$(readlink -f "$0")")/..}"
mkdir -p logs output

module load devel/cuda/12.8

echo "=== Rubik's Cube Smoke Test ==="
echo "GPU: $(nvidia-smi --query-gpu=name --format=csv,noheader 2>/dev/null || echo 'none')"
echo "Working dir: $(pwd)"

uv run src/main.py --game rubiks_cube --config src/config/rubiks_cube_dev.yaml --max_steps 10

echo "=== Exit code: $? ==="
echo "=== Smoke test complete ==="
