# Reference AI-use record

- Date: 2026-08-30.
- Tool and model: OpenAI Codex.
- Purpose: draft the descriptive contract, standard-library calculations, notebook, records, and independent checks.
- Data shared: public synthetic Synthea-derived fields, aggregate counts, and non-identifying synthetic rows.
- Advice used: keep result IDs and denominator definitions together; pair mean with median for skewed counts; preserve structural missingness; label strata unadjusted.
- Human verification: recomputed source counts, compared formulas with Python statistics documentation, ran independent validation, executed the notebook, and reproduced outputs byte for byte.
- Decision: accepted with edits and retained human-review conditions.
- Affected artifacts: builder, output schemas, denominator registry, memo, notebook, assessment, validator, and release record.

AI output is not evidence by itself. Source rows, formulas, exact output files, and the validator provide the technical evidence.
