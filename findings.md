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
