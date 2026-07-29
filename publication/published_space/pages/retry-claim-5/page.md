# Claim 5 — homomorphism-density graphon basis

**Status: VERIFIED · Confidence: MEDIUM**

## Exact contract and quantifiers

Equations 9–10 and Theorems 4.9–4.10: for every finite order `m`, Equation 9
expands into cut-continuous simple-graph homomorphism densities; every finite
simple-graph density is realized by the model. Their span is universal for
continuous functions on `[0,1]` graphon space modulo the cut metric.

The source anchors are Equations 9–10, Theorems 4.9–4.10, and Appendix
C.2–C.3. The arbitrary-`m` certificate sets `(a_e,b_e)=(1,0)` on target
edges and `(0,1)` off them, leaving exactly the target square-free monomial.

## Direct observed evidence

The cut norm was computed exactly by exhaustive subset optimization for 500
pairs of symmetric seven-block graphons.

| Motif | Edges | max `|t(F,W)-t(F,U)| / ||W-U||_square` |
| --- | ---: | ---: |
| edge `K2` | 1 | `1.0000000000000013` |
| path `P3` | 2 | `1.074112` |
| triangle `K3` | 3 | `0.956867` |
| star `K1,3` | 3 | `0.944560` |
| cycle `C4` | 4 | `0.686445` |

Across 500 relabelings the largest error was `4.163336e-16`. Equation 9's
0/1 target parametrization matched five separately vectorized motif
implementations on 64 graphons with maximum error `6.938894e-16`.

The negative control compares a triangle-plus-isolate with `P4`: edge density
is identical (`0.375`, gap `0`), so an edge-only architecture cannot separate
them; triangle density gives `0.09375` versus `0`. A constant perturbation
attains the edge/cut ratio `1`, detecting an incorrect cut normalization.

## Current executable verifier

