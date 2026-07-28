# Claim 3 source audit

Source: `https://ar5iv.labs.arxiv.org/html/2605.23156`, retrieved 2026-07-28
with an explicit browser User-Agent. HTML SHA-256:
`08550eb2200d91fcba610f1008e7cb0e207049aee014b5d31f9f5501d6cda5f3`.
The arXiv source archive SHA-256 is
`86929d4f4e75744d3ce0bc8c100003febd6bb4130a85d1faa2414c02db5aae0b`.

## Exact scope

Equation 5 maps an `ell_p(R^k)` sequence `X` to
`sigma(sum_i ||X_i||^p rho(X_i))`. Theorem 4.2 asserts continuity in the
symmetrized metric when `rho` and `sigma` are continuous. Theorem 4.3 asserts
that, for every compact `K subset ell_p(R^k)`, the neural family is dense in
`C(K/G_infinity)` whenever the activation is continuous and non-polynomial.

The quantifiers are every finite `k`, every `p in [1,infinity)`, every compact
`K`, every continuous target on the quotient, and every positive accuracy.
This is not a finite-data or fixed-target claim.

## Proof anchors and premises

- Proposition 4.1: compactness in `ell_p` is equivalent to closedness,
  boundedness, and uniform tail decay.
- Appendix B.2: the aggregate is a uniform limit of continuous finite sums.
- Appendix B.3, Lemma B.3: concatenation supplies addition and product
  constructors.
- Appendix B.3, Claim B.4 and Lemma B.5: differing nonzero multiplicities are
  isolated by a continuous bump.
- Appendix B.3, Lemma B.6: compact-set UAT for `rho` and `sigma`.
- Real Stone-Weierstrass and Leshno et al. (1993) are explicit external
  premises.

## Independently identified proof detail

The paper approximates `sigma` on the true aggregate image, then evaluates the
approximating network at a perturbed aggregate. The certificate closes this
minor domain omission by taking the compact closed `delta`-neighborhood of the
true aggregate image before applying the outer UAT and uniform continuity.
