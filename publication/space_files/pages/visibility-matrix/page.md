# Evaluator visibility matrix

Every row was traversed starting from `README.md`, `logbook.json`, and
`pages/index.md`. “Complete” means the canonical page exposes the exact claim,
assumptions, inline data, raw file, executable code, checker/control,
limitations, command, environment, provenance, CPU, and runtime.

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [Claim 1](#/claim-1) | Yes | Yes | Yes | In cumulative verifier | Eq. 5 converges | Yes | Complete |
| 2 | [Claim 2](#/claim-2) | Yes | Yes | Yes | Exact formulas | Linear map tends to zero | Yes | Complete |
| 3 | [Claim 3](#/claim-3) | Yes | Yes | Yes | Independent exact rational | Three destructive mutations | Yes | Complete |
| 4 | [Claim 4](#/claim-4) | Yes | Yes | Yes | Independent exact rational | Exponential growth and budget mutations | Yes | Complete |
| 5 | [Claim 5](#/claim-5) | Yes | Yes | Yes | Independent exact rational | Repeated-edge mutation | Yes | Complete |
| 6 | [Claim 6](#/claim-6) | Yes | Yes | Yes | In cumulative verifier | Distinct Gram | Yes | Complete |

Historical `verify` and `overview` files remain reachable and unchanged but are
explicitly labeled **Historical rejected baseline**. The current verifier at
commit `a63d9eaeb0fe8eaf4dd94a5c1f6ffdec93050bd5` supersedes them.

Release artifacts:
[allowlist](release/upload_allowlist.txt),
[SHA-256 manifest](release/upload_manifest.sha256),
[red-team record](release/red_team.md), and
[protected subset check](release/subset_check.json).
