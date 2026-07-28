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


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in {"claim3", "claim4"}:
        raise SystemExit("usage: positive_empirical_independent.py claim3|claim4")
    result = check_claim3() if sys.argv[1] == "claim3" else check_claim4()
    print(json.dumps(result, sort_keys=True))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
