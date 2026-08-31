# APP-4 course contract plan

## Purpose

Define APP-4, Data for Clinical Decision Support, as a distinct 3-credit applied course before building its first module. The contract must preserve the source curriculum, the official half-term calendar, the course's own 40 / 25 / 35 assessment weights, and the program rule that each applied course revisits foundations through a different clinical decision.

## Authority

- Authoritative source: `08-APP-4-Clinical-Decision-Support.docx` from both supplied curriculum archives.
- Source identity: 21,676 bytes; SHA-256 `20d651c3a777c878fa2d1219738366b99da76ba985e6082c73168cf8df63ded2`.
- Calendar authority: https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf
- Program architecture: `docs/specs/2026-08-29-curriculum-master-architecture-spec.md`.
- Ownership map: `docs/curriculum/CROSS-COURSE-CONCEPT-OWNERSHIP.md`.
- Prior handoffs: accepted FND-1, FND-2, DA-730, and APP-1 through APP-3 specifications and releases.

## Course decisions to lock

1. Use seven instructional weeks plus the official half-term end date, totaling 112.5 learner hours.
2. Preserve the source assessment components as 40 points at Week 3, 25 points at Week 6, and 35 points on the official half-term end date.
3. Use a continuing fictional adult general internal medicine service, `CGH-GIM-01`, to decide whether an advisory card about confirmatory HbA1c testing may advance from offline sandbox review to a locally governed silent-mode evaluation.
4. Use complete official NHANES releases for historical risk evidence, calibration, temporal holdout, and subgroup analysis. Do not treat NHANES as local workflow evidence or deployment validation.
5. Use a versioned synthetic FHIR R4 and CDS Hooks teaching layer for trigger timing, data availability, alert burden, workflow, calibration drift, stale inputs, missing inputs, and silent failure.
6. Keep the decision support advisory only. It cannot diagnose, order, deny, target a patient, change care, or run in production.
7. Put the embedded ML comparison in Module 06. Compare one fixed challenger with the accepted transparent model on identical splits, thresholds, alert budgets, and safety rules.
8. Assign Module 07 to Joe Joseph, MD, SFHM, under the dated identity boundary already accepted by the Commons. Direct participation and final biography wording remain pre-alpha conditions.

## Durable artifacts

- `docs/source/app-4-clinical-decision-support-source-record.md`
- `docs/curriculum/courses/APP-4/course-spec.md`
- `courses/clinical-decision-support/README.md`
- APP-4 checks in `scripts/check-curriculum-specs.ps1`
- APP-4 status and handoff updates in `README.md` and `docs/curriculum/BUILD-LEDGER.md`
- Commons version `0.76.0`

## Module architecture

| Module | Working title | Hours | Point role |
|---:|---|---:|---:|
| 01 | Framing a decision support use case | 15.5 | Required gate |
| 02 | Decision support logic, triggers, and data | 16.0 | 20 |
| 03 | Evidence, calibration, and validation | 16.5 | 20 |
| 04 | Alert burden, human factors, and equity | 16.5 | 25 |
| 05 | Sandbox prototype and failure modes | 16.0 | Required gate |
| 06 | Safety case, monitoring, governance, and embedded ML | 16.0 | Required gate |
| 07 | Clinician leadership, product brief, and defense | 16.0 | 35 |
| Total |  | 112.5 | 100 |

## Checkpoint architecture

- Week 3: logic, evidence, calibration, and validation readiness, 40 points.
- Week 6: workflow, alert burden, sandbox, failure-mode, safety, monitoring, governance, and embedded-ML release, 25 points.
- Official half-term end date: final clinical decision support package and defense, 35 points.

## Acceptance checks

- The source fingerprint and byte-identical archive comparison are recorded.
- Seven distinct modules total 112.5 hours.
- The three checkpoints total 100 points with no duplicate scoring.
- NHANES and synthetic FHIR/CDS Hooks roles are separate and explicit.
- Technical foundations, applied ownership, embedded ML, and clinician leadership are distinct.
- Each module has a decision, evidence contract, submission, protected handoff, and out-of-scope boundary.
- The course cannot authorize live clinical use, patient-level action, automatic ordering, production scoring, or deployment.
- The repository validator enforces the course contract and Commons version.

## Build order after this contract

1. Build Module 01 as a runnable source-feasibility and decision-charter release.
2. Build Modules 02 and 03, then freeze Checkpoint 01.
3. Build Modules 04 through 06, then freeze Checkpoint 02.
4. Build Module 07 and the final checkpoint.
5. Run the full curriculum regression after every isolated unit, then commit and push that unit with its semantic version decision.
