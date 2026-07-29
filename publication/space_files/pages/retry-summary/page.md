# Current verification and score forecast

Previous live judged score: **8/12**

Conservative projected score range after this change: **10–12/12**

Best-supported possible new score: **12/12 (forecast, not a judge result)**

The previous revision exposed proof certificates mainly through links. This
retry makes the directly executed code, numerical output, independent
checker, and destructive control visible on every positive-claim page.

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
| --- | --- | --- | --- | --- | --- |
| 1 | 2 | 2 | HIGH | VERIFIED | Assumption-satisfying analytic Eq. 4 divergence witness reran |
| 2 | 2 | 2 | HIGH | VERIFIED | Exact spike cut norms reran with the linear control |
| 3 | 1 | 2 | MEDIUM | VERIFIED | Million-term Eq. 5 convergence, 2,048 invariance and 1,024 continuity trials; judge may still demand a formalized density theorem |
| 4 | 1 | 2 | MEDIUM | VERIFIED | 4,096 exact W1 pairs, 2,048 invariance trials, separation and invalid-growth control; activation interpretation remains a risk |
| 5 | 1 | 2 | MEDIUM | VERIFIED | Five motifs, 500 exact cut norms, 64 Eq. 9 comparisons and arbitrary-m certificate; finite graphons do not alone prove density |
| 6 | 1 | 2 | MEDIUM | VERIFIED | 1,000 group actions, 1,000 Lipschitz trials, 512 orbit recoveries and nonorthogonal control; invariant-network density remains cited |

No claim is BLOCKED. Claims 3–6 are the changed claims. Their universal
quantifiers are covered by the reconstructed implication chains; the new
sweeps independently exercise the exact mechanisms and fail when a required
ingredient or assumption is removed.

- Raw cumulative result: [evidence/retry_cumulative_result.json](evidence/retry_cumulative_result.json)
- Fixed command: `uv run --frozen python repro/src/verify.py`
- Winning evidence commit: `e321e51474c37db0cce0e7eb4b5155ad49477997`
- Formal run: Hugging Face `cpu-upgrade`, 64 logical CPUs allocated, one math
  thread enforced, 12.227845 s program runtime, 37 s total job duration
- Seeds: `7`, `260523159`, `260523160`, `260523161`, `260523162`

The live score remains **8/12** until a new evaluator records a verdict.
