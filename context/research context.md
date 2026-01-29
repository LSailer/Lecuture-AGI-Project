# Research Context: MAKER Reimplementation & Extension

**Working Title**: Reimplementing and Extending MAKER: Massively Decomposed Agentic Processes Beyond Towers of Hanoi
**Field of Study**: Artificial Intelligence / Multi-Agent LLM Systems

## Project Overview

**Summary**
This project reimplements the MAKER framework introduced by Meyerson _et al._ (2025), a system that solved the Towers of Hanoi problem with 20 disks (over one million LLM steps) with zero errors. MAKER operates through extreme task decomposition into minimal subtasks, each handled by a focused microagent, combined with a multi-agent voting scheme for error correction and a red-flagging mechanism to discard structurally unreliable outputs. The reimplementation reproduces the 20-disk Towers of Hanoi experiment as a baseline and subsequently extends the framework to structurally diverse puzzle domains: sliding number puzzles, Wordle, and Sudoku. The goal is to investigate whether the principles underlying MAKER, namely maximal agentic decomposition (MAD), first-to-ahead-by-_k_ voting, and red-flagging, generalize beyond the single benchmark domain in which they were originally validated.

## The Core Problem

LLMs exhibit a persistent per-step error rate that compounds across sequential steps, causing performance to deteriorate exponentially with task length regardless of per-step complexity [Meyerson *et al.*, 2025; Dziri *et al.*, 2023; Sinha *et al.*, 2025]. A system with a 1% per-step error rate is expected to fail after only 100 steps. This makes monolithic single-agent approaches fundamentally infeasible for tasks requiring thousands or millions of dependent steps with high precision. Meyerson _et al._ (2025) demonstrated that massively decomposed agentic processes (MDAPs) can overcome this limitation, but validated the approach exclusively on Towers of Hanoi, a problem with known optimal algorithms, deterministic state transitions, and uniform step structure. It remains unclear whether the framework generalizes to problems with heterogeneous step difficulty, larger branching factors, constraint-satisfaction structure, or steps requiring semantic reasoning under uncertainty.

> **Core Conflict:** MAKER achieves zero-error execution over one million steps, but its generalizability beyond a single, structurally uniform benchmark domain has not been established.

## Research Questions

- **RQ1**: Does maximal agentic decomposition improve per-step reliability across puzzle domains with different structural properties (branching factor, constraint density, step heterogeneity)?
- **RQ2**: Do the scaling laws derived for uniform, sequential tasks (expected cost = Theta(s ln s)) hold when step difficulty varies or when steps have non-trivial interdependencies?
- **RQ3**: Are the red-flag heuristics (response length thresholds, format error detection) transferable across domains, or do different puzzle types require domain-specific unreliability indicators?
- **RQ4**: For which puzzle types is decomposition into minimal steps straightforward, and where does the framework encounter fundamental limits?

## Hypotheses

Based on the MDAP framework [Meyerson *et al.*, 2025] and the theoretical scaling laws therein, the following hypotheses are proposed:

1. **H1**: The Towers of Hanoi reimplementation will reproduce the zero-error result reported by Meyerson _et al._ (2025), confirming that the core components (MAD, voting, red-flagging) are sufficient for this domain when using a comparable base LLM.
2. **H2**: Sliding number puzzles, which share the sequential single-move structure of Towers of Hanoi but have a larger and variable branching factor, will benefit from MAD and voting, though the per-step error rate _p_ is expected to be lower due to increased move ambiguity, requiring a higher _k_ for equivalent reliability.
3. **H3**: Wordle, a task with few steps but high per-step reasoning depth, will expose a boundary of the MDAP framework: the voting mechanism may be less effective when each step involves semantic uncertainty rather than deterministic state transitions.
4. **H4**: Sudoku, a constraint-satisfaction problem with global interdependencies between cells, will require adaptations to the decomposition strategy, as single-cell steps are not fully independent and errors may propagate through constraint violations.

## Methodology Snapshot

**Setup & Environment**

- **Environment/Source**: LLM API calls (model selection based on cost-to-accuracy ratio _c/p_ as prescribed by the framework)
- **Model/Subject**: Non-reasoning LLMs (following the finding by Meyerson _et al._ (2025) that small non-reasoning models suffice for MAD-based execution)

**Procedure**

1. **Reimplementation**: Reproduce the MAKER system with the three core components (MAD, first-to-ahead-by-_k_ voting, red-flagging) and validate on 20-disk Towers of Hanoi.
2. **Per-step error estimation**: For each new domain, estimate the per-step success rate _p_ on a random subset of steps, following the calibration approach described in Section 4.2 of Meyerson _et al._ (2025).
3. **Cost projection**: Use the scaling law formula _E[cost] = c _ s _ k_min / (v _ (2p - 1))\* to project costs before running full-scale experiments.
4. **Full-scale execution**: Run MAKER on each puzzle domain with the calibrated parameters and evaluate: total errors, number of voting rounds per step, convergence behavior, and impact of red-flagging.
5. **Comparative analysis**: Compare empirical results across domains to assess generalizability of the framework and its components.
