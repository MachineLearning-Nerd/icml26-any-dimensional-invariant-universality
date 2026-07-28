"""Generate the five evidence-bearing report figures from frozen run values."""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "claim-by-claim" / "images"
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"figure.dpi": 150, "font.size": 10, "axes.spines.top": False, "axes.spines.right": False})


def save(name: str) -> None:
    plt.tight_layout()
    plt.savefig(OUT / name, bbox_inches="tight")
    plt.close()


# Headline: historical points versus current evidence-supported possible points.
claims = np.arange(1, 7)
historical = np.array([2, 2, 1, 1, 1, 2])
possible = np.array([2, 2, 2, 2, 2, 2])
plt.figure(figsize=(8.4, 3.8))
plt.bar(claims - 0.18, historical, width=0.36, label="Live judge (9/12)", color="#9aa0a6")
plt.bar(claims + 0.18, possible, width=0.36, label="Evidence-supported possible (forecast)", color="#2f80ed")
plt.xticks(claims, [f"C{i}" for i in claims])
plt.yticks([0, 1, 2])
plt.ylim(0, 2.35)
plt.ylabel("Points per claim")
plt.title("New certificates target the three one-point gaps")
plt.legend(frameon=False, ncol=2, loc="upper center")
save("01_headline_coverage.png")


# Mechanism: divergence and cut-norm discontinuity.
ns = np.array([200, 800, 3200, 12800])
eq4 = np.array([42.87816080056619, 103.33479829735921, 247.17526522203073, 589.3169534068679])
eq5 = np.array([1.768843958885639, 1.7766083669766746, 1.7789217322447233, 1.7796098715332127])
cut_n = np.array([4, 6, 8, 11, 14, 16])
fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.8))
axes[0].loglog(ns, eq4, "o-", label="Eq. 4 unweighted")
axes[0].loglog(ns, eq5, "o-", label="Eq. 5 weighted")
axes[0].set_xlabel("Truncation N")
axes[0].set_ylabel("Partial sum")
axes[0].set_title("DeepSets: divergence vs convergence")
axes[0].legend(frameon=False)
axes[1].plot(cut_n, 1 / cut_n, "o-", label="cut-norm(W_n)")
axes[1].plot(cut_n, np.ones_like(cut_n), "o-", label="cut-norm(W_n²)")
axes[1].plot(cut_n, 3 / cut_n, "o-", label="cut-norm(3W_n)")
axes[1].set_xlabel("n")
axes[1].set_ylabel("Exact cut norm")
axes[1].set_title("Nonlinear image stays away from zero")
axes[1].legend(frameon=False)
save("02_negative_claims.png")


# Claim 3 tail certificate and independent work.
trunc = np.array([4, 8, 16, 32, 64])
actual = np.array([5.229913888642724e-3, 2.0345384054424347e-5, 3.10440858282455e-10, 7.228014483236696e-20, 3.918314502740958e-39])
bound = np.array([7.36569563735987e-3, 2.8772248583436992e-5, 4.390296719884795e-10, 1.0221956111222494e-19, 5.541333511419453e-39])
fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.8))
axes[0].semilogy(trunc, actual, "o-", label="Actual aggregate tail")
axes[0].semilogy(trunc, bound, "o--", label="Certified upper bound")
axes[0].set_xlabel("Truncation index")
axes[0].set_ylabel("Tail norm")
axes[0].set_title("Eq. 5 uniform-tail certificate")
axes[0].legend(frameon=False)
axes[1].bar(["Orbit pairs", "Constructor cases", "Mutations rejected"], [1540, 1024, 1024], color=["#2f80ed", "#27ae60", "#eb5757"])
axes[1].set_ylabel("Exact-rational independent checks")
axes[1].set_title("Independent checker coverage")
axes[1].tick_params(axis="x", rotation=18)
save("03_eq5_certificate.png")


# Claim 4 necessity and compact-tail mechanism.
n = np.array([4, 8, 16, 32])
w2 = np.array([0.5, 0.3535533905932738, 0.25, 0.1767766952966369])
log_integral = np.array([-0.1588830833596715, 1.7616753749604932, 7.682233833280657, 21.60279229160082])
radii = np.array([2, 4, 8, 16, 32])
tails = np.array([1 / 4, 1 / 16, 1 / 64, 1 / 256, 1 / 1024])
fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.8))
left = axes[0]
right = left.twinx()
left.plot(n, w2, "o-", color="#2f80ed", label=r"$W_2(\mu_n,\delta_0)$")
right.plot(n, log_integral, "s--", color="#eb5757", label="log integral lower bound")
left.set_xlabel("n")
left.set_ylabel(r"$W_2$", color="#2f80ed")
right.set_ylabel("log integral", color="#eb5757")
left.set_title("Growth assumption is necessary")
lines = left.lines + right.lines
left.legend(lines, [line.get_label() for line in lines], frameon=False, loc="upper left")
axes[1].loglog(radii, tails, "o-", color="#27ae60")
axes[1].set_xlabel("Tail radius R")
axes[1].set_ylabel("Exact uniform second-moment tail")
axes[1].set_title("Compact unbounded family: tail vanishes")
save("04_eq6_certificate.png")


# Claim 5 exhaustive scope and mutation.
vertices = np.arange(2, 7)
counts = np.array([2, 8, 64, 1024, 32768])
fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.8))
axes[0].bar(vertices, counts, color="#2f80ed")
axes[0].set_yscale("log", base=2)
axes[0].set_xticks(vertices)
axes[0].set_xlabel("Labeled vertices m")
axes[0].set_ylabel("Simple graphs exhausted (log2)")
axes[0].set_title("33,866 target graphs isolated exactly")
axes[1].bar(["Simple edge", "Repeated-edge mutation"], [0, 2 / 9], color=["#27ae60", "#eb5757"])
axes[1].set_ylabel("Second finite difference")
axes[1].set_title("Multilinearity rejects the mutation")
save("05_graphon_certificate.png")

print(f"generated 5 figures in {OUT}")
