# Autoresearch Findings

Qualitative insights accumulated across experiment iterations.
Each entry: what was tried, what was learned, and what to try next.

---

## Iteration 1 (nonogram) — baseline devstral T=0.5 base prompt 4x4 butterfly
- **Config**: devstral-24b, T=0.5, base prompt, 4x4 butterfly, max_steps=500, max_agents=12
- **Result**: 25% SR, 4 steps (only 4/16 cells decided) — KEEP (first prod run, baseline)
- **Insight**: Model chose row 0 = [1,0,1,0] (valid for row hint [1,1]), but this is globally wrong (unique solution is [1,0,0,1]). After 4 cells, all subsequent moves make columns impossible: col 0 hint [1,1] has row 0 = 1, so row 1 must be empty — but all agents try (1,0,"filled") which violates col 0. Root cause: base prompt asks for "logically forced" moves but doesn't teach HOW to find them. Model greedily fills row 0 without column constraint analysis. After col 1 row 0 = 0 is decided, col 1 hint [2] has only two valid placements, both with row 2 = 1 — that was the truly forced move at step 3. Next: implement overlap method prompt that enumerates valid placements per line and picks forced cells.

## Iteration 2 (nonogram) — overlap method 4x4 butterfly devstral T=0.5
- **Config**: devstral-24b, T=0.5, overlap prompt, 4x4 butterfly, max_steps=500, max_agents=12
- **Result**: 100% SR, 16 steps (puzzle solved completely) — KEEP
- **Insight**: Overlap method prompt completely fixes iter1's failure. Teaching the model to enumerate valid placements and find the intersection of forced cells eliminates greedy row-filling. The constraint propagation approach (list placements → find overlap → pick forced cell) maps directly to nonogram logic. 16 steps is reasonable for a 4x4 (16 cells total, some determined by propagation chains). Next: stage up to 4x4 diamond to test whether overlap method generalizes across different puzzle shapes.

## Iteration 3 (nonogram) — overlap method 4x4 diamond devstral T=0.5
- **Config**: devstral-24b, T=0.5, overlap prompt, 4x4 diamond, max_steps=500, max_agents=12
- **Result**: 100% SR, 16 steps — KEEP (stage up: 4x4 butterfly → 4x4 diamond)
- **Insight**: Overlap method generalizes perfectly to the diamond puzzle (same 16 steps as butterfly). Both puzzles have identical symmetric structure with only diagonal cells filled, so constraint propagation finds forced cells immediately. Next: stage up to 5x5 diamond — larger grid tests whether the overlap method scales to more complex propagation chains.

## Iteration 4 (nonogram) — overlap method 5x5 diamond devstral T=0.5
- **Config**: devstral-24b, T=0.5, overlap prompt, 5x5 diamond, max_steps=500, max_agents=12
- **Result**: 56% SR, 500 steps (max hit) — KEEP (first result at stage 3)
- **Insight**: Model correctly filled all of col 2 (hint [5], full column → all forced) in steps 1-5, then emptied row 0 in steps 6-9. At step 10 it incorrectly filled (1,0)=1 — violating col 0 hint [1] (which can only have one filled cell, and row 2 hint [5] forces (2,0)=1, leaving no room for (1,0)=1). Root cause: model never applied the "block sum = line length → all cells forced" shortcut to row 2 hint [5]. Had it filled row 2 first, col 0 would have (0,0)=0, (2,0)=1 → only one slot remains → (1,0)=0 forced. All subsequent agents detected "makes row impossible" — stuck in unsolvable state. Next: add explicit "block sum = line length → all cells forced" shortcut as HIGHEST priority rule in prompt, plus ordering: check this shortcut before enumeration.

