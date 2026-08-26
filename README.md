# Open Clinical Learning Commons

One shared data layer. Many ways to learn, teach, and contribute.

The Open Clinical Learning Commons is a public teaching resource built from synthetic patients and open health data. It is for students, fellows, instructors, and health systems that need realistic health data analytics training without using patient records.

Each release will carry the data, documentation, teaching tasks, evaluation checks, contribution history, source terms, and known issues needed for another program to teach from it.

- Current version: `0.3.1`
- Status: Module 04 is a runnable release candidate with synthetic data, labs, checks, assessment, and an instructor key. Required human reviews are pending.

## First course

The first application is DA-730: Analyzing, Visualizing, and Storytelling with Data.

The course teaches learners to choose, build, critique, and explain healthcare visualizations based on the decision, the data structure, the audience, and what the display leaves out. Its concept modules are independent of software and clinical domain. R and ggplot2 provide the first lab environment.

The first build is Module 04, Distributions versus summaries. Learners examine an emergency department where median length of stay improves while the longest stays become much worse. They must find the hidden change, choose one chart for leadership, and explain what decision should change. The synthetic reference dataset is included; it is not a stable teaching release until the required reviews are recorded.

- [Data visualization course](courses/data-visualization/README.md)
- [Module 04: Distributions versus summaries](courses/data-visualization/modules/04-distributions-vs-summaries/README.md)
- [Module 04 build specification](docs/specs/2026-08-15-ali-goff-module-04-build-spec.md)
- [Module 04 assessment](courses/data-visualization/modules/04-distributions-vs-summaries/assessment.md)
- [Module 04 instructor notes](courses/data-visualization/modules/04-distributions-vs-summaries/instructor-notes.md)
- [Module 04 release record](courses/data-visualization/modules/04-distributions-vs-summaries/release.json)
- [Ali Goff's course redesign document in Markdown](docs/source/ali-goff-da-730-course-redesign.md)
- [Course foundation spec](docs/specs/2026-08-15-data-visualization-course-foundation.md)

## Competitors and adjacent products

Reviewed on August 26, 2026. Some of these projects compete for a learner's time; others provide data, software, or interface patterns that the Commons can build on.

| Product | How people use it | What it does well | What remains open for the Commons |
|---|---|---|---|
| Kaggle Learn Data Visualization<br>https://www.kaggle.com/learn/data-visualization | Learners move through short tutorials and browser-based coding exercises, then complete a project. | Free, clear progression, hosted practice, and a familiar course interface. | It teaches general Python visualization rather than synthetic data, healthcare interpretation, or instructor-ready modules. |
| Observable data visualization workshop<br>https://observablehq.com/collection/@observablehq/intro-data-vis-workshop | Learners open public notebooks, change live code, inspect charts, and reuse or share the work. | Immediate visual feedback and a strong connection between explanation, code, and output. | It centers JavaScript, D3, and Observable. It does not provide a synthetic-health-data learning path or a portable instructor pack. |
| AI4Healthcare synthetic data course<br>https://www.ai4healthcare.org/courses/synthetic-data | Learners enroll in a free, three-lesson course with video and pre- and post-activity questions. | A concise introduction to synthetic healthcare data for clinicians and AI learners. | It is a short, video-led overview rather than a downloadable dataset, reproducible lab, assessment, and instructor package. |
| Synthea<br>https://synthetichealth.github.io/synthea/ | Users download synthetic patient records in common health-data formats or run the open-source generator. | Widely reusable synthetic health data, open generation code, and direct downloads. | It supplies the data and generator, not a guided course that teaches a newcomer how to investigate, visualize, and explain the data. |
| SDV Community<br>https://docs.sdv.dev/SDV/explore/sdv-community | Technical users install a Python package and follow documentation and tutorials for generating and evaluating synthetic data. | Broad coverage of single-table, multi-table, sequential, quality, privacy, and visualization workflows. | It assumes Python setup and mainly teaches the SDV product. It is not a beginner-facing, domain-based learning experience. |
| MOSTLY AI tutorials<br>https://mostly-ai.github.io/mostlyai/tutorials/ | Users run technical notebooks in Google Colab or VS Code for generation, privacy, fairness, validation, and other tasks. | A large catalog of hands-on synthetic-data examples with runnable notebooks. | The entry point is code-first and tool-specific. Newcomers must already know what problem they want to solve and how to work in a notebook. |
| Syntho Bootcamp<br>https://docs.syntho.ai/overview/get-started/syntho-bootcamp | New platform users follow self-contained sections and embedded demonstrations covering the Syntho workflow. | Structured onboarding, short independent modules, and practical demonstrations. | The learning path is designed around adopting the Syntho platform rather than teaching portable synthetic-data judgment with open materials. |
| Simulacrum<br>https://simulacrum.healthdatainsight.org.uk/ | Researchers learn what the synthetic cancer dataset contains, read getting-started guidance, and download it for analysis. | A plain-language public website around a free, realistic health dataset. | It is primarily a data resource. It does not guide a beginner through an investigation or provide a complete teaching and assessment package. |

### Our position

The Commons will connect the strongest parts of these models: a plain-language public introduction, a guided first investigation, realistic synthetic health data, runnable analysis, visible results, and downloadable materials that instructors and independent learners can reuse.

The planned web interface is a learning front door, not another learning management system. A program manager should be able to understand the project in a few minutes. A new learner should then be able to open a module, inspect a dataset, follow the investigation, view the resulting charts, and download the data and code. GitHub remains the source and contribution layer.

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

1. Complete faculty, emergency department, accessibility, and independent-instructor review of Module 04.
2. Teach the Module 04 pilot, log defects, and promote the candidate to beta.
3. Add the remaining ten module briefs and the Fall 2026 course wrapper.
4. Connect tested modules to a small, versioned Commons data release.

## Licensing

Original documentation and synthetic data are planned for CC BY 4.0. Teaching and pipeline code are planned for the MIT License. Imported public data retain their source terms. See [LICENSE.md](LICENSE.md) for the scope and complete license links.

## Repository

https://github.com/ShuhanCS/open-clinical-learning-commons
