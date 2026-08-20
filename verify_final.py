#!/usr/bin/env python3
"""Verify the published documentation, evidence, and provenance contract."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_STATUS = "ALL_C1_C6_VERIFIED_SCOPED_C3_C4_C5_C6_MEDIUM_HISTORICAL_SCORES_9_OF_12_AND_8_OF_12_NO_CURRENT_SCORE"
EXPECTED_BRANCHES = {
    "audit/c3-c4-direct-verification",
    "audit/c3-eq5-proof",
    "audit/c4-eq6-wasserstein",
    "audit/c5-c6-direct-verification",
    "audit/c5-graphon-basis",
    "historical/judged-baseline-9-of-12",
    "main",
    "release/8-of-12-retry",
    "release/evaluator-candidate",
    "release/final-retry-gates",
    "release/published-retry-mirror",
    "release/published-space-mirror",
}
EXPECTED_COMMITS = 27
CANONICAL_IDENTITY = "MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>"


def load(path: str):
    return json.loads((ROOT / path).read_text())


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"verification failed: {message}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def published_branches() -> set[str]:
    remote = {
        name.removeprefix("origin/")
        for name in git(
            "for-each-ref", "refs/remotes/origin", "--format=%(refname:short)"
        ).splitlines()
        if name.startswith("origin/") and name != "origin/HEAD"
    }
    if remote:
        return remote
    return set(git("for-each-ref", "refs/heads", "--format=%(refname:short)").splitlines())


def subset_check_passes(check: dict) -> bool:
    return (
        check["old_file_set_is_subset"] is True
        and check["missing_old_paths"] == []
        and check["modified_originals_archived_byte_exact"] is True
        and check["archive_mismatches"] == []
        and all(check["unchanged_historical_pages"].values())
    )


def main() -> None:
    claims = load("claims.json")
    verdicts = load("reproduction_verdicts.json")
    manifest = load("EVIDENCE_MANIFEST.json")
    state = load("AUTONOMOUS_STATE.json")
    live = load(".openresearch/protected/live_verdict_summary.json")
    source = load(".openresearch/protected/paper_source_audit.json")
    baseline = load("publication/published_space/evidence/cumulative_result.json")
    retry = load("publication/published_space/evidence/retry_cumulative_result.json")
    subset = load("publication/published_space/release/subset_check.json")
    retry_subset = load("publication/published_space/release/retry_subset_check.json")
    README = (ROOT / "README.md").read_text()
    CFF = (ROOT / "CITATION.cff").read_text()

    expected_statuses = {
        "C1": "VERIFIED_SCOPED_HIGH",
        "C2": "VERIFIED_SCOPED_HIGH",
        "C3": "VERIFIED_SCOPED_MEDIUM",
        "C4": "VERIFIED_SCOPED_MEDIUM",
        "C5": "VERIFIED_SCOPED_MEDIUM",
        "C6": "VERIFIED_SCOPED_MEDIUM",
    }
    require(claims["overall_status"] == EXPECTED_STATUS, "claims overall status")
    require(state["overall_status"] == EXPECTED_STATUS, "state overall status")
    require(verdicts["claim_statuses"] == expected_statuses, "verdict statuses")
    require({claim["id"]: claim["status"] for claim in claims["claims"]} == expected_statuses, "claim statuses")
    require(all((ROOT / path).exists() for path in manifest["required_paths"]), "manifest paths")
    for artifact in manifest["artifacts"]:
        require(sha256(ROOT / artifact["path"]) == artifact["sha256"], f"artifact digest {artifact['path']}")
    require(claims["paper"]["arxiv"] == manifest["source"]["arxiv"] == "2605.23156", "paper source")
    require(source["arxiv_id"] == "2605.23156v1", "source revision")
    require("https://arxiv.org/abs/2605.23156" in CFF, "citation source")
    require(EXPECTED_STATUS in README and "leaky ReLU" in README, "README status and caveat")
    require(live["score"] == "9/12", "historical baseline score")
    require(retry["live_judged_score"] == "8/12", "historical retry score")
    historical = verdicts["historical_external_results"]
    require(historical["baseline"]["current_score_claim"] is False, "baseline current score claim")
    require(historical["retry"]["current_score_claim"] is False, "retry current score claim")
    require(verdicts["publication"]["publication_allowed"] is False, "publication state")
    require(verdicts["publication"]["author_endorsement_claimed"] is False, "author endorsement state")
    require(baseline["regression_passed"] is True, "baseline cumulative result")
    require(all(value["status"] == "VERIFIED" for value in baseline["claims"].values()), "baseline claim statuses")
    require(all(value["status"] == "VERIFIED" for value in retry["claims"].values()), "retry claim statuses")
    require(subset_check_passes(subset), "baseline protected subset")
    require(subset_check_passes(retry_subset), "retry protected subset")

    branches = published_branches()
    require(branches == EXPECTED_BRANCHES, "published branches")
    require(not any(branch.startswith("orx/") for branch in branches), "legacy orx branch")
    require(int(git("rev-list", "--all", "--count")) == EXPECTED_COMMITS, "reachable commit count")
    identities = git("log", "--all", "--format=%an <%ae>\n%cn <%ce>").splitlines()
    require(identities and all(identity == CANONICAL_IDENTITY for identity in identities), "canonical commit identity")

    print(
        "FINAL_AUDIT=VERIFIED "
        f"branches={len(branches)} commits={EXPECTED_COMMITS} "
        "claims=C1:C2_high_scoped,C3:C6_medium_scoped historical_scores=9/12,8/12 "
        "current_score_claim=false publication_allowed=false"
    )


if __name__ == "__main__":
    main()
