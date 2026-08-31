# Use-case and logic release

## Decision

The candidate logic, trigger, input, terminology, trace, and synthetic-test contract is complete enough to enter Module 03 historical evidence and threshold analysis for curriculum construction, with conditions.

## Inherited use case

- Fictional service: `CGH-GIM-01`.
- Primary user: the clinician responsible for the current adult encounter.
- Candidate hook: `patient-view` version `1.0`, invoked in the fictional workflow after intake information is available and before encounter close.
- Intended support: a nonbinding candidate card asking the clinician to consider whether confirmatory HbA1c testing is appropriate.
- Nonaction: no diagnosis, order, treatment, message, score display, or patient-facing action occurs automatically.
- Decision owner: `CGH-GIM-01 clinical decision support governance council`.

## Mechanics release

The ordered reference rule checks service and context, idempotency, event-time input readiness, terminology and unit validity, known-diabetes suppression, a candidate prior-HbA1c lookback, mock-score availability, a mock threshold branch, and response delivery. Every exit has a reason code and preserves clinician control.

The candidate lookback of 365 days and mock threshold of `0.20` are branch-test fixtures. They have not been clinically selected, estimated, recommended, or accepted. The score values are supplied fixtures, not predictions.

## Workflow and trace view

`service -> context -> idempotency -> input readiness -> semantics -> suppressions -> mock score -> mock threshold -> delivery`

The evaluator moves from left to right and stops at the first failed condition. Each stop records one stable terminal reason. A delivered candidate result and a silent delivery failure share the same path through the mock threshold branch but differ at the final transport step.

## Data result

The pinned release contains all 25 generated FHIR files, 811,803 resource rows, zero parse failures, and 11,109 duplicate resource IDs. The duplicates are preserved and must not enter an analytic join without an explicit entity-resolution decision.

All 16 Commons cases match their expected result and ordered trace, including missing, stale, inconsistent, duplicate, delayed, terminology, version, unit, context, suppression, and silent-delivery failures.

## Conditions

Clinical, interoperability, terminology, human-factors, safety, patient-access, privacy, accessibility, responsible-AI, and independent-reproduction reviews remain open. Module 03 must replace the mock score with a governed historical evidence process and must analyze rather than inherit the mock threshold.

## Permitted next action

Construct Module 03 historical evidence, calibration, decision-threshold, temporal, and subgroup analyses for curriculum use. Model fitting inside Module 02, threshold acceptance, real-patient scoring, clinical alerting, implementation, and deployment remain prohibited.
