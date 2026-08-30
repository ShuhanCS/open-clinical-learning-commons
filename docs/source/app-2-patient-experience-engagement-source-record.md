# APP-2 Data for Patient Experience and Engagement source record

- Source course ID: APP-2.
- Source title: Data for Patient Experience and Engagement.
- Source filename: `06-APP-2-Patient-Experience-and-Engagement.docx`.
- Source bytes: 25,906.
- Source SHA-256: `3feff30f5128587a482a3f4ca42979a46059bbe98e3febc98f4556c4cfafc009`.
- Verified: 2026-08-30.
- Commons course specification: `docs/curriculum/courses/APP-2/course-spec.md`.

## Package comparison

The source document was verified in both supplied curriculum packages:

- `Curriculum-30-Credits-2026-08-29.zip`; and
- `OneDrive_2026-08-29 (1).zip`.

The APP-2 DOCX files are byte-for-byte identical and have the same SHA-256 fingerprint above.

## Source course identity

- Credits: 3.
- Source format: seven-week online block.
- Prerequisites: FND-1 and FND-2.
- Total learner work: 112.5 hours.
- Primary graded language: Python with pandas and notebooks.
- Query backbone: SQL.
- R role: read, run, and interpret survey, reliability, weighting, and psychometric code; writing R from scratch is not graded.

## Source purpose and ownership

APP-2 treats patient experience, patient-reported outcomes, engagement, and patient voice as measured evidence. Learners select and score measures, assess who responded and who was missed, connect reported experience with access and service evidence, analyze comments within qualitative limits, compare groups without blaming patients, and design a patient-informed improvement.

APP-2 does not repeat general SQL, cleaning, modeling, or chart instruction. It revisits those foundation skills through patient-reported measurement, survey representation, response bias, patient partnership, and accountable feedback.

## Source module sequence

| Week | Source module | Hours | Source submission |
|---:|---|---:|---|
| 1 | Framing a patient-experience and engagement decision | 15.5 | Patient-experience decision charter |
| 2 | Patient-reported measurement | 16.0 | Patient-measurement lab |
| 3 | Response, representation, and bias | 16.5 | Response and representation audit |
| 4 | Linked patient evidence | 16.5 | Linked patient-evidence analysis |
| 5 | Patient voice, group differences, and equity | 16.0 | Equity and patient-voice memo |
| 6 | Patient partnership and improvement design | 16.0 | Draft improvement package |
| 7 | Recommendation, communication, and accountability | 16.0 | Final patient-experience and engagement package |
| Total |  | 112.5 |  |

## Source learning objectives

The source defines six course objectives:

1. frame a patient-experience or engagement decision with a defined population, patient partners, evidence needs, and accountable action;
2. select, score, and interpret patient-reported outcome and experience measures, including reliability, meaningful change, and measurement limits;
3. assess sampling, coverage, response rates, missingness, nonresponse, and mode effects before comparing results;
4. link patient-reported, access, communication, engagement, and service-use data in a governed workflow;
5. compare experience and engagement across groups and channels while addressing equity, privacy, and qualitative limits; and
6. produce a patient-informed improvement package with implementation measures, a feedback plan, and accountable ownership.

## Source assessment weights

| Source assessment | Source timing | Weight |
|---|---|---:|
| Patient-measurement lab | End of Week 2 | 20% |
| Response and linked-evidence analysis | End of Week 4 | 25% |
| Equity and patient-voice memo | End of Week 5 | 20% |
| Patient-experience and engagement package | End of Week 7 | 35% |
| Total |  | 100% |

## Commons checkpoint normalization

The Commons preserves every source point exactly once:

- Week 3: the 20-point patient-measurement lab is submitted with the Week 1 charter and Week 3 representation evidence. Week 3 response work is a progression gate for the later 25-point component.
- Week 6: the 25-point response and linked-evidence analysis plus the 20-point patient-voice memo form one cumulative 45-point release. The partnered-improvement and embedded-ML work is required but adds no points.
- Official half-term end date: the final patient-experience and engagement package remains 35 points.

Weeks 2, 4, and 5 remain feedback milestones. They do not create extra course points.

## Materials the source says must be developed

- patient-reported outcome and experience data with scoring, response, item missingness, language, and collection-mode fields;
- linked access, communication, portal, engagement, and service-use data;
- a governed synthetic patient-comment set;
- instrument-selection, scoring, meaningful-change, response, representation, linkage, provenance, comment-analysis, equity, accessibility, partnership, improvement, and AI-use templates;
- scoring, response-analysis, and assessment answer keys; and
- a patient-partnership facilitation guide.

These are build requirements. The source DOCX does not contain runnable data or code.

## Commons public-source decision

The public patient-experience backbone begins with the complete CMS Patient survey (HCAHPS) - Hospital dataset:

https://data.cms.gov/provider-data/dataset/dgck-syfz

The accepted snapshot covers 325,720 hospital-measure rows, 4,790 facilities, 68 measure IDs, 56 state or territory codes, and the period from 2024-10-01 through 2025-09-30. The raw CSV is 105,461,119 bytes with SHA-256 `b70e598f29552df302e30ed649d178abd1b3d3c868ae97cf8e55453dd33898fc`. The deterministic gzip is 2,195,547 bytes with SHA-256 `56c6c11f1d61820f367417a00b1e2abaaf02d0b7104d7a5429031e750332503c`.

The later response, access, and linkage modules use the current AHRQ Medical Expenditure Panel Survey public-use files. The primary person file is MEPS HC-256, 2024 Full Year Consolidated Data File:

https://meps.ahrq.gov/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256

Relevant 2024 event files are HC-254D inpatient stays, HC-254E emergency visits, HC-254F outpatient visits, and HC-254G office-based visits. They link to HC-256 by the public person identifier `DUPERSID`. Each later module must fingerprint the exact files it accepts.

The Commons creates documented synthetic data only where public sources do not contain the needed teaching evidence. The planned synthetic layers are a nonidentifiable patient-comment corpus and a known response-selection mechanism applied to a public-use analytic population. Neither may be described as observed patient testimony, real nonresponse, or population prevalence.

## Stable source decisions

- APP-2 remains a distinct applied course.
- The course totals 112.5 hours.
- SQL and Python are graded working tools; R remains read-run-interpret.
- Patient-reported measurement, scale construction, response patterns, missingness, representation, survey bias, linked patient evidence, patient voice, and patient partnership belong to APP-2.
- Module 06 contains eight hours of partnered improvement work and an eight-hour embedded ML extension.
- Module 07 is clinician led and includes patient-partner accountability.
- The Week 3, Week 6, and official-end-date checkpoints preserve the source 20/25/20/35 assessment weights as 20/45/35.
- Public facility data may be used for source and measurement instruction but not for unsupported ranking or local causal claims.
- No protected or identifiable patient data enter the public Commons or an external agent.

## Interpretation rule

The source document controls curriculum intent, workload, and assessment weight. The Commons specifications add exact public sources, filenames, synthetic boundaries, checkpoints, validation, accessibility, reviewer, and release controls needed to make the course runnable.
