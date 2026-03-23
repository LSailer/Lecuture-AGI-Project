# Autoresearch Findings — Tower of Hanoi

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

## Iteration 4 (prod iter2) — stage up to 6 disks
- **Config**: devstral T=0.1, base prompt, 6 disks
- **Result**: 100% SR, 63 steps (optimal, 2^6-1=63)
- **Insight**: Base prompt continues to scale optimally to 6 disks. The model has a robust internal representation of the recursive Tower of Hanoi strategy. Next: push to 7 disks (127 optimal moves) or try a different model (qwen3-32b / deepseek-r1-32b) at 6 disks to benchmark relative capability.

## Iteration 5 (tower iter3) — stage up to 7 disks
- **Config**: devstral-24b, T=0.1, base prompt, 7 disks
- **Result**: 100% SR, 127 steps (optimal, 2^7-1=127)
- **Insight**: Base prompt scales optimally to 7 disks. Wall-clock time ~110 min (~35 sec/inference x 127x3 calls). The alternating-disk-1 rule provably generates 2^n-1 optimal moves; model faithfully follows it without drift across all 127 sequential decisions. Next: push to 8 disks (255 optimal moves, ~220 min projected) OR benchmark alternative models (qwen3-32b, deepseek-r1-32b) at 7 disks to compare capability and speed.

## Iteration 6 (tower iter4) — stage up to 8 disks [TIMEOUT]
- **Config**: devstral-24b, T=0.1, base prompt, 8 disks (optimal=255 moves)
- **Result**: Run still in progress (PID 334021, started ~15:19 Mar 19). Expected ~220 min but taking longer (~10+ hrs). No output file yet.
- **Insight**: Run started but another parallel agent reverted the exp commit (config back to 7). Background process (PID 334021) still running with 8 disks since config was loaded at startup. Output will appear as `tower_of_hanoi_8d_3a_*.json` when complete. If run completes with 100% SR 255 steps, stage up to 9 disks (511 optimal). If it stalls, the model may be drifting at 8 disks — try T=0.0 or minimal prompt