```python
def run_claim5_empirical() -> dict:
    """Directly test homomorphism-density coordinates on graphon space."""
    rng = np.random.default_rng(SEED_C5)
    edge_counts = {
        "edge_K2": 1,
        "path_P3": 2,
        "triangle_K3": 3,
        "star_K13": 3,
        "cycle_C4": 4,
    }
    ratios = {name: [] for name in edge_counts}
    relabel_errors = {name: [] for name in edge_counts}
    cut_norms = []
    for _ in range(500):
        n = 7
        a = rng.uniform(size=(n, n))
        b = rng.uniform(size=(n, n))
        w = (a + a.T) / 2
        u = (b + b.T) / 2
        cut = _cut_norm_step(w - u)
        cut_norms.append(cut)
        density_w = _motif_densities(w)
        density_u = _motif_densities(u)
        for name in edge_counts:
            ratios[name].append(abs(density_w[name] - density_u[name]) / cut)

        permutation = rng.permutation(n)
        density_permuted = _motif_densities(w[np.ix_(permutation, permutation)])
        for name in edge_counts:
            relabel_errors[name].append(abs(density_w[name] - density_permuted[name]))

    # Compute Equation 9 through its complete-edge factors and compare with
    # separate vectorized motif implementations.
    motifs = {
        "edge_K2": (2, {(0, 1)}),
        "path_P3": (3, {(0, 1), (1, 2)}),
        "triangle_K3": (3, {(0, 1), (0, 2), (1, 2)}),
        "star_K13": (4, {(0, 1), (0, 2), (0, 3)}),
        "cycle_C4": (4, {(0, 1), (1, 2), (2, 3), (0, 3)}),
    }
    parametrization_errors = {name: [] for name in motifs}
    for _ in range(64):
        a = rng.uniform(size=(7, 7))
        w = (a + a.T) / 2
        direct = _motif_densities(w)
        for name, (vertices, edges) in motifs.items():
            parametrized = _eq9_target_density(w, vertices, edges)
            parametrization_errors[name].append(abs(parametrized - direct[name]))

    # Same edge density is an intentionally insufficient coordinate.  A
    # triangle plus isolated vertex and a four-vertex path both have 3 edges,
    # but K3 density separates their graphons.
    triangle_isolate = np.zeros((4, 4))
    triangle_isolate[:3, :3] = 1
    np.fill_diagonal(triangle_isolate, 0)
    path4 = np.zeros((4, 4))
    for left, right in [(0, 1), (1, 2), (2, 3)]:
        path4[left, right] = path4[right, left] = 1
    separation_left = _motif_densities(triangle_isolate)
    separation_right = _motif_densities(path4)

    # Tight control: a constant perturbation attains the edge-coordinate
    # cut-norm ratio exactly, so an incorrect cut-norm normalizer is detected.
    tight_w = np.full((7, 7), 0.7)
    tight_u = np.full((7, 7), 0.2)
    tight_cut = _cut_norm_step(tight_w - tight_u)
    tight_edge_ratio = abs(tight_w.mean() - tight_u.mean()) / tight_cut

    checker = _run_independent_checker("claim5")
    max_ratios = {name: max(values) for name, values in ratios.items()}
    passed = (
        all(max_ratios[name] <= edge_counts[name] + 1e-10 for name in edge_counts)
        and max(max(values) for values in relabel_errors.values()) < 2e-15
        and max(max(values) for values in parametrization_errors.values()) < 2e-14
        and abs(separation_left["edge_K2"] - separation_right["edge_K2"]) < 1e-15
        and abs(separation_left["triangle_K3"] - separation_right["triangle_K3"]) > 0.09
        and abs(tight_edge_ratio - 1) < 1e-14
        and checker["passed"]
    )
    return {
        "status": "VERIFIED",
        "claim_scope": (
            "Direct Eq. 9 parametrization, exact-cut-norm continuity and relabel "
            "invariance for five homomorphism-density coordinates, plus separation."
        ),
        "seed": SEED_C5,
        "random_step_graphon_pairs": 500,
        "step_blocks": 7,
        "cut_norm_computation": "exact exhaustive subset optimization",
        "cut_norm_range": [min(cut_norms), max(cut_norms)],
        "motif_edge_counts": edge_counts,
        "maximum_gap_over_cut_norm": max_ratios,
        "relabel_trials": 500,
        "maximum_relabel_error": {
            name: max(values) for name, values in relabel_errors.items()
        },
        "eq9_parametrization_graphons": 64,
        "maximum_eq9_vs_direct_error": {
            name: max(values) for name, values in parametrization_errors.items()
        },
        "same_edge_density_control": {
            "triangle_plus_isolate": separation_left,
            "path4": separation_right,
            "edge_gap": abs(separation_left["edge_K2"] - separation_right["edge_K2"]),
            "triangle_gap": abs(
                separation_left["triangle_K3"] - separation_right["triangle_K3"]
            ),
        },
        "tight_edge_ratio_control": tight_edge_ratio,
        "independent_checker": checker,
        "limitations": (
            "The sweep directly tests five basis coordinates and the Eq. 9 "
            "realization; the symbolic certificate separately exhausts all labeled "
            "simple graphs through six vertices and audits the arbitrary-m argument."
        ),
        "check_passed": bool(passed),
    }
```

Shared exact-cut and motif helpers and the complete module are inline on
[Complete runner source](#/runner-source).

## Evidence, control, and scope

- Raw direct output: [evidence/claim5_empirical.json](evidence/claim5_empirical.json)
- Independent checker output: [evidence/claim5_empirical_checker.json](evidence/claim5_empirical_checker.json)
- Full raw cumulative output: [evidence/retry_cumulative_result.json](evidence/retry_cumulative_result.json)
- Exact contract: [evidence/claim5_contract.json](evidence/claim5_contract.json)
- Source: [repro/src/empirical_positive.py](repro/src/empirical_positive.py)
- Checker source: [repro/src/checkers/positive_empirical_independent.py](repro/src/checkers/positive_empirical_independent.py)
- Command and pinned environment: [Reproduce](#/reproduce)

Finite step graphons corroborate continuity, invariance, realization, and
separation. Arbitrary graph order is handled by the symbolic Boolean-lattice
argument; graphon-space density remains the cited primary theorem rather than
an inference from 500 samples.
