# Evaluator instructions

Run:

```text
uv run --frozen python repro/src/verify.py
```

Require zero exit, Claim 6 `VERIFIED`, and `CUMULATIVE REGRESSION PASS`.
Inspect `primary_empirical_verification`: 1,000 group-action trials, 1,000
Lipschitz trials below `1/R`, 512 orbit recoveries, a nonorthogonal shear
detected by both Gram and readout, and an independent checker exit of zero.
