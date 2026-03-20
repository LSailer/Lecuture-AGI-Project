# autoresearch

This is an experiment to have Claude Code do its own research on the MAKER puzzle-solving framework. You are driven by a shell loop — each invocation you run ONE experiment, then exit. The loop feeds you the same prompt again, and you see your previous work in `results.tsv` and git history.

**You are running on a GPU node. Use `uv run` directly (no srun needed).**

## Setup (first iteration only)

If `results.tsv` does not exist yet, this is the first iteration. Do setup:

1. Read the in-scope files for context:
   - `program.md` — these instructions (you're reading it now)
   - `src/main.py` — the solver loop. Do not modify.
   - `src/config/<game>.yaml` — the config file you modify
   - `src/<game>/prompts/*.yaml` — prompt templates you modify or create
   - `src/<game>/enviroment.py` — game rules (read-only)
   - `src/<game>/prompts.py` — prompt loader (read-only)
2. Verify models: `ls LLM/models/` — should contain `qwen3-32b/`, `devstral-24b/`, `deepseek-r1-32b/`.
3. Create `results.tsv` with header:
   ```
   printf 'commit\tsr\tsteps\tstage\tstatus\tdescription\n' > results.tsv
   ```
4. Create `findings.md` with header (if it doesn't exist):
   ```
   printf '# Autoresearch Findings\n\nQualitative insights accumulated across experiment iterations.\nEach entry: what was tried, what was learned, and what to try next.\n\n---\n' > findings.md
   ```
5. Run the **baseline** experiment (step 6 below) with default config.

If `results.tsv` already exists, skip setup — go straight to the experiment loop.

## The game

The game is specified in the prompt (e.g. `game=tower_of_hanoi`). Read it from context.

## One iteration = one experiment

Each invocation, you do exactly ONE experiment:

1. **Read state**: `cat results.tsv`, `cat findings.md`, and `git log --oneline -10` — what worked, what didn't, and qualitative insights from prior iterations
2. **Decide**: based on previous results, pick what to try next. Be creative.
3. **Modify**: edit config YAML and/or prompt YAML files
4. **Commit config changes**: `git add src/config/ src/*/prompts/ && git commit -m "exp: <description>"`
   (Only commit config/prompt changes — results are logged separately in step 7)
5. **Run** (direct, already on GPU):
   ```bash
   uv run src/main.py --game <game> > run.log 2>&1
   ```
6. **Parse**: `grep "Success Rate\|solved in\|Max steps" run.log`
   - If empty → crash. `tail -50 run.log` for error. Log as crash.
7. **Log**: append result to `results.tsv`, then commit:
   `git add results.tsv findings.md && git commit -m "results: <status> <summary>"`
8. **Keep or discard**:
   - SR improved or same SR with fewer steps → keep (branch advances)
   - Worse → `git revert HEAD~1 --no-edit` (reverts the experiment commit, preserving history)
9. **Record insight**: append a brief entry to `findings.md` — what you tried, what you learned, what to try next. Use this format:
   ```
   ## Iteration N — short description
   - **Config**: model, temperature, prompt variant, difficulty
   - **Result**: SR%, steps (optimal?)
   - **Insight**: 1-2 sentences on what you learned and what to try next.
   ```
10. **Stage up**: if SR=100% → increase difficulty (more disks / harder puzzle)

Then **exit**. The shell loop will invoke you again. After all iterations, the shell script handles analysis notebook + PR automatically.

## What you CAN modify

- `src/config/<game>.yaml` — `temperature`, `model_path`, `prompt_variant`, `max_agents_per_step`, `margin_k`, `num_disks`, `initial_state`, `max_steps`
- `src/<game>/prompts/*.yaml` — system and user prompt templates. Create new variants too.
- `findings.md` — qualitative insights from experiments (append-only lab notebook)

## What you CANNOT modify

- `src/main.py`, `src/*/enviroment.py`, `src/utils/` — solver, games, and pipeline are fixed.

## The metric

**SR (Success Rate)** = `compute_progress()`, printed as `Success Rate: XX.X%`.
- `100%` = fully solved
- `< 100%` = partial progress

**Also track steps.** Fewer steps at same SR = better.

## Available models

- `LLM/models/qwen3-32b` — Qwen3-32B
- `LLM/models/devstral-24b` — Devstral-24B (default)
- `LLM/models/deepseek-r1-32b` — DeepSeek-R1-32B

## Difficulty stages

- **Tower of Hanoi**: `num_disks` 3 → 4 → 5 → ... (optimal = 2^n - 1 moves)
- **Sliding Puzzle**: `2x2` → `3x3 (easiest)` → `3x3 (hardest)` → `4x4 (easiest)` → `4x4 (hardest)` (use CONFIGS dict keys as `initial_state`)

## Results format

`results.tsv` — tab-separated, 6 columns:

```
commit	sr	steps	stage	status	description
a1b2c3d	1.000000	7	3	keep	baseline devstral T=0.1
b2c3d4e	1.000000	9	3	discard	qwen3 T=0.1 (more steps)
c3d4e5f	0.666667	200	4	keep	devstral T=0.1 4 disks
d4e5f6g	0.000000	0	4	crash	deepseek OOM
```

## Tips

1. **Start simple**: baseline first, then one change at a time
2. **Prompts matter most**: different reasoning strategies, CoT styles, examples, rule phrasings
3. **Temperature**: 0.0-0.1 for greedy, 0.3-0.7 for voting diversity
4. **Check failures.csv**: `output/failures.csv` shows parsing failures → fix prompt format
5. **Read the game**: Tower of Hanoi has a known optimal algorithm — try encoding it in the prompt
6. **Be creative**: if stuck, rewrite prompts from scratch, try radical changes
