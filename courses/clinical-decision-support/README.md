# APP-4: Data for Clinical Decision Support

- Course ID: APP-4.
- Credits: 3.
- Prerequisites: FND-1 and FND-2.
- Total learner work: 112.5 hours.
- Current Commons release: 0.81.0.
- Current build: Modules 01 through 04 and Checkpoint 01 are runnable release candidates; Module 05 is next.

APP-4 teaches learners to decide whether a prediction or rule can support one clinician at one workflow moment without creating unacceptable burden or harm. The course covers intended use, logic, triggers, input availability, calibration, thresholds, alert burden, human factors, a nonproduction prototype, failure modes, safety, monitoring, governance, and clinician-led defense.

The continuing case is an explicitly fictional adult general internal medicine and primary care service, `CGH-GIM-01`. Learners assess an advisory card that asks a clinician to consider confirmatory HbA1c testing. Public NHANES releases supply historical evidence. A separate synthetic FHIR R4 and CDS Hooks layer supplies workflow, burden, drift, interaction, and silent-failure evidence.

## Module sequence

| Module | Title | Hours | Build status |
|---:|---|---:|---|
| 01 | Framing a decision support use case | 15.5 | Runnable release candidate |
| 02 | Decision support logic, triggers, and data | 16.0 | Runnable release candidate |
| 03 | Evidence, calibration, and validation | 16.5 | Runnable release candidate |
| 04 | Alert burden, human factors, and equity | 16.5 | Runnable release candidate |
| 05 | Sandbox prototype and failure modes | 16.0 | Specified |
| 06 | Safety case, monitoring, governance, and embedded machine learning | 16.0 | Specified |
| 07 | Clinician leadership, product brief, and defense | 16.0 | Specified |
| Total |  | 112.5 |  |

## Checkpoints

- Week 3: 40-point logic, evidence, calibration, and validation readiness package. Runnable release candidate.
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

The third runnable package is [Module 03](modules/03-evidence-calibration-validation/README.md), governed by its [durable specification](../../docs/curriculum/courses/APP-4/modules/03-evidence-calibration-validation-spec.md). It verifies all 16 inherited NHANES sources, releases 14,892 age-eligible audit rows and 7,544 model rows with 328 outcomes, fits one fixed development-only weighted GLM, and evaluates a 1,806-row temporal holdout plus a separate 2,086-row transport stress test. Its 118-file learner or reference workspace contains 102 immutable files and 15 assessed records. The `continue with conditions` reference decision permits Checkpoint 01 assembly, keeps all six evidence thresholds unaccepted, rejects `0.20` as evidence, and prohibits Module 04 until the cumulative checkpoint passes.

The first runnable cumulative package is [Checkpoint 01](checkpoints/01-logic-evidence-validation-readiness/reference/README.md), governed by its [durable specification](../../docs/curriculum/courses/APP-4/checkpoints/01-logic-evidence-validation-readiness-spec.md). It freezes 245 files from the complete Module 01 through Module 03 reference workspaces and independently protects 204 nested immutable files. Module 01 remains a required zero-point gate. Module 02 and Module 03 contribute 20 points once each. The 263-file learner or reference workspace passes 1,284 reference checks and 1,245 learner checks. Its `continue with conditions` decision permits bounded Module 04 curriculum construction while all six evidence candidates remain unaccepted and every clinical-use, implementation, and deployment route remains prohibited.

The fourth runnable package is [Module 04](modules/04-alert-burden-human-factors-equity/README.md), governed by its [durable specification](../../docs/curriculum/courses/APP-4/modules/04-alert-burden-human-factors-equity-spec.md). It carries the complete Week 3 reference release into a 302-file learner or reference workspace, builds 1,200 synthetic encounter opportunities and 7,200 candidate-event rows, and compares six interruptive banners, six passive contextual panels, and no alert. The 25-point reference passes all 20 gates and permits only `panel-t003` Module 05 sandbox construction. The `0.03` value remains an unaccepted sandbox fixture.

No package may connect to a live clinical system, process real patient data, display a clinical alert, diagnose, order, deny, target, score real patients, implement, or deploy.
