# Evaluator instructions

Run the inherited fixed command:

```text
uv run --frozen python repro/src/verify.py
```

Require zero exit, `CLAIM 4 INDEPENDENT CHECKER`, Claim 4 status `VERIFIED`,
and `CUMULATIVE REGRESSION PASS`. The raw JSON files are generated in `raw/`.
The exponential-growth control must diverge while `W_2` tends to zero; the
mutated constructor and doubled tail budget must both be rejected.
