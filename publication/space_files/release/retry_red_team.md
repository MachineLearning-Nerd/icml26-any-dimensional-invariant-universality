# Evaluator-blind retry red-team record

The review uses only a freshly staged candidate and the evaluator rubric. It
does not use OpenResearch logs, unpublished branches, or repository knowledge
to locate evidence.

## Pass 1

Entry points: `README.md`, `logbook.json`, `pages/index.md`.

Files requested by navigation: retry summary, Claims 1–6, retry reproduce,
complete runner source, and retry visibility matrix. The automated pass must
locate six claims, six complete visibility rows, inline Python on Claims 3–6,
the complete current runner, per-claim raw JSON and checker output, and
byte-identical historical pages.

Any missing item blocks release. The completed post-fix pass and exact opened
file list are recorded by `publication/audit_candidate.py` before upload.
