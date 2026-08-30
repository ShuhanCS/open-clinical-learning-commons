# Reference AI-use record

## Material use

- Date: 2026-08-30.
- Tool and model: OpenAI Codex.
- Purpose: draft deterministic defect rules, profiling code, teaching records, and independent validation checks.
- Data shared: public synthetic Synthea-derived schema, aggregate counts, and non-identifying synthetic rows.
- Advice used: separate immutable accepted and defective layers; test grain before missingness; distinguish invalid values from supported extremes; align risk and resolution records by issue ID.
- Human verification route: rebuilt the defect layer and profiles from the frozen accepted source, reconciled manifest values and all rule counts, executed the notebook, and compared outputs byte for byte.
- Decision: accepted with edits and retained human-review conditions.
- Affected files: Python builder, profiler, validator, notebook, specifications, logs, assessment, instructor notes, and release record.

AI output is not evidence by itself. The accepted fingerprint, manifest, independent detectors, and clean reproduction provide the technical evidence.
