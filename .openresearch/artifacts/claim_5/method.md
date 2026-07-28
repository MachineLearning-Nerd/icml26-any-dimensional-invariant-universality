# Claim 5 method

The proof certificate expands every Equation 9 edge factor over the Boolean
lattice of the complete graph. Every term is square-free, hence a simple-graph
homomorphism density. The target parameter choice imposes both
`E(F) subset S` and `S subset E(F)`, leaving exactly `S=E(F)`.

The implementation:

- symbolically expands all 64 terms for a generic four-vertex model;
- applies the arbitrary-`m` bit-constraint derivation;
- exhausts every labeled simple graph for `2 <= m <= 6` (33,866 total);
- checks target and generic expansions on rational three-block graphons;
- checks relabeling and cut-continuity instances for four motifs;
- calls an exact checker that shares no certificate code.

The destructive mutation repeats an edge factor. A valid simple-edge
integrand is multilinear in every edge variable, while the mutation has
nonzero second derivative/finite difference and must be rejected.
