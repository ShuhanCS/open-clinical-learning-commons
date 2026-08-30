# APP-2: Data for Patient Experience and Engagement

- Course ID: APP-2.
- Credits: 3.
- Prerequisites: FND-1 and FND-2.
- Total learner work: 112.5 hours.
- Current Commons release: 0.64.0.
- Current build: all seven modules and all three cumulative checkpoints are runnable release candidates.

APP-2 teaches patient-reported measurement, survey representation, response bias, linked patient evidence, patient voice, patient partnership, and accountable improvement.

The course uses the complete public CMS HCAHPS hospital file as its first source. Later modules add current AHRQ MEPS public-use person and event files. Synthetic data are allowed only for patient comments and a known response-selection mechanism that public sources cannot provide safely.

## Module sequence

| Module | Title | Hours | Build status |
|---:|---|---:|---|
| 01 | Framing a patient-experience and engagement decision | 15.5 | Runnable release candidate |
| 02 | Patient-reported measurement and scale construction | 16.0 | Runnable release candidate |
| 03 | Response, representation, and survey bias | 16.5 | Runnable release candidate |
| 04 | Linked patient evidence | 16.5 | Runnable release candidate |
| 05 | Patient voice, group differences, and equity | 16.0 | Runnable release candidate |
| 06 | Partnered improvement and embedded machine learning | 16.0 | Runnable release candidate |
| 07 | Clinician and patient leadership, accountability, and defense | 16.0 | Runnable release candidate |
| Total |  | 112.5 |  |

## Checkpoints

- Week 3: 20-point measurement and representation readiness package.
- Week 6: 45-point linked evidence and patient-voice package.
- Official half-term end date: 35-point patient-experience and engagement package.

## Current runnable units

[Module 01](modules/01-patient-experience-decision/README.md) frames the recovery-at-home patient-experience decision against the full 325,720-row CMS HCAHPS source. Its durable contract is [the Module 01 specification](../../docs/curriculum/courses/APP-2/modules/01-patient-experience-decision-spec.md).

[Module 02](modules/02-patient-reported-measurement/README.md) fixes the updated HCAHPS Q22/Q23 measurement and scoring contract using the complete current instrument suite, a 240-row synthetic response fixture, and a 3,610-facility public-score concordance. Its durable contract is [the Module 02 specification](../../docs/curriculum/courses/APP-2/modules/02-patient-reported-measurement-spec.md).

[Module 03](modules/03-response-representation-bias/README.md) uses the full public MEPS HC-256 person file and a deterministic synthetic response layer to teach target, frame, response, item missingness, subgroup representation, and one bounded response adjustment. Its durable contract is [the Module 03 specification](../../docs/curriculum/courses/APP-2/modules/03-response-representation-bias-spec.md).

[Checkpoint 01](checkpoints/01-measurement-representation-readiness/README.md) freezes 135 accepted files from Modules 01 through 03, carries the 20-point Module 02 score exactly once, and controls progression into linked analysis. Its durable contract is [the Week 3 checkpoint specification](../../docs/curriculum/courses/APP-2/checkpoints/01-measurement-representation-readiness-spec.md).

[Module 04](modules/04-linked-patient-evidence/README.md) uses all five official MEPS person and event products to teach governed linkage, aligned denominators, access and communication measures, digital-channel limits, and noncausal service-use interpretation. Its durable contract is [the Module 04 specification](../../docs/curriculum/courses/APP-2/modules/04-linked-patient-evidence-spec.md).

[Module 05](modules/05-patient-voice-equity/README.md) uses a governed 420-comment synthetic corpus, a transparent coding and agreement exercise, bounded assisted classification, and design-aware public MEPS group comparisons to teach patient voice and equity reasoning without prevalence, causal, targeting, or proof-of-inequity claims. Its durable contract is [the Module 05 specification](../../docs/curriculum/courses/APP-2/modules/05-patient-voice-equity-spec.md).

[Module 06](modules/06-partnered-improvement-embedded-ml/README.md) turns the accepted evidence into a patient-partnered improvement proposal and compares the exact transparent response cells with one bounded random forest on 377 held-out records. The model does not meet the prespecified threshold for changing the adjustment decision. Its reference partnership record is a labelled simulation, and a named patient or caregiver partner remains required before alpha. Its durable contract is [the Module 06 specification](../../docs/curriculum/courses/APP-2/modules/06-partnered-improvement-embedded-ml-spec.md).

[Checkpoint 02](checkpoints/02-linked-evidence-patient-voice-release/reference/README.md) freezes all 160 accepted Module 04 through Module 06 files, counts 25 and 20 points once, and carries the complete linked-evidence, patient-voice, equity, partnership, improvement, and model decision into Module 07. Its durable contract is [the Week 6 checkpoint specification](../../docs/curriculum/courses/APP-2/checkpoints/02-linked-evidence-patient-voice-release-spec.md).

[Module 07](modules/07-clinician-patient-leadership-defense/README.md) freezes both accepted checkpoints into a 358-file leadership candidate. It requires shared clinician and patient authority, a patient-facing summary, a bounded universal-offer proposal, 14 monitoring measures, 14 stop rules, and a 14-question defense. Its durable contract is [the Module 07 specification](../../docs/curriculum/courses/APP-2/modules/07-clinician-patient-leadership-defense-spec.md).

[Final Checkpoint 03](checkpoints/03-patient-experience-engagement-package/README.md) freezes all 358 Module 07 files, records the final 35-point component once, and adds 15 final-review files. Its package is `accept with conditions`, while the organizational recommendation remains `revise before testing`. Its durable contract is [the final-checkpoint specification](../../docs/curriculum/courses/APP-2/checkpoints/03-patient-experience-engagement-package-spec.md).

The full course contract is [the APP-2 course specification](../../docs/curriculum/courses/APP-2/course-spec.md). Source normalization is recorded in [the APP-2 source record](../../docs/source/app-2-patient-experience-engagement-source-record.md).

No package authorizes clinical implementation, patient targeting, hospital ranking, or ML deployment.
