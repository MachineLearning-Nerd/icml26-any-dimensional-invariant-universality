# Claim 4 — Equation 6 Wasserstein universality

**Status: VERIFIED · Confidence: MEDIUM**

## Exact contract and quantifiers

Equation 6 and Theorems 4.5–4.6: integration of every continuous
componentwise `p`-growth `rho`, followed by continuous `sigma`, is
`W_p`-continuous. For every compact `Q subset P_p(R^k)`, every continuous
target, and every positive accuracy, the neural class is dense when the
activation is Lipschitz, continuous, nonpolynomial, and asymptotically
polynomial at both infinities.

Declared premises: the `W_p` convergence characterization, compact
tightness/`p`-uniform-integrability, measure regularity and Urysohn
separation, real Stone-Weierstrass, and van Nuland's global `C_0(R^k)` UAT
(arXiv:2308.03812v2).

## Machine-checkable implication chain

1. The `W_p` characterization gives continuity of `mu -> integral rho dmu`.
2. Concatenation preserves componentwise `p` growth and supplies exact
   addition/product constructors.
3. A bounded continuous bump separates any distinct probability measures.
4. Tightness and `p`-uniform-integrability bound truncation error by
   `delta/2`.
5. Global `C_0` UAT contributes the other `delta/2`; the corrected outer
   compact neighborhood closes the final error at `epsilon`.

## Evidence and controls

- 256 atomic Kantorovich–Rubinstein checks for `tanh`: maximum ratio
  `0.797225 < 1`.
- All 2,415 pairs among 70 denominator-four measures separated; minimum exact
  integral gap `1/4`.
- Exact compact unbounded family has second-moment tail
  `1/4,1/16,1/64,1/256,1/1024`.
- Exponential-growth control: `W_2` falls `0.5 -> 0.176777`, while the log
  integral lower bound rises `-0.158883 -> 21.602792`.
- Doubled tail allowances produce `3 delta/2`, correctly rejected.
- Independent checker: 1,540 measure pairs and 56 constructor cases, exit 0.

The paper lists ReLU, Softplus, and Sigmoid as examples, but its literal
ratio-to-polynomial definition is ambiguous when the activation tends to zero
at one end. The certificate uses leaky ReLU, whose asymptotes `0.1t` and `t`
unambiguously satisfy the written assumptions. This interpretation risk is why
confidence is MEDIUM.

- Source: [repro/src/certificates/claim4.py](repro/src/certificates/claim4.py)
- Independent checker: [repro/src/checkers/claim4_independent.py](repro/src/checkers/claim4_independent.py)
- Contract: [evidence/claim4_contract.json](evidence/claim4_contract.json)
- Raw checker: [evidence/claim4_checker.json](evidence/claim4_checker.json)
- Raw cumulative result: [evidence/cumulative_result.json](evidence/cumulative_result.json)
- Command/provenance: [Reproduce](#/reproduce)
