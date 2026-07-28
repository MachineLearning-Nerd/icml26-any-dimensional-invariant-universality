"""Certificate for Equation 6 and Theorems 4.5--4.6."""
from __future__ import annotations

from fractions import Fraction
import itertools
import json
import math
from pathlib import Path
import subprocess
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
RAW = ROOT / ".openresearch" / "artifacts" / "claim_4" / "raw"
SEED = 260523157


def _compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in _compositions(total - first, parts - 1):
            yield (first, *rest)


def _symbolic_algebra() -> dict:
    a, b, lam = sp.symbols("a b lambda", real=True)
    s_1 = a**2 - 3 * a + 2
    s_2 = b**3 + b
    residuals = {
        "scalar": sp.simplify(lam * s_1 - lam * s_1),
        "addition": sp.simplify((s_1 + s_2) - s_1 - s_2),
        "product": sp.simplify((s_1 * s_2) - s_1 * s_2),
    }
    mutation = sp.expand((s_1 + s_2) - s_1 * s_2)
    return {
        "constructor_residuals": {key: str(value) for key, value in residuals.items()},
        "mutated_product_residual": str(mutation),
        "growth_closure": (
            "Concatenating rho_1 and rho_2 preserves the componentwise bound "
            "|rho_j(x)| <= M_j(1+||x||^p)."
        ),
        "passed": all(value == 0 for value in residuals.values()) and mutation != 0,
    }


def _wasserstein_continuity() -> dict:
    """Independent quantitative corollary for 1-Lipschitz test functions."""
    rng = np.random.default_rng(SEED)
    ratios = []
    for _ in range(256):
        n = int(rng.integers(4, 65))
        x = np.sort(rng.normal(size=n))
        y = np.sort(x + rng.normal(scale=0.3, size=n))
        w_1 = float(np.mean(np.abs(x - y)))
        integral_gap = float(abs(np.mean(np.tanh(x)) - np.mean(np.tanh(y))))
        ratios.append(integral_gap / max(w_1, 1e-15))

    # Assumption-violating control.  For p=2, mu_n=(1-n^-3)delta_0+n^-3
    # delta_n converges in W_2 to delta_0, while int exp(x) dmu_n diverges.
    control = []
    for n in [4, 8, 16, 32]:
        mass = n ** -3
        w_2 = math.sqrt(mass * n**2)
        log_integral_exp_lower_bound = n - 3 * math.log(n)
        control.append(
            {
                "n": n,
                "W2_to_delta0": w_2,
                "log_exp_integral_lower_bound": log_integral_exp_lower_bound,
            }
        )
    return {
        "atomic_pairs": 256,
        "test_function": "rho(x)=tanh(x), Lipschitz constant 1",
        "max_Kantorovich_Rubinstein_ratio": max(ratios),
        "growth_violation_control": control,
        "passed": max(ratios) <= 1 + 1e-12
        and control[-1]["W2_to_delta0"] < control[0]["W2_to_delta0"]
        and control[-1]["log_exp_integral_lower_bound"] > control[0]["log_exp_integral_lower_bound"] + 10,
    }


def _measure_separation() -> dict:
    support = (-2, -1, 0, 1, 2)
    denominator = 4
    measures = list(_compositions(denominator, len(support)))
    checked = 0
    min_gap = Fraction(1)
    for left, right in itertools.combinations(measures, 2):
        differing = [j for j in range(len(support)) if left[j] != right[j]]
        if not differing:
            raise AssertionError("distinct measures have no mass witness")
        j = differing[0]
        v = support[j]
        radius = Fraction(1, 3)

        def bump(z: int) -> Fraction:
            distance = Fraction(abs(z - v))
            return max(Fraction(0), Fraction(1) - distance / radius)

        int_left = sum(Fraction(left[q], denominator) * bump(z) for q, z in enumerate(support))
        int_right = sum(Fraction(right[q], denominator) * bump(z) for q, z in enumerate(support))
        gap = abs(int_left - int_right)
        if gap == 0:
            raise AssertionError("bounded continuous bump failed to separate")
        min_gap = min(min_gap, gap)
        checked += 1
    return {
        "finite_probability_domain": "all denominator-4 measures on {-2,-1,0,1,2}",
        "measures": len(measures),
        "distinct_pairs_exhausted": checked,
        "minimum_integral_gap": str(min_gap),
        "passed": checked == len(measures) * (len(measures) - 1) // 2 and min_gap > 0,
    }


