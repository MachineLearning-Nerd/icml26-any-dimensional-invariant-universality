# Claim 2 — pointwise nonlinearity is cut-discontinuous

**Status: VERIFIED · Confidence: HIGH**

## Exact contract

Theorem 4.9, Section 4.2: a pointwise operator on the kernel space is
cut-norm continuous only when the scalar map is linear. The reproduction
checks the discontinuous nonlinear direction and the continuous linear
direction.

For `W_n=n 1_[0,1/n]^2`, the exact identities are
`||W_n||_square=1/n`, `||W_n^2||_square=1`, and
`||3W_n||_square=3/n`.

## Observed evidence

| n | `||W_n||_square` | `||W_n^2||_square` | `||3W_n||_square` |
| ---: | ---: | ---: | ---: |
| 4 | 0.25 | 1 | 0.75 |
| 6 | 0.166666667 | 1 | 0.5 |
| 8 | 0.125 | 1 | 0.375 |
| 11 | 0.090909091 | 1 | 0.272727273 |
| 14 | 0.071428571 | 1 | 0.214285714 |
| 16 | 0.0625 | 1 | 0.1875 |

Every identity is checked to `1e-12`. The nonlinear image remains at one
while the input tends to zero. The linear control tends to zero at the exact
expected rate.

## Control and limitations

The linear map is the required passing control. A single exact sequence is
enough to establish discontinuity of the nonlinear map; the reproduction does
not claim that its six displayed truncations alone prove the full “only if”
classification, which remains the cited theorem-level premise.

- Source: [repro/src/verify.py](repro/src/verify.py)
- Raw data: [evidence/cumulative_result.json](evidence/cumulative_result.json)
- Command/provenance: [Reproduce](#/reproduce)