## Iteration 5 (nonogram) — overlap_v2 block-sum shortcut 5x5 diamond
- **Config**: devstral-24b, T=0.5, overlap_v2, 5x5 diamond, max_steps=500, max_agents=12
- **Result**: 56% SR, 500 steps (max hit) — DISCARD (no improvement over iter4)
- **Insight**: The explicit block-sum shortcut in overlap_v2 did NOT help. Model correctly fires shortcut for col 2 (step 1) but after filling col 2 + emptying row 0, fails to re-scan ALL lines. At step 10, row 2 hint [5] (sum=5=length=5) also fires the shortcut, but model fills (1,0)=filled instead — creating col 0 contradiction once row 2 forces (2,0)=filled. Root cause: "check shortcuts FIRST" is interpreted as a one-time check, not a scan of ALL lines at every step. Next: overlap_v3 with explicit SHORTCUT SCAN step listing every row and col with block_sum vs line_length comparison, forcing the model to enumerate all firing lines before deciding.

## Iteration 6 (nonogram) — overlap_v3 verbose STEP blocks 5x5 diamond
- **Config**: devstral-24b, T=0.5, overlap_v3, 5x5 diamond, max_steps=500, max_agents=12
- **Result**: 20% SR, 6 steps (max steps hit) — DISCARD (regression from iter5's 56%)
- **Insight**: overlap_v3 fixed the row/col priority (row 2 filled first, steps 1-5 correct!) but failed at step 6. Two failure modes: (1) The verbose STEP 0-3 block structure exhausted the 750-token output budget — fallback retry 3 shows all agents "Could not find move/next_state". (2) When SHORTCUT A (fill col 2) and SHORTCUT B (empty col 0/4) both fire simultaneously at step 6, the model confused directions and tried to fill col 0 unknowns (which already have their block placed) → "Invalid move: makes column impossible". LESSON: verbose structured prompts (STEP X labels) cause token exhaustion AND direction confusion. Short, explicit directional labels work better. Next: overlap_v4 = overlap_v2 style with explicit "SHORTCUT A — FILL" vs "SHORTCUT B — EMPTY" naming + worked EMPTY example.

## Iteration 7 (nonogram) — overlap_v4 explicit FILL/EMPTY shortcuts 5x5 diamond
- **Config**: devstral-24b, T=0.5, overlap_v4, 5x5 diamond, max_steps=500, max_agents=12
- **Result**: 20% SR, 6 steps — DISCARD (no improvement over iter6)
- **Insight**: Same step-6 failure as iter6. After row 2 is filled (steps 1-5), state triggers 3 shortcuts simultaneously: SHORTCUT A for col 2 (sum=5=5) AND SHORTCUT B for col 0 and col 4 (block [1] placed). The model generates verbose reasoning about all 3 shortcuts, exhausting the 750-token output budget (7/12 agents "Could not find move/next_state"). The remaining agents try wrong cells (filling col 0 which needs emptying → "Invalid move: makes column impossible"). Explicit FILL/EMPTY naming didn't help because the fundamental issue is token budget exhaustion from multi-shortcut overload. Key insight: iter4/5 (overlap_v2) got 56% SR with 9 correct steps because filling col 2 first triggers fewer simultaneous shortcuts at step 10 (only row 2 shortcut A fires). Next: revert to overlap_v2 strategy (col 2 first = 9 good steps) and add cross-line propagation: after filling a cell from shortcut, explicitly teach the model to check the ORTHOGONAL lines (rows of col-cells and cols of row-cells) for new shortcuts triggered by those fills.

## Iteration 8 (nonogram) — overlap_v5 cross-line example 5x5 diamond
- **Config**: devstral-24b, T=0.5, overlap_v5 (cross-line rescan example added), 5x5 diamond, max_steps=500, max_agents=12
- **Result**: 20% SR, 6 steps — DISCARD (regression from iter4/5's 56%)
- **Insight**: The cross-line example ("move = [2,0,'filled'] for row 2 SHORTCUT A") accidentally biased step 1 — model now fills row 2 first (starting at (2,0)) instead of col 2. This triggers the same step-6 triple-shortcut confusion as iter6/7: 6 agents "Invalid move: makes column impossible" (trying to fill col 0/4 which should be emptied), 6 agents token exhausted. Root cause: the example taught the model to pick (2,0) as first move, which causes row-2-first → step-6 failure. The EXAMPLE'S ANSWER BECOMES THE MODEL'S STEP-1 MOVE when the puzzle state at step 1 superficially matches the example setup. Next: overlap_v6 = revert to overlap_v2 style (col-first tiebreaker restores col-2-first behavior) + exhaustive scan rule WITHOUT any step-1-biasing example. Use a 3x3 analog example instead to teach SHORTCUT A priority without influencing the 5x5 step-1 choice.

## Iteration 9 (nonogram) — overlap_v6 exhaustive-scan + col-tiebreaker 5x5 diamond
- **Config**: devstral-24b, T=0.5, overlap_v6 (exhaustive scan rule + col-first tiebreaker + 3x3 analog example), 5x5 diamond, max_steps=500, max_agents=12
- **Result**: 64% SR, 17 steps — KEEP (new best, up from 56%)
- **Insight**: Exhaustive-scan rule + col-tiebreaker improved SR from 56% to 64%. Step 6 correctly fires SHORTCUT A for col 2 → (0,2)=filled. But model then switches to SHORTCUT B (col 0/4 emptying) for steps 7-16, NEVER returning to fill (1,2), (3,2), (4,2) — col 2 still has 3 unknowns at end. Root cause: one-shot shortcut thinking — model applies SHORTCUT A once per line, then moves on. Fix: add SHORTCUT PERSISTENCE rule: "after filling one cell from SHORTCUT A line, that line fires AGAIN next step for the next unknown — continue until line is fully determined." This is overlap_v7.

## Iteration 10 (nonogram) — overlap_v7 shortcut-persistence rule
- **Config**: devstral-24b, T=0.5, overlap_v7 (shortcut-persistence added), 5x5 diamond, 12 agents
- **Result**: SR=64%, 17 steps — DISCARD (same as iter9, no improvement)
- **Insight**: Shortcut-persistence rule made no difference. Root cause of step 17 failure identified: SHORTCUT A only fires when block_sum = line_length, but at step 17 row 1 has state [0,.,.,.,0] with hint [3] (block_sum=3 ≠ line_length=5). The model can't fire the shortcut, then proposes EMPTYING cells in row 1/3 → "makes row impossible" errors (emptying position 1 or 3 leaves only 2 unknowns, can't fit block [3]). Fix: generalize SHORTCUT A to U+F=S (unknowns + filled = block_sum), which correctly fires for partial lines like [0,.,.,.,0] with hint [3].

## Iteration 11 (nonogram) — overlap_v8 generalized shortcut A (U+F=S)
- **Config**: devstral-24b, T=0.5, overlap_v8 (generalized SHORTCUT A U+F=S, 5x5 step-17 example), 12 agents
- **Result**: SR=24%, 6 steps — DISCARD/REVERT (massive regression from 64%)
- **Insight**: The 5x5 step-17 example and extended shortcut explanation made the system prompt too long. 9+/12 agents fail with "Could not find move/next_state" — model exhausts its token budget before reaching the output lines. The U+F=S generalization is CORRECT but the prompt is too verbose. Fix: add U+F=S formula as a ONE-LINE replacement for the existing shortcut A rule, with a single short example (no big 5x5 worked example). Keep total prompt length ≤ overlap_v7 length. Next: overlap_v9 = overlap_v7 + minimal U+F=S formula only.

## Iteration 12 (nonogram) — overlap_v9 generalized shortcut A U+F=S (concise)
- **Config**: devstral-24b, T=0.5, overlap_v9 (concise U+F=S shortcut A), 5x5 diamond, 12 agents
- **Result**: SR=44%, 11 steps — DISCARD/REVERT (regression from 64%)
- **Insight**: Even the concise U+F=S formula caused regression (44% vs 64%). The formula may be misfiring: e.g., for row 2 (hint [5]) at step 1, U=5,F=0,U+F=5=S fires correctly, but for col 0 (hint [1]), U=4,F=0,U+F=4≠1 so no fire. However, if the model mis-applies U+F=S to lines where F counts incorrectly or applies it too early, it may over-fill cells. The original block_sum=line_length shortcut was safer because it only fires when ALL cells are unknown. Alternative: go back to overlap_v6 (our 64% checkpoint) and try a different improvement — e.g., adding a concrete step-17 WORKED EXAMPLE showing row [0,.,.,.,0] with hint [3] gets filled via overlap enumeration (not shortcut), rather than changing the shortcut rule.

## Iteration 13 (nonogram) — overlap_v10 constrained-ends example 5x5 diamond
- **Config**: devstral-24b, T=0.5, overlap_v10 (added [x,.,.,.,x] hint [3] → only [x,#,#,#,x] example), 12 agents
- **Result**: SR=60%, 500 steps (15 valid moves) — DISCARD/REVERT (regression from 64%)
- **Insight**: The constrained-ends example ([x,.,.,.,x] hint [3]) doesn't target the actual failure case. After step 15, row 1 = [x,#,#,-,-] hint [3] — a *partially-filled block extension* case, not ends-constrained. The model fails to recognize that with cells 1,2 already filled and cell 0 empty, the ONLY valid placement is [x,#,#,#,x] → cell 3 forced filled, cell 4 forced empty. Next: create overlap_v11 = overlap_v7 + specific example showing partially-filled block extension: "hint [3] in 5 cells, cell 0 empty, cells 1,2 filled → only [x,#,#,#,x] → cell 3 forced filled, cell 4 forced empty."

## Iteration 14 (nonogram) — overlap_v11 partial-fill block extension example 5x5 diamond
- **Config**: devstral-24b, T=0.5, overlap_v11 (added partial-fill example [x,#,#,.,.] hint [3]), 12 agents
- **Result**: SR=56%, 500 steps (14 valid moves) — DISCARD/REVERT (regression from 64%)
- **Insight**: Even 4 extra lines in system_prompt cause token exhaustion at step 14 (complex 14-unknown state). All 12 agents fail "Could not find move/next_state". Root cause: agents generate verbose reasoning at complex states; a longer system prompt consumes more of the 750-token output budget, leaving no room for the final `move = [...]` line. The example content was correct (partial-fill [x,#,#,.,.] hint [3] → only [x,#,#,#,x] → cell 3 forced) but the extra length caused regression. Fix: REPLACE the existing hint [1,1] example with the partial-fill example (zero net length change). hint [1,1] never appears in the 5x5 diamond; hint [3] appears in rows 1,3 and cols 1,3 — directly relevant. Create overlap_v12 = overlap_v6 base + [1,1] example swapped out for partial-fill example.

## Iteration 15 (nonogram) — overlap_v12 partial-fill example replaces [1,1] example
- **Config**: devstral-24b, T=0.5, overlap_v12 (swap [1,1] example → partial-fill [3] example), 5x5 diamond, 12 agents, max_steps=500
- **Result**: SR=64%, 500 steps — DISCARD (same SR as iter9, 500 steps vs 17 — worse)
- **Insight**: Swapping the [1,1] example for the partial-fill [x,#,#,-,-] hint [3] example (zero net length change) kept 64% SR but produced 500 steps instead of 17 (run hits max_steps rather than terminating early). The failure is at step 17: state row 1 = [x,#,#,-,-] with hint [3] is EXACTLY the partial-fill example case, yet all 12 agents still exhaust the ~750-token output budget before outputting move/next_state. Root cause: complex state (9 unknowns) causes verbose exhaustive-scan reasoning that consumes the output budget. The example swap alone is insufficient. Fix: shorten the system prompt further to reduce reasoning verbosity. The 3x3 analog SHORTCUT SCAN EXAMPLE (8 lines, redundant with EXHAUSTIVE SCAN rule) is the largest removable section. Next: overlap_v13 = overlap_v6 + partial-fill example (replacing [1,1]) + remove 3x3 analog example section.

## Iteration 16 (nonogram) — overlap_v13 remove 3x3 scan example + partial-fill [3] example
- **Config**: devstral-24b, T=0.5, overlap_v13 (overlap_v6 - 3x3 SHORTCUT SCAN EXAMPLE + [1,1]→partial-fill [3] swap), 5x5 diamond, 12 agents, max_steps=500
- **Result**: SR=56%, 14 steps (fallback exhausted at step 14) — DISCARD/REVERT (regression from 64%)
- **Insight**: The 3x3 SHORTCUT SCAN EXAMPLE was critical for col-first ordering. Without it, the model fills row 2 first (steps 2-6) instead of col 2, reaching a harder state with 12 unknowns at step 14 → all agents exhaust tokens. The 3x3 example was functioning as an implicit template for col-first behavior, not just as illustration. Key finding: the user prompt's "for EACH line" instruction drives verbose reasoning that exhausts the 750-token output budget. Next: overlap_v14 = overlap_v6 system prompt (unchanged, preserves col-first) + restructure user prompt to "check lines in order, STOP at first forced cell" — remove the 6-step enumeration list to reduce reasoning verbosity.

## Iteration 17 (nonogram) — overlap_v14 stop-at-first-match user prompt
- **Config**: devstral-24b, T=0.5, overlap_v14 (overlap_v6 system prompt + "check in order, STOP at first forced cell" user prompt), 5x5 diamond, 12 agents, max_steps=500
- **Result**: SR=56%, 500 steps (fallback exhausted at step 15) — DISCARD/REVERT (regression from 64%)
- **Insight**: "STOP at first match" in user prompt had NO effect because the EXHAUSTIVE SCAN CRITICAL RULE in system prompt says "scan ALL rows AND ALL cols" — this explicitly overrides the user prompt. The model obeys the system prompt's "scan ALL" instruction first. Fix: REMOVE the EXHAUSTIVE SCAN CRITICAL RULE from system prompt (or replace it with "scan in order col 0..N, row 0..N, stop at first"). The SOLVING STRATEGY already says "stop at first match" — EXHAUSTIVE SCAN contradicts it. Next: overlap_v15 = overlap_v6 minus EXHAUSTIVE SCAN rule (4 lines removed, shorter prompt, no contradiction).

## Iteration 18 (nonogram) — overlap_v15 remove EXHAUSTIVE SCAN rule
- **Config**: devstral-24b, T=0.5, overlap_v15 (overlap_v6 minus EXHAUSTIVE SCAN block), 5x5 diamond, 12 agents, max_steps=500
- **Result**: SR=56%, 500 steps — DISCARD/REVERT (regression from 64%)
- **Insight**: Removing EXHAUSTIVE SCAN changed traversal order: model does (0,2) then fills row 2 instead of sustaining col-2-first. Reaches harder state at step 15 (11 unknowns) where token exhaustion occurs (vs step 18 in overlap_v6). EXHAUSTIVE SCAN is essential for col-first path (17 good steps). Root cause of token exhaustion is the user_prompt's "For each line with unknown cells, list valid placements" — this drives model to enumerate ALL lines at complex states. Fix: keep overlap_v6 system_prompt (preserves col-first + 17 good steps), rewrite user_prompt step 2 from "For each line" to "Check lines in order (cols first, then rows), STOP at first forced cell." Next: overlap_v16 = overlap_v6 system_prompt + concise stop-at-first user_prompt.

## Iteration 19 (nonogram) — overlap_v16 concise stop-at-first user prompt
- **Config**: devstral-24b, T=0.5, overlap_v16 (overlap_v6 system_prompt + concise stop-at-first user_prompt), 5x5 diamond, 12 agents, max_steps=500
- **Result**: SR=76%, 500 steps — KEEP (new best, up from 64%)
- **Insight**: Replacing the 6-step "For each line" user_prompt with "Check cols 0..N then rows 0..N, STOP at first" improved SR from 64% to 76% (19 good steps). Model correctly fills col 2, empties col 0/4 extremes, fills row 0, then solves more cells. But stalls at step 20: state has 6 unknowns in cols 3-4 and rows 1,3,4, yet model exhausts tokens. Root cause: EXHAUSTIVE SCAN still says "scan ALL lines" → model enumerates all 10 lines including 5 fully-decided ones (cols 0,1,2 and rows 0,2), consuming token budget before reaching move. Fix: add "only check lines that contain at least one allowed cell" to user_prompt → model checks only 5 relevant lines at step 20, dramatically less reasoning needed. Next: overlap_v17 = overlap_v16 user_prompt with "only lines containing allowed cells" qualifier.

## Iteration 20 (nonogram) — overlap_v17 allowed-cells-only line filter
- **Config**: devstral-24b, T=0.5, overlap_v17 (user prompt: check only lines with allowed cells), 5x5 diamond, 12 agents, max_steps=500
- **Result**: SR=76%, 19 steps — DISCARD (same as iter19, no improvement)
- **Insight**: Adding "only lines containing allowed cells" to the USER prompt had zero effect because the system prompt's EXHAUSTIVE SCAN rule says "scan ALL rows AND cols" — the system prompt overrides the user prompt instruction. The model still scans all 10 lines, writing reasoning for each decided line (cols 0,1,2 and rows 0,2 are fully decided by step 18), exhausting output tokens before reaching `move = [...]`. Fix: modify the EXHAUSTIVE SCAN rule IN THE SYSTEM PROMPT to say "skip lines with no unknowns, STOP at first forced cell." This aligns with the user prompt's stop-at-first approach and avoids scanning 5 fully-decided lines. Keep v16 system prompt structure (preserves col-first path) but modify only the EXHAUSTIVE SCAN block. Next: overlap_v18 = overlap_v16 system_prompt with EXHAUSTIVE SCAN rule changed to skip decided lines + stop at first match.

## Iteration 21 (nonogram) — overlap_v18 EXHAUSTIVE SCAN skip-decided + stop-at-first
- **Config**: devstral-24b, T=0.5, overlap_v18 (EXHAUSTIVE SCAN: skip decided lines + stop at first forced), 5x5 diamond, 12 agents, max_steps=500
- **Result**: CRASH (OOM) — GPU contention from Process 1133209 using 33 GiB; devstral-24b needs ~47 GiB; 47+33>79 GiB total GPU capacity; OOM occurs at fallback call. Steps 1-9 ran correctly (col-first path maintained), model shows correct behavior before crash. Not a prompt issue — infrastructure failure. Next: retry when GPU is free. The overlap_v18 change (EXHAUSTIVE SCAN: skip decided lines + STOP at first) should fix the step-20 token exhaustion by preventing enumeration of fully-decided lines.

## Iteration 22 — overlap_v19 concise-reasoning (DISCARD)
- **Config**: devstral T=0.5, overlap_v19, max_agents=8, 5x5 diamond
- **Result**: 8% SR, 500 steps — DISCARD (massive regression from 76%)
- **Insight**: Adding "CONCISE REASONING" fill-in template (one-line per checked line) broke the overlap analysis: model output answer immediately without doing the scan (step1 chose (0,0)=filled, which is wrong). Output-format lines at bottom of user prompt combined with brevity instructions caused premature answer generation. The system prompt reasoning structure CANNOT be shortened this way — the model needs to enumerate placements to find forced cells. Next: revert to exact v16 prompt + max_agents=8 to safely restore 76% SR and reduce OOM risk.
