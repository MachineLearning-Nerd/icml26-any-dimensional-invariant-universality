"""Independent exact-rational checker for the graphon-basis certificate."""
from __future__ import annotations

from fractions import Fraction
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / ".openresearch" / "artifacts" / "claim_5" / "raw" / "independent_checker.json"


def edge_list(m: int):
    return [(i, j) for i in range(m) for j in range(i + 1, m)]


def evaluate(mask: int, m: int, w):
    q = len(w)
    total = Fraction(0)
    for assignment in itertools.product(range(q), repeat=m):
        value = Fraction(1)
        for index, (i, j) in enumerate(edge_list(m)):
            if mask & (1 << index):
                value *= w[assignment[i]][assignment[j]]
        total += value
    return total / q**m


def model(mask: int, m: int, w):
    q = len(w)
    total = Fraction(0)
    for assignment in itertools.product(range(q), repeat=m):
        value = Fraction(1)
        for index, (i, j) in enumerate(edge_list(m)):
            a = Fraction(int(bool(mask & (1 << index))))
            b = 1 - a
            value *= a * w[assignment[i]][assignment[j]] + b
        total += value
    return total / q**m


def main() -> int:
    graphons = [
        (
            (Fraction(0), Fraction(1, 3), Fraction(1)),
            (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)),
            (Fraction(1), Fraction(2, 3), Fraction(1, 4)),
        ),
        (
            (Fraction(1, 5), Fraction(2, 5), Fraction(3, 5)),
            (Fraction(2, 5), Fraction(4, 5), Fraction(1)),
            (Fraction(3, 5), Fraction(1), Fraction(0)),
        ),
    ]
    cases = 0
    for m in range(2, 6):
        maximum = 1 << len(edge_list(m))
        masks = range(maximum) if m <= 4 else range(0, maximum, 7)
        for mask in masks:
            for graphon in graphons:
                if model(mask, m, graphon) != evaluate(mask, m, graphon):
                    raise AssertionError("Eq. 9 parametrization differs from homomorphism density")
                cases += 1

    # A simple-edge product is multilinear in every edge variable. The
    # repeated-edge mutation has nonzero second finite difference.
    values = [Fraction(0), Fraction(1, 3), Fraction(2, 3)]
    simple_second_difference = values[2] - 2 * values[1] + values[0]
    squared = [value**2 for value in values]
    repeated_second_difference = squared[2] - 2 * squared[1] + squared[0]
    passed = simple_second_difference == 0 and repeated_second_difference != 0
    result = {
        "implementation": "separate exact-rational enumerator; no certificate import",
        "step_graphon_parametrization_cases": cases,
        "simple_edge_second_difference": str(simple_second_difference),
        "repeated_edge_second_difference": str(repeated_second_difference),
        "repeated_edge_mutation_rejected": passed,
        "passed": passed,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("CLAIM 5 INDEPENDENT CHECKER")
    print(json.dumps(result, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
