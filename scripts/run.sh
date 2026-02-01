#!/bin/bash
#SBATCH --job-name=RunSimulation
#SBATCH --output=logs/Logs%j.out
#SBATCH --error=logs/Logs%j.err
#SBATCH --time=42:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=127G
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu_h100_il

uv run src/main.py --game tower_of_hanoi --margin_k 3
#uv run src/main.py --game sliding_puzzle --margin_k 3

# Slurm Commands
# module load devel/python/3.10.5
# sbatch -> Run script
# squeue -> show the list
# scancel <job_id> -> cancel job
# sinfo_t_idle
# squeue --start