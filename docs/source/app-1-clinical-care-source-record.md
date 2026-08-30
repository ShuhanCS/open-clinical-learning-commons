# APP-1 Data for Clinical Care source record

- Source course ID: APP-1.
- Source title: Data for Clinical Care.
- Source filename: `05-APP-1-Clinical-Care.docx`.
- Source bytes: 25,134.
- Source SHA-256: `00e1ecf99fe3ad365b21e934fca64c225b1a63a00067afcf451a06050a372d57`.
- Verified: 2026-08-30.
- Commons course specification: `docs/curriculum/courses/APP-1/course-spec.md`.

## Package comparison

The source document was verified in both supplied curriculum packages:

- `Curriculum-30-Credits-2026-08-29.zip`; and
- `OneDrive_2026-08-29 (1).zip`.

The APP-1 DOCX files are byte-for-byte identical and have the same SHA-256 fingerprint above.

## Source course identity

- Credits: 3.
- Source format: seven-week online block.
- Prerequisites: FND-1 and FND-2.
- Total learner work: 112.5 hours.
- Primary graded language: Python with pandas and notebooks.
- Query backbone: SQL.
- R role: read, run, and interpret survival-package code and output; writing R from scratch is not graded.
- Supporting practices: Git, semantic versioning, environment capture, source provenance, and accountable agent use.

## Source course purpose

APP-1 is the first applied course. Learners follow a clinical cohort over time, compare care and outcomes while accounting for baseline differences, and recommend a feasible care-pathway improvement. It takes longitudinal cohorts, censoring, survival analysis, risk adjustment, and clinical variation from foundation recognition to working skill.

APP-1 does not repeat the foundation courses. FND-1 owns general data retrieval, cohort construction, cleaning, and handoff. FND-2 owns general modeling, validity, testing, and governance. APP-1 reuses those skills to answer a named clinical-care decision.

## Source module sequence

| Week | Source module | Hours | Source submission |
|---:|---|---:|---|
| 1 | Framing a care-pathway decision | 15.5 | Care-pathway decision charter. |
| 2 | Longitudinal cohorts and follow-up | 16.0 | Validated phenotype and cohort with follow-up. |
| 3 | Survival and time-to-event outcomes | 16.5 | Survival analysis notebook. |
| 4 | Risk adjustment and fair comparison | 16.5 | Risk-adjusted comparison and interpretation memo. |
| 5 | Clinical variation and patterns of care | 16.0 | Clinical variation memo. |
| 6 | Equity, variation, and a feasible improvement | 16.0 | Equity checkpoint and draft improvement brief. |
| 7 | Integrated recommendation | 16.0 | Final clinical care improvement brief. |
| Total |  | 112.5 |  |

## Source learning objectives

The source defines six course objectives:

1. define a care-pathway decision, target population, treatment or exposure, comparison, outcome set, and evidence standard;
2. construct a longitudinal clinical cohort with phenotype, index, follow-up, outcome, and time-to-event definitions;
3. analyze time-to-event and other clinical outcomes with survival methods and transparent risk adjustment;
4. compare outcomes and patterns of care across treatments, sites, and time while accounting for case mix and measurement limits;
5. evaluate variation and equity across meaningful subgroups and sites without overstating causal claims; and
6. produce a clinical care improvement brief connecting evidence, feasibility, implementation measures, and next-step evaluation.

## Source assessment weights

| Source assessment | Source timing | Weight |
|---|---|---:|
| Phenotype and cohort lab | End of Week 2 | 20% |
| Survival and risk-adjusted outcome analysis | End of Week 4 | 25% |
| Clinical variation memo | End of Week 5 | 20% |
| Clinical care improvement brief | End of Week 7 | 35% |
| Total |  | 100% |

## Commons checkpoint normalization

The Commons preserves every source point exactly once while making the requested cumulative checkpoints explicit:

- Week 3 checkpoint: the 20-point phenotype and cohort component is submitted with the care-pathway charter and survival-readiness evidence. The survival draft is a progression gate, not added weight.
- Week 6 checkpoint: the 25-point survival and risk-adjusted component plus the 20-point clinical-variation component are submitted as one cumulative 45-point application release. Week 6 equity, improvement, and embedded machine-learning evidence are required gates, not added weight.
- Final checkpoint: the 35-point clinical care improvement brief remains due on the official last day of the half-term.

Week 2, Week 4, and Week 5 remain feedback milestones. They do not create extra assessment points.

## Source materials that must be developed

The source explicitly says these materials do not yet exist:

- a synthetic longitudinal EHR-style dataset with index events, follow-up time, censoring, outcomes, treatment and procedure records, site identifiers, and realistic case-mix differences;
- a clinical phenotype guide;
- censoring, follow-up, and survival notebook templates;
- a risk-adjustment template;
- a clinical-variation template;
- an equity and subgroup checklist;
- pathway-visualization examples;
- a driver-diagram template;
- an improvement-brief template;
- an AI-use log template;
- phenotype and analysis answer keys; and
- assessment rubrics.

These are build requirements, not claims that the source package already contains runnable data or code.

## Commons source decision

APP-1 reuses the complete pinned Synthea April 2020 CSV release already accepted in FND-1:

https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip

The archive is 8,982,431 bytes with SHA-256 `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a`. It contains 471,836 rows across 16 synthetic clinical tables and 82,293,440 uncompressed bytes.

Synthea is an open-source synthetic patient generator. Its official site states that its records are synthetic rather than real and are available without patient privacy restrictions:

https://synthetichealth.github.io/synthea/

The generator source is Apache-2.0 licensed:

https://github.com/synthetichealth/synthea

APP-1 keeps the full source layer available for phenotype and longitudinal logic. It adds only a documented deterministic teaching extension when the original release cannot support stable site comparison or a known data-generating mechanism. Synthetic values cannot estimate real prevalence, quality, treatment effect, equity, site performance, or clinical benefit.

## Stable source decisions

- APP-1 remains a distinct applied clinical-care course.
- The course totals 112.5 hours.
- SQL and Python are graded working tools.
- R remains a read-run-interpret competency.
- Longitudinal cohorts, survival analysis, risk adjustment, care variation, equity, and improvement recommendations are APP-1 ownership.
- Machine learning is embedded in Module 06 and must be compared with a simpler approach.
- Module 07 is clinician-led leadership and defense work tied to the learner's project.
- The Week 3, Week 6, and official-end-date checkpoints preserve the source's 20/25/20/35 assessment weights as 20/45/35 cumulative releases.
- No protected or identifiable patient data enter the public Commons or an external agent.

## Interpretation rule

The source document defines the curriculum, workload, and assessment intent. The Commons course and module specifications add exact data, filenames, checkpoints, rights, validation, accessibility, reviewer, and release controls needed to make the course runnable.
