# Claim 6 method

The verifier runs 1,000 combined orthogonal/permutation actions and compares
both normalized Gram kernels and five homomorphism-density readouts. It also
runs 1,000 Lipschitz pairs and 512 full-rank orbit recoveries using an
independently computed pseudoinverse transform.

The destructive control uses a nonorthogonal shear. It must have a nonzero
orthogonality gap, Gram gap, and hom-density readout gap. A separate checker
uses a fixed rotation and shear and imports none of the production functions.

Fixed command: `uv run --frozen python repro/src/verify.py`.
Seed: `260523162`.
