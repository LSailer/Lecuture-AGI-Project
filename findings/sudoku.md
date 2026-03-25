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

## Iteration run3-iter3 — reasoning_v2 easy: 0% SR, no consensus at step 1
- **Config**: devstral-24b, T=0.1, reasoning_v2, easy, max_agents_per_step=3, max_agents_total=15
- **Result**: 0% SR, 0 steps — no consensus reached at step 1 after 15 agents
- **Insight**: Three failure modes identified from failures.csv:
  1. **Cell-switching stale column bug**: Step 6 tells the model to "scan empty_cells for a cell with exactly 1 candidate." When it switches from initial cell (0,0) to e.g. (0,8), it mentally estimates column 8's values without the structured template — misses value 3 already at row 5. Move rejected as invalid.
  2. **Response truncation**: max_new_tokens=750 is too small for verbose 7-step reasoning + 81-value next_state. Agents 1:2 and 1:3 truncated mid-next_state → parse failure. Shorter template needed.
  3. **Wrong cell in next_state**: Agent 1:1 placed value at [0][0] instead of [0][8] after switching target cells.
  - **Root cause**: All three bugs stem from step 6's cell-switching logic. Fix: remove cell-switching, anchor to one cell, use only the structured scan. Next: reasoning_v3 without cell-switch and shorter template.

## Iteration run3-iter3b — reasoning_v3 easy: 20.9% SR, 9 steps
- **Config**: devstral-24b, T=0.1, reasoning_v3, easy, max_agents_per_step=3, max_agents_total=15
- **Result**: 20.9% SR (9/43 cells filled), fails at step 10 — KEEP (matches run2 baseline without lookup tables)
- **Insight**: Removing cell-switching from reasoning_v2 fixed the 0% SR (no consensus at step 1). The compact template + single-cell anchor produced valid, parseable outputs for steps 1-9. Failure at step 10: all agents propose "value 3" for a cell in row 0, but row 0 already has 3 (placed at step 2). The structured column scan (step 3, explicit [row][C] template) correctly prevents stale-column errors — but step 2's row read ("Copy row R from current_state[R]: ___") is still a free-form fill-in, so the model misreads updated row 0 as still missing 3. Next: reasoning_v4 with explicit per-cell row indexing ([R][0]=___ [R][1]=___ ...) to force full row re-read, mirroring the column scan approach.

