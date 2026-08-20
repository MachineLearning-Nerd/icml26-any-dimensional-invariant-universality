# Branch audit

Repository: [MachineLearning-Nerd/icml26-any-dimensional-invariant-universality](https://github.com/MachineLearning-Nerd/icml26-any-dimensional-invariant-universality)

The repository was renamed from `icml26-repro-wRVTDcEMv8-any-dimensional-invariant-universality`. Former `orx/*` labels are replaced with names that describe the evidence role.

## Old-to-new mapping

| Former branch | Clean branch | Role in the evidence lineage |
|---|---|---|
| `orx/judged-9-of-12-baseline-reconstruction` | `historical/judged-baseline-9-of-12` | Preserve the earlier judged baseline and its score context |
| `orx/claim-3-eq5-proof-certificate` | `audit/c3-eq5-proof` | Equation 5 continuity, algebra, separation, and UAT certificate |
| `orx/claim-4-eq6-wasserstein-proof-certificate` | `audit/c4-eq6-wasserstein` | Equation 6 Wasserstein continuity, tails, and UAT certificate |
| `orx/claim-5-graphon-basis-proof-certificate` | `audit/c5-graphon-basis` | Arbitrary-(m) Boolean-lattice graphon basis certificate |
| `orx/claims-3-4-evaluator-visible-empirical-verificat` | `audit/c3-c4-direct-verification` | Direct Equation 5 and Equation 6 retry stress tests |
| `orx/claims-5-6-direct-graphon-and-orbit-verification` | `audit/c5-c6-direct-verification` | Direct graphon and point-cloud orbit verification |
| `orx/evaluator-visible-release-candidate` | `release/evaluator-candidate` | Canonical evaluator-visible pages and release package |
| `orx/final-retry-evidence-and-release-gates` | `release/final-retry-gates` | Final retry evidence, manifests, and release gates |
| `orx/published-retry-mirror-and-github-main` | `release/published-retry-mirror` | Mirror of the published retry and GitHub main surface |
| `orx/published-space-and-github-mirror` | `release/published-space-mirror` | Mirror of the published Space revision and hashes |
| `orx/8-of-12-retry-evaluator-visible-candidate` | `release/8-of-12-retry` | Evaluator-visible retry candidate preserving the 8/12 context |

`main` is the canonical publication surface. The former `orx/*` remote branches are deleted after the clean replacements are pushed; reachable evidence content is retained in the corresponding histories.

## Claim lineage

| Claim | Primary branch evidence | Canonical files |
|---|---|---|
| 1 — Equation 4 divergence | historical baseline and cumulative retry | `repro/src/verify.py`, `publication/space_files/pages/claim-1/` |
| 2 — cut discontinuity | historical baseline and cumulative retry | `repro/src/verify.py`, `publication/space_files/pages/claim-2/` |
| 3 — Equation 5 | `audit/c3-eq5-proof`, `audit/c3-c4-direct-verification` | `repro/src/certificates/claim3.py`, `repro/src/checkers/claim3_independent.py` |
| 4 — Equation 6 | `audit/c4-eq6-wasserstein`, `audit/c3-c4-direct-verification` | `repro/src/certificates/claim4.py`, `repro/src/checkers/claim4_independent.py` |
| 5 — graphon basis | `audit/c5-graphon-basis`, `audit/c5-c6-direct-verification` | `repro/src/certificates/claim5.py`, `repro/src/checkers/claim5_independent.py` |
| 6 — Gram/orbit universality | `audit/c5-c6-direct-verification` | `repro/src/verify.py`, `repro/src/checkers/positive_empirical_independent.py` |

## Attribution and verification policy

- Clean maintenance commits use `MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>`.
- Branch cleanup changes labels and links, not the scientific evidence or its limitations.
- Historical score records remain labeled historical and must not be presented as new evaluator results.
- Release branches are candidate publication surfaces until the external evaluator runs them.
