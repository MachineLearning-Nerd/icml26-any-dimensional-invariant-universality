# Reproducing Any-Dimensional Invariant Universality

This repository reproduces [arXiv:2605.23156](https://arxiv.org/abs/2605.23156)
claim by claim. The latest live evaluator awarded **8/12**: Claims 1 and 2
received full credit, while the four positive universality claims received one
point each. This retry makes the direct runner evaluator-visible and adds
independent stress tests and destructive controls for Claims 3–6.

Current evidence assessment: all six contracts are **VERIFIED** internally.
The conservative projected score is **10–12/12** and the best-supported
possible score is **12/12**, both forecasts—not live judge results.

Published Space revision:
[`eab3d31bec4ecfafa9a28c1c29ab80c70f78865a`](https://huggingface.co/spaces/DineshAI/wRVTDcEMv8/commit/eab3d31bec4ecfafa9a28c1c29ab80c70f78865a).
This retry is published and awaiting the live judge. The score remains
**8/12** until the evaluator records a new verdict. The prior 48-file judged
tree is protected by a SHA-256 inventory, and all 64 published text paths are
mirrored under
[`publication/published_space`](publication/published_space).

Key observed numbers:

- Equation 4 grows **13.743989×** over a 64× horizon, while Equation 5 changes
  only **0.604959%**.
- Equation 5 reaches `pi²/6` within **4.999999e-7** at two million terms and
  passes **3,072** continuity/invariance trials.
- Equation 6 passes **4,096** exact-Wasserstein pairs and **2,048**
  permutation trials; an invalid quadratic-growth integral stays at one.
- Five graphon motifs pass **500** exact-cut-norm pairs; same edge density
  fails to separate a control that triangle density separates by `0.09375`.
- The Gram/two-stage route passes **2,512** group, Lipschitz, and orbit
  recovery trials; a nonorthogonal shear creates a readout gap.

Formal compute: Hugging Face `cpu-upgrade`, no GPU, one enforced math thread.
The cumulative verifier took 12.227845 seconds; total evidence job duration
was 37 seconds. The four upgraded claims carry MEDIUM confidence because
finite sweeps are combined with named density theorems rather than a
proof-assistant formalization.

[Read the illustrated 8/12 retry report](reports/8-of-12-retry/report.md) ·
[Open the tutorial notebook in Molab](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-wRVTDcEMv8-any-dimensional-invariant-universality/blob/main/notebooks/any_dimensional_universality.py)
[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-wRVTDcEMv8-any-dimensional-invariant-universality/blob/main/notebooks/any_dimensional_universality.py)

## Experiment log

Every experiment inherited the exact same command:

```bash
uv run --frozen python repro/src/verify.py
```

| Branch / experiment | Purpose or change | Exact run command | Assessment / outcome | Compute |
| --- | --- | --- | --- | --- |
| `main` | Public README, report, and notebook | Not run as an experiment (publication surface) | Presentation-only | None |
| [Judged baseline](https://github.com/MachineLearning-Nerd/icml26-repro-wRVTDcEMv8-any-dimensional-invariant-universality/tree/orx/judged-9-of-12-baseline-reconstruction) | Reconstruct live 9/12 state | `uv run --frozen python repro/src/verify.py` | Claims 1,2,6 VERIFIED; 3–5 historical TOY | HF `cpu-upgrade`, 21 s |
| [Claim 3 certificate](https://github.com/MachineLearning-Nerd/icml26-repro-wRVTDcEMv8-any-dimensional-invariant-universality/tree/orx/claim-3-eq5-proof-certificate) | Replace one-target fit with Eq. 5 implication certificate | `uv run --frozen python repro/src/verify.py` | Claim 3 VERIFIED; cumulative pass | HF `cpu-upgrade`, 4m57s including startup |
| [Claim 4 certificate](https://github.com/MachineLearning-Nerd/icml26-repro-wRVTDcEMv8-any-dimensional-invariant-universality/tree/orx/claim-4-eq6-wasserstein-proof-certificate) | Add Wasserstein tail/noncompact-UAT certificate | `uv run --frozen python repro/src/verify.py` | Claim 4 VERIFIED, MEDIUM confidence; cumulative pass | HF `cpu-upgrade`, 21 s |
| [Claim 5 certificate](https://github.com/MachineLearning-Nerd/icml26-repro-wRVTDcEMv8-any-dimensional-invariant-universality/tree/orx/claim-5-graphon-basis-proof-certificate) | Add arbitrary-m Boolean-lattice certificate | `uv run --frozen python repro/src/verify.py` | Claim 5 VERIFIED; all six cumulative claims pass | HF `cpu-upgrade`, 26 s |
| [Release candidate](https://github.com/MachineLearning-Nerd/icml26-repro-wRVTDcEMv8-any-dimensional-invariant-universality/tree/orx/evaluator-visible-release-candidate) | Package canonical Space pages, report, notebook, manifests, and red-team audit | `uv run --frozen python repro/src/verify.py` | All six cumulative claim checks pass; packaging gates complete | HF `cpu-upgrade` |
| [Published mirror](https://github.com/MachineLearning-Nerd/icml26-repro-wRVTDcEMv8-any-dimensional-invariant-universality/tree/orx/published-space-and-github-mirror) | Mirror exact published Space revision and finalize GitHub surface | `uv run --frozen python repro/src/verify.py` | 36/36 published text hashes match; all six cumulative checks pass | HF `cpu-upgrade` |
| [Claims 3–4 direct retry](https://github.com/MachineLearning-Nerd/icml26-repro-wRVTDcEMv8-any-dimensional-invariant-universality/tree/orx/claims-3-4-evaluator-visible-empirical-verificat) | Million-term Eq. 5 and exact-W1 Eq. 6 stress tests | `uv run --frozen python repro/src/verify.py` | Direct checks and cumulative regression pass | HF `cpu-upgrade`, 32 s |
| [Claims 5–6 direct retry](https://github.com/MachineLearning-Nerd/icml26-repro-wRVTDcEMv8-any-dimensional-invariant-universality/tree/orx/claims-5-6-direct-graphon-and-orbit-verification) | Exact-cut graphons and large orbit/two-stage sweeps | `uv run --frozen python repro/src/verify.py` | Direct checks and cumulative regression pass | HF `cpu-upgrade`, 32 s |
| [8/12 retry candidate](https://github.com/MachineLearning-Nerd/icml26-repro-wRVTDcEMv8-any-dimensional-invariant-universality/tree/orx/8-of-12-retry-evaluator-visible-candidate) | Inline source, raw evidence, historical preservation, blind traversal | `uv run --frozen python repro/src/verify.py` | Six claims pass; evaluator-visible audit complete | HF `cpu-upgrade`, 37 s |

## Reproduce locally

```bash
uv sync --frozen
uv run --frozen python repro/src/verify.py
marimo edit notebooks/any_dimensional_universality.py
```

The formal evidence is the fixed verifier output. The notebook opens with
embedded results and does not require an expensive rerun.
