# Open Clinical Learning Commons master curriculum architecture

- Status: architecture approved; course and module specifications in progress
- Date: 2026-08-29
- Release: 0.10.0
- Primary source package: `C:\Users\Shuha\Downloads\Curriculum-30-Credits-2026-08-29.zip`
- Comparison package: `C:\Users\Shuha\Downloads\OneDrive_2026-08-29 (1).zip`
- Academic calendar: https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

## Purpose

This specification defines the stable structure for the complete curriculum before individual course and module specifications are written. It records which course owns each concept, how applied courses revisit foundations, how open data becomes teachable material, what learners submit at each checkpoint, and how work continues safely across context resets.

The two supplied ZIP files contain the same 11 seven-week course documents. Those documents remain the content source, but the applied-course schedule is being reorganized into a half-term design with a final leadership block and embedded machine learning.

## Program architecture

The program contains four kinds of learning experiences. They do not share one universal weekly template.

| Type | Courses | Delivery rule |
|---|---|---|
| Technical foundations | FND-1 and FND-2 | Teach technical work straight through. Each foundation has its own learner-facing course release, module sequence, exercises, datasets, and assessments. |
| Applied domains | APP-1 through APP-7 | Revisit statistics and mathematics through a different clinical or health-system decision, then complete domain applications, an embedded machine-learning extension, and clinician-led leadership work. |
| Capstone | CAP-0 and CAP-1 | Preserve proposal preparation and project execution as capstone-specific sequences. Do not force the applied-course template onto them. |
| Standalone visualization | DA-730 | Remain separate from the 30-credit sequence. Redesign the existing Tableau-centered course as a concept-first clinical data visualization course with reproducible, software-flexible exercises. |

## Academic calendar rule

MGH Institute calls these offerings "half-term" courses. The 2026-2027 calendar does not state that every half-term is exactly 7.5 weeks.

| Half-term | First day | Last day | Elapsed span |
|---|---|---|---:|
| Fall 2026 half-term 1 | September 8, 2026 | October 27, 2026 | 49 days |
| Fall 2026 half-term 2 | October 28, 2026 | December 18, 2026 | 51 days |
| Spring 2027 half-term 1 | January 11, 2027 | March 2, 2027 | 50 days |
| Spring 2027 half-term 2 | March 3, 2027 | April 24, 2027 | 52 days |
| Summer 2027 half-term 1 | May 10, 2027 | June 29, 2027 | 50 days |
| Summer 2027 half-term 2 | June 30, 2027 | August 20, 2027 | 51 days |

The curriculum may use "7.5-week instructional design" as its planning model. Published schedules and due dates must use the official half-term start and end dates. The final checkpoint is due on the official last day rather than a hardcoded day called "week 7.5."

The term-mapping document for each offering will translate instructional weeks into actual dates and account for holidays. A course specification must remain reusable across fall, spring, and summer half-terms.

## Applied-course rhythm

Each applied course has seven distinct modules. The titles, concepts, datasets, exercises, and deliverables are specific to the course. The common rhythm is an alignment rule, not a copied syllabus.

| Module | Instructional period | Purpose | Checkpoint |
|---|---:|---|---|
| 1 | Week 1 | Revisit the first domain-specific statistics or mathematics foundation. | Practice submission |
| 2 | Week 2 | Extend the domain method and connect it to healthcare measurement. | Practice submission |
| 3 | Week 3 | Complete the technical foundation needed for the course decision. | Technical checkpoint |
| 4 | Week 4 | Apply the methods to a realistic public or synthetic health dataset. | Application submission |
| 5 | Week 5 | Extend the application, visualization, and interpretation. | Application submission |
| 6 | Weeks 6 through 6.5 | Complete the third application and its week-6 checkpoint, then add a half-week machine-learning extension inside the same module. | Application checkpoint plus ML extension |
| 7 | Weeks 6.5 through the end of the half-term | Work with Joe Joseph, MD, on clinical leadership, decision ownership, implementation, communication, and defense. | Final decision package and defense |

