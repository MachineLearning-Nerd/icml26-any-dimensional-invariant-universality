# Claim 4 source audit

Paper source and hashes are identical to the Claim 3 source audit. The relevant
anchors are Equation 6, Theorems 4.5–4.6, and Appendix B.4–B.5.

The continuity claim quantifies over every `p in [1,infinity)`, every finite
`k`, every continuous componentwise `p`-growth integrand `rho`, and every
continuous outer map `sigma`. The universality claim quantifies over every
compact `Q subset P_p(R^k)`, every continuous target on `Q`, every positive
accuracy, and every activation satisfying all four written activation
assumptions.

The noncompact UAT premise was independently checked against van Nuland,
*Noncompact uniform universal approximation*, Neural Networks 173 (2024)
106181, arXiv:2308.03812v2. It states that `C_0(R^k)` is uniformly
approximable by one-hidden-layer networks under the cited activation
conditions.

The paper's literal ratio-to-polynomial definition is ambiguous for activations
that tend to zero at one end, despite listing ReLU, Softplus, and Sigmoid.
The certificate uses leaky ReLU, with asymptotes `0.1t` and `t`, because it
unambiguously satisfies the written assumptions. This caveat does not broaden
the theorem contract.
