# autoresearch

This is an experiment to have Claude Code do its own research on the MAKER puzzle-solving framework.

## Setup

To set up a new experiment, work with the user to:

1. **Agree on a run tag**: propose a tag based on today's date (e.g. `mar14`). The branch `autoresearch/<game>-<tag>` must not already exist.
2. **Agree on the game**: `tower_of_hanoi` or `sliding_puzzle`. One game per session.
3. **Create the branch**: `git checkout -b autoresearch/<game>-<tag>` from current HEAD.
4. **Read the in-scope files** for full context:
   - `program.md` — these instructions (you're reading it now)
   - `src/main.py` — the solver loop. Read it but do not modify the core logic.
   - `src/config/<game>.yaml` — the config file you modify
   - `src/<game>/prompts/*.yaml` — prompt templates you modify (or create new ones)
   - `src/<game>/enviroment.py` — game environment (read-only, understand the rules)
   - `src/<game>/prompts.py` — prompt loader (read-only, understand how YAML → prompt)
5. **Verify models exist**: `ls LLM/models/` — should contain `qwen3-32b/`, `devstral-24b/`, `deepseek-r1-32b/`.
6. **Initialize results.tsv**: Create `results.tsv` with just the header row. The baseline will be recorded after the first run.
7. **Confirm and go**: Confirm setup looks good.

Once you get confirmation, kick off the experimentation.

## Experimentation

Each experiment runs on a single GPU. You launch it as:

```
uv run src/main.py --game <game> > run.log 2>&1
```

**What you CAN modify:**
- `src/config/<game>.yaml` — this is your main knob. Everything is fair game: `temperature`, `model_path`, `prompt_variant`, `max_agents_per_step`, `margin_k`, `num_disks` (tower_of_hanoi), `initial_state` (sliding_puzzle), `max_steps`.
- `src/<game>/prompts/*.yaml` — the system and user prompt templates. You can edit existing variants or create entirely new ones. This is where the real creativity happens: try different reasoning strategies, chain-of-thought styles, rule phrasings, examples, etc.

**What you CANNOT modify:**
- `src/main.py` — the solver loop is fixed.
- `src/*/enviroment.py` — game rules and environments are fixed.
- `src/utils/` — parser, LLM pipeline, fallback model are fixed.
- `prepare.py` equivalent: there is none. The games are deterministic.

**The goal is simple: get the highest SR (Success Rate) with the fewest steps.**

SR = `compute_progress()`, printed at the end of each run as `Success Rate: XX.X%`. It measures how close the agent got to solving the puzzle:
- `100%` = fully solved
- `< 100%` = partial progress (tiles in correct position / total tiles, or disks on target peg / total disks)

Since the step budget (`max_steps`) is configurable, you should also track total steps used. Fewer steps at the same SR is better.

**Available models** (pre-downloaded in `LLM/models/`):
- `LLM/models/qwen3-32b` — Qwen3-32B (strong reasoning)
- `LLM/models/devstral-24b` — Devstral-Small-2-24B-Instruct (current default)
- `LLM/models/deepseek-r1-32b` — DeepSeek-R1-Distill-Qwen-32B (reasoning-focused)

**Parameters to experiment with:**
- `model_path` — which model to use
- `temperature` — sampling temperature (0.0 = deterministic, greedy)
- `prompt_variant` — which YAML prompt file to load (e.g. `base`, `cot_detailed`, `minimal`, or new ones you create)
- `max_agents_per_step` — number of parallel agents voting per step (more = stronger consensus but slower)
- `margin_k` — consensus margin for voting (higher = stricter agreement needed)
- `num_disks` — difficulty level for tower_of_hanoi (start at 3)
- `initial_state` — puzzle config for sliding_puzzle (use keys from `CONFIGS` dict in enviroment.py)
- `max_steps` — step budget per run

**Stages (difficulty progression):**
- Tower of Hanoi: start with `num_disks: 3` (optimal = 7 moves). Once SR=100%, try 4, 5, 6, ...
- Sliding Puzzle: start with `2x2` config. Then `3x3 (easiest)`, `3x3 (hardest)`, `4x4 (easiest)`, `4x4 (hardest)`.

**The first run**: Your very first run should always be to establish the baseline with the default config, so you will run the solver as-is.

## Output format

The script prints a summary at the end:

```
Puzzle solved in 7 steps!
Success Rate: 100.0%
```

or:

```
Max steps (200) reached without solving.
Success Rate: 44.4%
```

Extract the key metrics from the log:

```
grep "Success Rate\|solved in\|Max steps" run.log
```

## Logging results

When an experiment is done, log it to `results.tsv` (tab-separated, NOT comma-separated).

The TSV has a header row and 6 columns:

```
commit	sr	steps	stage	status	description
```

1. git commit hash (short, 7 chars)
2. SR achieved (e.g. 1.000000) — use 0.000000 for crashes
3. total steps used
4. stage (num_disks for ToH, config name for sliding puzzle)
5. status: `keep`, `discard`, or `crash`
6. short text description of what this experiment tried

Example:

```
commit	sr	steps	stage	status	description
a1b2c3d	1.000000	7	3	keep	baseline devstral T=0.1
b2c3d4e	1.000000	9	3	discard	qwen3 T=0.1 (solved but more steps)
c3d4e5f	0.666667	200	4	keep	devstral T=0.1 4 disks (partial)
d4e5f6g	0.000000	0	4	crash	deepseek OOM
```

## The experiment loop

The experiment runs on a dedicated branch (e.g. `autoresearch/toh-mar14`).

LOOP FOREVER:

1. Look at the git state and `results.tsv` — what have you tried, what worked, what didn't
2. Think about what to try next. Be creative: try different models, temperatures, prompt strategies, agent counts. If something almost worked, iterate on it. If you're stuck, try something radically different.
3. Modify the config YAML and/or prompt YAML files with your experimental idea
4. git commit with a descriptive message
5. Run the experiment: `uv run src/main.py --game <game> > run.log 2>&1`
6. Read the results: `grep "Success Rate\|solved in\|Max steps" run.log`
7. If the grep output is empty, the run crashed. Run `tail -50 run.log` to read the stack trace and attempt a fix. If you can't fix it after a few attempts, give up on that idea.
8. Record the results in results.tsv (do NOT commit results.tsv, leave it untracked)
9. If SR improved (higher), or same SR with fewer steps → "advance" the branch, keeping the commit
10. If SR is equal or worse → `git reset --hard HEAD~1` to discard
11. If SR = 100% at current difficulty → increase difficulty (more disks / harder puzzle config), reset best SR tracking

The idea is that you are a completely autonomous researcher trying things out. If they work, keep. If they don't, discard. And you're advancing the branch so that you can iterate. If you feel like you're getting stuck, try something creative — rewrite the prompt from scratch, try a completely different reasoning strategy, combine ideas from previous near-misses.

**Timeout**: Each experiment should take at most ~30 minutes. If a run exceeds 30 minutes, kill it and treat it as a failure.

**Crashes**: If a run crashes (OOM, bug, etc.), use your judgment: if it's a typo or easy fix, fix and re-run. If the idea is fundamentally broken, skip it and move on.

**NEVER STOP**: Once the experiment loop has begun, do NOT pause to ask the human if you should continue. The human might be asleep or away. You are autonomous. If you run out of ideas, think harder — re-read the prompt files, try combining previous near-misses, try more radical changes. The loop runs until the human interrupts you.

## Tips for good experiments

1. **Start simple**: establish baseline, then change one thing at a time
2. **Prompt engineering matters most**: the prompts are where the real gains are. Try different reasoning strategies, more/fewer examples, different phrasings
3. **Temperature**: low (0.0-0.1) for deterministic/greedy, higher (0.3-0.7) for diversity in voting
4. **Models**: bigger isn't always better — smaller models with better prompts can beat larger ones
5. **Agents + voting**: more agents = better consensus but slower. Find the sweet spot.
6. **Read the game rules**: understand the optimal strategy (e.g. Tower of Hanoi has a known optimal algorithm — can you encode it in the prompt?)
7. **Check failures.csv**: `output/failures.csv` logs parsing failures — if the model can't follow the output format, fix the prompt
