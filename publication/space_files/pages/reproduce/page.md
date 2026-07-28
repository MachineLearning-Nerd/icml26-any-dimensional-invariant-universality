# Reproduce and inspect

## Fixed command

```text
uv run --frozen python repro/src/verify.py
```

The verifier writes `outputs/verdict.json`, prints the complete result, calls
three independent checkers, and exits nonzero if any claim or control fails.

## Pinned source

- [Top-level verifier](repro/src/verify.py)
- [Claim 3 certificate](repro/src/certificates/claim3.py)
- [Claim 4 certificate](repro/src/certificates/claim4.py)
- [Claim 5 certificate](repro/src/certificates/claim5.py)
- [Claim 3 independent checker](repro/src/checkers/claim3_independent.py)
- [Claim 4 independent checker](repro/src/checkers/claim4_independent.py)
- [Claim 5 independent checker](repro/src/checkers/claim5_independent.py)
- [pyproject.toml](pyproject.toml)
- [uv.lock](uv.lock)

Git commit: `a63d9eaeb0fe8eaf4dd94a5c1f6ffdec93050bd5`

`uv.lock` SHA-256: shown in [upload manifest](release/upload_manifest.sha256)

## Raw evidence

- [Cumulative result](evidence/cumulative_result.json)
- [Claim 3 checker output](evidence/claim3_checker.json)
- [Claim 4 checker output](evidence/claim4_checker.json)
- [Claim 5 checker output](evidence/claim5_checker.json)
- [Claim 3 contract](evidence/claim3_contract.json)
- [Claim 4 contract](evidence/claim4_contract.json)
- [Claim 5 contract](evidence/claim5_contract.json)

## Compute

Formal runs used Hugging Face `cpu-upgrade`, never GPU. The winning cumulative
run exposed 64 logical CPUs but enforced one thread in both OpenBLAS pools.
Algorithm estimate: one core. Verifier runtime: 5.294494 s. Total HF job
duration: 26 s. Cold-start/install overhead accounts for the difference.

Seeds: 7, 260523156, 260523157, 260523158.

Python: 3.12.12. NumPy: 2.4.6. SciPy: 1.17.1. SymPy: 1.14.0.

## Source provenance

Paper HTML retrieved 2026-07-28 from
`https://ar5iv.labs.arxiv.org/html/2605.23156`; SHA-256
`08550eb2200d91fcba610f1008e7cb0e207049aee014b5d31f9f5501d6cda5f3`.
ArXiv source archive SHA-256:
`86929d4f4e75744d3ce0bc8c100003febd6bb4130a85d1faa2414c02db5aae0b`.
