# APP-3 Data for Clinical Performance and Improvement source record

- Source course ID: APP-3.
- Source title: Data for Clinical Performance and Improvement.
- Source filename: `07-APP-3-Clinical-Performance-and-Improvement.docx`.
- Source bytes: 26,907.
- Source SHA-256: `084a412054c77169ea065cf15ed3cc7097e412a6017fbb58a260e909d17717e3`.
- Verified: 2026-08-30.
- Commons course specification: `docs/curriculum/courses/APP-3/course-spec.md`.

## Package comparison

The source document was verified in both supplied curriculum packages:

- `Curriculum-30-Credits-2026-08-29.zip`; and
- `OneDrive_2026-08-29 (1).zip`.

The APP-3 DOCX files are byte-for-byte identical. Both are 26,907 bytes and have the SHA-256 fingerprint above.

## Source course identity

- Credits: 3.
- Source format: seven-week online block.
- Prerequisites: FND-1 and FND-2.
- Total learner work: 112.5 hours.
- Primary graded language: Python with pandas, statsmodels, SimPy, and notebooks.
- Query backbone: SQL.
- R role: read, run, and interpret statistical process control and forecasting work; writing R from scratch is not graded.

The Commons treats the source's seven weeks as seven instructional weeks inside an official half-term. Week 3 and Week 6 are instructional checkpoints. The final checkpoint is due on the official last day of the assigned half-term, not on a fabricated universal day 52.

Official calendar:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

## Source purpose and ownership

APP-3 teaches learners to turn harm, delay, unreliable care, poor access, or a capacity constraint into a defensible clinical performance decision. Learners specify quality, safety, access, flow, capacity, and balancing measures; distinguish ordinary variation from signals; locate bottlenecks; forecast demand; test a bounded redesign; and set monitoring, escalation, and fallback rules.

APP-3 does not repeat general SQL, data cleaning, regression, prediction, or chart instruction. It revisits those foundation skills through measure stewardship, statistical process control, patient-safety surveillance, operational flow, demand and capacity, queueing, scenario testing, and accountable improvement.

## Source module sequence

| Week | Source module | Hours | Source submission |
|---:|---|---:|---|
| 1 | Framing a clinical performance problem | 15.5 | Clinical performance charter |
| 2 | Measures and operational metrics | 16.0 | Measure and operational metric build |
| 3 | Variation, safety signals, and bottlenecks | 16.5 | Performance diagnostic |
| 4 | Demand forecasting and capacity | 16.5 | Forecasting and capacity checkpoint |
| 5 | Improvement scenarios and evaluation | 16.0 | Improvement scenario and evaluation |
| 6 | Feasibility, equity, and monitoring | 16.0 | Draft clinical performance package |
| 7 | Recommendation and defense | 16.0 | Final clinical performance improvement package |
| Total |  | 112.5 |  |

## Source learning objectives

The source defines six course objectives:

1. frame a clinical performance problem with an accountable aim, eligible population or unit of flow, stakeholders, constraints, and success measures;
2. construct and validate quality, safety, access, flow, capacity, and balancing measures with correct numerator, denominator, exclusion, and event logic;
3. diagnose variation, safety signals, delays, and bottlenecks using process maps, run and control charts, and operational metrics;
4. build and validate a bounded demand or staffing forecast and use a guided scenario model to test capacity or workflow assumptions;
5. evaluate whether an improvement changed performance while accounting for trend, confounding, equity, workforce burden, and unintended harm; and
6. produce a clinical performance improvement package with measure logic, scenario results, implementation measures, and escalation and fallback thresholds.

## Source assessment weights

| Source assessment | Source timing | Weight |
|---|---|---:|
| Measure and operational metric build | End of Week 2 | 20% |
| Performance diagnostic | End of Week 3 | 20% |
| Forecast, scenario, and evaluation | End of Week 5 | 25% |
| Clinical performance improvement package | End of Week 7 | 35% |
| Total |  | 100% |

## Commons checkpoint normalization

The Commons preserves every source point exactly once:

- Week 3: the 20-point measure build and 20-point performance diagnostic form one cumulative 40-point technical release. Module 01 framing evidence is required but adds no points.
- Week 6: the 25-point forecast, scenario, and evaluation component forms one cumulative application release. Module 06 feasibility, monitoring, and embedded-ML evidence is required but adds no points.
- Official half-term end date: the final clinical performance improvement package remains 35 points.

