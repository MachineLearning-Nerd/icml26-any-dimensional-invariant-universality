# Claim 1 — original DeepSets aggregation diverges

**Status: VERIFIED · Confidence: HIGH**

## Exact contract

Theorem 4.2, Section 4.1.1: the Equation 4 infinite aggregation need not
converge for a continuous inner map that decays too slowly, so the original
DeepSets extension is not continuous/universal on the any-dimensional
`ell_p` domain.

Assumptions audited: `p=2`; `X_i=i^-0.75`, hence
`sum_i |X_i|^2=sum_i i^-1.5<infinity`; `rho(x)=sqrt(|x|)` is continuous and
zero at zero.

## Observed evidence

| N | Equation 4 partial sum | Equation 5 weighted sum |
| ---: | ---: | ---: |
| 200 | 42.8781608006 | 1.7688439589 |
| 800 | 103.3347982974 | 1.7766083670 |
| 3,200 | 247.1752652220 | 1.7789217322 |
| 12,800 | 589.3169534069 | 1.7796098715 |

Equation 4 grows **13.743989×** versus the finite-horizon analytic
`N^0.625` ratio **13.454343**. Equation 5 changes only **0.604959%** over the
same 64× horizon.

## Control and limitations

The negative control is the Equation 5 weighting on the same divergent input;
it converges. The claim is falsified by one assumption-satisfying witness, so
no extrapolation from a finite sample is needed. The asymptotic exponent is
used as calibration, not to choose the horizon.

- Source: [repro/src/verify.py](repro/src/verify.py)
- Raw data: [evidence/cumulative_result.json](evidence/cumulative_result.json)
- Command/provenance: [Reproduce](#/reproduce)
