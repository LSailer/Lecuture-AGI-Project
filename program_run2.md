# autoresearch — Run 2

This is Run 2 of the autoresearch experiment on the MAKER puzzle-solving framework. You are driven by a shell loop — each invocation you run ONE experiment, then exit. The loop feeds you the same prompt again, and you see your previous work in `results.tsv` and git history.

**You are running on a GPU node. Use `uv run` directly (no srun needed).**

## Run 2 constraints

1. **No lookup tables**: Do NOT pre-compute move outcomes, scores, or solution paths
   in the prompt. The LLM agents must reason through game mechanics at each step.
   Specifically:
   - No `{move_lookup}` placeholders or `_compute_move_lookup()` usage
   - No FSM (finite state machine) solution tables
   - No inline STEP→MOVE maps that pre-solve the puzzle
   - The agent should understand the game rules from the prompt and decide
     each move through its own reasoning

2. **Cross-game baseline**: On your first iteration, read results from solved games
   for transferable patterns:
   - `results/tower_of_hanoi.tsv` — what configs/approaches worked
   - `results/sliding_puzzle.tsv` — what configs/approaches worked
   These show proven strategies (voting consensus, intermediate reasoning fields,
   anti-cycle rules) that may transfer to your game.

3. **Write your own findings**: Append to `findings.md` (created fresh on first iteration).

## Game-specific guidance

- **Nonogram**: Continue from the `base_run2` prompt (based on Run 1's best overlap strategy, 76% SR on 5x5 diamond). Focus on improving constraint propagation reasoning — the LLM must learn to enumerate feasible placements and find forced cells.
- **Rubik's Cube**: Start fresh — design new prompts that teach the agent cube rotation mechanics WITHOUT lookup tables. The challenge: the LLM must learn to mentally simulate face rotations and sticker permutations. Consider encoding permutation rules in the prompt.
- **Sudoku**: Start fresh — design prompts that teach the agent constraint elimination WITHOUT pre-computed candidate lists. The agent must scan rows, columns, and boxes to find valid digits itself.

## Setup (first iteration only)

If `results.tsv` does not exist yet, this is the first iteration. Do setup:

1. Read the in-scope files for context:
   - `program_run2.md` — these instructions (you're reading it now)
   - `src/main.py` — the solver loop. Do not modify.
   - `src/config/<game>.yaml` — the config file you modify
   - `src/<game>/prompts/*.yaml` — prompt templates you modify or create
   - `src/<game>/enviroment.py` — game rules (read-only)
   - `src/<game>/prompts.py` — prompt loader (read-only)
   - `results/tower_of_hanoi.tsv` — cross-game baseline (read-only)
   - `results/sliding_puzzle.tsv` — cross-game baseline (read-only)
2. Verify models: `ls LLM/models/` — should contain `qwen3-32b/`, `devstral-24b/`, `deepseek-r1-32b/`.
3. Create `results.tsv` with header:
   ```
   printf 'commit\tsr\tsteps\tstage\tstatus\tdescription\n' > results.tsv
   ```
4. Create `findings.md` with header:
   ```
   printf '# Autoresearch Findings — Run 2\n\nQualitative insights accumulated across experiment iterations.\nEach entry: what was tried, what was learned, and what to try next.\n\n---\n' > findings.md
   ```
5. Run the **baseline** experiment (step 6 below) with default config.

If `results.tsv` already exists, skip setup — go straight to the experiment loop.

## The game

The game is specified in the prompt (e.g. `game=nonogram`). Read it from context.

## One iteration = one experiment

Each invocation, you do exactly ONE experiment:

1. **Read state**: `cat results.tsv`, `cat findings.md`, and `git log --oneline -10` — what worked, what didn't, and qualitative insights from prior iterations
2. **Decide**: based on previous results, pick what to try next. Be creative — but do NOT create lookup tables or pre-computed solution paths.
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
- `program_run2.md` — these instructions are fixed.
- `results/tower_of_hanoi.tsv`, `results/sliding_puzzle.tsv` — cross-game baselines are read-only.

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

- **Nonogram**: `4x4 (butterfly)` → `4x4 (diamond)` → `5x5 (diamond)` → `5x5 (fragmented)` → `7x7 (cross)` → `10x10 (large)` (use CONFIGS dict keys for `row_hints`/`col_hints`)
- **Rubik's Cube**: `2-move` → `4-move` → `6-move` → `8-move` → `10-move` → `12-move` (use CONFIGS dict keys as `scramble`)
- **Sudoku**: `easy` → `medium` → `hard` → `expert` → `master` (use CONFIGS dict keys as `initial_state`)

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
5. **Be creative**: if stuck, rewrite prompts from scratch, try radical changes
6. **No shortcuts**: the goal is LLM reasoning, not pre-computed answers. If you find yourself building a lookup table, stop and rethink.
7. **Learn from solved games**: tower_of_hanoi succeeded with algorithmic rule encoding in prompts; sliding_puzzle succeeded with intermediate reasoning fields (N, tile_at_N) and 9-agent voting consensus.
