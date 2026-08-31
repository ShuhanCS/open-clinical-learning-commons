# APP-4: Data for Clinical Decision Support

- Course ID: APP-4.
- Credits: 3.
- Prerequisites: FND-1 and FND-2.
- Total learner work: 112.5 hours.
- Current Commons release: 0.78.0.
- Current build: Modules 01 and 02 are runnable release candidates; Module 03 is next.

APP-4 teaches learners to decide whether a prediction or rule can support one clinician at one workflow moment without creating unacceptable burden or harm. The course covers intended use, logic, triggers, input availability, calibration, thresholds, alert burden, human factors, a nonproduction prototype, failure modes, safety, monitoring, governance, and clinician-led defense.

The continuing case is an explicitly fictional adult general internal medicine and primary care service, `CGH-GIM-01`. Learners assess an advisory card that asks a clinician to consider confirmatory HbA1c testing. Public NHANES releases supply historical evidence. A separate synthetic FHIR R4 and CDS Hooks layer supplies workflow, burden, drift, interaction, and silent-failure evidence.

## Module sequence

| Module | Title | Hours | Build status |
|---:|---|---:|---|
| 01 | Framing a decision support use case | 15.5 | Runnable release candidate |
| 02 | Decision support logic, triggers, and data | 16.0 | Runnable release candidate |
| 03 | Evidence, calibration, and validation | 16.5 | Specified |
| 04 | Alert burden, human factors, and equity | 16.5 | Specified |
| 05 | Sandbox prototype and failure modes | 16.0 | Specified |
| 06 | Safety case, monitoring, governance, and embedded machine learning | 16.0 | Specified |
| 07 | Clinician leadership, product brief, and defense | 16.0 | Specified |
| Total |  | 112.5 |  |

## Checkpoints

- Week 3: 40-point logic, evidence, calibration, and validation readiness package.
- Week 6: 25-point workflow, sandbox, failure-mode, safety, monitoring, governance, and embedded-ML package.
- Official half-term end date: 35-point clinical decision support package and defense.

The Week 3 checkpoint combines the source course's 20-point use-case and logic specification and 20-point evidence, calibration, and threshold audit. The Week 6 checkpoint carries the 25-point workflow, alert-burden, and equity review once. Modules 05 and 06 add required prototype, safety, monitoring, governance, and ML gates without adding points.

## Public and synthetic sources

- NHANES continuous survey portal: https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/
- CDS Hooks 2.0.1: https://cds-hooks.hl7.org/
- FHIR R4: https://hl7.org/fhir/R4/
- Synthea 4.0.0: https://github.com/synthetichealth/synthea/releases/tag/v4.0.0
- ONC SAFER Guides: https://www.healthit.gov/topic/safety/safer-guides
- Synthetic service: `CGH-GIM-01`, generated and labeled as teaching data only.

The full course contract is [the APP-4 course specification](../../docs/curriculum/courses/APP-4/course-spec.md). Source normalization, the 16 full NHANES file routes, synthetic boundaries, and module routing are recorded in [the APP-4 source record](../../docs/source/app-4-clinical-decision-support-source-record.md).

The first runnable package is [Module 01](modules/01-cds-use-case-decision/README.md), governed by its [durable specification](../../docs/curriculum/courses/APP-4/modules/01-cds-use-case-decision-spec.md). It acquires and fingerprints all 16 complete NHANES XPT files, profiles 145,563 component rows and 442 source fields, verifies zero duplicate `SEQN` rows, releases a 41-file learner or reference workspace, and permits Module 02 curriculum construction with conditions without fitting a model or selecting a threshold.

The second runnable package is [Module 02](modules/02-logic-triggers-data/README.md), governed by its [durable specification](../../docs/curriculum/courses/APP-4/modules/02-logic-triggers-data-spec.md). It releases a complete 25-file, 811,803-row Synthea FHIR source; preserves 11,109 repeated provider and organization IDs; links 16 deterministic normal and failure cases; and creates an 86-file learner or reference workspace with 73 immutable files and 12 assessed records. The 20-point reference release passes every expected mechanics trace and permits Module 03 curriculum construction with conditions. The score and `0.20` value remain arbitrary fixtures, not predictions or an accepted clinical threshold.

No package may connect to a live clinical system, process real patient data, display a clinical alert, diagnose, order, deny, target, score real patients, implement, or deploy.
