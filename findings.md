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
