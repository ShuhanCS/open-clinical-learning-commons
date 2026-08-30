# Instructor notes

## Teaching emphasis

The central lesson is that a longitudinal cohort is a sequence of observable states rather than a filtered spreadsheet. Keep all 518 initial people visible. Ask learners to explain exactly when a field becomes knowable and why a person does or does not enter the day-30 risk set.

Use the nine index deaths to teach source semantics. Synthea records a death date while encounters use timestamps. The correction is not a nuisance detail: a wrong time interpretation changed the risk set from 476 to 485.

## Reference findings

- 518 initial people: 451 emergency and 67 inpatient indexes.
- 9 index deaths, 8 early post-discharge deaths, and 25 early acute returns.
- 476 landmark eligible: 129 exposed and 347 unexposed.
- 87 later events: 25 exposed and 62 unexposed.
- 389 administrative censors and no competing death before the first acute return.
- 1,018 event-audit rows.
- Six teaching sites with 68 to 88 people and at least ten events each.

## Misinterpretations to stop

- Do not call a recorded encounter completed or beneficial follow-up.
- Do not treat exposure as known at discharge.
- Do not remove death or early return from the flow.
- Do not call administrative censoring no care or no event forever.
- Do not describe cause-specific death censoring as automatically noninformative.
- Do not rank source organizations or teaching sites.
- Do not present the extension as observed source data.
- Do not estimate clinical efficacy or authorize implementation.

## Module 03 handoff

Module 03 receives the exact 476-row analysis cohort and complete event audit. It owns Kaplan-Meier estimation, log-rank comparison, guided Cox modeling, proportional-hazards checks, uncertainty, paired R reading, competing-event interpretation, and the cumulative Week 3 release.