Weeks 2 and 5 remain feedback milestones. They do not create extra course points. The course total is `40 + 25 + 35 = 100`.

## Materials the source says must be developed

The source requires:

- a linked synthetic dataset with encounters, clinical and safety events, appointments, staffing, queues, capacity, census, throughput, and time-indexed demand;
- seeded measure defects, incident reports, near misses, subgroup differences, and one bounded staffing or workflow scenario;
- measure specifications, process-map and control-chart templates, a forecasting notebook, and a provided queue or discrete-event scenario model;
- an assumption register, cost-of-error worksheet, equity and workforce prompts, escalation rubric, monitoring plan, dashboard-accessibility checklist, and AI-use log; and
- measure, statistical process control, forecasting, and scenario answer keys plus assessment rubrics.

These are build requirements. The source DOCX does not contain runnable data or code.

## Commons continuing decision

The course uses an explicitly fictional service, `CGH-ED-01`, at Commons General Hospital. Learners decide whether its adult emergency service should propose a bounded 12-week test of a predeclared flex-staffing and fast-track activation rule.

The proposed test seeks to reduce arrival-to-clinician and arrival-to-departure delay without increasing left-before-seen events, 72-hour unplanned returns, escalation delays, staff overtime, or supported subgroup gaps.

No public hospital is represented by the synthetic service. Public aggregate measures provide definitions, reporting context, and source limitations. They do not supply local process truth, a current staffing judgment, or evidence that the proposed change will work.

## Public-source architecture

### CMS timely and effective care

Stable dataset page:

https://data.cms.gov/provider-data/dataset/yv7e-xc69

APP-3 begins with the complete CMS Timely and Effective Care - Hospital source already accepted by DA-730 Module 12. The accepted snapshot has these immutable facts:

| Item | Accepted fact |
|---|---|
| CMS release date | 2026-08-13 |
| Full rows | 138,084 |
| Full columns | 16 |
| Full bytes | 34,150,899 |
| Full SHA-256 | `1e5a1ca803c2b09468fe3ae3fe60fef3e910f5f5300630a24791c88a1abff516` |
| Accepted Massachusetts source rows for EDV, OP_18b, and OP_22 | 186 |
| Massachusetts source-selection SHA-256 | `f28f5d56e5e0e29001c7a275b01306762e673c9a21459dc7a68ff1aea782943b` |

The full source must be acquired and validated before a teaching extract is created. APP-3 may reuse the accepted immutable release rather than silently refresh it. If a later release is selected, the module must record a new URL, release date, bytes, rows, fields, hash, and semantic-version decision.

### CMS complications and deaths

Stable dataset page:

https://data.cms.gov/provider-data/dataset/ynj2-r877

This full public hospital release supplies aggregate patient-safety and adverse-event context, including CMS Medicare PSI 90 and component measures. Module 01 must pin one exact full release before use. Its release URL, date, rows, columns, bytes, hash, reporting periods, measure inventory, unavailable values, and rights record are required.

The source is public aggregate evidence. It cannot detect a current local incident, establish the cause of harm, replace incident review, or validate the synthetic service.

### HHS historical hospital capacity

Stable dataset page:

https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/anag-cw7u

The source contains weekly facility-level hospital utilization, capacity, occupancy, coverage, and staffing-shortage fields. Required reporting ended after 2024-05-03, so this is a historical source. It may teach source coverage, capacity definitions, reporting changes, and external context. It cannot support a current staffing decision.

Because the full source may exceed repository limits, the build must still inspect and fingerprint the complete accepted snapshot. A deterministic teaching selection may be committed only with the complete-source URL, metadata, acquisition date, row count, byte count, hash, query or selection code, and an explanation of why the full binary is not stored in Git.

### Public guidance and definitions

CMS measure periods and definitions:

https://data.cms.gov/provider-data/topics/hospitals/measures-and-current-data-collection-periods

CMS complications and deaths topic page:

https://data.cms.gov/provider-data/topics/hospitals/complications-deaths/

These pages support measure interpretation. They are not substitutes for the exact data releases or technical specifications used by a module.

## Synthetic operational layer

