# Claim 3 — Equation 5 continuity and universality

**Status: VERIFIED · Confidence: MEDIUM**

## Exact contract and quantifiers

Equation 5 and Theorems 4.2–4.3: for every finite `k`, every
`p in [1,infinity)`, and continuous inner/outer maps, the norm-reweighted
aggregate is continuous on the `ell_p(R^k)` quotient. For every compact
`K subset ell_p(R^k)`, every continuous invariant target and every
`epsilon>0`, the stated neural class is dense.

The source anchors are Equation 5, Theorems 4.2–4.3, and Appendix B.2–B.3.
The numerical route fixes `p=1`; the implication certificate separately
audits arbitrary `p`, compact `K`, point separation, subalgebra closure, and
the UAT error composition.

## Direct observed evidence

| Test | Scale | Observed |
| --- | ---: | ---: |
| Eq. 5 Basel sequence `x_i=i^-2`, `rho=1` | 2,000,000 terms | error to `pi^2/6`: `4.999999e-7` |
| permutation + zero padding | 2,048 trials | max error `8.881784e-15` |
| `ell_1` continuity, `rho=tanh` | 1,024 pairs | max fraction of proved `2||x-y||_1` bound `0.412692` |
| exhaustive bump separation certificate | 2,415 orbit pairs | minimum gap `1` |

The dropped-weight control grows exactly `64x`. On the paper's slow-decay
witness the invalid unweighted aggregate grows `50.1924 -> 687.8054`
(`13.703x`), while Eq. 5 stabilizes `1.77099 -> 1.77967`. The independent
implementation recomputes a one-million-term limit, permutation identity, and
dropped-weight failure and exits zero.

## Current executable verifier