Machine learning is not a detached survey module. It appears where the course decision naturally benefits from prediction, classification, clustering, language processing, anomaly detection, or another suitable method. The learner must compare it with a simpler method and explain whether the added complexity changes the decision.

## Foundation-course rule

FND-1 and FND-2 are separate technical courses. They do not use the applied-course rhythm.

### FND-1 ownership

FND-1 owns the work required to make healthcare data trustworthy and usable:

- healthcare data sources and generation processes;
- relational databases and SQL retrieval;
- cohort definitions, denominators, joins, and analytic tables;
- cleaning, reshaping, missingness profiling, and data-quality checks;
- descriptive summaries and basic visual inspection;
- Git, environments, version numbers, reproducible projects, and handoff;
- provenance, data dictionaries, validation records, and responsible agent use.

FND-1 receives its own Commons course release. Applied courses may reuse the underlying data layer but must not send learners back through an identical FND-1 lesson.

### FND-2 ownership

FND-2 owns the general modeling and inference work needed before domain specialization:

- translating decisions into analytic aims and estimands;
- regression foundations and interpretation;
- prediction workflows and evaluation;
- adjustment, confounding, missing-data strategy, and longitudinal structure;
- forecasting and temporal validation;
- model testing, failure analysis, and agent-assisted verification;
- model cards, governance, reproducibility, and defense.

FND-2 receives its own Commons course release. Applied courses revisit these ideas through a domain decision and must state which FND-2 skill they are extending.

## Cross-course ownership map

Each applied course has a distinct reason to revisit foundations. Course specifications must use this ownership map to prevent accidental duplication.

| Course | Domain-specific technical ownership | Application and decision ownership |
|---|---|---|
| APP-1: Clinical Care | Longitudinal cohorts, censoring, survival analysis, treatment comparison, risk adjustment, and clinically meaningful effects. | Care-pathway variation, equity, improvement design, and a clinical care recommendation. |
| APP-2: Patient Experience and Engagement | Patient-reported measures, scale construction, response patterns, missingness, representation, survey bias, and linked patient evidence. | Patient voice, subgroup interpretation, engagement strategy, partnered improvement, and accountability. |
| APP-3: Clinical Performance and Improvement | Operational measures, rates, variation, statistical process control, demand forecasting, capacity, and balancing measures. | Bottleneck diagnosis, improvement scenarios, feasibility, monitoring, and a performance recommendation. |
| APP-4: Clinical Decision Support | Decision thresholds, classification metrics, calibration, validation, alert burden, human factors, and subgroup performance. | Workflow logic, sandbox prototyping, failure modes, safety cases, monitoring, and governance. |
| APP-5: Population Health and Equity | Population denominators, standardization, disparities, small-area reasoning, geography, targeting, and fairness. | Place-based intervention design, resource targeting, community accountability, and an equity recommendation. |
| APP-6: Health Research and Innovation | Causal estimands, study design, directed acyclic graphs, confounding, identification, adjustment, sensitivity analysis, and reproducible protocols. | Innovation evaluation, preregistration, reporting standards, dissemination, and next-study logic. |
| APP-7: Strategy, Finance, and Value | Financial measures, utilization, value, service-line analysis, access, scenario modeling, uncertainty, and prioritization. | Strategic options, investment decisions, executive communication, implementation measures, and value monitoring. |

The standalone DA-730 course owns visualization concepts that should not be re-taught in full inside every applied course: chart selection, visual encoding, comparison, distributions, time, relationships, uncertainty, patient flow, networks, hierarchy, geography, dashboards, accessibility, annotation, critique, and decision storytelling. Applied courses use these skills in their own domain.

## The three checkpoint deliverables

Every applied course has three cumulative checkpoints. Course-specific specifications replace generic labels with exact filenames, dataset names, and rubric criteria.

### Week 3 technical checkpoint

The learner submits:

1. a reproducible technical notebook or script;
2. a validated analytic dataset or query that creates it;
3. a data dictionary and source record;
4. method checks and a plain-language interpretation;
5. a short note connecting the work to FND-1 and FND-2;
6. an AI-use record and verification statement.

