# Autoresearch Findings

Qualitative insights accumulated across experiment iterations.
Each entry: what was tried, what was learned, and what to try next.

---

## Iteration 1 — baseline 3 disks
- **Config**: devstral T=0.1, base prompt, 3 disks
- **Result**: 100% SR, 7 steps (optimal)
- **Insight**: Baseline solves 3 disks optimally out of the box. No prompt tuning needed at this stage.

## Iteration 2 — stage up to 4 disks
- **Config**: devstral T=0.1, base prompt, 4 disks
- **Result**: 100% SR, 15 steps (optimal)
- **Insight**: Model handles 4 disks optimally too. Next: try 5 disks or explore if other models/prompts can match this.

## Iteration 3 (prod iter1) — stage up to 5 disks
- **Config**: devstral T=0.1, base prompt, 5 disks
- **Result**: 100% SR, 31 steps (optimal, 2^5-1=31)
- **Insight**: The base prompt's alternating-disk-1 rule scales optimally to 5 disks. Model still achieves perfect steps. Next: push to 6 disks (63 optimal moves) or try alternative models to benchmark against devstral.

## Iteration 1 (sliding_puzzle) — baseline 2x2 devstral T=0.1
- **Config**: devstral-24b, T=0.1, base prompt, 2x2 initial_state=[2,1,3,0]
- **Result**: 100% SR, 8 steps (optimal for 2x2 is ~3; base prompt is greedy so 8 is acceptable)
- **Insight**: Base prompt solves 2x2 out of the box with devstral. SR=100%. Next: stage up to 3x3 (easiest) to test the greedy strategy at higher complexity.

## Iteration 2 (sliding_puzzle) — stage up to 3x3 easiest devstral T=0.1
- **Config**: devstral-24b, T=0.1, base prompt, 3x3 initial_state=[1,2,5,6,3,4,7,8,0]
- **Result**: 0% SR, max steps (200) — DISCARD
- **Insight**: Model produces "Inconsistent prediction" errors — next_state doesn't match current_state+move. 3x3 blank-movement arithmetic overwhelms the base prompt. The single 3x3 example in the system prompt wasn't enough. Next: add explicit coordinate mapping (row, col) to help the model compute next_state correctly, or try cot_detailed prompt which may provide more reasoning scaffolding.

## Iteration 3 (sliding_puzzle) — coordinate prompt 3x3 easiest devstral T=0.1
- **Config**: devstral-24b, T=0.1, coordinate prompt (new), 3x3 initial_state=[1,2,5,6,3,4,7,8,0]
- **Result**: 0% SR, max steps (200) — DISCARD
- **Insight**: Coordinate prompt fixed "Inconsistent prediction" errors (explicit index-swap arithmetic worked). New failure mode: **cycles** — model gets stuck looping valid states (cycle detected at step 24+). Greedy Manhattan strategy alone is insufficient for 3x3. Next: add explicit anti-cycle instructions (penalize revisited states, force different direction when cycling), or try deepseek-r1-32b which may do better longer-horizon planning, or try higher `max_agents_per_step` for vote diversity to escape cycles.

## Iteration 4 (prod iter2) — stage up to 6 disks
- **Config**: devstral T=0.1, base prompt, 6 disks
- **Result**: 100% SR, 63 steps (optimal, 2^6-1=63)
- **Insight**: Base prompt continues to scale optimally to 6 disks. The model has a robust internal representation of the recursive Tower of Hanoi strategy. Next: push to 7 disks (127 optimal moves) or try a different model (qwen3-32b / deepseek-r1-32b) at 6 disks to benchmark relative capability.

## Iteration 4 (sliding_puzzle) — explicit answer-first prompt devstral T=0.5 3x3 easiest
- **Config**: devstral-24b, T=0.5, explicit prompt (new answer-first variant), 3x3 initial_state=[1,2,5,6,3,4,7,8,0], 3 agents
- **Result**: 22.2% SR, 200 steps (max steps hit, partial progress) — KEEP (first >0% on 3x3)
- **Insight**: Answer-first format + explicit worked example + correct adjacency arithmetic got the model computing valid next_state. T=0.5 diversity helped escape some cycles (cycle_detected=False). But 22.2% means only 2/9 tiles correct at end — model still gets stuck. Next: increase T further (0.7) for more diversity to escape greedy traps, or add explicit anti-cycle instruction "if you've been at this state before, choose a different move direction than previously used".

