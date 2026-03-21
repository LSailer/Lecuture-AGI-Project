# Nonogram Autoresearch Preparation — Design Spec

## Context

The nonogram puzzle environment exists but is not ready for autoresearch. Two runtime-breaking issues must be fixed (prompts lack `variant` parameter, no YAML prompt files), the `CONFIGS` dict needs to be replaced with the correct user-specified puzzles, and the puzzle needs its own worktree to run autonomously alongside Tower of Hanoi and Sliding Puzzle.

**Note:** `compute_progress()` and a preliminary `CONFIGS` dict already exist in the codebase (added in a prior session). The CONFIGS must be replaced with the user's specific puzzle definitions.

## Changes

### 1. Replace `CONFIGS` dict in `src/nonogram/enviroment.py`

Replace the existing CONFIGS (which has 7 entries like `5x5 (diamond)`, `5x5 (cross)`, etc.) with the user's 6-stage progression:

```python
CONFIGS = {
    "4x4 (butterfly)": {
        "row_hints": [[1, 1], [2], [2], [1, 1]],
        "col_hints": [[1, 1], [2], [2], [1, 1]],
    },
    "4x4 (diamond)": {
        "row_hints": [[1], [2], [2], [1]],
        "col_hints": [[1], [2], [2], [1]],
    },
    "5x5 (diamond)": {
        "row_hints": [[1], [3], [5], [3], [1]],
        "col_hints": [[1], [3], [5], [3], [1]],
    },
    "5x5 (fragmented)": {
        "row_hints": [[1], [2], [3], [1, 1], [4]],
        "col_hints": [[1, 1], [2, 1], [3], [1, 1], [2]],
    },
    "7x7 (cross)": {
        "row_hints": [[1], [3], [5], [7], [5], [3], [1]],
        "col_hints": [[1], [3], [5], [7], [5], [3], [1]],
    },
    "10x10 (large)": {
        "row_hints": [[4], [6], [8], [10], [10], [10], [10], [8], [6], [4]],
        "col_hints": [[4], [6], [8], [10], [10], [10], [10], [8], [6], [4]],
    },
}
```

**Difficulty stages:** `4x4 (butterfly)` -> `4x4 (diamond)` -> `5x5 (diamond)` -> `5x5 (fragmented)` -> `7x7 (cross)` -> `10x10 (large)`.

**Convention:** Use `[]` (empty list) for "no filled cells in a line," never `[0]`. The `_line_feasible` function handles `m == 0` correctly; `[0]` would produce incorrect results in `_line_satisfied`.

### 2. Keep existing `compute_progress()` — already implemented

The method already exists and is correct:
```python
def compute_progress(self) -> float:
    total = self.n_rows * self.n_cols
    decided = sum(1 for row in self.grid for c in row if c != -1)
    return decided / total
```

No changes needed.

### 3. Refactor `src/nonogram/prompts.py` to YAML variant system

Replace hardcoded prompts with `_load_variant()` pattern matching `sliding_puzzle/prompts.py`:

- Add `import yaml`, `_PROMPTS_DIR`, `_prompt_cache`, `_load_variant(variant)`
- `get_system_prompt(environment, variant="base")` — loads from YAML, formats with `{n_rows}`, `{n_cols}`
- `build_user_prompt(current_state, previous_move, environment, step, variant="base")` — loads from YAML, formats with `{step}`, `{previous_move}`, `{n_rows}`, `{n_cols}`, `{n_rows_minus1}`, `{n_cols_minus1}`, `{row_hints}`, `{col_hints}`, `{current_state}`, `{state_visual}`, `{allowed_cells}`
- Keep `_visualize_state()`, `parse_move()`, `parse_state()`, `MOVE_PATTERN`, `STATE_PATTERN` unchanged

**Note on template variables:** The current f-string uses `{environment.n_rows-1}` for hint index ranges. Since `.format()` cannot do arithmetic, pre-compute `n_rows_minus1 = environment.n_rows - 1` and `n_cols_minus1 = environment.n_cols - 1` in `build_user_prompt()` before calling `.format()`.

### 4. Create `src/nonogram/prompts/base.yaml`

Move current hardcoded prompts into YAML with `system_prompt` and `user_prompt` keys using `{placeholder}` format strings. Replace f-string expressions like `{environment.n_rows-1}` with `{n_rows_minus1}`.

### 5. Update `src/config/nonogram.yaml`

Stage 1 (4x4 butterfly) as active config with user's exact format (commented-out stages 2-6). Add `prompt_variant: base`, `model_path`, `temperature`. Remove explicit `initial_state` (defaults to all -1).

### 6. Create `src/config/nonogram_dev.yaml`

4x4 butterfly puzzle with reduced settings for smoke testing:
- `max_steps: 50`
- `max_agents_per_step: 3`
- `margin_k: 2`
- `prompt_variant: base`
- `model_path: LLM/models/devstral-24b`
- `temperature: 0.5`
- Full fallback config (same as prod)

### 7. Update `program.md` difficulty stages

Add nonogram entry:
```
- **Nonogram**: `4x4 (butterfly)` -> `4x4 (diamond)` -> `5x5 (diamond)` -> `5x5 (fragmented)` -> `7x7 (cross)` -> `10x10 (large)` (use CONFIGS dict keys for row_hints/col_hints)
```

### 8. Create worktree

```bash
git branch autoresearch/nonogram main
git worktree add worktrees/nonogram autoresearch/nonogram
```

## Files Modified

| File | Action |
|------|--------|
| `src/nonogram/enviroment.py` | Replace `CONFIGS` dict (keep `compute_progress()` as-is) |
| `src/nonogram/prompts.py` | Refactor to YAML variant system |
| `src/nonogram/prompts/base.yaml` | New — prompt templates |
| `src/config/nonogram.yaml` | Update with autoresearch defaults + user's stage format |
| `src/config/nonogram_dev.yaml` | New — dev/smoke test config |
| `program.md` | Add nonogram difficulty stages |

## Verification

1. Run from `src/`: `python -c "from nonogram.enviroment import Nonogram, CONFIGS; n = Nonogram.from_config(**CONFIGS['4x4 (butterfly)']); print(n.compute_progress())"` — should print `0.0`
2. Run from `src/`: `python -c "from nonogram.prompts import get_system_prompt, build_user_prompt; from nonogram.enviroment import Nonogram, CONFIGS; n = Nonogram.from_config(**CONFIGS['4x4 (butterfly)']); p = get_system_prompt(n, 'base'); print(p[:80])"` — should print start of system prompt without KeyError
3. Format test: `python -c "from nonogram.prompts import build_user_prompt; from nonogram.enviroment import Nonogram, CONFIGS; n = Nonogram.from_config(**CONFIGS['4x4 (butterfly)']); p = build_user_prompt(n.get_state(), None, n, 1, 'base'); print(p[:80])"` — should print user prompt without KeyError
4. Dev smoke test (GPU node): `uv run src/main.py --game nonogram --config src/config/nonogram_dev.yaml`
5. Worktree: `git worktree list` should show `worktrees/nonogram` on `autoresearch/nonogram`
