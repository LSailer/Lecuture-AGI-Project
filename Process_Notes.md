# Process Notes

## Feature: WandB Integration, Fallback Mechanism & Pipeline Optimization

**Branch:** `feat/wandb-fallback-optimization`
**Date:** 2026-02-07

---

### Problem Statement

The MAKER framework had three gaps:
1. **No observability** -- no way to track experiments, compare runs, or inspect per-agent predictions across steps.
2. **No recovery when all agents fail** -- if every agent in a voting step produced an unparseable or invalid response, the solver immediately broke out of the game loop with no retry mechanism.
3. **Sequential bottleneck** -- agents were called one-by-one in the voting loop, wasting GPU throughput on a model that supports batch inference.

---

### Decisions Made

#### 1. Observability: WandB + failures.csv

- **WandB** tracks each run end-to-end: config is logged at init, a `predictions` Table captures every (step, agent, state, action, error) row, and summary metrics (`total_steps`, `solved`) are logged at the end.
- **`output/failures.csv`** is a lightweight, always-available failure log (timestamp, current_state, agent_id) written in the `Agent.parse_response()` error path. This complements WandB for quick offline debugging.

#### 2. Fallback Architecture: Gemini API + Local DeepSeek

When all agents fail a step, a **FallbackModel** rewrites the system and user prompts:

- **Fallback chain:** Gemini 2.5 Flash API (free tier) first, then local DeepSeek-R1-Distill-Qwen-32B if Gemini fails or is rate-limited.
- **Meta-prompt approach:** The fallback receives the original prompts + all failed predictions, analyzes the failure modes, and produces improved prompts in a structured `<SYSTEM_PROMPT>` / `<USER_PROMPT>` format.
- **Prompt composition:** The fallback's system prompt fully replaces the original (it's state-independent). The fallback's user prompt is **prepended** as additional guidance to the state-specific user prompt built by `agent.build_prompt()` -- this ensures game state (previous_move, current_state, step) is always present.
- **Lazy loading:** The local DeepSeek model is only loaded into VRAM when `_call_local()` is actually invoked, avoiding memory conflict with the primary Devstral model.
- **Debug tracking:** Each fallback invocation appends to `output/debug_prompts.md` with the rewritten prompts and the failures that triggered them.
- **Config-driven:** `max_fallback_retries` (default 3), `fallback_api` ("gemini" | "local" | "both"), model IDs all live in the per-game YAML configs.

#### 3. Pipeline Optimization: Batch Inference

- **`LLM.generate_batch()`** passes N message sets to the HuggingFace pipeline in a single call with `batch_size=N`. This is the primary speedup -- the GPU processes all prompts in one forward pass instead of N sequential passes.
- **`run_voting_batch()`** in main.py builds all N prompts, runs one batched LLM call, then parses responses and tallies votes. If the margin isn't met after the batch, additional single-agent tiebreaker calls are made sequentially.
- **Async for API fallback:** Gemini calls use `google-genai`'s async client (`client.aio.models.generate_content`) wrapped in a sync entrypoint that handles both event-loop and non-event-loop contexts.

#### 4. Agent Refactoring

The `Agent` class was split into three composable methods:
- `build_prompt(previous_move, current_state, step)` -- returns `(messages_list, user_prompt_str)`
- `parse_response(content, current_state, step, agent_num)` -- parses, logs to CSV + failures.csv, raises on error
- `execute_decompose_prompt(...)` -- convenience method that chains both (kept for backward compatibility and single-agent tiebreaker calls)

This separation enables batch inference (main.py builds N prompts, batches them, parses individually) without duplicating code.

#### 5. Type Annotations

All modified/created files are fully typed:
- `parser.py`: `re.Pattern`, `Callable`, `tuple[Any, Any]` returns
- `llm.py`: `Message` and `Conversation` type aliases, typed returns
- `decomposer.py`: `ModuleType` for prompts, `Conversation` for messages, `tuple[Any, Any]` for action/state
- `fallback.py`: `FailedPrediction` type alias, all methods typed with `str`, `int`, `tuple[str, str]` returns
- `main.py`: `argparse.Namespace`, `dict[str, Any]`, `wandb.Table | None`, full `run_voting_batch` signature

---

### Files Changed

| File | Action | What Changed |
|------|--------|-------------|
| `pyproject.toml` | Modified | Added `wandb`, `google-genai`, `aiohttp` dependencies |
| `src/config/tower_of_hanoi.yaml` | Modified | Added `max_fallback_retries`, `fallback_api`, `fallback_local_model`, `gemini_model` |
| `src/config/sliding_puzzle.yaml` | Modified | Same fallback config keys |
| `src/utils/parser.py` | Modified | Added type annotations |
| `src/utils/llm.py` | Modified | Added `generate_batch()`, `Message`/`Conversation` type aliases, type annotations |
| `src/utils/decomposer.py` | Modified | Split into `build_prompt()` + `parse_response()` + `execute_decompose_prompt()`, added `failures.csv` tracking, type annotations |
| `src/utils/fallback.py` | **Created** | `FallbackModel` class: Gemini async + local DeepSeek fallback chain, meta-prompt builder, debug logging |
| `src/main.py` | Modified | WandB init/table/logging, `run_voting_batch()` for batch inference, fallback retry loop, type annotations |
| `LLM/download.py` | Modified | Added DeepSeek-R1-Distill-Qwen-32B download |

---

### New Output Artifacts

| File | When Created | Purpose |
|------|-------------|---------|
| `output/failures.csv` | On agent parse errors | Quick offline failure log (timestamp, state, agent_id) |
| `output/debug_prompts.md` | On fallback invocations | Tracks rewritten prompts and the failures that triggered them |
| WandB `predictions` Table | End of each run | Per-agent prediction log viewable in WandB dashboard |

---

### Environment Requirements

- `GEMINI_API_KEY` env var required for Gemini fallback (free tier: 250 req/day)
- `HF_TOKEN` env var required for model downloads (existing requirement)
- `WANDB_API_KEY` env var or `wandb login` for experiment tracking

---

### Verification Plan

1. **WandB:** Run Tower of Hanoi (3 disks) -- verify WandB dashboard shows predictions table, config, and summary metrics
2. **failures.csv:** Temporarily break model output parsing -- verify `output/failures.csv` populates
3. **Fallback trigger:** Set `max_agents_per_step: 1` and break parsing -- verify fallback engages, `debug_prompts.md` populates, retries respect `max_fallback_retries`
4. **Batch inference:** Time 3-disk solve with sequential vs batch voting -- measure speedup
5. **Fallback chain:** Block Gemini API (invalid key) -- verify local DeepSeek loads and takes over
