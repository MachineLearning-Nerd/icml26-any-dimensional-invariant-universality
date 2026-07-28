# Evaluator visibility matrix

Traversal starts only from `README.md`, `logbook.json`, or `pages/index.md`.
“Complete” means the canonical page exposes the exact contract, assumptions,
inline output, raw JSON, executable source inline, independent checker,
destructive control, limitations, fixed command, environment, Git SHA, seed,
CPU allocation, and runtime.

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [Claim 1](#/claim-1) | Yes | Yes | Yes | Cumulative exact formulas | Eq. 5 convergence | Yes | Complete |
| 2 | [Claim 2](#/claim-2) | Yes | Yes | Yes | Cumulative exact formulas | Linear map tends to zero | Yes | Complete |
| 3 | [Claim 3](#/claim-3) | Inline function + full runner | Yes | Yes | Independent recomputation | Dropped norm weight diverges | Yes | Complete |
| 4 | [Claim 4](#/claim-4) | Inline function + full runner | Yes | Yes | Independent recomputation | Invalid growth breaks continuity | Yes | Complete |
| 5 | [Claim 5](#/claim-5) | Inline function + full runner | Yes | Yes | Independent recomputation | Edge-only basis cannot separate | Yes | Complete |
| 6 | [Claim 6](#/claim-6) | Inline function + full runner | Yes | Yes | Independent recomputation | Nonorthogonal shear detected | Yes | Complete |

The exact `b0dc5a7` pages remain unchanged at their original paths. Current
navigation points first to the retry pages, which supersede the
**Historical rejected 8/12 baseline**.

Release artifacts:
[allowlist](release/retry_upload_allowlist.txt),
[SHA-256 manifest](release/retry_upload_manifest.sha256),
[red-team record](release/retry_red_team.md), and
[protected subset check](release/retry_subset_check.json).
