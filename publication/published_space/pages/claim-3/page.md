# Claim 3 — Equation 5 continuity and universality

**Status: VERIFIED · Confidence: HIGH**

## Exact contract and quantifiers

Equation 5 and Theorems 4.2–4.3: for every finite `k`, every
`p in [1,infinity)`, and continuous `rho,sigma`, the weighted aggregate is
continuous on the `ell_p(R^k)` quotient. For every compact
`K subset ell_p(R^k)`, every continuous target on `K/G_infinity`, every
positive accuracy, and every continuous nonpolynomial activation, the neural
class is dense.

Declared premises: compactness/uniform-tail characterization in `ell_p`,
uniform-limit theorem, Leshno compact-set UAT, and real Stone-Weierstrass.

## Machine-checkable implication chain

1. `||tau(X)-tau_N(X)|| <= M_rho sum_{i>=N}||X_i||^p`; compactness makes the
   right side uniformly vanish.
2. Explicit latent concatenation plus outer scalar/add/product maps forms a
   unital subalgebra.
3. Distinct quotient points have a differing nonzero multiplicity isolated
   by a continuous bump.
4. Stone-Weierstrass makes the continuous class dense.
5. Inner UAT error `delta/B` gives aggregate error `delta`; outer approximation
   and uniform continuity contribute `epsilon/2` each.

The certificate repairs a minor written-proof omission by applying outer UAT
on a compact closed `delta`-neighborhood containing both true and perturbed
aggregates.

## Evidence and controls

- 128 deterministic constructor/invariance instances: maximum valid error
  `4.44e-16`.
- 2,415 distinct finite-domain orbit pairs: every pair separated; minimum gap
  `1`.
- Uniform-tail maximum actual/bound ratio: `0.710037`.
- Unweighted control on the divergence witness grows `13.703378×`.
- Wrong addition-for-product mutation: minimum observed error `0.0289585`;
  symbolic residual is nonzero.
- Doubled inner UAT budget yields `2 delta`, not `delta`.
- Independent exact-rational checker: 1,540 orbit pairs, 1,024 constructor
  cases, 1,024 mutation rejections, exit 0.

This is not a one-target fit. Finite sweeps are regression checks; the
universal verdict comes from the implication certificate and named premises.

- Source: [repro/src/certificates/claim3.py](repro/src/certificates/claim3.py)
- Independent checker: [repro/src/checkers/claim3_independent.py](repro/src/checkers/claim3_independent.py)
- Contract: [evidence/claim3_contract.json](evidence/claim3_contract.json)
- Raw checker: [evidence/claim3_checker.json](evidence/claim3_checker.json)
- Raw cumulative result: [evidence/cumulative_result.json](evidence/cumulative_result.json)
- Command/provenance: [Reproduce](#/reproduce)
