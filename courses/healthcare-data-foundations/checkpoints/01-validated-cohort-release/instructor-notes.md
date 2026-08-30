# Instructor notes and answer key

## Review purpose

Decide whether the learner has a trustworthy technical input for Module 04. Keep the review on source preservation, reproducibility, cohort meaning, table grain, and explanation. Do not turn synthetic outcome counts into clinical findings.

## Weight map

- Module 01 setup: 15 course points.
- Module 02 relational work: required gateway, no added course points.
- Module 03 SQL cohort: 25 course points.
- Checkpoint 1 total: 40 course points.
- Numeric pass threshold: 32.
- Gates and disposition still apply.

## Immutable source facts

- Archive bytes: 8,982,431.
- Archive SHA-256: `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a`.
- Source tables: 16.
- Source fields: 168.
- Source rows: 471,836.
- Database dictionary rows: 177.
- Database bytes in the tested build: 141,234,176.
- Database SHA-256 in the tested build: `1116dda22c4297fcfeab6bf2c99bb3dbfaf9f9b5e04041b96be90719c76e704a`.
- Foreign-key failures: 0.
- Integrity: `ok`.

## First-extract answer key

| Output | Rows | SHA-256 |
|---|---:|---|
| table-inventory.csv | 16 | `3f8fc12567ef57d1b74c21aa9fcfaedfac764c772e8d422ced002b7901358c07` |
| encounter-class-counts.csv | 6 | `26106dd682622ddbc6d75857a93607d48a353ba707ef56fc51d231be8f201d65` |
| observation-linkage.csv | 3 | `901e06e7c9b71b5e11daf021772837af9223338c921641aeff60cc1ca214dd12` |
| selected-patient-timeline.csv | 25 | `411a05229819cd5e7cfe9d678fc8920053db8e2be8cc93135c6fcb88d1b28a0c` |
| numeric-observation-sample.csv | 25 | `f6854aeeeca3a7083147f53fa7e41fd7797e3ee94f459864c087190126c2d940` |

## Cohort answer key

| Fact | Expected |
|---|---:|
| Source patients | 1,171 |
| Acute events in period | 1,243 |
| Patients with an acute event | 481 |
| No-acute exclusions | 690 |
| Under-18-only exclusions | 107 |
| Adult eligible events | 1,048 |
| Included adults | 374 |
| Eligible non-index events | 674 |
| Emergency indexes | 314 |
| Inpatient indexes | 60 |
| Analytic rows | 374 |
| Analytic fields | 29 |
| Query checks | 16 passing |

The conservation equation is `690 + 107 + 374 = 1,171`.

## Follow-up answer key

- No encounter recorded within 30 days: 263.
- Scheduled care: 92.
- Urgent care: 4.
- Acute return within 30 days: 15.
- Any acute return within 90 days: 36.
- Death within 90 days: 8.
- No acute-return endpoint: 330.
- Complete 90-day source coverage: 374.

`No encounter recorded` is not no care. Death and return fields are synthetic generator-derived observations, not real rates.

## SQL explanation key

- Completed age subtracts one when the event month and day precede the birth month and day.
- Adult filtering happens before ranking so a minor event cannot become the index for an adult-eligible patient.
- Encounter ID breaks timestamp ties.
- History ends immediately before index start.
- Follow-up starts strictly after index stop.
- Separate history CTEs prevent encounter-by-condition-by-medication multiplication.
- A left-preserving follow-up design retains people with no next recorded encounter.
- Death precedence applies only to the mutually exclusive endpoint, not to the separate flags.

## Review order

1. Scan for prohibited data and secrets.
2. Verify versions and release manifest.
3. Inspect environment and Git evidence.
4. Verify source, schema, dictionary, and first extracts.
5. Read cohort and table definitions before SQL.
6. Reconcile flow and keys.
7. Run complete validation.
8. Review AI verification and accessibility.
9. Conduct the defense.
10. Score each preserved component.
11. Record every gate and disposition.

## Common interventions

- Event count presented as patient count: compare `COUNT(*)` and distinct patient count.
- Wrong cohort after ranking: verify completed-age filtering occurs first.
- Inflated history: inspect for a multi-event join product.
- Missing people: inspect inner follow-up joins.
- Unsupported no-care statement: replace it with the exact source-observation wording.
- Changed immutable file: return to the owning module and version the change.
- Plausible AI explanation without evidence: require an independent query, source row, or official documentation check.

## Technical reference result

Reference assembly creates 45 files and a 35-row immutable manifest. Starter validation passes 295 checks. Complete reference validation passes 341 checks and invokes the Module 03 submission validator. Existing targets and incomplete checkpoint folders are rejected.

## Human review still required

Faculty, senior clinical analyst, SQL and data engineering, clinical informatics, reproducibility, accessibility, privacy, responsible-AI, and independent-instructor review remains pending before alpha promotion.
