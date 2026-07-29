# Evaluator-blind retry red-team record

The review uses only a freshly staged candidate and the evaluator rubric. It
does not use OpenResearch logs, unpublished branches, or repository knowledge
to locate evidence.

## Pass 1 — pre-final provenance

Entry points: `README.md`, `logbook.json`, `pages/index.md`.

Files requested by navigation: retry summary, Claims 1–6, retry reproduce,
complete runner source, and retry visibility matrix. The automated pass must
locate six claims, six complete visibility rows, inline Python on Claims 3–6,
the complete current runner, per-claim raw JSON and checker output, and
byte-identical historical pages.

Automated result: six claims located, six complete visibility rows, no missing
links, no unresolved conclusions, and all eleven judged pages byte-identical.

## Pass 2 — post-fix candidate

After importing formal run `0881b838-e36f-4959-b7ab-78183437f876`, the
reviewer again opened:

- `README.md`
- `logbook.json`
- `pages/index.md`
- `pages/retry-summary/page.md`
- `pages/claim-1/page.md`
- `pages/claim-2/page.md`
- `pages/retry-claim-3/page.md`
- `pages/retry-claim-4/page.md`
- `pages/retry-claim-5/page.md`
- `pages/retry-claim-6/page.md`
- `pages/retry-reproduce/page.md`
- `pages/runner-source/page.md`
- `pages/retry-visibility-matrix/page.md`

Release is allowed only if the second automated traversal again reports
`passed: true`; its output is copied into the final release report.
