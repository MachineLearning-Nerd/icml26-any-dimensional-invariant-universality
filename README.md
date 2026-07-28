# Reproducing Any-Dimensional Invariant Universality

This repository reproduces [arXiv:2605.23156](https://arxiv.org/abs/2605.23156)
claim by claim. The previous live evaluator awarded **9/12**: Claims 1, 2, and
6 received full credit, while the three universality claims received one point
each for toy demonstrations. The new work replaces those demonstrations with
machine-checkable implication certificates, independent checkers, and
destructive controls.

Current evidence assessment: all six contracts are **VERIFIED** internally.
The conservative projected score is **11–12/12** and the best-supported
possible score is **12/12**, both forecasts—not live judge results.

Key observed numbers:

- Equation 4 grows **13.743989×** over a 64× horizon, while Equation 5 changes
  only **0.604959%**.
- Equation 5 certificate exhausts **2,415** finite-domain orbit pairs; its
  independent checker exhausts another **1,540**.
- Equation 6 certificate exhausts **2,415** atomic-measure pairs and rejects
  an exponential-growth continuity control.
- The graphon certificate isolates all **33,866** labeled simple graphs
  through six vertices and rejects a repeated-edge mutation.

Formal compute: Hugging Face `cpu-upgrade`, no GPU, one enforced math thread.
The cumulative verifier took 5.294494 seconds; total final job duration was
26 seconds. Standard compactness, UAT, Stone–Weierstrass, Wasserstein, and
graphon-density results are declared premises rather than proof-assistant
formalizations. Claim 4 carries MEDIUM confidence because the paper’s named
activation examples are broader than its literal asymptotic-polynomial
definition.

[Read the illustrated report](reports/claim-by-claim/report.md) ·
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

## Reproduce locally

```bash
uv sync --frozen
uv run --frozen python repro/src/verify.py
marimo edit notebooks/any_dimensional_universality.py
```

The formal evidence is the fixed verifier output. The notebook opens with
embedded results and does not require an expensive rerun.
