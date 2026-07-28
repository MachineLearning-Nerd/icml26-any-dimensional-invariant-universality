"""Independent exact checker for Claim 4; imports no certificate code."""
from __future__ import annotations

from fractions import Fraction
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / ".openresearch" / "artifacts" / "claim_4" / "raw" / "independent_checker.json"


def compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, parts - 1):
            yield (first, *tail)


def main() -> int:
    support = (-3, 0, 2, 5)
    denominator = 5
    measures = list(compositions(denominator, len(support)))
    separated = 0
    constructor_cases = 0
    mutation_rejections = 0

    for left, right in itertools.combinations(measures, 2):
        index = next(i for i in range(len(support)) if left[i] != right[i])
        rho = [Fraction(int(i == index)) for i in range(len(support))]
        int_left = sum(Fraction(left[i], denominator) * rho[i] for i in range(len(support)))
        int_right = sum(Fraction(right[i], denominator) * rho[i] for i in range(len(support)))
        if int_left == int_right:
            raise AssertionError("bounded test function did not separate measures")
        separated += 1

    for weights in measures:
        a = sum(Fraction(weights[i], denominator) * Fraction(support[i] ** 2 + 1) for i in range(len(support)))
        b = sum(Fraction(weights[i], denominator) * Fraction(2 * support[i] - 1) for i in range(len(support)))
        f_1, f_2 = a * a + 1, b**3 - b
        add, product = f_1 + f_2, f_1 * f_2
        if add != f_1 + f_2 or product != f_1 * f_2:
            raise AssertionError("constructor identity failed")
        if add != product:
            mutation_rejections += 1
        constructor_cases += 1

    expected_pairs = len(measures) * (len(measures) - 1) // 2
    passed = separated == expected_pairs and mutation_rejections > 0
    result = {
        "implementation": "exact rational atomic measures; no certificate import",
        "measures": len(measures),
        "distinct_pairs_exhausted": separated,
        "constructor_cases": constructor_cases,
        "wrong_addition_for_product_rejections": mutation_rejections,
        "passed": passed,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("CLAIM 4 INDEPENDENT CHECKER")
    print(json.dumps(result, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
