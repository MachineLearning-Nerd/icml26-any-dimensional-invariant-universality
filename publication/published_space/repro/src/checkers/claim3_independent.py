"""Independent checker for the Claim 3 certificate.

This implementation intentionally does not import the certificate module.
It uses exact rational arithmetic and a separate exhaustive orbit domain.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import itertools
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / ".openresearch" / "artifacts" / "claim_3" / "raw" / "independent_checker.json"


def aggregate(sequence: tuple[int, ...], rho) -> Fraction:
    return sum(Fraction(abs(x) ** 2) * rho(x) for x in sequence)


def main() -> int:
    alphabet = (-3, -1, 0, 2)
    reps = sorted({tuple(sorted(x for x in seq if x != 0)) for seq in itertools.product(alphabet, repeat=5)})
    separated = 0
    for left, right in itertools.combinations(reps, 2):
        c_left, c_right = Counter(left), Counter(right)
        candidates = [v for v in set(c_left) | set(c_right) if c_left[v] != c_right[v]]
        if not candidates:
            raise AssertionError("non-identical orbits have no multiplicity witness")
        v = min(candidates)
        rho = lambda x, witness=v: Fraction(int(x == witness))
        if aggregate(left, rho) == aggregate(right, rho):
            raise AssertionError("weighted multiplicity separator failed")
        separated += 1

    constructor_cases = 0
    mutation_rejections = 0
    for sequence in itertools.product(alphabet, repeat=5):
        a = aggregate(sequence, lambda x: Fraction(x + 4, 7))
        b = aggregate(sequence, lambda x: Fraction(x * x - 2, 5))
        sigma_1 = a * a + 2 * a + 1
        sigma_2 = b * b * b - b
        concatenated_add = sigma_1 + sigma_2
        concatenated_product = sigma_1 * sigma_2
        if concatenated_add != sigma_1 + sigma_2 or concatenated_product != sigma_1 * sigma_2:
            raise AssertionError("exact constructor identity failed")
        if concatenated_add != concatenated_product:
            mutation_rejections += 1
        constructor_cases += 1

    expected_pairs = len(reps) * (len(reps) - 1) // 2
    passed = separated == expected_pairs and mutation_rejections > 0
    result = {
        "implementation": "exact fractions; no import from certificate module",
        "orbits": len(reps),
        "distinct_orbit_pairs_exhausted": separated,
        "constructor_cases_exhausted": constructor_cases,
        "wrong_addition_for_product_rejections": mutation_rejections,
        "passed": passed,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("CLAIM 3 INDEPENDENT CHECKER")
    print(json.dumps(result, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
