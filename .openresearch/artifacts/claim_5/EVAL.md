# Evaluator instructions

Run:

```text
uv run --frozen python repro/src/verify.py
```

Require zero exit, `CLAIM 5 INDEPENDENT CHECKER`, Claim 5 `VERIFIED`, and
`CUMULATIVE REGRESSION PASS`. Confirm that 33,866 labeled graphs were
exhausted, every rational comparison is exact, and the repeated-edge mutation
has a nonzero second derivative/finite difference.
