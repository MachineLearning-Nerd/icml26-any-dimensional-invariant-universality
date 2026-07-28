"""Evaluator-blind traversal and release checks for a staged Space tree."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re


LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
SECRET = re.compile(
    r"(hf_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|ghp_[A-Za-z0-9]{20,}|"
    r"AKIA[0-9A-Z]{16}|-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----)"
)
REQUIRED_CLAIM_TOKENS = (
    "Status:",
    "Exact contract",
    "Source:",
    "Raw",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--pass-name", required=True)
    args = parser.parse_args()
    root = args.candidate.resolve()

    opened = []
    missing_links = []
    unresolved = []
    manifest = json.loads((root / "logbook.json").read_text())
    entrypoints = ["README.md", "logbook.json", "pages/index.md"]
    opened.extend(entrypoints)
    slug_map = {
        child["slug"]: child["file"]
        for child in manifest["root"]["children"]
    }
    current_slugs = ["current-summary", "claim-1", "claim-2", "claim-3", "claim-4", "claim-5", "claim-6", "reproduce", "visibility-matrix"]
    for slug in current_slugs:
        relative = slug_map.get(slug)
        if not relative or not (root / relative).is_file():
            unresolved.append(f"missing canonical page for {slug}")
            continue
        opened.append(relative)
        text = (root / relative).read_text()
        if slug.startswith("claim-"):
            for token in REQUIRED_CLAIM_TOKENS:
                if token not in text:
                    unresolved.append(f"{relative}: missing token {token}")
        for _, target in LINK.findall(text):
            if target.startswith("#/") or target.startswith("http"):
                continue
            clean = target.split("#", 1)[0]
            if clean and not (root / clean).is_file():
                missing_links.append(f"{relative} -> {clean}")

    all_text = []
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".json", ".py", ".toml", ".lock", ".txt"}:
            content = path.read_text(errors="replace")
            all_text.append(content)
            if SECRET.search(content):
                unresolved.append(f"possible secret in {path.relative_to(root)}")

    subset = json.loads((root / "release/subset_check.json").read_text())
    if not subset["old_file_set_is_subset"] or not subset["modified_originals_archived_byte_exact"]:
        unresolved.append("protected subset/archive gate failed")
    if not all(subset["unchanged_historical_pages"].values()):
        unresolved.append("historical evidence page changed")

    visibility = (root / "pages/visibility-matrix/page.md").read_text()
    complete_rows = sum(1 for line in visibility.splitlines() if line.startswith("| ") and line.rstrip().endswith("| Complete |"))
    if complete_rows != 6:
        unresolved.append(f"visibility matrix has {complete_rows}, expected 6 complete rows")

    report = {
        "pass": args.pass_name,
        "review_mode": "candidate tree and rubric only; no OpenResearch logs or unpublished branches consulted",
        "entrypoints": entrypoints,
        "files_opened": opened,
        "claims_located": len([slug for slug in current_slugs if slug.startswith("claim-") and slug in slug_map]),
        "visibility_complete_rows": complete_rows,
        "missing_internal_links": missing_links,
        "unresolved_conclusions": unresolved,
        "historical_pages_unchanged": subset["unchanged_historical_pages"],
        "candidate_tree_sha256": sha256(root / "logbook.json"),
        "passed": not missing_links and not unresolved and complete_rows == 6,
    }
    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
