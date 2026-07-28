"""Build the additive text-only Hugging Face Space candidate.

The input directory must be a clean checkout of the protected judged Space
revision. The output directory must not exist. Historical evidence files are
copied first; only navigation metadata is overlaid, with exact originals
archived under historical/judged-revision/.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess


PROTECTED_REVISION = "ad3feb1493175f9af2a232174cd89d3a2688bd6b"
MODIFIED_HISTORICAL_PATHS = ("README.md", "logbook.json", "pages/index.md")
SOURCE_PATHS = (
    "pyproject.toml",
    "uv.lock",
    "repro/src/verify.py",
    "repro/src/certificates/__init__.py",
    "repro/src/certificates/claim3.py",
    "repro/src/certificates/claim4.py",
    "repro/src/certificates/claim5.py",
    "repro/src/checkers/claim3_independent.py",
    "repro/src/checkers/claim4_independent.py",
    "repro/src/checkers/claim5_independent.py",
)
CONTRACTS = {
    ".openresearch/artifacts/claim_3/claim_contract.json": "evidence/claim3_contract.json",
    ".openresearch/artifacts/claim_4/claim_contract.json": "evidence/claim4_contract.json",
    ".openresearch/artifacts/claim_5/claim_contract.json": "evidence/claim5_contract.json",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_head(directory: Path) -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=directory,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()


def copy_text(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--judged", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    judged = args.judged.resolve()
    out = args.out.resolve()
    if out.exists():
        raise SystemExit(f"output must not exist: {out}")
    if git_head(judged) != PROTECTED_REVISION:
        raise SystemExit("judged checkout is not the protected revision")

    shutil.copytree(judged, out, ignore=shutil.ignore_patterns(".git"))
    archived = {}
    for relative in MODIFIED_HISTORICAL_PATHS:
        source = judged / relative
        destination = out / "historical" / "judged-revision" / relative
        copy_text(source, destination)
        archived[relative] = sha256(destination)

    additions = repo / "publication" / "space_files"
    for source in sorted(path for path in additions.rglob("*") if path.is_file()):
        copy_text(source, out / source.relative_to(additions))

    for relative in SOURCE_PATHS:
        copy_text(repo / relative, out / relative)
    for source_relative, destination_relative in CONTRACTS.items():
        copy_text(repo / source_relative, out / destination_relative)

    original_manifest = {}
    manifest_path = repo / ".openresearch" / "protected" / "judged_space_manifest.sha256"
    for line in manifest_path.read_text().splitlines():
        digest, relative = line.split(maxsplit=1)
        original_manifest[relative.removeprefix("./")] = digest

    missing = sorted(relative for relative in original_manifest if not (out / relative).is_file())
    changed = sorted(
        relative
        for relative, digest in original_manifest.items()
        if (out / relative).is_file() and sha256(out / relative) != digest
    )
    archive_mismatches = sorted(
        relative
        for relative in MODIFIED_HISTORICAL_PATHS
        if archived[relative] != original_manifest[relative]
    )
    subset = {
        "protected_revision": PROTECTED_REVISION,
        "original_file_count": len(original_manifest),
        "candidate_file_count": sum(1 for path in out.rglob("*") if path.is_file()),
        "old_file_set_is_subset": not missing,
        "missing_old_paths": missing,
        "old_paths_with_modified_navigation_content": changed,
        "modified_originals_archived_byte_exact": not archive_mismatches,
        "archive_mismatches": archive_mismatches,
        "unchanged_historical_pages": {
            "pages/verify/page.md": sha256(out / "pages/verify/page.md") == original_manifest["pages/verify/page.md"],
            "pages/overview/page.md": sha256(out / "pages/overview/page.md") == original_manifest["pages/overview/page.md"],
        },
    }
    release = out / "release"
    release.mkdir(parents=True, exist_ok=True)
    (release / "subset_check.json").write_text(json.dumps(subset, indent=2) + "\n")
    if missing or archive_mismatches:
        raise SystemExit("protected subset/archive check failed")

    candidate_paths = sorted(
        str(path.relative_to(out))
        for path in out.rglob("*")
        if path.is_file()
        and (
            path.is_relative_to(out / "evidence")
            or path.is_relative_to(out / "historical")
            or path.is_relative_to(out / "pages")
            or path.is_relative_to(out / "repro")
            or path.is_relative_to(out / "release")
            or path.name in {"README.md", "logbook.json", "pyproject.toml", "uv.lock"}
        )
        and str(path.relative_to(out)) not in {"pages/verify/page.md", "pages/overview/page.md"}
    )
    allowlist = release / "upload_allowlist.txt"
    if "release/upload_allowlist.txt" not in candidate_paths:
        candidate_paths.append("release/upload_allowlist.txt")
    if "release/upload_manifest.sha256" not in candidate_paths:
        candidate_paths.append("release/upload_manifest.sha256")
    candidate_paths = sorted(candidate_paths)
    allowlist.write_text("\n".join(candidate_paths) + "\n")

    manifest = release / "upload_manifest.sha256"
    hashable = [path for path in candidate_paths if path != "release/upload_manifest.sha256"]
    manifest.write_text(
        "".join(f"{sha256(out / relative)}  {relative}\n" for relative in hashable)
    )
    print(json.dumps(subset, indent=2))
    print(f"candidate={out}")
    print(f"allowlisted_text_files={len(candidate_paths)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
