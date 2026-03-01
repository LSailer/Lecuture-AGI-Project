#!/bin/sh
#SBATCH --job-name=RunSimulation
#SBATCH --output=logs/slurm-%j.out
#SBATCH --error=logs/slurm-%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=127G
#SBATCH --gres=gpu:1

CMD="uv run src/main.py --game ${GAME:-tower_of_hanoi} \
  --margin_k ${MARGIN_K:-2} \
  --max_agents_per_step ${MAX_AGENTS:-15} \
  --temperature ${TEMPERATURE:-0.1} \
  --num_disks ${NUM_DISKS:-10}"

[ "${TEMP_ESCALATION:-0}" = "1" ] && CMD="$CMD --temp_escalation"

eval $CMD
