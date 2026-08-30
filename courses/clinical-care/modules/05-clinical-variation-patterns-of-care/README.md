# APP-1 Module 05: Clinical variation and patterns of care

This module turns the accepted 476-person care-transition cohort into a reproducible analysis of recorded follow-up, treatment orders, procedures, utilization, outcomes, clinical subgroup, teaching-site, and time variation.

The reference uses 1,694 post-landmark encounter rows, 742 medication rows, 1,832 procedure rows, and 92 care-plan rows from the full pinned Synthea database. It generates no new clinical records. A medication row is treated as recorded treatment exposure, never medication adherence.

The main teaching finding is deliberately bounded. Recorded scheduled follow-up ranges from 22.99% at SITE-E to 37.80% at SITE-F, an absolute spread of 14.82 percentage points. The global six-site p-value is 0.27993975, and all sites are synthetic labels with a known direct effect of zero. The spread supports a prospective measurement question, not a site grade or causal claim.

## Build the reference outputs

```powershell
python build_variation.py --database <accepted-synthea-sqlite> --target <new-output-directory>
```

The builder verifies the database, Module 02 cohort, and Module 04 expected-outcome fingerprints; opens SQLite read-only; writes eleven deterministic outputs; and refuses an existing target.

## Build a learner workspace

```powershell
python build_workspace.py --target <new-workspace>
python <new-workspace>/build_variation.py --database <accepted-synthea-sqlite> --cohort <analysis-cohort.csv> --expected <expected-outcomes.csv> --target <new-workspace>/outputs
python <new-workspace>/validate_variation.py <new-workspace> --submission
```

## Boundaries

- All patient and clinical records are synthetic.
- A record does not prove care need, access, attendance, quality, completion, adherence, benefit, or harm.
- Counts and rates describe this source, not real care utilization.
- SITE-A through SITE-F are fixed synthetic teaching labels, not facilities.
- No causal, efficacy, fairness, ranking, real-population, or deployment claim is supported.

Module version: 0.1.0. Commons release: 0.53.0.

Durable specification: `docs/curriculum/courses/APP-1/modules/05-clinical-variation-patterns-of-care-spec.md`.
