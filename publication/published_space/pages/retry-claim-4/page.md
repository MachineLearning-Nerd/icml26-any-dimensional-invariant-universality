# Claim 4 — Equation 6 Wasserstein universality

**Status: VERIFIED · Confidence: MEDIUM**

## Exact contract and quantifiers

Equations 6 and Theorems 4.5–4.6: integration of every continuous
componentwise `p`-growth inner map followed by a continuous outer map is
`W_p`-continuous. On every compact `Q subset P_p(R^k)`, the stated neural
family is dense for every continuous target and `epsilon>0`, under the
paper's activation assumptions.

The source anchors are Equations 6, Theorems 4.5–4.6, and Appendix B.4–B.5.
The direct route uses `p=1`, one-dimensional empirical measures, exact `W1`,
and `rho=tanh`, whose Lipschitz constant is one.

## Direct observed evidence

| Test | Scale | Observed |
| --- | ---: | ---: |
| exact 1D Wasserstein pairs | 4,096 | max integral-gap/`W1` ratio `0.760925 <= 1` |
| permutation invariance | 2,048 | max error `1.554312e-15` |
| equal-mean measure separation | one exact control | `0.5` versus `0` |
| exhaustive rational separation certificate | 2,415 measure pairs | minimum exact gap `1/4` |

The destructive control violates the required linear-growth condition with
`rho(x)=x^2`. For
`mu_n=(1-n^-2)delta_0+n^-2 delta_n`, exact `W1(mu_n,delta_0)` falls
`0.1 -> 0.0001`, but the invalid quadratic integral remains exactly `1`.
The independent checker recomputes continuity, separation, and this failure.

## Current executable verifier

```python
def run_claim4_empirical() -> dict:
    """Stress Eq. 6 with exact one-dimensional W_1 distances."""
    rng = np.random.default_rng(SEED_C4)
    ratios: list[float] = []
    pair_rows = []
    for _ in range(4_096):
        n = int(rng.integers(8, 257))
        x = rng.normal(size=n)
        perturbation_scale = float(10 ** rng.uniform(-7, 0))
        y = x + perturbation_scale * rng.normal(size=n)
        w1 = float(wasserstein_distance(x, y))
        integral_gap = float(abs(np.tanh(x).mean() - np.tanh(y).mean()))
        ratio = integral_gap / max(w1, np.finfo(float).tiny)
        ratios.append(ratio)
        pair_rows.append((w1, integral_gap))

    permutation_errors: list[float] = []
    for _ in range(2_048):
        n = int(rng.integers(8, 513))
        x = rng.normal(size=n)
        before = float(np.mean(np.column_stack((np.tanh(x), np.cos(x))), axis=0).sum())
        perm = rng.permutation(n)
        after = float(np.mean(np.column_stack((np.tanh(x[perm]), np.cos(x[perm]))), axis=0).sum())
        permutation_errors.append(abs(before - after))

    # Bounded continuous functions separate measures even when their means
    # agree: 1/2(delta_-1+delta_1) and delta_0 both have mean zero.
    mu = np.array([-1.0, 1.0])
    nu = np.array([0.0])
    rho = lambda z: z**2 / (1 + z**2)
    separation = [float(np.mean(rho(mu))), float(np.mean(rho(nu)))]

    # Destructive growth control for p=1: rho(x)=x^2 violates the allowed
    # linear growth.  mu_n=(1-n^-2)delta_0+n^-2 delta_n tends to delta_0 in W1
    # while its rho integral remains exactly one.
    growth_control = []
    for n in [10, 100, 1_000, 10_000]:
        mass = n**-2
        growth_control.append(
            {
                "n": n,
                "W1_to_delta0": mass * n,
                "quadratic_integral": mass * n**2,
            }
        )

    checker = _run_independent_checker("claim4")
    passed = (
        max(ratios) <= 1 + 1e-12
        and max(permutation_errors) < 2e-15
        and abs(separation[0] - separation[1]) > 0.4
        and growth_control[-1]["W1_to_delta0"] < 2e-4
        and all(abs(row["quadratic_integral"] - 1) < 1e-15 for row in growth_control)
        and checker["passed"]
    )
    return {
        "status": "VERIFIED",
        "claim_scope": (
            "Direct Eq. 6 W_1 continuity for a 1-Lipschitz integrand, measure "
            "invariance and separation, plus a destructive p-growth violation."
        ),
        "seed": SEED_C4,
        "wasserstein_pairs": len(ratios),
        "max_Kantorovich_Rubinstein_ratio": max(ratios),
        "wasserstein_range": [
            min(row[0] for row in pair_rows),
            max(row[0] for row in pair_rows),
        ],
        "permutation_trials": len(permutation_errors),
        "max_permutation_error": max(permutation_errors),
        "equal_mean_measure_separation_values": separation,
        "growth_violation_control": growth_control,
        "independent_checker": checker,
        "limitations": (
            "The finite stress test targets the theorem's quantitative continuity "
            "mechanism; the accompanying constructive certificate separately "
            "exhausts a finite measure domain and audits the implication chain."
        ),
        "check_passed": bool(passed),
    }
```

The shared helpers and complete module are inline on
[Complete runner source](#/runner-source).

## Evidence, control, and scope

- Raw direct output: [evidence/claim4_empirical.json](evidence/claim4_empirical.json)
- Independent checker output: [evidence/claim4_empirical_checker.json](evidence/claim4_empirical_checker.json)
- Full raw cumulative output: [evidence/retry_cumulative_result.json](evidence/retry_cumulative_result.json)
- Exact contract: [evidence/claim4_contract.json](evidence/claim4_contract.json)
- Source: [repro/src/empirical_positive.py](repro/src/empirical_positive.py)
- Checker source: [repro/src/checkers/positive_empirical_independent.py](repro/src/checkers/positive_empirical_independent.py)
- Command and pinned environment: [Reproduce](#/reproduce)

The finite sweep does not infer density. The universal conclusion uses the
separate explicit measure-separation/subalgebra/error-budget chain. The
paper's literal activation examples remain interpretation-sensitive; leaky
ReLU is the certificate's unambiguous assumption-satisfying witness.
