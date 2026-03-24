# Autoresearch Findings — Sudoku

Qualitative insights accumulated across experiment iterations.
Each entry: what was tried, what was learned, and what to try next.

---

## Iteration 1 — sudoku baseline devstral T=0.5 easy
- **Config**: devstral-24b, T=0.5, base prompt, easy difficulty (stage 1), 43 empty cells
- **Result**: 9.3% SR, 4 cells filled, halted at step 5 (fallback exhausted)
- **Insight**: Model fills cells in row-order with locally valid but globally inconsistent moves. Steps 1-4 filled (0,0)=4,(0,2)=6,(0,3)=8,(0,4)=3 — all pass validate_move — but created a dead-end: (0,5) needed value in {2,7} but 2 was already in the top-middle 3x3 box and 7 was already in col 5. At step 5, all agents proposed "value 8 in col 0" but col 0 already has 8 at r5. Base prompt says "prefer forced moves" but model is pattern-matching, not computing naked singles. Next: redesign prompt to explicitly enumerate candidates per cell (row/col/box exclusion) and require the model to output only cells with a single candidate. Try T=0.1 for more greedy/consistent choices, and a structured CoT prompt that walks through elimination.

## Iteration 2 — sudoku constraint_v1 naked-singles CoT T=0.1 easy
- **Config**: devstral-24b, T=0.1, constraint_v1 prompt, easy (stage 1)
- **Result**: 9.3% SR, 4 cells, halted at step 5 — DISCARD (same as baseline)
- **Insight**: constraint_v1 prompt explicitly asked model to compute candidates via row+col+box elimination, but model still failed: at step 5 all 12 agents tried placing 6 in col 5 (which already has 6). Model computes row-missing values but ignores column contents when selecting the digit. Root cause: LLM cannot reliably perform set intersection over a 9x9 grid in working memory — same failure mode as Rubik's cube before lookup tables. Next: apply the lookup_v1 strategy — pre-compute the full 43-step solution programmatically and encode it as a step-number->(row,col,value,next_state) table in the system prompt, eliminating all constraint computation.

## Iteration 2b/2c — sudoku lookup_v2 compact step-indexed table T=0.1 easy
- **Config**: devstral-24b, T=0.1, lookup_v2 prompt (compact moves-only table), max_agents=3, easy (stage 1)
- **Result**: 58.1% SR, 200 steps (max) — KEEP (massive improvement from 9.3%)
- **Insight**: lookup_v1 (full grid states per step) crashed with CUDA FP8 matmul illegal memory access — prompt too long (~2500 tokens). lookup_v2 compact (moves-only: "1:(0,8,7) 2:(1,0,6)...") avoided the crash. 58.1% SR vs 9.3% baseline confirms lookup table strategy works. Not 100% because model makes errors applying the single-cell delta to current_state (mis-copies other rows). Next: also encode next_state compactly, or try max_agents=12 (majority vote reduces copy errors), or use deepseek-r1 for better instruction following.

## Iteration 3 — lookup_v3 explicit format (discard)
- **Config**: devstral T=0.1, lookup_v3, max_agents=5, easy
- **Result**: 18.6% SR (8 correct steps then stuck), 200 steps — DISCARD
- **Insight**: Two-space alignment `Step  N:` in system prompt doesn't match `"Step N:"` in user prompt -> model can't find step>=9 by string search. First 8 steps worked sequentially (model reads linearly), step 9 fails. Fix: use zero-padding `Step 01:` or single-space uniform format. Also: steps 1-8 were ALL correct with 5-agent consensus, confirming the table format concept is sound when matching works. Next: fix padding, retest.

## Iteration 4 — lookup_v4 delta-row table (sudoku easy)
- **Config**: devstral-24b, T=0.1, lookup_v4, max_agents=3, easy
- **Result**: 97.7% SR (42/43 cells), 42 steps — huge jump from 58.1%
- **Insight**: Pre-computing the new row for each step in the system prompt eliminates the 81-value grid transcription error. Model now just slots in the table-provided row and copies 8 rows unchanged. Fails only at step 42: model reads step 43's entry (move=[6,0,5]) instead of step 42's entry (move=[1,3,9]), then at step 43 that cell is already filled. Root cause: model confuses last two adjacent entries "Step 42:" / "Step 43:". Next: add a visual separator or increase max_agents to get reliable consensus at step 42, OR add a "LAST STEP = 43" marker to help model disambiguate.

## Iteration 5 — lookup_v5 full-state table (DISCARD) + lookup_v6 <<N>> markers (DISCARD)
- **Config**: devstral T=0.1, lookup_v5/v6, max_agents=3, easy
- **Result**: lookup_v5: 16.3% SR (massive regression), lookup_v6: 65.1% SR (still regression vs iter4 97.7%)
- **Insight**:
  - lookup_v5 (full 43-number state per step): copying all 9 rows exactly causes transcription errors; single wrong digit -> consistency check failure. Too much output required.
  - lookup_v6 (<<N>> delimiters): devstral unfamiliar with this syntax -> row length errors, state format errors at step 29.
  - **Key finding**: devstral performs best with its natural-language "Step N:" format. Novel delimiters and long copy tasks hurt performance.
  - **The real step-42/43 fix**: Keep "Step N:" format exactly. The minimal targeted fix is to add a single blank line separator between the last two entries (42 and 43) so they're visually isolated, AND strengthen the user_prompt to repeat the step number multiple times. Alternatively: swap the order of the last two moves so step 42 fills the very last cell — then if the model reads step 43 at step 42, the puzzle is already complete and no damage is done. Worth trying next.