The checkpoint proves that the learner can perform the course's technical foundation before the signature application begins.

### Week 6 application checkpoint

The learner submits:

1. the updated analysis repository;
2. one primary and, when justified, one supporting visualization;
3. an application memo for the named clinical or health-system audience;
4. subgroup, uncertainty, validity, and failure checks required by the course;
5. a source and transformation record for every dataset used;
6. a draft recommendation and the evidence that could change it.

The first six weeks must produce a complete analytic case. The half-week machine-learning extension may improve, challenge, or fail to improve that case, but it cannot replace the simpler analysis.

### Final half-term checkpoint

The learner submits:

1. a final decision package written for the course's real audience;
2. the complete reproducible repository and versioned data release;
3. the technical and clinical evidence behind the recommendation;
4. a comparison of the simple and machine-learning approaches;
5. implementation, monitoring, and unintended-consequence measures;
6. a leadership reflection and stakeholder plan;
7. an oral, recorded, or live defense;
8. a final AI-use and accountability statement.

The final package must make clear who owns the decision, what should happen next, what will be measured, and when the decision should be revisited.

## Clinician leadership block

Joe Joseph, MD, is the designated clinician for the final leadership block. The strongest public match found during initial research is Joe Joseph, MD, SFHM, a hospital medicine leader associated with Sound Physicians, including a Regional Chief Medical Officer role:

- https://www.soundphysicians.com/press-release/sound-physicians-acquires-indigo-health-partners/
- https://www.soundphysicians.com/press-release/sound-physicians-actively-participating-hospital-medicine-2015/

Confirm this identity before publishing biographical copy. The course architecture does not depend on a current job title.

The leadership block is built around the learner's own course project. It includes:

- reading an analysis as a clinical decision owner;
- identifying the stakeholder who can act and the people affected;
- weighing evidence, feasibility, equity, safety, and operational constraints;
- communicating uncertainty without avoiding a recommendation;
- planning implementation, monitoring, escalation, and reassessment;
- defending the decision under questioning.

## DA-730 standalone visualization course

DA-730 remains separate from the 30-credit program path. The old course is Tableau-centered. The Commons redesign is concept-first and software flexible.

The course keeps its existing seven-week, 13-module concept map unless an official catalog decision changes the course number or duration. Tableau may remain an allowed implementation tool, but no outcome may depend on recalling a Tableau menu path. R and ggplot2 provide the first reproducible lab path. Python, Tableau, Power BI, Observable, and other tools are allowed when the learner submits the source and the work can be reproduced.

DA-730 must teach learners to choose, build, critique, and explain visualizations based on the healthcare decision, data structure, audience, uncertainty, accessibility, and what the display leaves out. Its separate course specification is the first course-level specification to produce under this architecture.

## Open-data teaching system

The curriculum will use public clinical sources, open datasets, and documented synthetic teaching data extensively. Data collection must remain purposeful and reproducible rather than becoming an unreviewed file archive.

Every imported source receives a source record with:

- publisher and dataset title;
- complete source and documentation URLs;
- retrieval date and source version;
- license, terms, and redistribution limits;
- original filename, file size, and checksum;
- geographic and temporal coverage;
- unit of observation and important denominators;
- variables used by the course;
- transformations and derived teaching extracts;
- known missingness, bias, suppression, and interpretation limits;
- the module, exercise, and learning outcome the data support.

The data pipeline keeps three layers:

1. immutable raw downloads when redistribution is allowed;
2. small, versioned teaching extracts with reproducible build scripts;
3. synthetic extensions when public data cannot safely or realistically support the exercise.

No real patient records or protected health information enter the public repository. Restricted datasets may be referenced as examples, but public modules must run on sources that learners and adopters can legally access.

## Module specification contract

Every module specification must contain the following sections:

