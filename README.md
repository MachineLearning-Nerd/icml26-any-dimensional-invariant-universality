# ICML 2026 — Any-Dimensional Invariant Universality

[![Open in Molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-any-dimensional-invariant-universality/blob/main/notebooks/any_dimensional_universality.py)

Independent claim-by-claim reproduction audit for [arXiv:2605.23156](https://arxiv.org/abs/2605.23156), *Any-Dimensional Invariant Universality*.

The repository was renamed from `icml26-repro-wRVTDcEMv8-any-dimensional-invariant-universality` to `icml26-any-dimensional-invariant-universality` so the public name describes the paper rather than the challenge identifier.

> **Audit status:** `ALL_C1_C6_VERIFIED_SCOPED_C3_C4_C5_C6_MEDIUM_HISTORICAL_SCORES_9_OF_12_AND_8_OF_12_NO_CURRENT_SCORE`.
> All six claim contracts pass in the current evidence package. Claims 1–2 are high-confidence witnesses/checks; Claims 3–6 are medium-confidence implication certificates plus finite/direct evidence that retain named compactness, density, UAT, and activation-interpretation premises. The historical 9/12 baseline and 8/12 retry scores are preserved, not replaced by a new judge score.

The detailed claim production paths are in [`CLAIM_EVIDENCE.md`](CLAIM_EVIDENCE.md), source and premise boundaries in [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md), environment notes in [`ENVIRONMENT.md`](ENVIRONMENT.md), and machine-readable verdicts in [`claims.json`](claims.json) and [`reproduction_verdicts.json`](reproduction_verdicts.json). [`verify_final.py`](verify_final.py) checks the published branch set, evidence hashes, retry records, and claim boundaries.

## What the paper does

The paper studies universality for models whose inputs can grow in size, such as graphs and point clouds. It embeds finite inputs and their limits in a suitable infinite-dimensional space, equips the quotient by the relevant symmetries with a useful topology, and develops invariant approximation results on compact sets.

Its six audited claims cover two failure mechanisms and four constructive universality results:

1. the original infinite DeepSets aggregation can diverge;
2. nonlinear pointwise maps can be discontinuous in graphon cut norm;
3. a weighted aggregate repairs continuity and supports universality;
4. a Wasserstein aggregate supports universality under a growth condition;
5. the graphon Equation 9 family spans simple-graph homomorphism densities;
6. a normalized Gram map plus invariant graphon architecture is universal on point-cloud orbits.

## Claim and evidence ledger

The current repository evidence marks all six contracts `VERIFIED`. The historical live evaluator scores remain unchanged: the repository records an earlier 9/12 judged baseline and a later 8/12 retry. Forecasts in the reports are not judge results.

| Claim | Paper anchor | How the claim is produced and checked | Current assessment |
|---|---|---|---|
| 1 | Theorem 4.2 — original Equation 4 aggregation | [`verify.py`](repro/src/verify.py) evaluates the assumption-satisfying (X_i=i^{-0.75}\in\ell_2), (ho(x)=\sqrt{|x|}) witness; the partial sum diverges while the weighted control converges | `VERIFIED`, high confidence; one exact asymptotic witness is sufficient |
| 2 | Theorem 4.9 — nonlinear cut-norm discontinuity | [`verify.py`](repro/src/verify.py) checks (W_n=n1_{[0,1/n]^2}): (|W_n|_\square=1/n), (|W_n^2|_\square=1), and the linear control (|3W_n|_\square=3/n) | `VERIFIED`, high confidence; the cited theorem supplies the full classification, while the reproduction audits the decisive counterexample and control |
| 3 | Equations 5, Theorems 4.2–4.3 — weighted aggregate | [`certificates/claim3.py`](repro/src/certificates/claim3.py) builds the uniform-tail, algebra, separator, and neural-error implication chain; [`claim3_independent.py`](repro/src/checkers/claim3_independent.py) performs exact-rational constructor and orbit regressions | `VERIFIED`, medium confidence; finite checks corroborate a certificate using named compactness, Stone–Weierstrass, and UAT premises |
| 4 | Equation 6, Theorems 4.5–4.6 — Wasserstein aggregate | [`certificates/claim4.py`](repro/src/certificates/claim4.py) combines (W_p) continuity, measure separation, compact tail truncation, and global (C_0) UAT; [`claim4_independent.py`](repro/src/checkers/claim4_independent.py) runs exact transport and controls | `VERIFIED`, medium confidence; the growth-condition interpretation uses leaky ReLU because the paper’s ratio-to-polynomial wording is ambiguous for some named activations |
| 5 | Equations 9–10, Theorems 4.9–4.10 — graphon basis | [`certificates/claim5.py`](repro/src/certificates/claim5.py) proves the arbitrary-(m) Boolean-lattice expansion isolates every finite simple graph; [`claim5_independent.py`](repro/src/checkers/claim5_independent.py) checks exact rational graphons and rejects repeated-edge mutations | `VERIFIED`, high confidence; the universal step is the symbolic arbitrary-(m) argument, not only the finite graph sweep |
| 6 | Equations 12 and 14, Theorems 4.12–4.13 — Gram/orbit universality | [`verify.py`](repro/src/verify.py) checks the radius-(R) Lipschitz bound, Gram invariance, orthogonal recovery, and a distinct-Gram control | `VERIFIED`, high confidence; numerical checks corroborate the constructive ingredients while the cited invariant-network density theorem supplies the universal scope |

### Common evidence path

Every claim follows the same chain:

`paper anchor → exact claim contract → executable certificate or witness → independent checker/control → raw evidence → cumulative verifier → report`

Run the cumulative audit with:

```bash
uv run --frozen python repro/src/verify.py
```

The evaluator-facing contracts and raw outputs are under [`publication/space_files`](publication/space_files); the independent synthesis reports are [`reports/claim-by-claim/report.md`](reports/claim-by-claim/report.md) and [`reports/8-of-12-retry/report.md`](reports/8-of-12-retry/report.md).

## Key evidence

| Result | Recorded evidence |
|---|---|
| Equation 4 failure | 13.743989× growth over a 64× horizon for the divergent witness |
| Equation 5 repair | 0.604959% change on the same horizon; 2,000,000-term Basel check reaches (π^2/6) within (4.999999\times10^{-7}) |
| Equation 6 | 4,096 exact (W_1) pairs and 2,048 invariance trials in the retry; invalid growth controls fail as intended |
| Graphon Equation 9 | 33,866 labeled simple graphs through six vertices isolated exactly in the proof certificate; exact-cut direct retry also passes |
| Point-cloud orbits | 2,512 group, Lipschitz, and recovery trials in the retry; a nonorthogonal shear produces a nonzero control gap |

Finite sweeps are regression evidence. The universal claims rely on the explicit implication certificates and named mathematical premises; they are not presented as proof-assistant formalizations.

## Reproduce locally

Dependencies are pinned by [`pyproject.toml`](pyproject.toml) and [`uv.lock`](uv.lock). No GPU is required.

```bash
uv sync --frozen
uv run --frozen python repro/src/verify.py
marimo edit notebooks/any_dimensional_universality.py
```

The notebook opens with embedded evidence and does not require an expensive rerun. Formal jobs used Hugging Face `cpu-upgrade` with numerical libraries restricted to one math thread; command and run details are in the reports and Space logbook.

## Branch map

The live branch names describe their evidence role:

| Branch family | Purpose |
|---|---|
| [`historical/judged-baseline-9-of-12`](https://github.com/MachineLearning-Nerd/icml26-any-dimensional-invariant-universality/tree/historical/judged-baseline-9-of-12) | Preserve the earlier 9/12 judged baseline |
| [`audit/c3-eq5-proof`](https://github.com/MachineLearning-Nerd/icml26-any-dimensional-invariant-universality/tree/audit/c3-eq5-proof) | Build the Equation 5 continuity/universality certificate |
| [`audit/c4-eq6-wasserstein`](https://github.com/MachineLearning-Nerd/icml26-any-dimensional-invariant-universality/tree/audit/c4-eq6-wasserstein) | Build the Equation 6 Wasserstein certificate and growth controls |
| [`audit/c5-graphon-basis`](https://github.com/MachineLearning-Nerd/icml26-any-dimensional-invariant-universality/tree/audit/c5-graphon-basis) | Prove the arbitrary-(m) graphon Boolean-lattice basis |
| [`audit/c3-c4-direct-verification`](https://github.com/MachineLearning-Nerd/icml26-any-dimensional-invariant-universality/tree/audit/c3-c4-direct-verification) | Direct Equation 5 and Equation 6 retry stress tests |
| [`audit/c5-c6-direct-verification`](https://github.com/MachineLearning-Nerd/icml26-any-dimensional-invariant-universality/tree/audit/c5-c6-direct-verification) | Direct graphon and point-cloud orbit verification |
| [`release/evaluator-candidate`](https://github.com/MachineLearning-Nerd/icml26-any-dimensional-invariant-universality/tree/release/evaluator-candidate) | Package evaluator-visible pages and release artifacts |
| [`release/final-retry-gates`](https://github.com/MachineLearning-Nerd/icml26-any-dimensional-invariant-universality/tree/release/final-retry-gates) | Final retry evidence and release gates |
| [`release/published-retry-mirror`](https://github.com/MachineLearning-Nerd/icml26-any-dimensional-invariant-universality/tree/release/published-retry-mirror) | Mirror the published retry and GitHub main surface |
| [`release/published-space-mirror`](https://github.com/MachineLearning-Nerd/icml26-any-dimensional-invariant-universality/tree/release/published-space-mirror) | Mirror the published Space revision and hashes |
| [`release/8-of-12-retry`](https://github.com/MachineLearning-Nerd/icml26-any-dimensional-invariant-universality/tree/release/8-of-12-retry) | Evaluator-visible 8/12 retry candidate |

[`branch-audit.md`](branch-audit.md) records the exact old-to-new mapping and the claim lineage for every branch.

## Repository contents

- `repro/src/` — witnesses, proof certificates, independent checkers, and cumulative verifier.
- `reports/` — illustrated claim-by-claim and retry reports.
- `publication/space_files/` — evaluator-facing pages, claim contracts, raw evidence, controls, and release manifests.
- `publication/published_space/` — mirrored published Space content and historical snapshots.
- `notebooks/` — interactive evidence-first tutorial.

## Scope and limitations

- The historical 9/12 and 8/12 scores are preserved records, not results of this documentation update.
- Finite numerical trials cannot prove universal density theorems by themselves.
- Claims 3–6 combine executable implication checks with named compactness, density, and UAT premises; no Lean/Coq proof-kernel formalization is included.
- Claim 4 uses leaky ReLU to satisfy the literal asymptotic-growth contract; this is documented as an interpretation choice rather than hidden.
- The original paper authors’ claims and the independent audit’s evidence are kept distinct.

## Citation

```bibtex
@misc{yao2026anydimensional,
  title         = {Any-Dimensional Invariant Universality},
  author        = {Yao, Shengtai and Levin, Eitan and D{\'i}az, Mateo},
  year          = {2026},
  eprint        = {2605.23156},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url           = {https://arxiv.org/abs/2605.23156}
}
```

## Thank you

Thank you to Shengtai Yao, Eitan Levin, and Mateo Díaz for developing a clear framework for reasoning about continuity, symmetry, and universality when input dimensions grow. This independent audit is intended to make the paper’s assumptions, constructive steps, and failure mechanisms easier to inspect and reproduce.

## Attribution

Repository maintenance commits in the cleaned branch histories use:

`MachineLearning-Nerd <37579156+MachineLearning-Nerd@users.noreply.github.com>`

The paper and its authors remain the source of the research claims; this repository contains an independent reproduction and audit record.
