# Claim 3 limitations and deviations

- The result is a machine-checkable implication certificate, not a formal
  Lean/Coq proof.
- Compactness in `ell_p`, the uniform-limit theorem, real
  Stone-Weierstrass, and the Leshno neural UAT are declared external premises.
- Finite exhaustive and randomized instances test the implementation but do
  not by themselves prove the universal theorem.
- The certificate strengthens the paper's written UAT step by enlarging the
  compact outer approximation domain to contain perturbed aggregates.
- No GPU is used. Numerical libraries are restricted to one math thread.
