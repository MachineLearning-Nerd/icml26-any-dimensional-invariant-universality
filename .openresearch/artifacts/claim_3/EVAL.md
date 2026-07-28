# Evaluator instructions

Run:

```text
uv run --frozen python repro/src/verify.py
```

The command must exit zero, print the direct Claim 3 checker result, label
Claim 3 `VERIFIED`, and finish with `CUMULATIVE REGRESSION PASS`. Inspect the
`primary_empirical_verification` object in `outputs/verdict.json`; require:

- 2,000,000-term absolute error below `5.1e-7`;
- 2,048 invariance trials below `2e-13`;
- 1,024 continuity trials within the analytic bound;
- both dropped-weight controls to diverge;
- the independent direct checker to exit zero.

The older certificate outputs remain supporting evidence.
