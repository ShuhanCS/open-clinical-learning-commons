# Instructor notes and answer key

## Teaching decision

Begin with grain and source identity. Do not let the exercise become a race to call every blank or extreme value bad. The learner's job is to decide what evidence warrants correction and what must remain visible as a condition.

## Reference facts

| Fact | Expected |
|---|---:|
| Accepted rows / fields | 374 / 29 |
| Defective rows / distinct people | 379 / 374 |
| Exact duplicates | 5 |
| Seeded defect families / cases | 20 / 56 |
| Manifest changes | 68 |
| Natural rules / total rules | 8 / 28 |
| Accepted missing death dates | 343 |
| Accepted paired missing reason fields | 226 each |
| Accepted no-next-event companion blanks | 263 each |
| Accepted ages at least 100 | 5 |
| Prior encounter counts above 100 | 2 |
| Prior medication counts above 100 | 1 |
| Rows in race categories below 10 | 6 |
| Urgent-state or death-endpoint rows | 12 |

## Review sequence

1. Verify source bytes and immutable layer separation.
2. Reconcile rows, people, duplicate cases, and manifest changes.
3. Inspect all 29 profile and missingness rows.
4. Re-run all 28 detectors rather than trusting registered counts.
5. Ask the learner to defend one blocking correction, one retained extreme, one optional blank, and one small-cell condition.
6. Confirm issue IDs align across rule, risk, and resolution records.
7. Verify the resolved file equals the accepted file byte for byte.
8. Review the notebook narrative, reproduction record, AI disclosure, and final disposition.

## Common interventions

- If all incomplete rows are dropped, show the denominator loss and require rule-specific restoration.
- If age 100 or high utilization is called impossible, require source tracing and an explicit validity boundary.
- If blank next-event companions are filled, return to the explicit `No encounter recorded` state contract.
- If a learner edits the defective CSV manually, require a fresh deterministic build.
- If `resolved` is called clinically valid, narrow the claim to technical restoration of a synthetic release.

## Reference decision

Initial defect layer: `fix`. Resolved release: `proceed with conditions`.

Faculty, Python/notebook, clinical informatics, data quality, accessibility, privacy, responsible-AI, and independent reproduction reviews remain pending before alpha promotion.
