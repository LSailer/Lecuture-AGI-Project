"""
Autoresearch loop for Tower of Hanoi / Sliding Puzzle.

Inspired by github.com/karpathy/autoresearch — iterates over parameter
combinations (model, temperature, prompt variant, agents, margin_k),
runs main.py for each, keeps improvements, discards regressions.

Usage:
  uv run scripts/autoresearch.py --game tower_of_hanoi --time-budget 23.5
  uv run scripts/autoresearch.py --game sliding_puzzle --dry-run
"""

import argparse
import csv
import itertools
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = REPO_ROOT / "src" / "config"
RESULTS_TSV = REPO_ROOT / "results.tsv"
RESULTS_CSV = REPO_ROOT / "output" / "autoresearch_results.csv"

MODELS = {
    "qwen3-32b": "LLM/models/qwen3-32b",
    "devstral-24b": "LLM/models/devstral-24b",
    "deepseek-r1-32b": "LLM/models/deepseek-r1-32b",
}

TEMPERATURES = [0.0, 0.1, 0.3, 0.5, 0.7, 1.0]
PROMPT_VARIANTS = ["base", "cot_detailed", "minimal"]
AGENT_COUNTS = [1, 3, 5]
MARGIN_KS = [1, 2, 3]

# Tower of Hanoi stages: num_disks
TOH_STAGES = [3, 4, 5, 6, 7, 8, 9, 10]

# Sliding Puzzle stages: config key name → initial_state
SP_STAGES = [
    "2x2",
    "3x3 (easiest)",
    "3x3 (hardest)",
    "4x4 (easiest)",
    "4x4 (hardest)",
]

# Per-experiment timeout (seconds)
EXPERIMENT_TIMEOUT = 3600  # 60 min


def get_sp_configs():
    """Import CONFIGS from sliding_puzzle environment."""
    sys.path.insert(0, str(REPO_ROOT / "src"))
    from sliding_puzzle.enviroment import CONFIGS
    return CONFIGS


def load_config(game: str) -> dict:
    path = CONFIG_DIR / f"{game}.yaml"
    with open(path) as f:
        return yaml.safe_load(f)


def save_config(game: str, config: dict):
    path = CONFIG_DIR / f"{game}.yaml"
    with open(path, "w") as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)


def git_commit(message: str):
    subprocess.run(["git", "add", "-A"], cwd=REPO_ROOT, check=True)
    subprocess.run(
        ["git", "commit", "-m", message, "--allow-empty"],
        cwd=REPO_ROOT, check=True,
    )


def git_reset():
    subprocess.run(["git", "reset", "--hard", "HEAD~1"], cwd=REPO_ROOT, check=True)


def git_short_hash() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    return result.stdout.strip()


def run_experiment(game: str, config: dict, timeout: int = EXPERIMENT_TIMEOUT) -> dict:
    """Run main.py and parse SR + steps from output."""
    cmd = [
        "uv", "run", "src/main.py",
        "--game", game,
        "--model_path", config.get("model_path", "LLM/model"),
        "--temperature", str(config.get("temperature", 0.1)),
        "--max_agents_per_step", str(config.get("max_agents_per_step", 3)),
        "--margin_k", str(config.get("margin_k", 2)),
        "--prompt_variant", config.get("prompt_variant", "base"),
    ]
    if game == "tower_of_hanoi":
        cmd += ["--num_disks", str(config.get("num_disks", 3))]

    log_path = REPO_ROOT / "output" / "autoresearch_run.log"
    os.makedirs(REPO_ROOT / "output", exist_ok=True)

    try:
        with open(log_path, "w") as log_file:
            result = subprocess.run(
                cmd, cwd=REPO_ROOT, timeout=timeout,
                stdout=log_file, stderr=subprocess.STDOUT,
            )
        exit_code = result.returncode
    except subprocess.TimeoutExpired:
        return {"sr": 0.0, "steps": 0, "solved": False, "cycle_detected": False, "crash": True, "error": "timeout"}

    # Parse output
    try:
        log_content = log_path.read_text()
    except Exception:
        return {"sr": 0.0, "steps": 0, "solved": False, "cycle_detected": False, "crash": True, "error": "no_log"}

    sr = 0.0
    steps = 0
    solved = False
    cycle_detected = False

    sr_match = re.search(r"Success Rate:\s*([\d.]+)%", log_content)
    if sr_match:
        sr = float(sr_match.group(1)) / 100.0

    steps_match = re.search(r"(?:solved in|Max steps.*reached).*?(\d+)\s+steps", log_content, re.IGNORECASE)
    if steps_match:
        steps = int(steps_match.group(1))

    if "Puzzle solved" in log_content:
        solved = True
    if "Cycle detected" in log_content:
        cycle_detected = True

    return {
        "sr": sr,
        "steps": steps,
        "solved": solved,
        "cycle_detected": cycle_detected,
        "crash": exit_code != 0,
        "error": None if exit_code == 0 else f"exit_{exit_code}",
    }


