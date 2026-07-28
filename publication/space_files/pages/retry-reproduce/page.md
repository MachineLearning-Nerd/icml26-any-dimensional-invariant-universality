# Reproduce and inspect

## Fixed command

```text
uv run --frozen python repro/src/verify.py
```

The command writes `outputs/verdict.json`, prints the complete six-claim
result, invokes independent checkers, and exits nonzero if any current
contract or destructive control fails.

## Pinned source and environment

- [Top-level verifier](repro/src/verify.py)
- [Direct Claims 3–6 runner](repro/src/empirical_positive.py)
- [Independent direct checker](repro/src/checkers/positive_empirical_independent.py)
- [Complete source inline](#/runner-source)
- [pyproject.toml](pyproject.toml)
- [uv.lock](uv.lock)

Git commit: `8e6d43cd67ef70ba8511358b84b3d856853a7f65`

## Raw evidence

- [Cumulative result](evidence/retry_cumulative_result.json)
- [Claim 3 direct result](evidence/claim3_empirical.json) and [checker](evidence/claim3_empirical_checker.json)
- [Claim 4 direct result](evidence/claim4_empirical.json) and [checker](evidence/claim4_empirical_checker.json)
- [Claim 5 direct result](evidence/claim5_empirical.json) and [checker](evidence/claim5_empirical_checker.json)
- [Claim 6 direct result](evidence/claim6_empirical.json) and [checker](evidence/claim6_empirical_checker.json)

## Compute and provenance

Formal run `c68cbf81-62df-4541-b09b-29208f32540d` used Hugging Face
`cpu-upgrade`, never GPU. Estimate: one algorithmic core. Actual allocation:
64 logical CPUs visible; both OpenBLAS pools enforced one thread. Program
runtime: 11.082165 s; total job duration: 32 s.

Seeds: `7`, `260523159`, `260523160`, `260523161`, `260523162`.

Python 3.12.12; NumPy 2.4.6; SciPy 1.17.1; SymPy 1.14.0.

Paper HTML was retrieved 2026-07-28 from
`https://ar5iv.labs.arxiv.org/html/2605.23156`; SHA-256
`08550eb2200d91fcba610f1008e7cb0e207049aee014b5d31f9f5501d6cda5f3`.
ArXiv source archive SHA-256:
`86929d4f4e75744d3ce0bc8c100003febd6bb4130a85d1faa2414c02db5aae0b`.
