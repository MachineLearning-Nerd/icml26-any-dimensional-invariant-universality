# Claim 5 method — current direct route

The primary retry verifier computes exact cut norms by exhaustive subset
optimization for 500 pairs of symmetric seven-block graphons. It evaluates
five separately implemented motifs, 500 relabelings, and Equation 9's 0/1
parametrization on 64 graphons. The same-edge/different-triangle pair and a
tight constant-kernel perturbation are destructive/calibration controls.

The secondary proof certificate expands every Equation 9 edge factor over the Boolean
lattice of the complete graph. Every term is square-free, hence a simple-graph
homomorphism density. The target parameter choice imposes both
`E(F) subset S` and `S subset E(F)`, leaving exactly `S=E(F)`.

That certificate:

- symbolically expands all 64 terms for a generic four-vertex model;
- applies the arbitrary-`m` bit-constraint derivation;
- exhausts every labeled simple graph for `2 <= m <= 6` (33,866 total);
- checks target and generic expansions on rational three-block graphons;
- checks relabeling and cut-continuity instances for four motifs;
- calls an exact checker that shares no certificate code.

The destructive mutation repeats an edge factor. A valid simple-edge
integrand is multilinear in every edge variable, while the mutation has
nonzero second derivative/finite difference and must be rejected.
