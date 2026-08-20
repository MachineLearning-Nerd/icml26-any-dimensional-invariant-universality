# Reproduction environment

Dependencies are pinned by [`pyproject.toml`](pyproject.toml) and [`uv.lock`](uv.lock). The cumulative command is:

```bash
uv sync --frozen
uv run --frozen python repro/src/verify.py
```

Recorded retry environment:

| Component | Value |
| --- | --- |
| Python | `3.12.12` |
| Platform | Linux x86_64 |
| Backend | Hugging Face `cpu-upgrade` |
| Math threads | 1 |
| GPU | None required |
| Claim 3 direct retry | 4,096 exact `W_1` pairs and 2,048 invariance trials |
| Claim 5/6 direct retry | 33,866 graph labels and 2,512 orbit/group trials |

The notebook opens with embedded evidence and does not require expensive regeneration. The committed raw evidence, protected manifests, and retry subset checks are verified by [`verify_final.py`](verify_final.py).