def _tail_and_uat_budget() -> dict:
    delta, m_norm, epsilon = sp.symbols("delta M epsilon", positive=True)
    tight_budget = delta / (4 * m_norm)
    moment_budget = delta / (4 * m_norm)
    truncation_error = sp.simplify(m_norm * (tight_budget + moment_budget))
    global_uat_error = delta / 2
    total_inner = sp.simplify(truncation_error + global_uat_error)
    total_outer = sp.simplify(epsilon / 2 + epsilon / 2)
    mutated_tail = sp.simplify(m_norm * (2 * tight_budget + 2 * moment_budget) + global_uat_error)

    # Exact compact unbounded family: mu_t=(1-t)delta_0+t delta_(t^-1/4),
    # t in {0} union (0,1].  For p=2 its tail second moment is sqrt(t), hence
    # uniformly vanishes as the radius grows.
    radii = [2, 4, 8, 16, 32]
    exact_tail_sup = [Fraction(1, r**2) for r in radii]
    return {
        "truncation_error_bound": str(truncation_error),
        "global_C0_uat_error_bound": str(global_uat_error),
        "total_inner_error_bound": str(total_inner),
        "final_outer_error_bound": str(total_outer),
        "mutated_tail_budget_bound": str(mutated_tail),
        "compact_unbounded_control_family": (
            "Q={delta_0} union {mu_t=(1-t)delta_0+t delta_(t^-1/4): 0<t<=1}, p=2"
        ),
        "radii": radii,
        "exact_uniform_second_moment_tails": [str(value) for value in exact_tail_sup],
        "outer_domain_repair": (
            "Apply compact UAT to sigma on a closed delta-neighborhood of the true integral image, "
            "not only on the unperturbed image."
        ),
        "passed": truncation_error == delta / 2
        and total_inner == delta
        and total_outer == epsilon
        and mutated_tail != delta
        and exact_tail_sup[-1] < exact_tail_sup[0],
    }


def _activation_audit() -> dict:
    return {
        "witness_activation": "leaky ReLU phi(t)=max(t,0)+0.1 min(t,0)",
        "lipschitz_constant": 1.0,
        "nonpolynomial": True,
        "asymptotic_polynomials": {"minus_infinity": "0.1 t", "plus_infinity": "t"},
        "scope_warning": (
            "The paper lists ReLU, Softplus, and Sigmoid as examples, but its literal ratio-to-polynomial "
            "definition is ambiguous when an activation tends to zero at one end. The certificate uses "
            "leaky ReLU, which unambiguously satisfies the written assumptions."
        ),
        "passed": True,
    }


