# Evaluator-blind red-team record

The reviewer used only the staged candidate tree and the evaluator rubric. It
did not use OpenResearch logs, dashboard artifacts, unpublished branches, or
instructions about where evidence was stored.

## Pass 1 — pre-fix

Entry points opened: `README.md`, `logbook.json`, `pages/index.md`.

The reviewer then opened the current summary, all six claim pages,
`reproduce`, and the visibility matrix. All six claims and all six complete
visibility rows were located. Historical `verify` and `overview` hashes still
matched the protected revision.

Items not immediately verifiable:

- Claim 3 linked its certificate but did not use the explicit label `Source:`.
- Claim 4 linked its certificate but did not use the explicit label `Source:`.
- Claim 5 linked its certificate but did not use the explicit label `Source:`.
- The visibility matrix linked this red-team record before it existed.

Fix: add explicit source labels and materialize this record. No scientific
verdict, number, code path, or historical evidence changed.

## Pass 2 — post-fix

Audit label: `post-fix-2`.

Files opened from the canonical entrypoints:

- `README.md`
- `logbook.json`
- `pages/index.md`
- `pages/current-summary/page.md`
- `pages/claim-1/page.md`
- `pages/claim-2/page.md`
- `pages/claim-3/page.md`
- `pages/claim-4/page.md`
- `pages/claim-5/page.md`
- `pages/claim-6/page.md`
- `pages/reproduce/page.md`
- `pages/visibility-matrix/page.md`

Result: six claims located, six complete visibility rows located, no missing
links, and no unresolved conclusions. The historical `pages/verify/page.md`
and `pages/overview/page.md` files remained byte-identical to the protected
judged revision. The automated audit returned `passed: true`.
