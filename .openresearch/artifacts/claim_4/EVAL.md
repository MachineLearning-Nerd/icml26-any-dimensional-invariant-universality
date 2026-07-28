# Evaluator instructions

Run the inherited fixed command:

```text
uv run --frozen python repro/src/verify.py
```

Require zero exit, Claim 4 status `VERIFIED`, and `CUMULATIVE REGRESSION PASS`.
The `primary_empirical_verification` object must show 4,096 exact-Wasserstein
pairs with maximum ratio at most one, 2,048 invariant permutations, nonzero
measure separation, and the destructive quadratic integral fixed at one as
`W1` reaches `1e-4`. The direct independent checker must exit zero.
