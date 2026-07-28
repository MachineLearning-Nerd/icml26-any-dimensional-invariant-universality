# Current verification and score forecast

Previous live judged score: **9/12**

Conservative projected score range after this change: **11–12/12**

Best-supported possible new score: **12/12 (forecast, not a judge result)**

The candidate does not infer universality from a finite fit. Claims 3–5 use
machine-checkable implication certificates whose external mathematical
premises are named and whose constructive steps have independent checkers and
destructive controls.

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
| --- | --- | --- | --- | --- | --- |
| 1 | 2 | 2 | HIGH | VERIFIED | Assumption-satisfying analytic divergence witness; cumulative rerun passes |
| 2 | 2 | 2 | HIGH | VERIFIED | Exact spike cut norms verify nonlinear and linear directions |
| 3 | 1 | 2 | HIGH | VERIFIED | Exact Eq. 5 implication chain, 2,415 separation pairs, independent checker; standard theorems remain cited premises |
| 4 | 1 | 2 | MEDIUM | VERIFIED | Exact tail/UAT chain and independent checker; paper's listed activation examples are broader than its literal ratio definition |
| 5 | 1 | 2 | HIGH | VERIFIED | Arbitrary-m Boolean-lattice derivation plus all 33,866 labeled graphs through m=6 |
| 6 | 2 | 2 | HIGH | VERIFIED | Lipschitz, Procrustes recovery, identical-Gram and distinct-Gram controls rerun |

No claim is BLOCKED in the candidate. Claims 3–5 changed from historical TOY
evidence to current VERIFIED certificates. The live score remains **9/12**
until an evaluator judges the published revision.

Raw cumulative result: [evidence/cumulative_result.json](evidence/cumulative_result.json)

Independent checkers: [Claim 3](evidence/claim3_checker.json),
[Claim 4](evidence/claim4_checker.json), [Claim 5](evidence/claim5_checker.json)

- Fixed command: `uv run --frozen python repro/src/verify.py`
- Environment: Python 3.12, [pyproject.toml](pyproject.toml), [uv.lock](uv.lock)
- Backend/flavor: Hugging Face `cpu-upgrade`
- Estimated algorithm cores: 1; actual allocation visible: 64 logical CPUs;
  enforced math threads: 1
- Verifier runtime: 5.294494 s; total HF job duration: 26 s
- Seeds: baseline 7; Claim 3 260523156; Claim 4 260523157; Claim 5 260523158
