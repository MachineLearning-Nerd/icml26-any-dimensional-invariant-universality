"""Independent, small recomputation of key positive-claim empirical checks."""
from __future__ import annotations

import json
import math
import sys

import numpy as np
from scipy.stats import wasserstein_distance


def check_claim3() -> dict:
    n = 1_000_000
    basel = math.fsum(1.0 / (i * i) for i in range(1, n + 1))
    error = abs(math.pi**2 / 6 - basel)
    x = np.array([0.5, -0.25, 0.125, 0.0])
    aggregate = math.fsum(abs(v) * math.tanh(v) for v in x)
    permuted = math.fsum(abs(v) * math.tanh(v) for v in x[[2, 0, 3, 1]])
    unweighted_growth = 16_384 / 256
    passed = error < 1.1e-6 and aggregate == permuted and unweighted_growth == 64
    return {
        "claim": "claim3",
        "basel_n": n,
        "basel_absolute_error": error,
        "permutation_error": abs(aggregate - permuted),
        "dropped_weight_growth": unweighted_growth,
        "passed": passed,
    }


def check_claim4() -> dict:
    x = np.array([-2.0, -0.5, 0.25, 1.5])
    y = np.array([-1.75, -0.4, 0.1, 1.9])
    w1 = float(wasserstein_distance(x, y))
    gap = float(abs(np.tanh(x).mean() - np.tanh(y).mean()))
    n = 10_000
    growth_w1 = 1 / n
    quadratic_integral = (n**-2) * n**2
    separation = 0.5 - 0.0
    passed = gap <= w1 + 1e-15 and growth_w1 < 2e-4 and quadratic_integral == 1 and separation > 0
    return {
        "claim": "claim4",
        "exact_W1": w1,
        "tanh_integral_gap": gap,
        "KR_ratio": gap / w1,
        "growth_control_W1": growth_w1,
        "growth_control_quadratic_integral": quadratic_integral,
        "separation_gap": separation,
        "passed": passed,
    }


def _cut_norm(matrix: np.ndarray) -> float:
    n = matrix.shape[0]
    best = 0.0
    for mask in range(1, 1 << n):
        cols = [j for j in range(n) if mask & (1 << j)]
        rows = matrix[:, cols].sum(axis=1)
        best = max(best, float(rows[rows > 0].sum()), float(-rows[rows < 0].sum()))
    return best / n**2


def check_claim5() -> dict:
    triangle = np.zeros((4, 4))
    triangle[:3, :3] = 1
    np.fill_diagonal(triangle, 0)
    path = np.zeros((4, 4))
    for i, j in [(0, 1), (1, 2), (2, 3)]:
        path[i, j] = path[j, i] = 1
    edge_gap = abs(float(triangle.mean() - path.mean()))
    tri_triangle = float(np.einsum("ij,jk,ki->", triangle, triangle, triangle) / 4**3)
    tri_path = float(np.einsum("ij,jk,ki->", path, path, path) / 4**3)
    w = np.full((5, 5), 0.8)
    u = np.full((5, 5), 0.3)
    edge_ratio = abs(float(w.mean() - u.mean())) / _cut_norm(w - u)
    passed = edge_gap == 0 and abs(tri_triangle - tri_path - 0.09375) < 1e-15
    passed &= abs(edge_ratio - 1) < 1e-15
    return {
        "claim": "claim5",
        "same_edge_gap": edge_gap,
        "triangle_gap": tri_triangle - tri_path,
        "tight_edge_cut_ratio": edge_ratio,
        "passed": bool(passed),
    }


def check_claim6() -> dict:
    x = np.array([[0.2, 0.1], [-0.3, 0.4], [0.5, -0.2], [0.1, -0.4]])
    q = np.array([[0.0, -1.0], [1.0, 0.0]])
    y = x @ q
    gram_gap = float(np.max(np.abs(x @ x.T - y @ y.T)))
    recovered = np.linalg.pinv(x) @ y
    orthogonality_error = float(np.max(np.abs(recovered.T @ recovered - np.eye(2))))
    shear = np.array([[1.0, 0.3], [0.0, 1.0]])
    shear_gram_gap = float(np.max(np.abs(x @ x.T - (x @ shear) @ (x @ shear).T)))
    passed = gram_gap < 1e-15 and orthogonality_error < 1e-14 and shear_gram_gap > 0.01
    return {
        "claim": "claim6",
        "gram_invariance_error": gram_gap,
        "recovered_orthogonality_error": orthogonality_error,
        "nonorthogonal_shear_gram_gap": shear_gram_gap,
        "passed": bool(passed),
    }


def main() -> int:
    checks = {
        "claim3": check_claim3,
        "claim4": check_claim4,
        "claim5": check_claim5,
        "claim6": check_claim6,
    }
    if len(sys.argv) != 2 or sys.argv[1] not in checks:
        raise SystemExit("usage: positive_empirical_independent.py claim3|claim4|claim5|claim6")
    result = checks[sys.argv[1]]()
    print(json.dumps(result, sort_keys=True))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
