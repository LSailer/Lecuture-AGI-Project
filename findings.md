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
