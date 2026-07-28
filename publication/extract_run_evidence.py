"""Extract the formal cumulative JSON result from an OpenResearch run log."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess


CLAIMS = {
    "claim3": "claim_3_eq5_universality",
    "claim4": "claim_4_eq6_universality",
    "claim5": "claim_5_graphon_basis",
    "claim6": "claim_6_gram_map",
}


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_id")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    evidence = repo / "publication" / "space_files" / "evidence"
    process = subprocess.run(
        ["orx", "logs", args.run_id, "--bytes", "200000"],
        check=True,
        capture_output=True,
        text=True,
    )
    marker = '{\n  "artifact_kind": "complete_six_claim_cumulative_reproduction"'
    start = process.stdout.find(marker)
    if start < 0:
        raise SystemExit("cumulative JSON marker not found in run log")
    result, _ = json.JSONDecoder().raw_decode(process.stdout[start:])
    write_json(evidence / "retry_cumulative_result.json", result)
    for short, key in CLAIMS.items():
        empirical = result["claims"][key]["primary_empirical_verification"]
        write_json(evidence / f"{short}_empirical.json", empirical)
        write_json(evidence / f"{short}_empirical_checker.json", empirical["independent_checker"])
        claim_number = short.removeprefix("claim")
        internal = (
            repo / ".openresearch" / "artifacts" / f"claim_{claim_number}" / "raw"
        )
        write_json(internal / "empirical.json", empirical)
        write_json(internal / "empirical_checker.json", empirical["independent_checker"])
    print(
        json.dumps(
            {
                "run_id": args.run_id,
                "git_sha": result["git_sha"],
                "runtime_seconds": result["runtime_seconds"],
                "regression_passed": result["regression_passed"],
                "evidence_directory": str(evidence),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
