# Autoresearch Findings — Run 2

Qualitative insights accumulated across experiment iterations.
Each entry: what was tried, what was learned, and what to try next.

---

## Iteration 1 — baseline 2-move devstral T=0.1 base prompt
- **Config**: model=devstral-24b, temperature=0.1, prompt=base, scramble=2-move (R,U)
- **Result**: SR=59.3%, steps=2000 (max — not solved)
- **Insight**: The `base` prompt asks agents to compute next_state from scratch given only rotation descriptions. All 9 agents (+ all 3 fallback retries) fail with "Inconsistent prediction: next_state does not match current_state + move" at step 1. The LLM cannot reliably apply 3D face rotations to a 54-char sticker string without explicit permutation tables. The existing `permutation.yaml` prompt provides index-level tables for all 18 moves + a worked example — this should be tried next as it removes the mental rotation burden and replaces it with deterministic index lookup.
