# Claim 3 method — current direct route

The primary retry verifier directly executes Equation 5:

1. evaluates the independently known Basel limit through 2,000,000 terms;
2. runs 2,048 permutation/zero-padding invariance trials;
3. runs 1,024 `ell_1` continuity trials against the analytic Lipschitz bound;
4. removes the norm weight in two destructive controls, both of which diverge;
5. calls a separately implemented checker.

The earlier implication certificate remains a secondary arbitrary-`p` audit.

The verifier follows the theorem's implication chain instead of fitting one
target. It:

1. symbolically validates the scalar, concatenation/addition, and
   concatenation/product outer constructors;
2. tests those constructors on 128 deterministic sequence instances,
   including permutation and zero-padding invariance;
3. checks the exact uniform tail bound on a compact infinite product family;
4. exhausts every distinct orbit pair in a finite sequence domain and builds
   the paper's multiplicity bump separator;
5. symbolically closes the two-stage UAT error budget for arbitrary positive
   `epsilon`, `delta`, and mass bound `B`;
6. invokes a separate exact-rational checker that imports none of the
   certificate implementation.

The negative controls use addition where multiplication is required, remove
the Equation 5 `ell_p` weight on the paper's divergent witness, and double the
permitted inner UAT error.

Fixed command: `uv run --frozen python repro/src/verify.py`.
Deterministic seeds: direct route `260523159`; certificate `260523156`.
