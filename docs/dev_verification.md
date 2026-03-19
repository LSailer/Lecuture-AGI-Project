# Dev Verification Report — Autoresearch Pipeline

## Run 1 (initial): Job 3643387
## Run 2 (git fix rerun): Job 3643486

## Date: 2026-03-19
## Partition: dev_gpu_h100 (uc3n082)

---

## Run 2 — Git Commit Behavior Fix (latest)

### What was fixed

| Problem | Before (Run 1) | After (Run 2) |
|---------|----------------|---------------|
| Discard mechanism | `git reset --hard HEAD~1` — destroys commit history | `git revert HEAD~1 --no-edit` — preserves history |
| Commit separation | `git commit -am` (config + results mixed) | Config and results in separate commits |
| Config file safety | Pre-created YAML deleted by `reset --hard` | Config files preserved across iterations |
| Staging up | Iteration 2 didn't stage up to 4 disks | Iteration 2 staged up to 4 disks (15 steps optimal) |
| findings.md | Not present | Created and populated with qualitative insights |

### Checklist

| # | Check | Status | Notes |
|---|-------|--------|-------|
| 1 | sbatch submitted | PASS | job 3643486 |
| 2 | GPU detected | PASS | `NVIDIA H100` |
| 3 | Iteration 1 ran | PASS | SR=100%, 7 steps (optimal for 3 disks) |
| 4 | Iteration 2 ran | PASS | SR=100%, 15 steps (optimal for 4 disks) |
| 5 | Staged up 3→4 disks | PASS | Claude increased `num_disks` from 3 to 4 after SR=100% |
| 6 | results.tsv populated | PASS | header + 2 data rows |
| 7 | findings.md populated | PASS | 2 iteration entries with insights |
| 8 | Config/results separated | PASS | `d521145` = config only, `6ccb502` = results only |
| 9 | Analysis notebook executed | PASS | nbconvert succeeded |
| 10 | git push succeeded | PASS | pushed to origin/feature/parameter-sweep |
| 11 | No discard needed (both kept) | N/A | Both experiments improved — revert path not exercised |

### Results

```
commit    sr         steps  stage  status   description
27b8ca5   1.000000   7      3      keep     dev baseline devstral T=0.1 base prompt 3 disks
d521145   1.000000   15     4      keep     dev iter2 stage up 4 disks base prompt devstral T=0.1 optimal 15 steps
```

### Git History (clean separation)

```
1366f8a feat: add findings.md as persistent knowledge file for autoresearch
43a6f0d exp: dev iter2 validation 3 disks base prompt devstral T=0.1
e33db4c dev: analysis notebook
6ccb502 results: dev iter2 100% SR 15 steps 4 disks — keep (staged up, optimal)
d521145 exp: dev iter2 stage up to 4 disks base prompt devstral T=0.1
85d447b results: dev iter1 baseline 100% SR 7 steps 3 disks — keep
27b8ca5 feat: add configuration and scripts for autoresearch pipeline
```

### Wall-clock: 21 minutes (within 30-minute dev_gpu_h100 limit)

### Known limitation

The `git revert` discard path was NOT exercised in this run because both experiments were `keep`. To fully verify, a run where one experiment is discarded is needed. However, the structural fix (separate commits) is confirmed working, which is the prerequisite for `git revert HEAD~1` to target the right commit.

---

## Run 1 — Initial Validation (superseded)

### Job ID: 3643387 | Wall-clock: 16m 11s

| # | Check | Status | Notes |
|---|-------|--------|-------|
| 1 | sbatch submitted | PASS | job 3643387 |
| 2 | GPU detected | PASS | `NVIDIA H100` |
| 3 | Iteration 1 ran | PASS | SR=100%, 7 steps (optimal for 3 disks) |
| 4 | Iteration 2 ran | PASS | SR=100%, 7 steps (cot_detailed, discarded — same as baseline) |
| 5 | results.tsv populated | PASS | header + 2 data rows |
| 6 | git commits created | PASS | 4 commits |
| 7 | Analysis notebook executed | PASS | nbconvert succeeded |
| 8 | git push succeeded | PASS | pushed to origin/feature/parameter-sweep |
| 9 | PR created | PASS | [PR #20](https://github.com/LSailer/Lecuture-AGI-Project/pull/20) |

### Bugs found in Run 1

1. **`git reset --hard HEAD~1` deleted pre-created config** — destructive discard wiped `tower_of_hanoi_dev.yaml`
2. **Iteration 2 didn't stage up** — Claude chose prompt exploration over difficulty increase
3. **Config + results mixed in one commit** — made `git reset` boundary unclear

All three bugs were fixed for Run 2.
