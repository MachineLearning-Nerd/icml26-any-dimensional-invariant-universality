# Claim 4 — Equation 6 Wasserstein universality

**Status: VERIFIED · Confidence: MEDIUM**

## Exact contract and quantifiers

Equations 6 and Theorems 4.5–4.6: integration of every continuous
componentwise `p`-growth inner map followed by a continuous outer map is
`W_p`-continuous. On every compact `Q subset P_p(R^k)`, the stated neural
family is dense for every continuous target and `epsilon>0`, under the
paper's activation assumptions.

The source anchors are Equations 6, Theorems 4.5–4.6, and Appendix B.4–B.5.
The direct route uses `p=1`, one-dimensional empirical measures, exact `W1`,
and `rho=tanh`, whose Lipschitz constant is one.

## Direct observed evidence

| Test | Scale | Observed |
| --- | ---: | ---: |
| exact 1D Wasserstein pairs | 4,096 | max integral-gap/`W1` ratio `0.760925 <= 1` |
| permutation invariance | 2,048 | max error `1.554312e-15` |
| equal-mean measure separation | one exact control | `0.5` versus `0` |
| exhaustive rational separation certificate | 2,415 measure pairs | minimum exact gap `1/4` |

The destructive control violates the required linear-growth condition with
`rho(x)=x^2`. For
`mu_n=(1-n^-2)delta_0+n^-2 delta_n`, exact `W1(mu_n,delta_0)` falls
`0.1 -> 0.0001`, but the invalid quadratic integral remains exactly `1`.
The independent checker recomputes continuity, separation, and this failure.

## Current executable verifier

```python
{{CLAIM4_SOURCE}}
```

The shared helpers and complete module are inline on
[Complete runner source](#/runner-source).

## Evidence, control, and scope

- Raw direct output: [evidence/claim4_empirical.json](evidence/claim4_empirical.json)
- Independent checker output: [evidence/claim4_empirical_checker.json](evidence/claim4_empirical_checker.json)
- Full raw cumulative output: [evidence/retry_cumulative_result.json](evidence/retry_cumulative_result.json)
- Exact contract: [evidence/claim4_contract.json](evidence/claim4_contract.json)
- Source: [repro/src/empirical_positive.py](repro/src/empirical_positive.py)
- Checker source: [repro/src/checkers/positive_empirical_independent.py](repro/src/checkers/positive_empirical_independent.py)
- Command and pinned environment: [Reproduce](#/reproduce)

The finite sweep does not infer density. The universal conclusion uses the
separate explicit measure-separation/subalgebra/error-budget chain. The
paper's literal activation examples remain interpretation-sensitive; leaky
ReLU is the certificate's unambiguous assumption-satisfying witness.
