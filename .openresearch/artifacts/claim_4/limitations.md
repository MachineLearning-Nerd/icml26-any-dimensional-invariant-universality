# Claim 4 limitations and deviations

- This is an executable implication certificate, not a proof-assistant
  formalization.
- Wasserstein convergence, regularity/Urysohn separation, compactness,
  Stone-Weierstrass, and the noncompact UAT are declared standard premises.
- Finite atomic sweeps corroborate the constructors and checker; they are not
  presented as proof of universality.
- The certificate records an ambiguity in the paper's activation examples and
  uses leaky ReLU as an assumption-satisfying witness.
- No GPU is used and all numerical libraries are restricted to one thread.