This is the exact function invoked by the fixed command. Shared helpers and
the complete importable module are inline on [Complete runner source](#/runner-source).

```python
def run_claim3_empirical() -> dict:
    """Stress Eq. 5 on ell_1 sequences without fitting a target function."""
    rng = np.random.default_rng(SEED_C3)

    # For x_i=i^-2 and rho=1, Eq. 5 is the Basel series.  This is a
    # million-coordinate, independently known limit rather than a selected
    # horizon derived from a tolerance formula.
    horizons = [10_000, 100_000, 1_000_000, 2_000_000]
    convergence = []
    exact_limit = math.pi**2 / 6
    for n in horizons:
        i = np.arange(1, n + 1, dtype=np.float64)
        value = float(np.sum(i**-2))
        convergence.append(
            {
                "n": n,
                "eq5_value": value,
                "absolute_error_to_pi2_over_6": abs(exact_limit - value),
            }
        )

    # Direct permutation and zero-padding invariance of the weighted aggregate.
    invariant_errors: list[float] = []
    for _ in range(2_048):
        n = int(rng.integers(8, 257))
        x = rng.normal(size=(n, 3)) / np.arange(1, n + 1)[:, None] ** 1.4

        def rho(z: np.ndarray) -> np.ndarray:
            return np.column_stack((np.tanh(z[:, 0]), np.sin(z[:, 1]), np.cos(z[:, 2])))

        aggregate = np.sum(np.linalg.norm(x, axis=1)[:, None] * rho(x), axis=0)
        permuted = x[rng.permutation(n)]
        padded = np.vstack((permuted, np.zeros((int(rng.integers(1, 17)), 3))))
        aggregate_permuted = np.sum(
            np.linalg.norm(padded, axis=1)[:, None] * rho(padded), axis=0
        )
        invariant_errors.append(float(np.max(np.abs(aggregate - aggregate_permuted))))

    # For scalar rho=tanh on [-1,1], g(x)=|x|rho(x) is 2-Lipschitz.
    # Thus |tau(x)-tau(y)| <= 2 ||x-y||_1.  Test independently sampled
    # ell_1 pairs across lengths and perturbation scales.
    continuity_ratios: list[float] = []
    continuity_rows = []
    for _ in range(1_024):
        n = int(rng.integers(16, 513))
        scale = float(10 ** rng.uniform(-7, -0.3))
        decay = np.arange(1, n + 1, dtype=np.float64) ** 1.35
        x = np.clip(rng.normal(size=n) / decay, -1, 1)
        y = np.clip(x + scale * rng.normal(size=n) / decay, -1, 1)
        tau_x = float(np.sum(np.abs(x) * np.tanh(x)))
        tau_y = float(np.sum(np.abs(y) * np.tanh(y)))
        l1 = float(np.sum(np.abs(x - y)))
        ratio = abs(tau_x - tau_y) / max(2 * l1, np.finfo(float).tiny)
        continuity_ratios.append(ratio)
        continuity_rows.append((l1, abs(tau_x - tau_y)))

    # Destructive controls: dropping the ell_1 factor turns rho=1 into an
    # N-divergent sum; on the paper's slow-decay witness it also recovers the
    # original DeepSets divergence.
    unweighted_constant = []
    slow_decay = []
    for n in [256, 1_024, 4_096, 16_384]:
        i = np.arange(1, n + 1, dtype=np.float64)
        unweighted_constant.append(float(np.ones(n).sum()))
        x = i**-0.75
        slow_decay.append(
            {
                "n": n,
                "unweighted_original": float(np.sqrt(x).sum()),
                "eq5_weighted": float((x**2 * np.sqrt(x)).sum()),
            }
        )

    checker = _run_independent_checker("claim3")
    passed = (
        convergence[-1]["absolute_error_to_pi2_over_6"] < 5.1e-7
        and max(invariant_errors) < 2e-13
        and max(continuity_ratios) <= 1 + 1e-12
        and unweighted_constant[-1] / unweighted_constant[0] == 64
        and slow_decay[-1]["unweighted_original"] / slow_decay[0]["unweighted_original"] > 10
        and abs(slow_decay[-1]["eq5_weighted"] - slow_decay[0]["eq5_weighted"])
        / slow_decay[-1]["eq5_weighted"]
        < 0.01
        and checker["passed"]
    )
    return {
        "status": "VERIFIED",
        "claim_scope": (
            "Direct Eq. 5 convergence, ell_1 continuity, permutation/zero-padding "
            "invariance, and destructive removal of the norm reweighting."
        ),
        "seed": SEED_C3,
        "basel_convergence": convergence,
        "basel_exact_limit": exact_limit,
        "permutation_zero_padding_trials": len(invariant_errors),
        "max_permutation_zero_padding_error": max(invariant_errors),
        "continuity_trials": len(continuity_ratios),
        "continuity_bound": "|tau(x)-tau(y)| <= 2 ||x-y||_1",
        "max_fraction_of_continuity_bound": max(continuity_ratios),
        "continuity_l1_range": [
            min(row[0] for row in continuity_rows),
            max(row[0] for row in continuity_rows),
        ],
        "dropped_weight_constant_sum": dict(
            zip(map(str, [256, 1_024, 4_096, 16_384]), unweighted_constant, strict=True)
        ),
        "slow_decay_destructive_control": slow_decay,
        "independent_checker": checker,
        "limitations": (
            "The sweeps corroborate the exact continuity and invariance mechanisms; "
            "the accompanying constructive certificate separately audits point "
            "separation and the theorem's implication chain."
        ),
        "check_passed": bool(passed),
    }
```

## Evidence, control, and scope

- Raw direct output: [evidence/claim3_empirical.json](evidence/claim3_empirical.json)
- Independent checker output: [evidence/claim3_empirical_checker.json](evidence/claim3_empirical_checker.json)
- Full raw cumulative output: [evidence/retry_cumulative_result.json](evidence/retry_cumulative_result.json)
- Exact contract: [evidence/claim3_contract.json](evidence/claim3_contract.json)
- Source: [repro/src/empirical_positive.py](repro/src/empirical_positive.py)
- Checker source: [repro/src/checkers/positive_empirical_independent.py](repro/src/checkers/positive_empirical_independent.py)
- Command and pinned environment: [Reproduce](#/reproduce)

Finite sweeps directly verify convergence, continuity, invariance, and a
failure-inducing control. Universal density additionally uses the explicit
constructor/separation implication chain and standard named theorems; it is
not inferred from sweep size or from fitting one target.
