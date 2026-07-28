# Claim 5 — homomorphism-density graphon basis

**Status: VERIFIED · Confidence: HIGH**

## Exact contract and quantifiers

Equations 9–10 and Theorems 4.9–4.10: for every finite `m>=2`, Equation 9
expands only into simple-graph homomorphism densities and is cut-continuous.
For every finite simple graph `F`, its density `t(F,.)` belongs to the model
class. Consequently the class is dense in continuous functions on compact
`[0,1]`-valued graphon space.

Declared premises: graphon compactness; Borgs et al. (2008), Theorem 2.7,
for cut-continuity; Diao et al. (2015), Theorem 2.2, for density of the simple
homomorphism-density span.

## Arbitrary-m certificate

Distributivity gives

```text
prod_e(a_e W_e+b_e)
= sum_{S subset E_m} (prod_{e in S}a_e)(prod_{e notin S}b_e) prod_{e in S}W_e.
```

Every monomial is square-free, hence represents a simple graph. For target
`F`, set `(a_e,b_e)=(1,0)` on `E(F)` and `(0,1)` off it. A surviving subset
must satisfy both `E(F) subset S` and `S subset E(F)`, so exactly
`S=E(F)` survives. Isolated vertices integrate to one.

## Evidence and controls

- Generic four-vertex symbolic expansion: 64 terms, residual exactly `0`.
- Exhaustive labeled graphs: `2 + 8 + 64 + 1,024 + 32,768 = 33,866` for
  `m=2..6`; every target isolated exactly.
- 32 target and two generic expansions on rational three-block graphons:
  exact fractional equality.
- Four relabeling checks: exact zero error.
- Independent exact checker: 442 step-graphon cases, exit 0.
- Repeated-edge mutation: valid simple integrands have second derivative `0`
  in each edge variable; the mutation has derivative `2` and exact second
  finite difference `2/9`, so it is rejected.

The finite sweep is corroboration. Universal scope comes from the arbitrary-m
Boolean constraint and primary density theorem.

- Source: [repro/src/certificates/claim5.py](repro/src/certificates/claim5.py)
- Independent checker: [repro/src/checkers/claim5_independent.py](repro/src/checkers/claim5_independent.py)
- Contract: [evidence/claim5_contract.json](evidence/claim5_contract.json)
- Raw checker: [evidence/claim5_checker.json](evidence/claim5_checker.json)
- Raw cumulative result: [evidence/cumulative_result.json](evidence/cumulative_result.json)
- Command/provenance: [Reproduce](#/reproduce)