def log_result_tsv(commit: str, sr: float, steps: int, status: str, description: str):
    """Append to results.tsv (Karpathy-style)."""
    exists = RESULTS_TSV.exists()
    with open(RESULTS_TSV, "a") as f:
        if not exists:
            f.write("commit\tsr\tsteps\tstatus\tdescription\n")
        f.write(f"{commit}\t{sr:.6f}\t{steps}\t{status}\t{description}\n")


def log_result_csv(
    experiment_id: int, game: str, model: str, temperature: float,
    prompt_variant: str, max_agents: int, margin_k: int, stage: str,
    sr: float, steps: int, cycle_detected: bool, solved: bool,
    status: str, commit: str, description: str,
):
    """Append to CSV for pandas analysis."""
    os.makedirs(RESULTS_CSV.parent, exist_ok=True)
    exists = RESULTS_CSV.exists()
    with open(RESULTS_CSV, "a", newline="") as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow([
                "experiment_id", "timestamp", "game", "model", "temperature",
                "prompt_variant", "max_agents", "margin_k", "stage",
                "sr", "steps", "cycle_detected", "solved", "status",
                "commit_hash", "description",
            ])
        writer.writerow([
            experiment_id, datetime.now().isoformat(), game, model, temperature,
            prompt_variant, max_agents, margin_k, stage,
            f"{sr:.6f}", steps, cycle_detected, solved, status,
            commit, description,
        ])


def generate_experiment_configs(game: str):
    """Generate all parameter combinations to try."""
    configs = []
    for model_name, model_path in MODELS.items():
        for temp in TEMPERATURES:
            for prompt in PROMPT_VARIANTS:
                for agents in AGENT_COUNTS:
                    for mk in MARGIN_KS:
                        configs.append({
                            "model_name": model_name,
                            "model_path": model_path,
                            "temperature": temp,
                            "prompt_variant": prompt,
                            "max_agents_per_step": agents,
                            "margin_k": mk,
                        })
    return configs


def should_advance_stage(results_at_stage: list[dict]) -> bool:
    """Advance if SR=100% for 2 consecutive experiments."""
    if len(results_at_stage) < 2:
        return False
    return results_at_stage[-1]["sr"] == 1.0 and results_at_stage[-2]["sr"] == 1.0


def save_best_and_pr(game: str, tag: str):
    """Push branch and create PR with results."""
    branch = f"autoresearch/{game}-{tag}"
    try:
        subprocess.run(["git", "push", "-u", "origin", branch], cwd=REPO_ROOT, check=True)
    except Exception as e:
        print(f"Push failed: {e}")
        return

    # Build PR body from results.tsv
    body = "## Autoresearch Results\n\n"
    if RESULTS_TSV.exists():
        body += "```\n" + RESULTS_TSV.read_text() + "```\n"
    body += f"\nGame: {game}\nBranch: {branch}\n"

    try:
        subprocess.run(
            ["gh", "pr", "create", "--title", f"autoresearch: {game} {tag}", "--body", body],
            cwd=REPO_ROOT, check=True,
        )
    except Exception as e:
        print(f"PR creation failed: {e}")


