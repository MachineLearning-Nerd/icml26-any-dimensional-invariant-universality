# Any-dimensional invariant universality — reproduction workspace

Paper: arXiv 2605.23156 / OpenReview wRVTDcEMv8.

This branch reconstructs the immutable 9/12 judged baseline before stronger
claim-by-claim evidence is added on child experiment branches.

Fixed experiment command:

```bash
uv run --frozen python repro/src/verify.py
```

The baseline deliberately preserves the live judge's distinction between three
full-credit claims (1, 2, and 6) and three toy-level universality checks (3–5).
Passing this regression suite does not upgrade those historical verdicts.
