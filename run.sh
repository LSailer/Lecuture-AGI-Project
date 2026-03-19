#!/bin/bash
export WANDB_MODE=disabled
srun --partition=dev_gpu_a100_il --gres=gpu:1 --time=00:30:00 --mem=64G \
  bash -c "module load devel/cuda/12.8 && uv run jupyter nbconvert --to notebook --execute --inplace notebooks/test_autoresearch.ipynb"