def main():
    parser = argparse.ArgumentParser(description="Autoresearch loop")
    parser.add_argument("--game", required=True, choices=["tower_of_hanoi", "sliding_puzzle"])
    parser.add_argument("--time-budget", type=float, default=23.5, help="Hours")
    parser.add_argument("--dry-run", action="store_true", help="Print experiments without running")
    parser.add_argument("--tag", default=None, help="Branch tag (default: date)")
    args = parser.parse_args()

    game = args.game
    time_budget_s = args.time_budget * 3600
    start_time = time.time()
    tag = args.tag or datetime.now().strftime("%b%d").lower()

    if game == "sliding_puzzle":
        sp_configs = get_sp_configs()
        stages = SP_STAGES
    else:
        stages = TOH_STAGES

    experiment_configs = generate_experiment_configs(game)

    if args.dry_run:
        print(f"Game: {game}")
        print(f"Stages: {stages}")
        print(f"Total param combos: {len(experiment_configs)}")
        print(f"Time budget: {args.time_budget}h")
        print("\nFirst 5 experiments:")
        for i, ec in enumerate(experiment_configs[:5]):
            print(f"  {i+1}. {ec}")
        return

    # State
    current_stage_idx = 0
    best_sr = 0.0
    best_steps = float("inf")
    experiment_id = 0
    stage_results: list[dict] = []

    print(f"=== Autoresearch: {game} ===")
    print(f"Time budget: {args.time_budget}h")
    print(f"Stages: {stages}")
    print(f"Param combos per stage: {len(experiment_configs)}")

    while current_stage_idx < len(stages):
        current_stage = stages[current_stage_idx]
        print(f"\n{'='*60}")
        print(f"STAGE: {current_stage}")
        print(f"{'='*60}")

        stage_results = []
        best_sr = 0.0
        best_steps = float("inf")

        for ec in experiment_configs:
            # Time check
            elapsed = time.time() - start_time
            remaining = time_budget_s - elapsed
            if remaining < 1800:  # 30 min reserve
                print(f"\nTime budget nearly exhausted ({remaining/60:.0f} min left). Saving best and creating PR.")
                save_best_and_pr(game, tag)
                return

            experiment_id += 1

            # Build config
            config = load_config(game)
            config["model_path"] = ec["model_path"]
            config["temperature"] = ec["temperature"]
            config["prompt_variant"] = ec["prompt_variant"]
            config["max_agents_per_step"] = ec["max_agents_per_step"]
            config["margin_k"] = ec["margin_k"]

            if game == "tower_of_hanoi":
                config["num_disks"] = current_stage
                stage_label = str(current_stage)
            else:
                config["initial_state"] = sp_configs[current_stage]
                stage_label = current_stage

            # Adjust max_steps for small problems
            if game == "tower_of_hanoi":
                optimal = 2 ** current_stage - 1
                config["max_steps"] = max(optimal * 3, 100)

            description = (
                f"{ec['model_name']} T={ec['temperature']} "
                f"p={ec['prompt_variant']} a={ec['max_agents_per_step']} "
                f"mk={ec['margin_k']} stage={stage_label}"
            )

            print(f"\n--- Experiment {experiment_id}: {description} ---")

            # Save config and commit
            save_config(game, config)
            git_commit(f"exp: {game} {description}")

            # Run
            result = run_experiment(game, config)
            commit = git_short_hash()

            sr = result["sr"]
            steps = result["steps"]
            solved = result["solved"]
            cycle = result["cycle_detected"]
            crash = result.get("crash", False)

            # Determine status
            if crash:
                status = "crash"
            elif sr > best_sr or (sr == best_sr and steps < best_steps):
                status = "keep"
            else:
                status = "discard"

            print(f"  SR={sr:.1%} steps={steps} solved={solved} → {status}")

            # Log
            log_result_tsv(commit, sr, steps, status, description)
            log_result_csv(
                experiment_id, game, ec["model_name"], ec["temperature"],
                ec["prompt_variant"], ec["max_agents_per_step"], ec["margin_k"],
                stage_label, sr, steps, cycle, solved, status, commit, description,
            )

            # Keep or discard
            if status == "keep":
                best_sr = sr
                best_steps = steps
                stage_results.append({"sr": sr, "steps": steps})
                print(f"  New best! SR={best_sr:.1%} steps={best_steps}")
            else:
                git_reset()
                stage_results.append({"sr": sr, "steps": steps})

            # Check stage advancement
            if should_advance_stage(stage_results):
                print(f"\n>>> Stage {current_stage} complete! Advancing...")
                break

        current_stage_idx += 1

    print(f"\nAll stages completed! Creating PR...")
    save_best_and_pr(game, tag)


if __name__ == "__main__":
    main()
