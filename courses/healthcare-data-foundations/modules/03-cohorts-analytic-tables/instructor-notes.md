# Instructor notes and answer key

## Teaching decision

Keep the review centered on whether the cohort definition and table are technically fit for the next module. Do not turn synthetic outcomes into clinical findings.

## Reference facts

| Fact | Expected |
|---|---:|
| Source patients | 1,171 |
| Source encounters | 53,346 |
| Acute period events | 1,243 |
| Emergency period events | 687 |
| Inpatient period events | 556 |
| Patients with an acute event | 481 |
| Patients with no acute event | 690 |
| Patients with only under-18 acute events | 107 |
| Adult eligible events | 1,048 |
| Included adults | 374 |
| Eligible non-index events | 674 |
| Emergency indexes | 314 |
| Inpatient indexes | 60 |
| No 30-day encounter recorded | 263 |
| Scheduled care within 30 days | 92 |
| Urgent care within 30 days | 4 |
| Acute return within 30 days | 15 |
| Any acute return within 90 days | 36 |
| Death within 90 days | 8 |
| No acute-return endpoint | 330 |

## Review sequence

1. Verify the Module 02 database fingerprint and logical table counts.
2. Ask the learner to distinguish events from people.
3. Test a birthday before, on, and after the event month and day.
4. Verify the adult filter occurs before event ranking.
5. Inspect the encounter-ID tie-breaker.
6. Confirm each history source is aggregated separately.
7. Test open-left and closed-right follow-up boundaries.
8. Reconcile all four cohort-flow rows.
9. Confirm post-index fields are labeled and not presented as baseline features.
10. Rebuild in a new target and compare all five files.

## Common interventions

- If 1,048 is reported as the cohort size, compare `COUNT(*)` with `COUNT(DISTINCT patient_id)`.
- If the cohort differs, check age calculation and whether ranking happened before the adult filter.
- If history counts are inflated, inspect for an encounter-by-condition-by-medication join product.
- If rows disappear, inspect for an inner join to optional follow-up.
- If no recorded encounter is called no care, require the learner to rewrite the claim.
- If output differs between reruns, inspect ordering, tie-breaking, line endings, and manual CSV edits.

## Human review still required

Faculty, SQL and data engineering, clinical informatics, temporal logic, accessibility, privacy, responsible-AI, and independent reproduction reviews remain pending before alpha promotion.
