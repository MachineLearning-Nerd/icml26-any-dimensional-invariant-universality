# Claim 3 — Equation 5 continuity and universality

**Status: VERIFIED · Confidence: MEDIUM**

## Exact contract and quantifiers

Equation 5 and Theorems 4.2–4.3: for every finite `k`, every
`p in [1,infinity)`, and continuous inner/outer maps, the norm-reweighted
aggregate is continuous on the `ell_p(R^k)` quotient. For every compact
`K subset ell_p(R^k)`, every continuous invariant target and every
`epsilon>0`, the stated neural class is dense.

The source anchors are Equation 5, Theorems 4.2–4.3, and Appendix B.2–B.3.
The numerical route fixes `p=1`; the implication certificate separately
audits arbitrary `p`, compact `K`, point separation, subalgebra closure, and
the UAT error composition.

## Direct observed evidence

| Test | Scale | Observed |
| --- | ---: | ---: |
| Eq. 5 Basel sequence `x_i=i^-2`, `rho=1` | 2,000,000 terms | error to `pi^2/6`: `4.999999e-7` |
| permutation + zero padding | 2,048 trials | max error `8.881784e-15` |
| `ell_1` continuity, `rho=tanh` | 1,024 pairs | max fraction of proved `2||x-y||_1` bound `0.412692` |
| exhaustive bump separation certificate | 2,415 orbit pairs | minimum gap `1` |

The dropped-weight control grows exactly `64x`. On the paper's slow-decay
witness the invalid unweighted aggregate grows `50.1924 -> 687.8054`
(`13.703x`), while Eq. 5 stabilizes `1.77099 -> 1.77967`. The independent
implementation recomputes a one-million-term limit, permutation identity, and
dropped-weight failure and exits zero.

## Current executable verifier

This is the exact function invoked by the fixed command. Shared helpers and
the complete importable module are inline on [Complete runner source](#/runner-source).

```python
{{CLAIM3_SOURCE}}
```

## Evidence, control, and scope

- Raw direct output: [evidence/claim3_empirical.json](evidence/claim3_empirical.json)
- Independent checker output: [evidence/claim3_empirical_checker.json](evidence/claim3_empirical_checker.json)
- Full raw cumulative output: [evidence/retry_cumulative_result.json](evidence/retry_cumulative_result.json)
- Exact contract: [evidence/claim3_contract.json](evidence/claim3_contract.json)
- Source: [repro/src/empirical_positive.py](repro/src/empirical_positive.py)
- Checker source: [repro/src/checkers/positive_empirical_independent.py](repro/src/checkers/positive_empirical_independent.py)
- Command and pinned environment: [Reproduce](#/reproduce)

Finite sweeps directly verify convergence, continuity, invariance, and a
failure-inducing control. Universal density additionally uses the explicit
constructor/separation implication chain and standard named theorems; it is
not inferred from sweep size or from fitting one target.
