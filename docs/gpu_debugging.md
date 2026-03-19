# GPU Debugging Log

## Issue: "No GPU" when running notebook with srun

**Symptom:** `torch.cuda.is_available()` returns `False` and Test 7 prints
`SKIP: no nvidia-smi (not on GPU node)` even when using `srun --gres=gpu:1`.

**Root cause:** The CUDA runtime libraries are not in `LD_LIBRARY_PATH`.
On this HPC cluster, CUDA is provided via environment modules. Without
`module load devel/cuda/12.8`, PyTorch cannot find `libcuda.so` and reports
no GPU — even though SLURM allocated the GPU hardware via `--gres=gpu:1`.

| Layer | What it does | Without it |
|-------|-------------|------------|
| `--gres=gpu:1` | SLURM allocates GPU hardware, sets `CUDA_VISIBLE_DEVICES` | No GPU hardware assigned |
| `module load devel/cuda/12.8` | Adds CUDA libs to `LD_LIBRARY_PATH` | `torch.cuda.is_available()` → `False` |

**Fix applied:**

1. **`run.sh`** — added `module load devel/cuda/12.8` and the notebook execution command:
   ```bash
   srun --partition=dev_gpu_a100_il --gres=gpu:1 --time=00:30:00 --mem=64G \
     bash -c "module load devel/cuda/12.8 && uv run jupyter nbconvert --to notebook --execute --inplace notebooks/test_autoresearch.ipynb"
   ```

2. **`src/main.py`** — added diagnostic prints after device detection so the
   selected device is always visible in logs.

**Working command (H100 partition):**
```bash
srun --partition=dev_gpu_h100 --time=00:10:00 --gres=gpu:1 --mem=64G \
  bash -c "module load devel/cuda/12.8 && uv run jupyter nbconvert --to notebook --execute --inplace notebooks/test_autoresearch.ipynb"
```

## Verification (2026-03-19)

All 9 tests passed after the fix:

- Test 7: `NVIDIA H100, 95830 MiB` — **PASS: GPU visible**
- Test 8: `claude version: 2.1.79` — **PASS: Claude Code works**
- Test 9: `main.py` ran 5 steps on GPU — **PASS: main.py runs on GPU**
