"""Generate five evidence-bearing figures for the 8/12 retry report."""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RAW = json.loads(
    (ROOT / "publication/space_files/evidence/retry_cumulative_result.json").read_text()
)
OUT = ROOT / "reports" / "8-of-12-retry" / "images"
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update(
    {
        "figure.dpi": 150,
        "font.size": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
    }
)


def save(name: str) -> None:
    plt.tight_layout()
    plt.savefig(OUT / name, bbox_inches="tight")
    plt.close()


c3 = RAW["claims"]["claim_3_eq5_universality"]["primary_empirical_verification"]
c4 = RAW["claims"]["claim_4_eq6_universality"]["primary_empirical_verification"]
c5 = RAW["claims"]["claim_5_graphon_basis"]["primary_empirical_verification"]
c6 = RAW["claims"]["claim_6_gram_map"]["primary_empirical_verification"]

# 1. Headline: exact live points versus possible points after the retry.
claims = np.arange(1, 7)
live = np.array([2, 2, 1, 1, 1, 1])
possible = np.full(6, 2)
plt.figure(figsize=(8.4, 3.8))
plt.bar(claims - 0.18, live, width=0.36, label="Live judge (8/12)", color="#9aa0a6")
plt.bar(
    claims + 0.18,
    possible,
    width=0.36,
    label="Best-supported possible (forecast)",
    color="#2f80ed",
)
plt.xticks(claims, [f"C{i}" for i in claims])
plt.yticks([0, 1, 2])
plt.ylim(0, 2.35)
plt.ylabel("Points per claim")
plt.title("Retry targets the four positive-claim visibility gaps")
plt.legend(frameon=False, ncol=2, loc="upper center")
save("01_headline_retry.png")

# 2. Equation 5 convergence and destructive removal of its weight.
convergence = c3["basel_convergence"]
slow = c3["slow_decay_destructive_control"]
fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
axes[0].loglog(
    [row["n"] for row in convergence],
    [row["absolute_error_to_pi2_over_6"] for row in convergence],
    "o-",
    color="#2f80ed",
)
axes[0].set(xlabel="Terms N", ylabel="Absolute error", title=r"Eq. 5 approaches $\pi^2/6$")
axes[1].loglog(
    [row["n"] for row in slow],
    [row["unweighted_original"] for row in slow],
    "o-",
    label="Dropped weight",
    color="#eb5757",
)
axes[1].loglog(
    [row["n"] for row in slow],
    [row["eq5_weighted"] for row in slow],
    "o-",
    label="Equation 5",
    color="#27ae60",
)
axes[1].set(xlabel="Terms N", ylabel="Aggregate", title="Required weight changes the limit")
axes[1].legend(frameon=False)
save("02_eq5_direct.png")

# 3. Equation 6: direct KR stress test and invalid-growth control.
growth = c4["growth_violation_control"]
fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
axes[0].bar(
    ["Observed max", "1-Lipschitz bound"],
    [c4["max_Kantorovich_Rubinstein_ratio"], 1],
    color=["#2f80ed", "#9aa0a6"],
)
axes[0].set(ylim=(0, 1.12), ylabel="Integral gap / exact W1", title="4,096 exact-W1 pairs")
left = axes[1]
right = left.twinx()
left.loglog(
    [row["n"] for row in growth],
    [row["W1_to_delta0"] for row in growth],
    "o-",
    color="#2f80ed",
    label="W1 to delta0",
)
right.plot(
    [row["n"] for row in growth],
    [row["quadratic_integral"] for row in growth],
    "s--",
    color="#eb5757",
    label="Invalid integral",
)
left.set(xlabel="n", ylabel="W1", title="Quadratic-growth control breaks continuity")
right.set_ylabel("Integral")
lines = left.lines + right.lines
left.legend(lines, [line.get_label() for line in lines], frameon=False)
save("03_eq6_direct.png")

# 4. Five graphon coordinates versus their edge-count calibration.
names = list(c5["motif_edge_counts"])
ratios = [c5["maximum_gap_over_cut_norm"][name] for name in names]
bounds = [c5["motif_edge_counts"][name] for name in names]
x = np.arange(len(names))
plt.figure(figsize=(8.8, 3.8))
plt.bar(x - 0.18, ratios, width=0.36, label="Maximum over 500 pairs", color="#2f80ed")
plt.bar(x + 0.18, bounds, width=0.36, label="Edge-count calibration", color="#9aa0a6")
plt.xticks(x, ["K2", "P3", "K3", "K1,3", "C4"])
plt.ylabel("Density gap / exact cut norm")
plt.title("Five graphon coordinates satisfy the direct continuity stress test")
plt.legend(frameon=False)
save("04_graphon_direct.png")

# 5. Orbit invariance precision and destructive shear response.
fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
axes[0].bar(
    ["Gram action", "Two-stage readout", "Orbit recovery", "Orthogonality"],
    [
        c6["max_gram_action_error"],
        c6["max_two_stage_readout_action_error"],
        c6["max_recovery_error"],
        c6["max_recovered_orthogonality_error"],
    ],
    color=["#2f80ed", "#56ccf2", "#27ae60", "#6fcf97"],
)
axes[0].set_yscale("log")
axes[0].set(ylabel="Maximum absolute error", title="2,512 valid-action/recovery trials")
axes[0].tick_params(axis="x", rotation=18)
control = c6["nonorthogonal_shear_control"]
axes[1].bar(
    ["Orthogonality", "Gram", "Readout"],
    [control["orthogonality_gap"], control["gram_gap"], control["hom_density_readout_gap"]],
    color="#eb5757",
)
axes[1].set_yscale("log")
axes[1].set(ylabel="Detected gap", title="Nonorthogonal shear must fail")
save("05_orbit_direct.png")

print(f"generated 5 retry figures in {OUT}")
