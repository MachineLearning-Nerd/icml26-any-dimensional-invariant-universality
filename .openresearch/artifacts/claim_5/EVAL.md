# Evaluator instructions

Run:

```text
uv run --frozen python repro/src/verify.py
```

Require zero exit, Claim 5 `VERIFIED`, and `CUMULATIVE REGRESSION PASS`.
Inspect `primary_empirical_verification`: 500 exact-cut pairs across five
motifs, 500 relabelings, 64 Eq. 9/direct comparisons, same edge gap zero with
triangle gap `0.09375`, tight edge/cut ratio one, and an independent checker
exit of zero. The 33,866-graph certificate remains supporting evidence.
