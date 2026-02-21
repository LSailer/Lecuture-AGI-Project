#!/bin/sh
#SBATCH --job-name=RunSimulation
#SBATCH --output=logs/slurm-%j.out
#SBATCH --error=logs/slurm-%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=127G
#SBATCH --gres=gpu:1

uv run src/main.py --game sliding_puzzle --margin_k 3

# Usage:
# Dev:  sbatch --partition=dev_gpu_h100 --time=00:30:00 scripts/run.sh
# Prod: sbatch --partition=gpu_h100_il  --time=42:00:00 scripts/run.sh