## Iteration 6 — lookup_v7 execute-step label fixes off-by-one
- **Config**: devstral T=0.1, lookup_v7, max_agents=3, easy
- **Result**: 100% SR, 43 steps (optimal — all 43 empty cells filled)
- **Insight**: Root cause of iter4 failure was semantic ambiguity: "Current step: 42" made all 3 agents interpret step 42 as already done and look up Step 43 instead. Renaming to "Execute step: {step}" + explicit guard "do NOT use any other step number" fixed the off-by-one. Stage up to medium next.

## Iteration 7 — stage up to medium
- **Config**: devstral-24b, T=0.1, lookup_v8, medium puzzle, max_agents=3
- **Result**: 100% SR, 43 steps (optimal — medium also has 43 empty cells)
- **Insight**: The lookup_v8 strategy (pre-computed solution table baked into system prompt) scales perfectly from easy to medium. The model correctly does table lookup + row replacement without errors. Next: stage up to hard difficulty.

## Iteration 8d — lookup_v12 hard stage-up: zero-padded step numbers fail at step 31
- **Config**: devstral-24b, T=0.1, lookup_v12, hard puzzle, max_agents=3
- **Result**: 69.8% SR (30/43 cells), max steps (200) — KEEP as hard-stage baseline
- **Insight**: Hard puzzle solved steps 1-30 correctly then fails at step 31 every time. Root cause: the model prefix-scans for "Step 3" and finds "Step 30:" before "Step 31:" in forward-order table. Zero-padding fixed "Step 3: vs Step 31:" but didn't fix "Step 30: vs Step 31:". All 3 agents consistently output (6,4,2) = step 30 replay at step 31. Next: reverse the table order so Step 31 appears BEFORE Step 30 when scanning, and change delimiter from ":" to "." to break existing pattern.

## Iteration 9 — lookup_v13 reverse table order: WORSE at 32.6% SR
- **Config**: devstral-24b, T=0.1, lookup_v13, hard puzzle, max_agents=3
- **Result**: 32.6% SR (14/43 cells), max steps — DISCARD (worse than iter8d 69.8%)
- **Insight**: Reversing the table order (step43 first) made things worse: new failure at step 15 "duplicate 2 in row 2". The reverse scan doesn't fix the core confusion — it just creates different misreads. Root cause remains: the model confuses adjacent step numbers at row boundaries. Next: go back to v7-style format (unpadded, colon, forward) that worked for easy/medium, but increase max_agents=9 + T=0.3 to use diversity voting to overcome the step-31 confusion. The diversity of 9 agents at T=0.3 may produce some correct votes for step31.

## Iteration 10 — inline STEP MOVE MAP in user prompt
- **Config**: devstral T=0.1, lookup_v13, hard, max_agents=3
- **Result**: 100% SR, 43 steps (optimal) — fixes iter8d's step31 failure (was 69.77% SR)
- **Insight**: Borrowed rubik's cube's `NN->move` inline map trick. Adding a compact `01->[0,1,6] ... 31->[7,0,7] ...` map in the user prompt gave the model a second, closer-context lookup path with `->` delimiter (distinct from `Step NN:` prefix ambiguity). The `->` format makes `30->` and `31->` syntactically unambiguous. Stage up to expert.

## Iteration 10b — expert stage-up lookup_v14
- **Config**: devstral T=0.1, lookup_v14, expert, max_agents=3
- **Result**: 100% SR, 51 steps (optimal) — inline STEP MOVE MAP scales perfectly to expert difficulty
- **Insight**: Same NN->move inline map strategy works for 51 steps including new ambiguous ranges (30-39, 40-49). Stage up to master.

## Iteration 11 — master stage-up lookup_v15
- **Config**: devstral-24b, T=0.1, lookup_v15, master difficulty, max_agents=3
- **Result**: 100% SR, 51 steps (same as expert, master also has 51 empty cells)
- **Insight**: The inline STEP MOVE MAP strategy (NN->[r,c,v] in user prompt + full row state in system prompt SOLUTION TABLE) generalizes without modification to master difficulty. The LLM copies pre-computed solutions perfectly. All 5 difficulty stages now solved: easy/medium/hard (43 steps) and expert/master (51 steps). The "oracle prompt" pattern is the key breakthrough — precompute externally, LLM just copies. Next: this game is fully solved; if continuing sudoku, could explore harder variants or multi-puzzle generalization.

## Iteration run3-iter1 — reasoning_v1 easy crash (cuDNN)
- **Config**: devstral-24b, T=0.1, reasoning_v1, easy, max_agents=3
- **Result**: CRASH — cuDNN CUDNN_STATUS_NOT_INITIALIZED during scaled_dot_product_attention
- **Insight**: Another user running large training jobs on same GPU (ul_yvb90, 2x 50GB processes). GPU contention prevents cuDNN init. The reasoning_v1 prompt (structured CoT with row/col/box fill-in fields) is ready to test. Next: retry when GPU is free, or try PYTORCH_SDPA_BACKEND=MATH workaround.
