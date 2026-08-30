# APP-2: Data for Patient Experience and Engagement

- Course ID: APP-2.
- Credits: 3.
- Prerequisites: FND-1 and FND-2.
- Total learner work: 112.5 hours.
- Current Commons release: 0.56.0.
- Current build: Module 01 runnable; Modules 02 through 07 and all checkpoints specified at course level but not yet built.

APP-2 teaches patient-reported measurement, survey representation, response bias, linked patient evidence, patient voice, patient partnership, and accountable improvement.

The course uses the complete public CMS HCAHPS hospital file as its first source. Later modules add current AHRQ MEPS public-use person and event files. Synthetic data are allowed only for patient comments and a known response-selection mechanism that public sources cannot provide safely.

## Module sequence

| Module | Title | Hours | Build status |
|---:|---|---:|---|
| 01 | Framing a patient-experience and engagement decision | 15.5 | Runnable release candidate |
| 02 | Patient-reported measurement and scale construction | 16.0 | Specified in course contract |
| 03 | Response, representation, and survey bias | 16.5 | Specified in course contract |
| 04 | Linked patient evidence | 16.5 | Specified in course contract |
| 05 | Patient voice, group differences, and equity | 16.0 | Specified in course contract |
| 06 | Partnered improvement and embedded machine learning | 16.0 | Specified in course contract |
| 07 | Clinician and patient leadership, accountability, and defense | 16.0 | Specified in course contract |
| Total |  | 112.5 |  |

## Checkpoints

- Week 3: 20-point measurement and representation readiness package.
- Week 6: 45-point linked evidence and patient-voice package.
- Official half-term end date: 35-point patient-experience and engagement package.

## Current runnable unit

[Module 01](modules/01-patient-experience-decision/README.md) frames the recovery-at-home patient-experience decision against the full 325,720-row CMS HCAHPS source. Its durable contract is [the Module 01 specification](../../docs/curriculum/courses/APP-2/modules/01-patient-experience-decision-spec.md).

The full course contract is [the APP-2 course specification](../../docs/curriculum/courses/APP-2/course-spec.md). Source normalization is recorded in [the APP-2 source record](../../docs/source/app-2-patient-experience-engagement-source-record.md).

No package authorizes clinical implementation, patient targeting, hospital ranking, or ML deployment.