1. module identity, duration, prerequisites, and place in the course;
2. the healthcare decision and named audience;
3. the foundation skill being revisited or extended;
4. learning outcomes that can be assessed;
5. concept ownership and explicit out-of-scope boundaries;
6. lesson sequence with estimated learner time;
7. authoritative readings and public clinical sources;
8. dataset inventory, provenance, license, and teaching purpose;
9. data dictionary and expected analytic structure;
10. worked example and instructor walkthrough;
11. guided practice;
12. independent exercise;
13. visualization and communication requirements;
14. exact submission package and filenames;
15. rubric and pass conditions;
16. common errors, failure modes, and instructor interventions;
17. accessibility, equity, privacy, and responsible-claim checks;
18. AI and agent policy, required disclosure, and verification;
19. answer key and instructor notes;
20. runnable acceptance checks for data, code, links, and expected findings;
21. release status, reviewers, version, and known issues.

A module is not complete because prose exists. It is complete when an independent learner can perform the work, an instructor can teach and grade it, the data and code run, and the release checks pass.

## Course specification contract

Every course specification must contain:

- catalog description, credits, half-term mapping, prerequisites, and role in the program;
- course-level outcomes and program-outcome mapping;
- the course's concept ownership and dependencies;
- the complete module sequence and workload totaling 112.5 hours for a 3-credit course;
- the week-3, week-6, and final checkpoint contracts where the applied rhythm is used;
- the continuing dataset or project thread;
- assessment weights and grading criteria;
- required public and synthetic data releases;
- instructor and clinician interaction plan;
- software and reproducibility policy;
- accessibility, responsible AI, and data-governance policies;
- all module-specification paths;
- build order, review gates, release criteria, and unresolved decisions.

CAP-0 remains zero credits unless the approved program documents change it. Other courses retain the credits recorded in the source package.

## Context-safe build workflow

The curriculum will be produced one module at a time. Each unit of work follows the same sequence:

1. read the master architecture, course source, ownership map, and previous module handoff;
2. write or update the module specification;
3. collect and register the required public data;
4. build the learner lesson, exercise, assessment, instructor notes, and runnable assets;
5. run data, code, link, accessibility, and visual checks;
6. update the course progress ledger and known issues;
7. bump the semantic version when the release changes;
8. commit and push the completed unit;
9. record the next exact module and any unresolved dependency before context is compacted.

The repository will use these durable locations:

```text
docs/curriculum/BUILD-LEDGER.md
docs/curriculum/courses/<course-id>/course-spec.md
docs/curriculum/courses/<course-id>/modules/<module-id>-spec.md
courses/<course-slug>/modules/<module-id>/
data/sources/<source-id>/
```

The build ledger is the resume point. It must identify the last completed module, current release, checks run, open issues, and next module. Chat history is never the only record of curriculum decisions.

## Build order

1. Confirm the identity and publishable biography of Joe Joseph, MD.
2. Finish the DA-730 course specification and ownership map.
3. Build DA-730 module specifications and teaching releases in sequence.
4. Create the separate FND-1 course specification and build its modules.
5. Create the separate FND-2 course specification and build its modules.
6. Lock the cross-course concept ownership matrix against all supplied DOCX files.
7. Specify and build APP-1 through APP-7, one module at a time.
8. Specify and build CAP-0 and CAP-1.
9. Audit workload, prerequisites, checkpoints, duplication, source provenance, and progression across the full program.
10. Update the public course catalog and deploy the verified curriculum release.

## Architecture acceptance checks

- FND-1 and FND-2 remain separate straight-through technical courses.
- APP-1 through APP-7 use distinct domain modules and do not copy one generic statistics sequence.
- Each applied course has checkpoints at instructional weeks 3 and 6 and on the official last day of the half-term.
- Machine learning is embedded in module 6 and compared with a simpler approach.
- Module 7 is a clinician-led leadership and decision-defense block.
- DA-730 remains a standalone concept-first visualization course.
- Every 3-credit course totals 112.5 learner hours.
- CAP-0 remains zero credits unless an approved program change says otherwise.
- Every dataset has provenance, terms, a checksum, a teaching purpose, and known limits.
- Every module defines exact learner and instructor deliverables and includes runnable release checks.
- Every completed module leaves a committed ledger entry so work can resume after a context reset.
