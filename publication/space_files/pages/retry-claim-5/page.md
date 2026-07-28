# Claim 5 — homomorphism-density graphon basis

**Status: VERIFIED · Confidence: MEDIUM**

## Exact contract and quantifiers

Equations 9–10 and Theorems 4.9–4.10: for every finite order `m`, Equation 9
expands into cut-continuous simple-graph homomorphism densities; every finite
simple-graph density is realized by the model. Their span is universal for
continuous functions on `[0,1]` graphon space modulo the cut metric.

The source anchors are Equations 9–10, Theorems 4.9–4.10, and Appendix
C.2–C.3. The arbitrary-`m` certificate sets `(a_e,b_e)=(1,0)` on target
edges and `(0,1)` off them, leaving exactly the target square-free monomial.

## Direct observed evidence

The cut norm was computed exactly by exhaustive subset optimization for 500
pairs of symmetric seven-block graphons.

| Motif | Edges | max `|t(F,W)-t(F,U)| / ||W-U||_square` |
| --- | ---: | ---: |
| edge `K2` | 1 | `1.0000000000000013` |
| path `P3` | 2 | `1.074112` |
| triangle `K3` | 3 | `0.956867` |
| star `K1,3` | 3 | `0.944560` |
| cycle `C4` | 4 | `0.686445` |

Across 500 relabelings the largest error was `4.163336e-16`. Equation 9's
0/1 target parametrization matched five separately vectorized motif
implementations on 64 graphons with maximum error `6.938894e-16`.

The negative control compares a triangle-plus-isolate with `P4`: edge density
is identical (`0.375`, gap `0`), so an edge-only architecture cannot separate
them; triangle density gives `0.09375` versus `0`. A constant perturbation
attains the edge/cut ratio `1`, detecting an incorrect cut normalization.

## Current executable verifier

```python
{{CLAIM5_SOURCE}}
```

Shared exact-cut and motif helpers and the complete module are inline on
[Complete runner source](#/runner-source).

## Evidence, control, and scope

- Raw direct output: [evidence/claim5_empirical.json](evidence/claim5_empirical.json)
- Independent checker output: [evidence/claim5_empirical_checker.json](evidence/claim5_empirical_checker.json)
- Full raw cumulative output: [evidence/retry_cumulative_result.json](evidence/retry_cumulative_result.json)
- Exact contract: [evidence/claim5_contract.json](evidence/claim5_contract.json)
- Source: [repro/src/empirical_positive.py](repro/src/empirical_positive.py)
- Checker source: [repro/src/checkers/positive_empirical_independent.py](repro/src/checkers/positive_empirical_independent.py)
- Command and pinned environment: [Reproduce](#/reproduce)

Finite step graphons corroborate continuity, invariance, realization, and
separation. Arbitrary graph order is handled by the symbolic Boolean-lattice
argument; graphon-space density remains the cited primary theorem rather than
an inference from 500 samples.
