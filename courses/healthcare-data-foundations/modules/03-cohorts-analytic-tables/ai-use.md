# Reference AI-use record

## Material use

- Date: 2026-08-30.
- Tool and model: OpenAI Codex.
- Purpose: Draft SQL, contract documentation, and independent validation logic.
- Data shared: Public synthetic Synthea schema, aggregate counts, and non-identifying synthetic rows.
- Advice used: Named CTE structure, separate history aggregation, deterministic event tie-breaking, and invariant checks.
- Human verification route: Rebuilt the pinned upstream database, executed every SQL file, inspected boundary rules, and reproduced all outputs byte for byte.
- Decision: Accepted with edits and retained human-review conditions.
- Affected files: SQL, Python builder and validator, cohort and table specifications, assessment, instructor notes, and release record.

AI output is not evidence by itself. The pinned source, SQL results, and validator provide the technical evidence.
