# Claim 6 — Gram map and point-cloud orbits

**Status: VERIFIED · Confidence: MEDIUM**

## Exact contract and quantifiers

Equations 12 and 14 and Theorems 4.12–4.13: on radius-`R` point clouds, the
normalized Gram graphon is Lipschitz, invariant to simultaneous orthogonal
action and permutation, determines the orbit, and permits invariant graphon
readouts to transfer universality to bounded point-cloud orbits.

The source anchors are Equations 12 and 14, Theorems 4.12–4.13, and Appendix
E. The direct tests use `R=2`, varying cloud sizes and dimensions `k=2..5`.

## Direct observed evidence

| Test | Scale | Observed |
| --- | ---: | ---: |
| orthogonal + permutation Gram action | 1,000 clouds | max error `4.440892e-16` |
| five hom-density two-stage readouts | same 1,000 | max action error `1.443290e-15` |
| Gram Lipschitz ratio | 1,000 pairs | max `0.178517 <= 1/R = 0.5` |
| orbit completeness recovery | 512 full-rank pairs | max recovery `6.730727e-15` |
| recovered transform orthogonality | same 512 | max error `1.030874e-14` |

The destructive control applies a non-orthogonal shear. Its orthogonality gap
is `0.24`, Gram gap `0.0215174`, and five-coordinate hom-density readout gap
`0.000240004`: the invariant architecture correctly rejects it as a distinct
orbit. A separately implemented checker reproduces exact rotation invariance,
orthogonal recovery, and shear detection.

## Current executable verifier

```python
{{CLAIM6_SOURCE}}
```

Shared Gram and motif helpers and the complete module are inline on
[Complete runner source](#/runner-source).

## Evidence, control, and scope

- Raw direct output: [evidence/claim6_empirical.json](evidence/claim6_empirical.json)
- Independent checker output: [evidence/claim6_empirical_checker.json](evidence/claim6_empirical_checker.json)
- Full raw cumulative output: [evidence/retry_cumulative_result.json](evidence/retry_cumulative_result.json)
- Exact contract: [evidence/claim6_contract.json](evidence/claim6_contract.json)
- Source: [repro/src/empirical_positive.py](repro/src/empirical_positive.py)
- Checker source: [repro/src/checkers/positive_empirical_independent.py](repro/src/checkers/positive_empirical_independent.py)
- Command and pinned environment: [Reproduce](#/reproduce)

The sweeps directly test the exact Gram, orbit-recovery, and two-stage
invariance mechanisms. The final invariant-network density theorem remains a
named mathematical premise rather than a conclusion drawn only from finite
clouds.