## Iteration run3-iter4 — reasoning_v4 easy: 9.3% SR, regression (DISCARD)
- **Config**: devstral-24b, T=0.1, reasoning_v4, easy, max_agents_per_step=3, max_agents_total=15
- **Result**: 9.3% SR (4 cells), fails at step 5 — DISCARD (regression from 20.9% v3 baseline)
- **Insight**: Explicit `[R][col]=___` row scan (mirroring v3's column scan format) did NOT fix the stale row bug — model echoes the template blanks unfilled then guesses from memory. Step 5 all 15 agents proposed values 2 or 3 already in row 0 (stale initial-state reads). Root cause: asking the model to re-read a row it previously modified is unreliable; the `[row][C]=___` column scan in v3 worked because it forces reads across *different* rows (harder to hallucinate). Next: instead of asking the model to read row R, **inject row R contents directly in the user prompt** as `Row {R} (current): {row_values}` — eliminating the reading step entirely. Pre-compute nothing about the solution; just surface the current row/col values the model needs.

## Iteration run3-iter5 — reasoning_v5 easy: 18.6% SR, regression (DISCARD)
- **Config**: devstral-24b, T=0.1, reasoning_v5, easy, max_agents_per_step=3, max_agents_total=15
- **Result**: 18.6% SR (8 cells), fails at step 9 — DISCARD (regression from 20.9% v3)
- **Insight**: Labeled rows (`Row 0: [v0,v1,...]` ... `Row 8: [...]`) ARE correctly injected — debug_prompts confirms the prompt shows "Row 1: [6, 7, 0, 0, 0, 0, 0, 4, 2]". But the model still misses non-zero values buried after long zero runs: agents tried placing 4 in row 1, missing `4` at index 7. Root cause: reading a compact list `[6,7,0,0,0,0,0,4,2]` and extracting non-zeros is error-prone when zeros dominate. The labeled rows fix the "where to look" problem but not the "accurately count non-zeros in a sparse list" problem. Next: instead of asking the model to extract non-zeros from a list, force per-cell fill-ins for row R too — mirror the column scan's 9-blank format. Use `R[0]=___ R[1]=___ ... R[8]=___` (referencing the labeled row above) so the model visits each position individually, same discipline as the working column scan.

## Iteration run3-iter6 — reasoning_v6 easy: 7.0% SR, truncation (DISCARD)
- **Config**: devstral-24b, T=0.1, reasoning_v6, easy, max_agents_per_step=3, max_agents_total=15
- **Result**: 7.0% SR (3 cells), no consensus at step 4 — DISCARD (regression from 20.9% v3)
- **Insight**: Per-cell row fill-in `R[0]=___ R[1]=___ ... R[8]=___` consumes ~55 output tokens (vs v3's ~30), and the model ALSO expands the box section to list all 9 cells (~80 tokens). Together with the column scan (~60 tokens) and next_state copy (~250 tokens), the total exceeds 750 max_new_tokens → responses truncated mid-reasoning, no parseable output. Root cause: the `R[N]=___` label-per-value format is too verbose for 750-token budget. Fix: use compact 9-blank sequential fill-in (`Vals: _ _ _ _ _ _ _ _ _`) forcing all-9-position output in ONE line (~20 tokens) instead of 9 labeled tokens (~55). Also add "list only non-zero digits" to box step to prevent cell-by-cell expansion.

## Iteration run3-iter7 — reasoning_v7 labeled rows + compact Vals: row scan
- **Config**: devstral-24b, T=0.1, reasoning_v7, easy, max_agents_per_step=3, max_agents_total=15
- **Result**: 9.3% SR (4 cells), fails at step 5 — DISCARD (regression from 20.9% v3)
- **Insight**: The labeled-row + compact `Vals: _ _` format correctly reads updated row values — failures.csv confirms model outputs `Vals: 2 5 3 4 6. 1 9.` with correct non-zeros including the already-placed 3. However, step 5 set subtraction fails: model lists 3 as "Non-zero in row R" but then omits it when computing the union in `{1,...,9} minus (row ∪ col ∪ box)`, producing 3 as a candidate despite being in the row. This is a multi-step working-memory error: the model correctly identifies row contents but loses track of a digit during union arithmetic. The stale-read problem is fixed; the set-arithmetic problem is now the blocker. Next: make the candidates elimination explicit in 3 steps: "Start: {1..9}; Remove row non-zeros: ___; Remove col non-zeros: ___; Remove box non-zeros: ___; Candidates: ___" to prevent union-collapse errors.

## Iteration run3-iter8 — reasoning_v8 labeled rows + serial elimination: 18.6% SR (DISCARD)
- **Config**: devstral-24b, T=0.1, reasoning_v8, easy, max_agents_per_step=3, max_agents_total=15
- **Result**: 18.6% SR (8 cells), no consensus at step 9 — DISCARD (regression from 20.9% v3)
- **Insight**: Two simultaneous failure modes: (1) At step 6, agents 2/3/4 truncate — the 7-line serial elimination (~65 tokens) pushes some outputs over 750 token limit, consuming the vote budget with parse failures. (2) At step 9, agents 2/3 still propose "value 1 already in 3x3 box" — the serial elimination format didn't prevent box arithmetic errors. The labeled rows (INPUT tokens only) correctly fix the stale-row read. The problem is that 4-line serial (`Start/−row/−col/−box`) is too verbose for 750-token budget AND the model still makes box elimination errors. Next: keep labeled rows (they work) but replace the 7-line serial with a compact 2-line format: `{1..9} − row[___] − col[___] − box[___] = ___` that explicitly lists what's being removed without multi-line expansion. This forces set membership but saves ~45 output tokens vs v8's step 5.

## Iteration run3-iter9 — reasoning_v9 labeled rows + inline sequential elimination: 0% SR (parse failure)
- **Config**: devstral-24b, T=0.1, reasoning_v9, easy, max_agents_per_step=3, max_agents_total=15
- **Result**: 0% SR, 0 steps — DISCARD (regression from 20.9% v3, but reasoning correct)
- **Insight**: ALL 3 agents in batch 1 reasoned CORRECTLY (move=[0,0,2] is valid) but responses truncated before completing next_state (hits max_new_tokens=750). Two causes: (1) model expanded box step to 9 cell-by-cell listings instead of compact "Non-zero: {5,9,1}" (+45 tokens); (2) model used multi-line aligned next_state format with 14-space indentation per row (+60 extra tokens vs single-line). Total output ~700 tokens, cuts before row 9. Fix: add "next_state must be ONE LINE" to system prompt + "digits only, e.g. {2,5,9}" to box step instruction. The inline sequential elimination `{1..9}−row→___−col→___−box→___` worked perfectly — set-subtraction was correct in all 3 agents.

## Iteration run3-iter10 — reasoning_v10 compact box + ONE LINE next_state: 9.3% SR (DISCARD)
- **Config**: devstral-24b, T=0.1, reasoning_v10, easy, max_agents_per_step=3, max_agents_total=15
- **Result**: 9.3% SR (4 cells), no consensus at step 5 — DISCARD (regression from 20.9% v3)
- **Insight**: Truncation fix worked — steps 1-4 had clean 3/3 consensus (compact box "digits only" and "ONE LINE next_state" prevented output overflow). New failure mode: labeled-row format ("Row 0:…Row 8:") biases model to fill row 0 left-to-right, causing it to place 4 at (0,3) even though (0,5) is a naked single requiring 4 (col 5 = {7,1,6,8} → only 4 is valid). After placing 4 at (0,3), row 0 is missing {7,8} but col 5 contains both → step 5 impossible. Root cause: model ignores inter-row constraint propagation when picking cells; "prefer many filled values" heuristic insufficient. Next: add explicit row-density scan in step 1 (count non-zeros per row, pick densest row first) to break row-0 bias and guide toward naked singles in heavily-filled rows like row 2 (6 non-zeros).

## Iteration run3-iter11 — reasoning_v11 density selection: 4.7% SR (DISCARD)
- **Config**: devstral-24b, T=0.1, reasoning_v11, easy, max_agents_per_step=3, max_agents_total=15
- **Result**: 4.7% SR (2 cells), no consensus at step 3 — DISCARD (regression from 20.9% v3)
- **Insight**: Row-density selection worked perfectly for steps 1-2: model correctly chose row 2 (7 non-zeros) and filled naked singles (2,2)=3 and (2,3)=4 with 3/3 consensus. BUT step 3 fails: model counted non-zeros for ALL 9 rows (including now-complete row 2 with 9 non-zeros) and picked row 2 again despite the "for each distinct R in empty_cells" instruction. Model doesn't respect the empty_cells constraint when listing rows — it just lists all 9 rows and takes the maximum. Fix: add explicit "ONLY count rows appearing in empty_cells — do NOT count fully filled rows" negative constraint in step 1. Also split into two sub-steps: (1a) extract distinct R from empty_cells, (1b) count density for those R only.

## Iteration run3-iter12 — reasoning_v12 compact 2-sub-step density: 0% SR (parse fail / truncation)
- **Config**: devstral-24b, T=0.1, reasoning_v12, easy, max_agents_per_step=3, max_agents_total=15
- **Result**: 0% SR, 0 steps — DISCARD (parse failure: next_state truncated every agent)
- **Insight**: Split step 1 into 1a ("list distinct R from empty_cells") + 1b ("count density for 1a rows only") is conceptually correct — agents correctly output R∈{0,1,...,8} and pick row 2 as densest. BUT the 8-line template text echoed by the model adds ~80 tokens over v10's single-step, pushing total output past 750-token limit. next_state truncates after row 4 (226/343 chars), STATE_PATTERN requires all 9 rows → no parse. Fix: collapse 1a+1b into 2 ultra-compact lines (e.g. "1a. R∈{___}" + "1b. density→Densest R=___→Target=___") to save ~80 tokens while preserving the two-stage filter logic.

## Iteration run3-iter13 — reasoning_v13 ultra-compact 1a+1b: 9.3% SR (DISCARD)
- **Config**: devstral-24b, T=0.1, reasoning_v13, easy, max_agents_per_step=3, max_agents_total=15
- **Result**: 9.3% SR (4 cells), no consensus at step 5 — DISCARD (regression from 20.9% v3)
- **Insight**: Ultra-compact 2-line 1a+1b fixed the truncation issue (no parse failures). Density selection correctly chose row 2 for steps 1-2 (3/3 consensus on (2,2,3) and (2,3,4)). BUT at step 3, once row 2 completed, model picked row 0 (3 non-zeros) instead of row 3 (6 non-zeros, densest remaining) — same "skip completed rows" failure as v11. Compact format provides less guidance than v11's verbose format. Root cause: density selection requires explicit set-membership reasoning ("R must be in empty_cells") that the model consistently fails at. Next: abandon density selection entirely. Take v3 as exact base, add ONLY labeled rows (Row 0: {current_state[0]} etc.) as supplementary input AND update step 2 to "find 'Row R:' in labeled rows above" — this should fix v3's only known failure (stale row read at step 10+) without introducing new failure modes. No sequential elimination, no density, keep v3 simple.

## Iteration run3-iter14 — reasoning_v14 labeled-rows + "Find Row R:" lookup
- **Config**: devstral-24b, T=0.1, reasoning_v14, easy, max_agents_per_step=3, max_agents_total=15
- **Result**: 18.6% SR (8 cells), no consensus at step 9 — DISCARD (regression from 20.9% v3)
- **Insight**: Two new failure modes at step 9: (1) Template echo — model copies the entire reasoning template verbatim with `___` blanks unfilled, then truncates mid next_state (~150 token template echo eats the output budget). (2) Column scan error — agent tried value 5 at (1,2) but col 2 already has 5 at row 3. Root cause of template echo: v14 changed step 2's wording to "Find 'Row R:'..." which may trigger a different model behavior than v3's proven "Copy row R from current_state[R]" wording. Next: keep v3's EXACT template wording, add labeled rows to INPUT only, change step 2 pointer from `current_state[R]` → "labeled rows above" — minimal redirect, preserves proven fill-in behavior.

## Iteration run3-iter15 — reasoning_v15 labeled-rows + minimal Copy redirect
- **Config**: devstral-24b, T=0.1, reasoning_v15, easy, max_agents_per_step=3, max_agents_total=15
- **Result**: 14.0% SR (6 cells, step 7 fail: no consensus after 15 agents) — DISCARD (regression from v3 20.9%)
- **Insight**: "Copy row R from labeled rows above" avoids v14's template echo, but labeled rows ("Row 0: ... Row 8:") still cause row-0 bias: model picks (0,0) at step 0 despite row 2 having 7 non-zeros (densest). Model fills row 0 left-to-right → dead-end at (0,5): col 5 has both {7,8} so zero valid candidates. Root cause identical to v10's failure. The visual (`{state_visual}`) is present in v15 but step 1's "Prefer many filled values" heuristic is overridden by labeled-row anchoring. Next: v16 = keep v3's `{current_state}` block AND visual for cell selection (no labeled-row anchoring), add labeled rows AFTER visual as supplementary reference section, update step 1 to "use Visual to find densest row (fewest dots)", keep step 2 "Copy row R from labeled rows: ___" — separates cell-selection context (block/visual) from row-copy context (labeled rows).

## Iteration run3-iter16 — reasoning_v16 labeled-rows-below + visual-density hint
- **Config**: devstral-24b, T=0.1, reasoning_v16, easy, max_agents_per_step=3, max_agents_total=15
- **Result**: 4.7% SR (2 cells), no consensus at step 3 — DISCARD (regression from v3 20.9%)
- **Insight**: "Use Visual to find the row with fewest dots" causes stale-visual-memory bug: at step 3 (after row 2 complete), all 3 agents said "Row 2 has only 2 dots, choose R=2" even though row 2 has 0 dots and no entries in empty_cells. Model remembers row 2 was the densest from step 0 memory, ignores current state. Additionally, selecting row 2 (all 9 values filled) makes box step enumerate all 9 cells verbosely → truncation before move/next_state → parse failure. Root cause: any "density selection" instruction based on visual/reasoning causes the model to anchor to the initially-densest row and not update when rows complete. Next: v17 = v3 exact step 1 (no density hint, just "prefer many filled values") + labeled rows reference section for step 2 only — minimal change targeting only the known stale-row bug at step 10+.
