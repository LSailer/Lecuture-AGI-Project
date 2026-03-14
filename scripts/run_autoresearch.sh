#!/bin/sh
#SBATCH --job-name=autoresearch
#SBATCH --output=logs/autoresearch-%j.out
#SBATCH --error=logs/autoresearch-%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=127G
#SBATCH --gres=gpu:1
#SBATCH --time=24:00:00
#SBATCH --partition=gpu_h100_il

mkdir -p logs output

uv run scripts/autoresearch.py \
  --game ${GAME:-tower_of_hanoi} \
  --time-budget 23.5 \
  --tag ${TAG:-$(date +%b%d | tr '[:upper:]' '[:lower:]')}