The public sources do not contain one linked, current, patient-level operational trace with arrivals, queues, staffing, process steps, incident reports, and known intervention truth. The Commons therefore builds an explicitly synthetic operational release for `CGH-ED-01`.

The release must contain at least these linked tables:

| Table | Required grain and role |
|---|---|
| encounters | one synthetic adult emergency encounter with eligibility, arrival, acuity, disposition, and return fields |
| process-events | one timestamped synthetic state transition per encounter and process step |
| staffing | one synthetic role, shift, scheduled capacity, actual capacity, and workload record |
| queue-snapshots | one synthetic service queue and capacity state per declared interval |
| safety-events | one synthetic incident, near miss, trigger, or reviewed non-event with known truth |
| calendar-demand | one date and shift with arrivals, calendar features, coverage, and forecast eligibility |
| scenarios | one baseline or redesign configuration with declared capacity and workflow assumptions |
| known-truth | one seeded defect, signal, bottleneck, subgroup effect, scenario effect, or null condition |

Every generated table requires a generator version, seed, field dictionary, row count, checksum, relational checks, known-truth contract, defect register, and explicit synthetic flag. Names, facility identifiers, and values must not imply that the release describes a real hospital, patient, clinician, or workforce.

## Source-to-module routing

| Module | Source role | Protected handoff |
|---:|---|---|
| 01 | Inspect all accepted public sources, their full-release identities, measure meanings, coverage, and limits; define the synthetic service and decision. | Source feasibility, decision charter, measure family, and claim boundary. |
| 02 | Build validated operational measures from the synthetic linked tables while preserving public definitions as context. | Accepted measure logic, event validation, defects, and operational metric tables. |
| 03 | Use synthetic time, safety, and process evidence for control charts, bottlenecks, and escalation; retain public aggregate limits. | Accepted 40-point Week 3 technical release. |
| 04 | Forecast synthetic service demand with time-ordered validation and translate error into capacity consequences. | Accepted forecast, folds, errors, Little's Law check, and capacity implication. |
| 05 | Run the provided synthetic scenario and evaluate redesign assumptions, sensitivity, confounding, and balancing measures. | Accepted 25-point scenario and evaluation component. |
| 06 | Add feasibility, equity, workforce, monitoring, and the bounded ML forecast comparison without changing accepted evidence silently. | Accepted 25-point Week 6 application release and Module 07 permission. |
| 07 | Freeze both checkpoints and add clinician leadership, stewardship, accountability, communication, defense, and final disposition. | Accepted or conditioned final course package. |

## Embedded machine-learning decision

Module 06 contains eight hours of application and monitoring work plus an eight-hour ML extension. The extension compares the accepted transparent arrival-demand approach with one bounded gradient-boosted regression forecast using the same target, eligible calendar and lag features, information cutoffs, temporal folds, horizons, and evaluation rows.

The comparison must report forecast errors in operational units, under- and over-forecast consequences, subgroup or shift support where appropriate, leakage tests, failure cases, reproducibility, and whether the ML forecast changes the staffing-scenario recommendation. ML may challenge or fail to improve the simple approach. It cannot replace the process diagnosis, queue model, safety review, human ownership, or simpler benchmark.

## Stable source decisions

- APP-3 remains a distinct applied course.
- The course totals 112.5 hours.
- SQL and Python are graded working tools; R remains read-run-interpret.
- APP-3 owns operational measures, rates, variation, statistical process control, safety signals, demand forecasting, capacity, bottlenecks, scenarios, balancing measures, and improvement monitoring.
- The continuing case uses a fictional service. No synthetic result is attributed to a public hospital.
- Module 06 contains eight hours of application and monitoring plus an eight-hour embedded ML extension.
- Module 07 is clinician led.
- Checkpoints preserve the source weights as 40 points at Week 3, 25 points at Week 6, and 35 points on the official half-term end date.
- Full public releases must be acquired, inspected, and fingerprinted before derived teaching evidence is created.
- No protected, identifiable, workplace, or restricted patient data enter the Commons or an external agent.

## Interpretation rule

The source document controls curriculum intent, workload, and assessment weight. The Commons specification adds exact public sources, synthetic boundaries, filenames, checkpoints, validation, accessibility, reviewer, leadership, and release controls needed to make the course runnable.
