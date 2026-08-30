# FND-1 healthcare data foundations source record

- Source course ID: FND-1
- Source title: Healthcare Data Foundations
- Source filename: `03-FND-1-Healthcare-Data-Foundations.docx`
- Source bytes: 24,148
- Source SHA-256: `70a78f38824066770b724aca907211ce6df94b3232cbeb8dbfa8389a24556692`
- Verified: 2026-08-30
- Commons course specification: `docs/curriculum/courses/FND-1/course-spec.md`

## Package comparison

The source document was verified in both supplied curriculum packages:

- `Curriculum-30-Credits-2026-08-29.zip`; and
- `OneDrive_2026-08-29 (1).zip`.

The FND-1 DOCX files are byte-for-byte identical and have the same SHA-256 fingerprint above.

## Source course identity

- Credits: 3.
- Source format: seven-week online block.
- Prerequisites: none.
- Total learner work: 112.5 hours.
- Primary graded language: Python with pandas and notebooks.
- Database language: SQL.
- R role: read, run, and interpret R Markdown or Quarto; writing R from scratch is not graded.
- Supporting practices: Git, semantic versioning, environment files, source provenance, and an AI-use log.

## Source course purpose

FND-1 owns the work required to make healthcare data trustworthy and usable before modeling. Learners obtain, retrieve, join, clean, profile, describe, document, version, and hand off data so another analyst can rerun the work and reach the same answer.

FND-1 is separate from FND-2. FND-1 concerns the data. FND-2 concerns the analytic decision, model, assumptions, performance, and interpretation.

## Source module sequence

| Week | Source module | Hours | Source submission |
|---:|---|---:|---|
| 1 | Setting up a reproducible workspace | 15.5 | Working repository, versioned setup check, environment note, AI-use statement. |
| 2 | Databases and retrieving data | 16.0 | Data model diagram, schema notes, first SQL extracts. |
| 3 | Cohorts and analytic tables | 16.5 | Tested SQL cohort, cohort flow counts, table specification. |
| 4 | Cleaning and profiling | 16.5 | Data-quality notebook, quality-risk log, stop/fix/proceed recommendation. |
| 5 | Descriptive results | 16.0 | Descriptive analysis notebook and interpretation memo. |
| 6 | Accessible charts and time-indexed data | 16.0 | Accessible chart set and exploratory notebook section. |
| 7 | Reproducible handoff and AI audit | 16.0 | Final toolkit package with SQL, notebook, README, version tag, and data brief. |
| Total |  | 112.5 |  |

## Source learning objectives

The source defines six course objectives:

1. explain how healthcare data are created, stored, connected, governed, and retrieved across EHR, claims, registry, survey, operational, and public sources;
2. maintain a reproducible workspace with Git, version numbers, environment files, notebooks, and a SQL client;
3. query relational healthcare data with joins, filters, aggregation, and common table expressions and confirm results;
4. clean, reshape, and profile healthcare data and document missingness, defects, and analytic consequences;
5. produce descriptive and stratified analyses with correct denominators and accessible charts; and
6. use AI and agent tools for explanation, testing, and documentation while remaining accountable for every result.

## Source assessment weights

| Source assessment | Source timing | Weight |
|---|---|---:|
| Environment, Git, version, and database setup check | End of Week 1 | 15% |
| SQL cohort and analytic-table workflow | End of Week 3 | 25% |
| Cleaning, profiling, and descriptive labs | End of Week 5 | 25% |
| Reproducible toolkit package | End of Week 7 | 35% |
| Total |  | 100% |

## Commons checkpoint normalization

The Commons preserves the source weights and technical sequence while making the three requested cumulative checkpoints explicit:

- Week 3 checkpoint: the Week 1 setup component remains 15% and the Week 3 SQL/cohort component remains 25%, submitted together as a cumulative 40% release.
- Week 6 checkpoint: the source Week 5 cleaning, profiling, and descriptive component remains 25% and now includes the Week 6 accessibility and time-indexed outputs.
- Final checkpoint: the source final toolkit remains 35% and is due on the official last day of the half-term.

Week 1 and Week 5 remain required feedback milestones. They are not extra assessments or extra weight.

## Source materials that must be developed

The source explicitly says these materials do not yet exist:

- a synthetic longitudinal healthcare database with EHR-style encounters, diagnoses, medications, labs, claims, and registry tables;
- a documented schema and data dictionary;
- example FHIR and JSON records;
- deterministic quality defects covering duplicates, missingness, coding drift, and small cells;
- a starter Git repository with Python and R environments;
- a SQL client setup;
- data-quality and chart-accessibility checklists;
- an AI-use log template;
- a cohort answer key;
- validation queries; and
- the signature-project rubric.

These are build requirements, not claims that the source package already contains runnable data or code.

## Stable source decisions

- FND-1 stays a straight-through technical course.
- FND-1 and FND-2 remain separate.
- SQL and Python are graded core tools.
- R is a read-run-interpret competency in this course.
- Git, version numbers, environment capture, provenance, and AI accountability are required throughout.
- The final deliverable is a reproducible data toolkit another analyst can rerun and audit.
- No protected or identifiable patient data enter an external AI tool or the public Commons.

## Interpretation rule

The source document defines the curriculum and workload. The Commons course specification adds exact public and synthetic sources, filenames, checkpoint folders, validation gates, accessibility requirements, review dispositions, and release controls needed to make the course runnable.
