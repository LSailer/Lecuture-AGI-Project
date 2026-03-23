# Autoresearch Findings — Run 2

Qualitative insights accumulated across experiment iterations.
Each entry: what was tried, what was learned, and what to try next.

---

## Iteration 1 — baseline 2-move devstral T=0.1 base prompt
- **Config**: model=devstral-24b, temperature=0.1, prompt=base, scramble=2-move (R,U)
- **Result**: SR=59.3%, steps=2000 (max — not solved)
- **Insight**: The `base` prompt asks agents to compute next_state from scratch given only rotation descriptions. All 9 agents (+ all 3 fallback retries) fail with "Inconsistent prediction: next_state does not match current_state + move" at step 1. The LLM cannot reliably apply 3D face rotations to a 54-char sticker string without explicit permutation tables. The existing `permutation.yaml` prompt provides index-level tables for all 18 moves + a worked example — this should be tried next as it removes the mental rotation burden and replaces it with deterministic index lookup.

## Iteration 2 — permutation prompt devstral T=0.1
- **Config**: model=devstral-24b, temperature=0.1, prompt=permutation, scramble=2-move (R,U)
- **Result**: SR=59.3%, steps=2000 (max — not solved), same as baseline
- **Insight**: With the permutation table prompt, all 9 agents output `next_state = current_state` (unchanged). The LLM correctly parses the format but makes zero changes to the string — it cannot execute 20 index-swap operations on a 54-character string even with explicit tables. This is a model capability issue, not prompt design: Devstral-24B lacks reliable string manipulation. **Next**: switch to `deepseek-r1-32b` which has strong step-by-step chain-of-thought reasoning — pair it with the permutation prompt so the model can think through each index substitution explicitly.

## Iteration 3 — deepseek-r1-32b + permutation prompt
- **Config**: model=deepseek-r1-32b, temperature=0.1, prompt=permutation, scramble=2-move (R,U)
- **Result**: SR=59.3%, steps=2000 (max — fallback exhausted at step 1), discard
- **Insight**: DeepSeek-R1-32B is a reasoning model that generates verbose natural-language responses ("Okay, so I'm trying to solve...") regardless of strict 2-line formatting instructions. It cannot comply with "output EXACTLY TWO LINES". **Next**: try `qwen3-32b` — strong instruction-following + step-by-step CoT without the free-form reasoning of R1. Pair with permutation prompt since devstral has already demonstrated the format can be parsed.

## Iteration 4 — qwen3-32b + permutation prompt
- **Config**: model=qwen3-32b, temperature=0.1, prompt=permutation, scramble=2-move (R,U)
- **Result**: SR=59.3%, steps=2000 (max — fallback exhausted at step 1), discard
- **Insight**: Qwen3-32B defaults to thinking mode — wraps all chain-of-thought in `<think>...</think>` tags before the final answer. The parser scans the raw output for "move = " and "next_state = " but only finds them buried inside the think block (not at the top level), so all 9 agents fail every step. Qwen3 supports a `/no_think` suffix in the user message to disable thinking mode entirely and force direct 2-line output. **Next**: create `qwen3_permutation.yaml` prompt variant that appends `/no_think` to the user prompt to suppress thinking mode, keeping qwen3-32b which showed correct format compliance in the Gemini fallback agent (Agent 6 at retry 3 correctly computed U' → next_state).
