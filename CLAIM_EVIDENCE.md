# Claim-to-evidence ledger

Every claim follows:

`paper anchor → exact claim contract → executable certificate or witness → independent checker/control → raw evidence → cumulative verifier → report`

| Claim | Paper surface | How the claim is produced | Current result | Boundary |
| --- | --- | --- | --- | --- |
| C1 | Theorem 4.2, original Equation 4 aggregation | Evaluate `X_i=i^-0.75` in `ell_2` with `rho(x)=sqrt(|x|)`, compare divergent partial sums with the weighted repair. | 64× horizon growth ratio `13.743989`; weighted change `0.604959%`. | One exact assumption-satisfying witness is sufficient for the failure mechanism. |
| C2 | Theorem 4.9, nonlinear cut-norm discontinuity | Use `W_n=n 1_[0,1/n]^2` and check `||W_n||_cut=1/n`, `||W_n^2||_cut=1`, and `||3W_n||_cut=3/n`. | Spike identities pass for six `n` values. | The theorem supplies the full classification; the audit checks the decisive witness/control. |
| C3 | Equations 5, Theorems 4.2–4.3 | Build the uniform-tail, algebra, separator, and neural-error implication certificate; independently check rational constructors, continuity, invariance, and Basel convergence. | Certificate and direct checks pass; 128 constructor instances, 2,415 orbit pairs, and 2,000,000-term Basel check. | Named compactness, uniform-limit, UAT, and Stone–Weierstrass results are premises; outer-domain repair is explicit. |
| C4 | Equation 6, Theorems 4.5–4.6 | Combine Wasserstein continuity, measure separation, compact tail truncation, and global `C_0` UAT; independently check exact transport and invalid growth controls. | Certificate and direct checks pass; 4,096 exact `W_1` pairs and 2,048 invariance trials in retry. | Leaky ReLU is used for the literal growth interpretation; no proof assistant formalization. |
| C5 | Equations 9–10, Theorems 4.9–4.10 | Prove the arbitrary-`m` Boolean-lattice expansion isolates every finite simple graph; check exact rational graphons and repeated-edge mutations. | 33,866 labeled simple graphs through six vertices; symbolic residual `0`; exact-cut retry passes. | Universal step is the symbolic arbitrary-`m` argument, not only finite enumeration. |
| C6 | Equations 12 and 14, Theorems 4.12–4.13 | Check radius Lipschitz bound, Gram invariance, orthogonal recovery, and distinct-Gram control with independent point-cloud trials. | 2,512 retry group/Lipschitz/recovery trials; nonorthogonal shear control gap nonzero. | Invariant-network density is a named premise, not a proof-kernel object. |

## Branch lineage

- `historical/judged-baseline-9-of-12` preserves the earlier 9/12 record.
- `release/8-of-12-retry`, `release/final-retry-gates`, and the published mirrors preserve the 8/12 retry and release gates.
- `audit/c3-eq5-proof` and `audit/c3-c4-direct-verification` produce/check C3.
- `audit/c4-eq6-wasserstein` and `audit/c3-c4-direct-verification` produce/check C4.
- `audit/c5-graphon-basis` and `audit/c5-c6-direct-verification` produce/check C5.
- `audit/c5-c6-direct-verification` produces/checks C6.

The complete old-to-new mapping is in [`branch-audit.md`](branch-audit.md).
