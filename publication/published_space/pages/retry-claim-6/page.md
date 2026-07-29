# Claim 6 — Gram map and point-cloud orbits

**Status: VERIFIED · Confidence: MEDIUM**

## Exact contract and quantifiers

Equations 12 and 14 and Theorems 4.12–4.13: on radius-`R` point clouds, the
normalized Gram graphon is Lipschitz, invariant to simultaneous orthogonal
action and permutation, determines the orbit, and permits invariant graphon
readouts to transfer universality to bounded point-cloud orbits.

The source anchors are Equations 12 and 14, Theorems 4.12–4.13, and Appendix
E. The direct tests use `R=2`, varying cloud sizes and dimensions `k=2..5`.

## Direct observed evidence

| Test | Scale | Observed |
| --- | ---: | ---: |
| orthogonal + permutation Gram action | 1,000 clouds | max error `4.440892e-16` |
| five hom-density two-stage readouts | same 1,000 | max action error `1.443290e-15` |
| Gram Lipschitz ratio | 1,000 pairs | max `0.178517 <= 1/R = 0.5` |
| orbit completeness recovery | 512 full-rank pairs | max recovery `6.730727e-15` |
| recovered transform orthogonality | same 512 | max error `1.030874e-14` |

The destructive control applies a non-orthogonal shear. Its orthogonality gap
is `0.24`, Gram gap `0.0215174`, and five-coordinate hom-density readout gap
`0.000240004`: the invariant architecture correctly rejects it as a distinct
orbit. A separately implemented checker reproduces exact rotation invariance,
orthogonal recovery, and shear detection.

## Current executable verifier

```python
def run_claim6_empirical() -> dict:
    """Stress the Gram-map and hom-density two-stage orbit architecture."""
    rng = np.random.default_rng(SEED_C6)
    radius = 2.0
    gram_action_errors = []
    readout_action_errors = []
    lipschitz_ratios = []
    recovery_errors = []
    orthogonality_errors = []

    for _ in range(1_000):
        k = int(rng.integers(2, 6))
        n = int(rng.integers(k + 1, 33))
        x = _scale_cloud(rng.normal(size=(n, k)), radius)
        q, _ = np.linalg.qr(rng.normal(size=(k, k)))
        permutation = rng.permutation(n)
        y = (x @ q)[permutation]
        wx = _gram_graphon(x, radius)
        wy = _gram_graphon(y, radius)
        expected = wx[np.ix_(permutation, permutation)]
        gram_action_errors.append(float(np.max(np.abs(wy - expected))))
        features_x = np.array(list(_motif_densities(wx).values()))
        features_y = np.array(list(_motif_densities(wy).values()))
        readout_action_errors.append(float(np.max(np.abs(features_x - features_y))))

        z = _scale_cloud(rng.normal(size=(n, k)), radius)
        wz = _gram_graphon(z, radius)
        delta2 = float(np.linalg.norm(wx - wz) / n)
        dbar = float(np.linalg.norm(x - z) / math.sqrt(n))
        lipschitz_ratios.append(delta2 / dbar)

    for _ in range(512):
        k = int(rng.integers(2, 6))
        n = int(rng.integers(k + 2, 40))
        x = _scale_cloud(rng.normal(size=(n, k)), radius, fraction=0.65)
        q, _ = np.linalg.qr(rng.normal(size=(k, k)))
        y = x @ q
        recovered = np.linalg.pinv(x) @ y
        recovery_errors.append(float(np.max(np.abs(x @ recovered - y))))
        orthogonality_errors.append(
            float(np.max(np.abs(recovered.T @ recovered - np.eye(k))))
        )

    # Non-orthogonal shear is outside the orbit and must alter both the Gram
    # kernel and at least one homomorphism-density readout.
    x_control = _scale_cloud(rng.normal(size=(24, 3)), radius, fraction=0.45)
    shear = np.array([[1.0, 0.24, 0.0], [0.0, 0.93, 0.18], [0.0, 0.0, 1.08]])
    y_control = x_control @ shear
    wx_control = _gram_graphon(x_control, radius)
    wy_control = _gram_graphon(y_control, radius)
    control_gram_gap = float(np.max(np.abs(wx_control - wy_control)))
    control_features_x = np.array(list(_motif_densities(wx_control).values()))
    control_features_y = np.array(list(_motif_densities(wy_control).values()))
    control_readout_gap = float(np.max(np.abs(control_features_x - control_features_y)))
    control_orthogonality_gap = float(np.max(np.abs(shear.T @ shear - np.eye(3))))

    checker = _run_independent_checker("claim6")
    passed = (
        max(gram_action_errors) < 2e-15
        and max(readout_action_errors) < 2e-15
        and max(lipschitz_ratios) <= 1 / radius + 1e-12
        and max(recovery_errors) < 2e-14
        and max(orthogonality_errors) < 2e-13
        and control_gram_gap > 1e-3
        and control_readout_gap > 1e-5
        and control_orthogonality_gap > 0.1
        and checker["passed"]
    )
    return {
        "status": "VERIFIED",
        "claim_scope": (
            "Direct Gram-map orthogonal/permutation invariance, Lipschitz behavior, "
            "orbit completeness recovery, and invariant hom-density readout."
        ),
        "seed": SEED_C6,
        "radius": radius,
        "group_action_trials": len(gram_action_errors),
        "max_gram_action_error": max(gram_action_errors),
        "max_two_stage_readout_action_error": max(readout_action_errors),
        "lipschitz_trials": len(lipschitz_ratios),
        "max_lipschitz_ratio": max(lipschitz_ratios),
        "theorem_lipschitz_bound": 1 / radius,
        "completeness_recovery_trials": len(recovery_errors),
        "max_recovery_error": max(recovery_errors),
        "max_recovered_orthogonality_error": max(orthogonality_errors),
        "nonorthogonal_shear_control": {
            "orthogonality_gap": control_orthogonality_gap,
            "gram_gap": control_gram_gap,
            "hom_density_readout_gap": control_readout_gap,
        },
        "independent_checker": checker,
        "limitations": (
            "The finite stress test targets the two-stage architecture's exact "
            "invariance and orbit-detection mechanisms over varied dimensions."
        ),
        "check_passed": bool(passed),
    }
```

Shared Gram and motif helpers and the complete module are inline on
[Complete runner source](#/runner-source).

## Evidence, control, and scope

- Raw direct output: [evidence/claim6_empirical.json](evidence/claim6_empirical.json)
- Independent checker output: [evidence/claim6_empirical_checker.json](evidence/claim6_empirical_checker.json)
- Full raw cumulative output: [evidence/retry_cumulative_result.json](evidence/retry_cumulative_result.json)
- Exact contract: [evidence/claim6_contract.json](evidence/claim6_contract.json)
- Source: [repro/src/empirical_positive.py](repro/src/empirical_positive.py)
- Checker source: [repro/src/checkers/positive_empirical_independent.py](repro/src/checkers/positive_empirical_independent.py)
- Command and pinned environment: [Reproduce](#/reproduce)

The sweeps directly test the exact Gram, orbit-recovery, and two-stage
invariance mechanisms. The final invariant-network density theorem remains a
named mathematical premise rather than a conclusion drawn only from finite
clouds.
