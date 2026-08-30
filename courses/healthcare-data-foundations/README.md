# FND-1: Healthcare Data Foundations

FND-1 teaches learners to build, check, describe, and hand off healthcare data another analyst can trust. It is a separate straight-through technical foundations course, not an applied-course statistics block.

- Credits: 3
- Delivery: online half-term
- Learner work: 112.5 hours
- Prerequisites: none
- Core tools: SQL, Python, pandas, notebooks, SQLite, Git, and semantic versioning
- R role: read, run, and interpret, without grading from-scratch R programming
- Continuing case: a synthetic longitudinal acute-care data system built from Synthea and documented public-source contrasts
- Final deliverable: a reproducible healthcare data toolkit
- Course specification status: complete candidate
- Module package status: Modules 01 through 06 are runnable release candidates; Module 07 is not yet built
- Course package version: 0.1.0
- Commons release: 0.34.0

## Seven technical modules

1. Setting up a reproducible workspace.
2. Databases and retrieving healthcare data.
3. Cohorts and analytic tables.
4. Cleaning and profiling.
5. Descriptive results.
6. Accessible charts and time-indexed data.
7. Reproducible handoff and AI audit.

Runnable module packages:

- [Setting up a reproducible workspace](modules/01-reproducible-workspace/README.md)
- [Durable Module 01 specification](../../docs/curriculum/courses/FND-1/modules/01-reproducible-workspace-spec.md)
- [Module 01 release record](modules/01-reproducible-workspace/release.json)
- [Databases and retrieving healthcare data](modules/02-databases-retrieval/README.md)
- [Durable Module 02 specification](../../docs/curriculum/courses/FND-1/modules/02-databases-retrieval-spec.md)
- [Module 02 release record](modules/02-databases-retrieval/release.json)
- [Cohorts and analytic tables](modules/03-cohorts-analytic-tables/README.md)
- [Durable Module 03 specification](../../docs/curriculum/courses/FND-1/modules/03-cohorts-analytic-tables-spec.md)
- [Module 03 release record](modules/03-cohorts-analytic-tables/release.json)
- [Cleaning and profiling](modules/04-cleaning-profiling/README.md)
- [Durable Module 04 specification](../../docs/curriculum/courses/FND-1/modules/04-cleaning-profiling-spec.md)
- [Module 04 release record](modules/04-cleaning-profiling/release.json)
- [Descriptive results](modules/05-descriptive-results/README.md)
- [Durable Module 05 specification](../../docs/curriculum/courses/FND-1/modules/05-descriptive-results-spec.md)
- [Module 05 release record](modules/05-descriptive-results/release.json)
- [Accessible charts and time-indexed data](modules/06-accessible-charts-time-data/README.md)
- [Durable Module 06 specification](../../docs/curriculum/courses/FND-1/modules/06-accessible-charts-time-data-spec.md)
- [Module 06 release record](modules/06-accessible-charts-time-data/release.json)

## Three cumulative checkpoints

- Week 3: workspace, database, validated SQL cohort, analytic table, and query checks.
- Week 6: cleaned analytic table, quality profile, descriptive evidence, accessible charts, and stop/fix/proceed recommendation.
- Official half-term end date: versioned toolkit release, clean reproduction, provenance and data brief, AI audit, and technical handoff defense.

Runnable Week 3 checkpoint:

- [Validated cohort and analytic-table release](checkpoints/01-validated-cohort-release/README.md)
- [Durable Checkpoint 1 specification](../../docs/curriculum/courses/FND-1/checkpoints/01-validated-cohort-release-spec.md)
- [Checkpoint 1 release record](checkpoints/01-validated-cohort-release/release.json)

The 7.5-week phrase is a planning model. Published dates use the official MGH Institute half-term calendar:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

## Course decision

The final decision owner is a health-system analytics engineering lead. The decision is whether to accept the released cohort and analytic table as trustworthy input for downstream modeling and applied analysis.

The available dispositions are:

- accept;
- accept with conditions;
- revise; or
- refer for privacy, rights, integrity, or governance review.

## Data plan

The core relational case uses the pinned Synthea April 2020 synthetic patient sample already registered in the Commons. A deterministic build will create a SQLite teaching database and a separately versioned defect layer. Public CMS and CDC records provide schema and provenance contrasts without entering the patient-level cohort.

Synthea sources:

- https://synthea.mitre.org/downloads
- https://github.com/synthetichealth/synthea/wiki/CSV-File-Data-Dictionary

FHIR R4 references:

- https://hl7.org/fhir/R4/patient.html
- https://hl7.org/fhir/R4/encounter.html
- https://hl7.org/fhir/R4/observation.html

CMS synthetic claims extension:

https://data.cms.gov/collection/synthetic-medicare-enrollment-fee-for-service-claims-and-prescription-drug-event

## Durable records

- [Course specification](../../docs/curriculum/courses/FND-1/course-spec.md)
- [Source record](../../docs/source/fnd-1-healthcare-data-foundations-source-record.md)
- [Master curriculum architecture](../../docs/specs/2026-08-29-curriculum-master-architecture-spec.md)
- [Build ledger](../../docs/curriculum/BUILD-LEDGER.md)

## Build order

Build Modules 01 through 07 one at a time. Each release receives its own 21-section module specification, teaching data, runnable exercise, learner assessment, instructor notes, validator, review fields, semantic version, commit, and push.