## Iteration 5 (sliding_puzzle) — anti-backtrack rule + 2nd example + blank_index hint
- **Config**: devstral-24b, T=0.5, explicit prompt (anti-backtrack, 2nd example, blank_index), 3x3 easiest
- **Result**: 11.1% SR, 1 valid step then all Inconsistent prediction — DISCARD
- **Insight**: Adding `blank_index:` to the output format caused severe regression. The model correctly identifies the target index (e.g., UP from blank_idx=7 reaches idx=4=tile3) but **labels the direction wrong** (says LEFT when it means UP). The anti-backtrack rule was understood but ignored. The reasoning also enters infinite "Wait..." loops that fill the token budget. Root cause: the model's direction-name↔index arithmetic is unreliable. Next: try qwen3-32b (stronger spatial reasoning) or deepseek-r1-32b (CoT might fix direction confusion), or redesign prompt to ask for INDEX of tile to swap rather than direction name.

## Iteration 6 (sliding_puzzle) — model switch + prompt redesign experiments
- **Config**: (a) qwen3-32b T=0.5 explicit; (b) devstral T=0.5 explicit_v2 offset-chain; (c) devstral T=0.7 explicit
- **Result**: (a) 0% SR — qwen3 thinking-mode exhausts 750-token budget before reaching move= line; (b) 0% SR — offset-chain fields confuse model, cycles from step 1; (c) 22.2% SR — same as iter4, no gain from higher temperature
- **Insight**: Root cause is cycling — model oscillates tile back and forth while Gemini fallback is quota-exhausted (all fallback retries fail silently). Cycle-avoidance MUST be baked into the prompt rules rather than relying on fallback. Next: add explicit anti-backtrack rule to explicit.yaml system prompt — "Do not reverse your previous move" — without changing output format (the output-format changes in iter5 caused regression).

## Iteration 7 (sliding_puzzle) — explicit_v3 anti-reversal rule
- **Config**: devstral-24b, T=0.5, explicit_v3 (anti-reversal rule added to system prompt), 3x3 easiest
- **Result**: 0% SR, 200 steps — DISCARD
- **Insight**: Gemini fallback is quota-exhausted (free tier: 20 req/day). Without fallback, ALL "Inconsistent prediction" steps fail — the 22.2% in iter4 was entirely dependent on Gemini correcting next_state errors. Root cause: model computes `next_state` greedily (places tile at goal) instead of mechanically (swap blank↔adjacent). Anti-reversal rule had no effect because cycling isn't the bottleneck — wrong next_state is. Next: redesign prompt to force explicit swap arithmetic: "blank at B, neighbor at N=B±{n}, swap B and N in state". Do NOT add new output fields (iter5 lesson) — add the swap derivation as a reasoning step in the system prompt example only.

## Iteration 8 (sliding_puzzle) — explicit_v4 swap arithmetic in system prompt examples
- **Config**: devstral-24b, T=0.5, explicit_v4 (swap arithmetic B/N in examples), 3x3 easiest
- **Result**: 0% SR, total_steps=1 — DISCARD
- **Insight**: Failures.csv reveals a precise bug: model correctly says "blank at B=8, LEFT neighbor at N=7 (tile 8)" but writes next_state that swaps blank with the TARGET tile (index 4), not the LEFT neighbor (index 7). The reasoning and next_state computation are **disconnected** — the model treats next_state as a goal-seeking operation regardless of what the move direction implies. Adding swap arithmetic to examples (as reasoning steps) does not fix this because the model does not generalize. Next: add an explicit intermediate output field `swap = [B, N]` BEFORE next_state — force the model to commit to swap indices first, then derive next_state from them. Different from iter5's `blank_index` failure (which caused direction confusion); this bridges reasoning to next_state.

## Iteration 9 (sliding_puzzle) — explicit_v5 swap=[B,N] bridge field
- **Config**: devstral-24b, T=0.5, explicit_v5 (swap=[B,N] before next_state), 3x3 easiest
- **Result**: 0% SR, total_steps=1 valid — DISCARD
- **Insight**: The `swap` field is being populated correctly (model says `swap = [8, 7]`), but `next_state` is STILL goal-seeking (swaps positions 6 and 8, not 7 and 8). The reasoning and next_state remain disconnected even with the explicit swap commitment. Also: most agents say `move = RIGHT` when blank is at corner index 8 (RIGHT is invalid) — the model doesn't track boundary conditions. Gemini quota remains exhausted, exposing all failures. Root cause may be deeper: the model conflates "where blank should go eventually" with "where blank goes now". Next: try DeepSeek-R1-32B which has explicit CoT reasoning chains for arithmetic — it may better propagate the swap indices into next_state. Keep explicit_v5 prompt or simplify back to explicit.