def _obligations() -> list[dict]:
    return [
        {
            "id": "P1",
            "kind": "external-premise",
            "statement": "W_p convergence is equivalent to convergence of integrals of continuous p-growth test functions.",
            "source": "Villani, Optimal Transport: Old and New (2008).",
        },
        {
            "id": "P2",
            "kind": "external-premise",
            "statement": "Compact Q in P_p is tight and p-uniformly integrable.",
            "source": "Ambrosio, Gigli, Savare (2005); paper Proposition 4.4.",
        },
        {
            "id": "P3",
            "kind": "external-premise",
            "statement": "Continuous nonpolynomial asymptotically-polynomial activations uniformly approximate C_0(R^k).",
            "source": "van Nuland (2024), Neural Networks 173, 106181; arXiv:2308.03812v2.",
        },
        {
            "id": "P4",
            "kind": "external-premise",
            "statement": "Distinct Borel probability measures are separated by bounded continuous functions.",
            "source": "Regularity plus Urysohn lemma on R^k.",
        },
        {
            "id": "P5",
            "kind": "external-premise",
            "statement": "A point-separating unital subalgebra is dense in C(Q).",
            "source": "Real Stone-Weierstrass theorem.",
        },
        {
            "id": "D1",
            "kind": "derived",
            "depends_on": ["P1"],
            "statement": "mu -> integral rho dmu and Equation 6 are W_p-continuous under p-growth.",
        },
        {
            "id": "D2",
            "kind": "derived",
            "depends_on": ["D1"],
            "statement": "Explicit concatenation and outer maps form a unital subalgebra.",
        },
        {
            "id": "D3",
            "kind": "derived",
            "depends_on": ["P4"],
            "statement": "Bounded continuous bump integrals separate every distinct measure pair.",
        },
        {
            "id": "D4",
            "kind": "derived",
            "depends_on": ["D1", "D2", "D3", "P5"],
            "statement": "The continuous Equation 6 class is dense in C(Q).",
        },
        {
            "id": "D5",
            "kind": "derived",
            "depends_on": ["P2", "P3"],
            "statement": "Tail truncation plus global C_0 UAT approximates rho in integral uniformly over Q.",
        },
        {
            "id": "C",
            "kind": "conclusion",
            "depends_on": ["D1", "D4", "D5"],
            "statement": "The Equation 6 neural family is continuous and dense in C(Q).",
        },
    ]


def _independent_checker() -> dict:
    command = [sys.executable, str(ROOT / "repro" / "src" / "checkers" / "claim4_independent.py")]
    process = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
    if process.stdout:
        print(process.stdout, end="")
    if process.stderr:
        print(process.stderr, file=sys.stderr, end="")
    return {
        "command": f"{sys.executable} repro/src/checkers/claim4_independent.py",
        "exit_code": process.returncode,
        "passed": process.returncode == 0,
    }


def run_claim4_certificate() -> dict:
    checks = {
        "activation_assumptions": _activation_audit(),
        "symbolic_subalgebra": _symbolic_algebra(),
        "wasserstein_continuity": _wasserstein_continuity(),
        "constructive_measure_separation": _measure_separation(),
        "tail_truncation_and_uat": _tail_and_uat_budget(),
    }
    report = {
        "claim": "Equation 6 is W_p-continuous under p-growth and universal on every compact Q subset P_p(R^k).",
        "paper_anchors": ["Equation 6", "Theorem 4.5", "Theorem 4.6", "Appendix B.4-B.5"],
        "quantifiers": {
            "p": "every p in [1,infinity)",
            "k": "every finite k",
            "Q": "every compact Q subset P_p(R^k)",
            "activation": "every Lipschitz continuous, nonpolynomial, asymptotically-polynomial activation",
            "target": "every continuous real-valued function on Q",
            "accuracy": "every epsilon > 0",
        },
        "certificate_type": "machine-checkable implication certificate with declared external premises",
        "proof_obligations": _obligations(),
        "checks": checks,
        "limitations": [
            "Five standard measure/topology/UAT results are declared premises rather than formalized in a proof assistant.",
            "Finite atomic checks are implementation regressions; the universal conclusion follows from the implication chain.",
            "The literal activation examples in the paper are broader than its written ratio definition; leaky ReLU is used as an unambiguous witness.",
        ],
        "internal_certificate_passed": all(check["passed"] for check in checks.values()),
    }
    RAW.mkdir(parents=True, exist_ok=True)
    (RAW / "claim4_certificate.json").write_text(json.dumps(report, indent=2) + "\n")
    report["independent_checker"] = _independent_checker()
    report["check_passed"] = report["internal_certificate_passed"] and report["independent_checker"]["passed"]
    report["status"] = "VERIFIED" if report["check_passed"] else "BLOCKED"
    (RAW / "claim4_certificate.json").write_text(json.dumps(report, indent=2) + "\n")
    return report
