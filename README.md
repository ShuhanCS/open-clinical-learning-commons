# Open Clinical Learning Commons

One shared data layer. Many ways to learn, teach, and contribute.

The Open Clinical Learning Commons is a public teaching resource built from synthetic patients and open health data. It is for students, fellows, instructors, and health systems that need realistic health data analytics training without using patient records.

Each release will carry the data, documentation, teaching tasks, evaluation checks, contribution history, source terms, and known issues needed for another program to teach from it.

- Current version: `0.2.0`
- Status: Ali Goff's course document and the first module record are available. No data release has shipped yet.

## First course

The first application is DA-730: Analyzing, Visualizing, and Storytelling with Data.

The course teaches learners to choose, build, critique, and explain healthcare visualizations based on the decision, the data structure, the audience, and what the display leaves out. Its concept modules are independent of software and clinical domain. R and ggplot2 provide the first lab environment.

The first build is Module 04, Distributions versus summaries. Learners examine an emergency department where median length of stay improves while the longest stays become much worse. They must find the hidden change, choose one chart for leadership, and explain what decision should change.

- [Data visualization course](courses/data-visualization/README.md)
- [Module 04: Distributions versus summaries](courses/data-visualization/modules/04-distributions-vs-summaries/README.md)
- [Ali Goff's course redesign document in Markdown](docs/source/ali-goff-da-730-course-redesign.md)
- [Course foundation spec](docs/specs/2026-08-15-data-visualization-course-foundation.md)

## What a release contains

| Asset | What it provides |
|---|---|
| Data release | Synthetic and open data, a data dictionary, provenance, source terms, and known issues. |
| Assignment pack | Concept material, a worked healthcare case, labs, critique exercises, and assessments. |
| Benchmark | Runnable checks that confirm the data and teaching conditions behave as documented. |
| Contribution record | Authors, reviewers, changes, reuse terms, and the release version. |

## Data layers

| Layer | Planned contents |
|---|---|
| Research and evidence | ClinicalTrials.gov registrations, OpenAlex publication metadata, and data-sharing records. |
| Hospital and community context | CMS quality measures, CDC health estimates, social vulnerability measures, and Census demographics. |
| Patient layer | Synthea-generated people, coverage, encounters, diagnoses, medications, labs, and claims-like events. |
| Teaching layer | Case briefs, notebooks, data dictionaries, documented flaws, rubrics, and instructor answer keys. |

## Data boundary

- No real patient records enter this repository.
- MGB patient data, MIMIC, and partner datasets are outside the public release.
- Every imported source keeps its own license and terms.
- Every synthetic release must include its generator, version, row count, checksum, and known issues.
- An incomplete build or a dataset that fails its teaching checks does not ship.

## Why this connects MSDA and IDEA

The Commons supplies a shared practice environment for the MGB University Master of Science in Health Data Analytics and the IDEA Fellowship in emergency medicine. MSDA learners can use it across foundation, applied, and capstone courses. IDEA fellows can use the same assets for reproducible coding, clinical data analysis, research communication, and reusable scholarly contributions.

Other programs can adopt a release without an IRB submission, data use agreement, or local patient data.

## Build order

1. Approve the data visualization course and module contract. The draft is published for review.
2. Build and test Module 04 end to end. The content record is complete; the generator, data, code, and checks are next.
3. Add the remaining ten module briefs and the Fall 2026 course wrapper.
4. Teach the course, log defects, and revise the module contract.
5. Connect tested modules to a small, versioned Commons data release.

## Licensing

Original documentation and synthetic data are planned for CC BY 4.0. Teaching and pipeline code are planned for the MIT License. Imported public data retain their source terms. See [LICENSE.md](LICENSE.md) for the scope and complete license links.

## Repository

https://github.com/ShuhanCS/open-clinical-learning-commons