## Iteration 5 (tower iter3) — stage up to 7 disks
- **Config**: devstral-24b, T=0.1, base prompt, 7 disks
- **Result**: 100% SR, 127 steps (optimal, 2^7-1=127)
- **Insight**: Base prompt scales optimally to 7 disks. Wall-clock time ~110 min (~35 sec/inference × 127×3 calls). The alternating-disk-1 rule provably generates 2^n-1 optimal moves; model faithfully follows it without drift across all 127 sequential decisions. Next: push to 8 disks (255 optimal moves, ~220 min projected) OR benchmark alternative models (qwen3-32b, deepseek-r1-32b) at 7 disks to compare capability and speed.

## Iteration 10 (sliding_puzzle) — DeepSeek-R1-32B token budget exhausted
- **Config**: deepseek-r1-32b, T=0.5, explicit prompt, 3x3 easiest
- **Result**: 0% SR, 200 steps (max) — DISCARD
- **Insight**: R1 generates verbose inline reasoning ("Okay, so I'm trying to solve...") filling 750 token budget before reaching `move=` format — same failure as qwen3 iter6. All agents fail "Could not find move or next_state in the response." R1 is incompatible with 750-token budget + answer-first format. Devstral remains the only usable model.

## Iteration 10b (sliding_puzzle) — explicit_v5 row/col boundary enumeration
- **Config**: devstral-24b, T=0.5, explicit_v5 (new: blank_row/col + Valid_moves enumeration), 3x3 easiest
- **Result**: 0% SR, 4 valid steps — KEEP (best without Gemini fallback)
- **Insight**: Row/col boundary enumeration FIXED the dominant "Invalid move: No tile in that direction" failure mode — 0 invalid boundary moves vs 7/9 agents failing before. 4 valid consensus steps taken. But model cycles on step 4 (tile 6 right then immediately left — reversal). Next: add explicit anti-reversal rule to explicit_v5 now that valid steps are being taken (iter7's anti-reversal failed because Gemini was exhausted and next_state errors dominated; now valid moves are being found, anti-reversal can take effect).

## Iteration 11 (sliding_puzzle) — explicit_v6 anti-reversal rule
- **Config**: devstral-24b, T=0.5, explicit_v6 (anti-reversal removes opposite of Previous_move from Valid_moves), 3x3 easiest
- **Result**: 11.1% SR, 3 valid steps — KEEP (SR improved from 0% in iter10b)
- **Insight**: Anti-reversal IS applied correctly (model removes UP when Previous=DOWN etc.), and SR improved to 11.1% (1 tile at goal). But "Inconsistent prediction" now dominates: model selects valid move direction correctly but writes next_state as goal-seeking prediction (not mechanical swap). Example: says `move = LEFT` (blank_idx=4) but writes next_state that swaps indices 4↔7 (goal-seeking) not 4↔3 (LEFT neighbor). Next: add explicit `N:` (neighbor index), `tile_at_N:` (state[N] value), and reframe next_state as "copy current_state, set index blank_idx = tile_at_N, set index N = 0" — three explicit derivation steps before the array. Also keep anti-reversal.

## Iteration 12 (sliding_puzzle) — explicit_v7 N+tile_at_N bridge fields
- **Config**: devstral-24b, T=0.5, explicit_v7 (N: neighbor index, tile_at_N: state[N] lookup, next_state as copy+swap), 3x3 easiest
- **Result**: 22.2% SR, 153 steps — KEEP (best SR so far, fewer steps than iter4's 200)
- **Insight**: Adding N and tile_at_N intermediate fields helped: SR jumped from 11.1% (iter11) back to 22.2% (matching iter4 best) but with 153 steps instead of 200 — cycle detection halted earlier. However, 340 "Could not find move/next_state" errors still occur (format parsing failure — the longer output format exceeds some agents' effective token budget or confuses response parsing). 529 successful predictions shows the format works when agents comply. Inconsistent prediction still present (next_state goal-seeking) in some cases. Next: the failing agents may be truncating output before next_state — try reducing format verbosity or only add N/tile_at_N in system prompt example (not user_prompt output fields), so agents only output move + next_state. Keep N/tile_at_N in reasoning but not as required output fields.

## Iteration 13 (sliding_puzzle) — explicit_v8 short user_prompt output
- **Config**: devstral-24b, T=0.5, explicit_v8 (system_prompt same as v7; user_prompt reduced to Target + move + next_state only), 3x3 easiest
- **Result**: 0% SR, 200 steps — DISCARD (regression from v7's 22.2%)
- **Insight**: Removing intermediate output fields (blank_idx, blank_row, blank_col, Valid_moves, Anti-reversal, N, tile_at_N) from the user_prompt causes immediate regression to goal-seeking next_state. The "Could not find" errors in v7 (340 total) were NOT caused by output truncation — they were Gemini fallback quota-exhaustion failures. The intermediate fields ARE necessary to force mechanical swap computation. Next: keep v7 prompt verbosity unchanged but try increasing `max_agents_per_step` from 3 to 9 for greater consensus diversity and better cycle escape; more agents = more votes = less likely that goal-seeking minority wins. Alternatively, try adding an explicit final verification step: "Verify: does next_state differ from current_state ONLY at positions blank_idx and N?"

## Iteration 14 (sliding_puzzle) — max_agents_per_step 3→9 voting diversity
- **Config**: devstral-24b, T=0.5, explicit_v7, 3x3 easiest, max_agents_per_step=9
- **Result**: 100% SR, 76 steps — KEEP (massive breakthrough: 22.2%→100%)
- **Insight**: Increasing agents from 3→9 was decisive. The "wisdom of crowds" effect overrides goal-seeking minority: with 9 votes, the correct mechanical swap answer wins consensus consistently. 76 steps (vs optimal ~20) shows cycles still occur but resolve quickly. Next: stage up to 3x3 hardest initial_state=[8,6,7,2,5,4,3,1,0] to test whether 9-agent consensus can handle a harder configuration, or try reducing steps by decreasing T (more greedy → fewer exploration cycles).

## Iteration 4 (tower iter4) — stage up to 8 disks [TIMEOUT]
- **Config**: devstral-24b, T=0.1, base prompt, 8 disks (optimal=255 moves)
- **Result**: Run still in progress (PID 334021, started ~15:19 Mar 19). Expected ~220 min but taking longer (~10+ hrs). No output file yet.
- **Insight**: Run started but another parallel agent reverted the exp commit (config back to 7). Background process (PID 334021) still running with 8 disks since config was loaded at startup. Output will appear as `tower_of_hanoi_8d_3a_*.json` when complete. If run completes with 100% SR 255 steps, stage up to 9 disks (511 optimal). If it stalls, the model may be drifting at 8 disks — try T=0.0 or minimal prompt

## Iteration 15 (sliding_puzzle) — stage up to 3x3 hardest
- **Config**: devstral-24b, T=0.5, explicit_v7, 3x3 hardest initial_state=[8,6,7,2,5,4,3,1,0], max_agents=9
- **Result**: 22.2% SR, 200 steps (max steps hit, partial progress) — KEEP (first result at stage 3)
- **Insight**: Same SR as best iter12 result on 3x3 *easiest*, despite 9 agents — the harder configuration requires longer detour paths that the greedy Manhattan heuristic cannot plan. "Inconsistent prediction" errors persist throughout (next_state goal-seeking). The 9-agent wisdom-of-crowds effect that solved easiest does not transfer to hardest. Root cause: 3x3 hardest requires temporarily moving tiles AWAY from goal to create detour paths; greedy rule 6 ("pick direction that moves Target closer to its goal") directly prevents these necessary detours. Next: try adding a lookahead hint in the prompt — "sometimes you must temporarily move Target away from goal to clear a path; if the best greedy move would displace an already-placed tile (goal index < Target's goal), consider an alternative move instead" — or try increasing max_steps beyond 200 to see if the model eventually solves it given more attempts.

## Iteration 16 (sliding_puzzle) — explicit_v9 two-tier heuristic + max_steps=400
- **Config**: devstral-24b, T=0.5, explicit_v9 (Tier-1/Tier-2 placed-tile safety + 2nd detour example), 3x3 hardest, max_agents=9, max_steps=400
- **Result**: 0% SR, 400 steps — DISCARD (regression from iter15's 22.2%)
- **Insight**: The extra `Tier-1:` output field + second worked example in system_prompt pushed agents past the 750-token output budget — "Could not find move/next_state" errors dominate. **Hard constraint**: any change that adds output fields or lengthens the system_prompt causes total format failure. Next: keep explicit_v7 output format UNCHANGED, only modify rule 6 text to "prefer moves that don't displace placed tiles; among those, pick move closest to Target's goal" — no new output fields. This changes decision logic without touching format.

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
