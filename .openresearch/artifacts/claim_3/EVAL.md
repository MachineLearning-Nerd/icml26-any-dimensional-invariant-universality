# Evaluator instructions

Run:

```text
uv run --frozen python repro/src/verify.py
```

The command must exit zero, print `CLAIM 3 INDEPENDENT CHECKER`, label Claim 3
`VERIFIED`, and finish with `CUMULATIVE REGRESSION PASS`. Inspect:

- `raw/claim3_certificate.json`
- `raw/independent_checker.json`
- the baseline `outputs/verdict.json`

Mutation controls are successful only when the wrong product constructor,
unweighted divergent aggregate, and excessive inner error are rejected.
