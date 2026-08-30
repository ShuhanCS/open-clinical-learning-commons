# Open Clinical Learning Commons

One shared data layer. Many ways to learn, teach, and contribute.

The Open Clinical Learning Commons is a public teaching resource built from synthetic patients and open health data. It is for students, fellows, instructors, and health systems that need realistic health data analytics training without using patient records.

Each release will carry the data, documentation, teaching tasks, evaluation checks, contribution history, source terms, and known issues needed for another program to teach from it.

- Current version: `0.42.0`
- Status: The public preview has an all-courses home page and the original 77 roadmap module routes. DA-730 has all 13 concept-first modules and all three cumulative checkpoints as runnable release candidates. FND-1 has all seven technical modules and all three cumulative checkpoints as runnable release candidates. FND-2 has a complete source-normalized course specification, its first three runnable modules, and its cumulative Week 3 checkpoint.

The durable curriculum rules, checkpoint contracts, open-data requirements, and context-safe build order are recorded in [docs/specs/2026-08-29-curriculum-master-architecture-spec.md](docs/specs/2026-08-29-curriculum-master-architecture-spec.md).

The first full course specification is [DA-730: Clinical data visualization and decision storytelling](docs/curriculum/courses/DA-730/course-spec.md).

The separate straight-through technical foundation is specified in [FND-1: Healthcare Data Foundations](docs/curriculum/courses/FND-1/course-spec.md), with its source fingerprint and normalization record in [the FND-1 source record](docs/source/fnd-1-healthcare-data-foundations-source-record.md).

Its first runnable unit is [FND-1 Module 01: Setting up a reproducible workspace](courses/healthcare-data-foundations/modules/01-reproducible-workspace/README.md), governed by the durable [Module 01 specification](docs/curriculum/courses/FND-1/modules/01-reproducible-workspace-spec.md).

The next unit is [FND-1 Module 02: Databases and retrieving healthcare data](courses/healthcare-data-foundations/modules/02-databases-retrieval/README.md), governed by the durable [Module 02 specification](docs/curriculum/courses/FND-1/modules/02-databases-retrieval-spec.md).

The third unit is [FND-1 Module 03: Cohorts and analytic tables](courses/healthcare-data-foundations/modules/03-cohorts-analytic-tables/README.md), governed by the durable [Module 03 specification](docs/curriculum/courses/FND-1/modules/03-cohorts-analytic-tables-spec.md). Its four read-only SQL files produce 1,048 eligible event rows, one deterministic index for each of 374 synthetic adults, a 29-field analytic table, and a conserved four-step cohort flow.

The cumulative [FND-1 Week 3 checkpoint](courses/healthcare-data-foundations/checkpoints/01-validated-cohort-release/README.md) joins the 15-point setup component and 25-point SQL cohort component into one portable release. Its durable [checkpoint specification](docs/curriculum/courses/FND-1/checkpoints/01-validated-cohort-release-spec.md) defines the exact 40-point assessment, 19 gates, learner defense, and Module 04 progression decision.

The fourth unit is [FND-1 Module 04: Cleaning and profiling](courses/healthcare-data-foundations/modules/04-cleaning-profiling/README.md), governed by the durable [Module 04 specification](docs/curriculum/courses/FND-1/modules/04-cleaning-profiling-spec.md). It preserves the accepted table, adds a transparent 20-family defect layer, reconciles 28 quality rules, and hands Module 05 the exact restored table with retained conditions.

The fifth unit is [FND-1 Module 05: Descriptive results](courses/healthcare-data-foundations/modules/05-descriptive-results/README.md), governed by the durable [Module 05 specification](docs/curriculum/courses/FND-1/modules/05-descriptive-results-spec.md). It releases 17 profiles, two complete cross-tabs, six rates, two unadjusted strata, and a 27-row denominator registry for Module 06.

The sixth unit is [FND-1 Module 06: Accessible charts and time-indexed data](courses/healthcare-data-foundations/modules/06-accessible-charts-time-data/README.md), governed by the durable [Module 06 specification](docs/curriculum/courses/FND-1/modules/06-accessible-charts-time-data-spec.md). It releases three exact tables, six accessible figure exports, three structured text alternatives, and a fingerprinted Week 6 handoff.

The cumulative [FND-1 Week 6 checkpoint](courses/healthcare-data-foundations/checkpoints/02-quality-descriptive-accessible-release/README.md) freezes 35 accepted artifacts from Modules 04 through 06 into one 25-point decision package. Its durable [checkpoint specification](docs/curriculum/courses/FND-1/checkpoints/02-quality-descriptive-accessible-release-spec.md) defines the exact quality, denominator, accessibility, defense, and Module 07 progression contract.

The seventh unit is [FND-1 Module 07: Reproducible handoff and AI audit](courses/healthcare-data-foundations/modules/07-reproducible-handoff-ai-audit/README.md), governed by the durable [Module 07 specification](docs/curriculum/courses/FND-1/modules/07-reproducible-handoff-ai-audit-spec.md). It assembles the accepted evidence and 23 exact pipeline-source files into a 90-file candidate with a 74-row immutable manifest, data brief, release records, material AI audit, and technical defense.

The [FND-1 final checkpoint](courses/healthcare-data-foundations/checkpoints/03-reproducible-toolkit/README.md) freezes all 90 candidate files and adds the final score, 20 gates, defense score, reviewer record, reproduction record, disposition, and FND-2 acceptance record. Its durable [checkpoint specification](docs/curriculum/courses/FND-1/checkpoints/03-reproducible-toolkit-spec.md) defines the exact 35-point course decision and 100-file release contract.

The separate second technical foundation is specified in [FND-2: Modeling, Inference, and Reproducible Analytics](docs/curriculum/courses/FND-2/course-spec.md), with its source fingerprint and normalization record in [the FND-2 source record](docs/source/fnd-2-modeling-inference-reproducible-analytics-source-record.md). It starts from the accepted FND-1 toolkit, teaches general modeling and inference straight through, and keeps package acceptance separate from model-use permission.

Its first runnable unit is [FND-2 Module 01: Analytic aims and a reproducible modeling workspace](courses/modeling-inference-reproducible-analytics/modules/01-aims-reproducible-workspace/README.md), governed by the durable [Module 01 specification](docs/curriculum/courses/FND-2/modules/01-aims-reproducible-workspace-spec.md). It freezes the exact 374-row source, classifies all 34 source and derived fields, creates the 224/75/75 temporal split, and registers the training-prevalence baseline before any candidate model is fit.

The second runnable unit is [FND-2 Module 02: Regression models and interpretation](courses/modeling-inference-reproducible-analytics/modules/02-regression-interpretation/README.md), governed by the durable [Module 02 specification](docs/curriculum/courses/FND-2/modules/02-regression-interpretation-spec.md). It fits bounded training-only linear and logistic cases, preserves structural blanks, exposes residual, influence, sparsity, and extreme-probability conditions, and keeps coefficients separate from causal or predictive-performance claims.

The third runnable unit is [FND-2 Module 03: Prediction workflows and evaluation](courses/modeling-inference-reproducible-analytics/modules/03-prediction-evaluation/README.md), governed by the durable [Module 03 specification](docs/curriculum/courses/FND-2/modules/03-prediction-evaluation-spec.md). It fits preprocessing inside training only, compares the constant baseline, accepted logistic candidate, bounded random forest, and a prohibited leaked model, locks the selected model and threshold on validation, and preserves one-time test evidence with four outcomes and exact confusion counts.

The cumulative [FND-2 Week 3 checkpoint](courses/modeling-inference-reproducible-analytics/checkpoints/01-modeling-readiness-release/README.md) freezes 72 accepted artifacts from Modules 01 through 03 and six checkpoint controls into a 78-row immutable manifest. Its durable [checkpoint specification](docs/curriculum/courses/FND-2/checkpoints/01-modeling-readiness-release-spec.md) defines the corrected 40-point map, 23 gates, 12-question defense, reviewer evidence, and Module 04 progression decision.

The first rebuilt module is [DA-730 Module 01: Encoding and the grammar of graphics](courses/data-visualization/modules/01-encoding-grammar/README.md), with its durable [module specification](docs/curriculum/courses/DA-730/modules/01-encoding-grammar-spec.md).

The second rebuilt module is [DA-730 Module 02: Perception and visual accuracy](courses/data-visualization/modules/02-perception-accuracy/README.md), with its durable [module specification](docs/curriculum/courses/DA-730/modules/02-perception-accuracy-spec.md).

The third rebuilt module is [DA-730 Module 03: Chart selection in practice](courses/data-visualization/modules/03-chart-selection/README.md), with its durable [module specification](docs/curriculum/courses/DA-730/modules/03-chart-selection-spec.md).

## Program course path

The curriculum uses one shared synthetic and open data layer across two foundation courses, seven applied courses, capstone preparation, and a final capstone.

| Stage | Course | Main work |
|---|---|---|
| Foundation | FND-1: Healthcare Data Foundations | Build, check, describe, and hand off trustworthy healthcare data. |
| Foundation | FND-2: Modeling, Inference, and Reproducible Analytics | Choose, test, explain, and govern analytics that fit the decision. |
| Applied | APP-1: Data for Clinical Care | Longitudinal cohorts, survival, risk adjustment, and care-pathway improvement. |
| Applied | APP-2: Data for Patient Experience and Engagement | Patient-reported measures, representation, patient voice, and partnered improvement. |
| Applied | APP-3: Data for Clinical Performance and Improvement | Quality and operational measures, process variation, capacity, and improvement evaluation. |
| Applied | APP-4: Data for Clinical Decision Support | Workflow logic, validation, human factors, safety cases, monitoring, and governance. |
| Applied | APP-5: Data for Population Health and Equity | Population measures, disparities, place-based evidence, targeting, and accountability. |
| Applied | APP-6: Data for Health Research and Innovation | Causal questions, study design, protocol analytics, sensitivity analysis, and dissemination. |
| Applied | APP-7: Data for Health Systems Strategy, Finance, and Value | Financial and value modeling, strategic options, investment decisions, and monitoring. |
| Capstone | CAP-0: Capstone Preparation | Problem framing, data feasibility, methods, ethics, and proposal approval. |
| Capstone | CAP-1: Capstone: Learning Health System Analytics | One complete, reproducible healthcare analytics project and oral defense. |

The complete seven-week path, prerequisites, and final deliverable for every course are shown in the public page. The source-to-page implementation record is [docs/plans/2026-08-29-program-course-roadmap-plan.md](docs/plans/2026-08-29-program-course-roadmap-plan.md).

## Site routes

| Page | Example | Purpose |
|---|---|---|
| All courses | `index.html` | Shows the complete foundation, applied, and capstone path. |
| Course | `course.html?id=FND-1` | Shows one course and its seven modules. |
| Module | `module.html?course=FND-1&week=1` | Shows the outcome, topics, submission, workload, and course context for one roadmap module. |
| Working lesson | `courses/data-visualization/atlas.html#atlas` | Opens the clinical visualization atlas and guided synthetic-data case. |

The shared [curriculum-data.js](curriculum-data.js) file is the single source for all 11 courses and 77 modules. See [docs/plans/2026-08-29-course-module-site-plan.md](docs/plans/2026-08-29-course-module-site-plan.md) for the page contract and release checks.

## Current working course example

The first standalone course build is DA-730: Clinical Data Visualization and Decision Storytelling.

The course teaches learners to choose, build, critique, and explain healthcare visualizations based on the decision, the data structure, the audience, and what the display leaves out. Its concept modules are independent of software and clinical domain. R and ggplot2 provide the first lab environment.

Modules 01 through 13 are complete sequential rebuilds. Learners map real CMS HCAHPS variables to marks and channels, test how accurately they can read different encodings, select a chart, table, coordinated pair, or no display, audit whether a summary hides a consequential distribution, distinguish modeled counts from adjusted rates, decide how much confidence to place in a ranked estimate, make the result work in color, grayscale, print, text, and an exact table, distinguish a weekly pattern from smoothing or reporting change, compare many groups without changing scale, order, or reference meaning, decide whether geography adds useful information, define flows and composition without changing units or denominators, compose the minimum dashboard needed for one decision, and adapt one stable evidence chain for technical and executive audiences without changing its values or limits. All thirteen require recorded human reviews before alpha release.

The public preview also includes a [chart atlas](courses/data-visualization/atlas.html#atlas) covering comparison, distribution, time, relationship, uncertainty, flow, network, composition, place, and dashboard views. Each family includes a healthcare example and matching R code. The complete runnable script is [chart_gallery.R](courses/data-visualization/chart_gallery.R).

- [Data visualization course](courses/data-visualization/README.md)
- [Module 01: Encoding and the grammar of graphics](courses/data-visualization/modules/01-encoding-grammar/README.md)
- [Module 01 specification](docs/curriculum/courses/DA-730/modules/01-encoding-grammar-spec.md)
- [Module 01 release record](courses/data-visualization/modules/01-encoding-grammar/release.json)
- [Module 02: Perception and visual accuracy](courses/data-visualization/modules/02-perception-accuracy/README.md)
- [Module 02 specification](docs/curriculum/courses/DA-730/modules/02-perception-accuracy-spec.md)
- [Module 02 release record](courses/data-visualization/modules/02-perception-accuracy/release.json)
- [Module 03: Chart selection in practice](courses/data-visualization/modules/03-chart-selection/README.md)
- [Module 03 specification](docs/curriculum/courses/DA-730/modules/03-chart-selection-spec.md)
- [Module 03 release record](courses/data-visualization/modules/03-chart-selection/release.json)
- [Module 04: Distributions versus summaries](courses/data-visualization/modules/04-distributions-vs-summaries/README.md)
- [Module 04 specification](docs/curriculum/courses/DA-730/modules/04-distributions-summaries-spec.md)
- [Module 04 original build record](docs/specs/2026-08-15-ali-goff-module-04-build-spec.md)
- [Module 04 assessment](courses/data-visualization/modules/04-distributions-vs-summaries/assessment.md)
- [Module 04 instructor notes](courses/data-visualization/modules/04-distributions-vs-summaries/instructor-notes.md)
- [Module 04 release record](courses/data-visualization/modules/04-distributions-vs-summaries/release.json)
- [Module 05: Rates, denominators, and adjustment](courses/data-visualization/modules/05-rates-denominators-adjustment/README.md)
- [Module 05 specification](docs/curriculum/courses/DA-730/modules/05-rates-denominators-adjustment-spec.md)
- [Module 05 assessment](courses/data-visualization/modules/05-rates-denominators-adjustment/assessment.md)
- [Module 05 instructor notes](courses/data-visualization/modules/05-rates-denominators-adjustment/instructor-notes.md)
- [Module 05 release record](courses/data-visualization/modules/05-rates-denominators-adjustment/release.json)
- [Module 06: Uncertainty, variation, and small numbers](courses/data-visualization/modules/06-uncertainty-variation-small-numbers/README.md)
- [Module 06 specification](docs/curriculum/courses/DA-730/modules/06-uncertainty-variation-small-numbers-spec.md)
- [Module 06 assessment](courses/data-visualization/modules/06-uncertainty-variation-small-numbers/assessment.md)
- [Module 06 instructor notes](courses/data-visualization/modules/06-uncertainty-variation-small-numbers/instructor-notes.md)
- [Module 06 release record](courses/data-visualization/modules/06-uncertainty-variation-small-numbers/release.json)
- [Week 3 visualization judgment checkpoint](courses/data-visualization/checkpoints/01-visualization-judgment-dossier/README.md)
- [Week 3 checkpoint specification](docs/curriculum/courses/DA-730/checkpoints/01-visualization-judgment-dossier-spec.md)
- [Module 07: Color and accessible visual communication](courses/data-visualization/modules/07-color-accessible-communication/README.md)
- [Module 07 specification](docs/curriculum/courses/DA-730/modules/07-color-accessible-communication-spec.md)
- [Module 07 assessment](courses/data-visualization/modules/07-color-accessible-communication/assessment.md)
- [Module 07 instructor notes](courses/data-visualization/modules/07-color-accessible-communication/instructor-notes.md)
- [Module 07 release record](courses/data-visualization/modules/07-color-accessible-communication/release.json)
- [Module 08: Time and process variation](courses/data-visualization/modules/08-time-process-variation/README.md)
- [Module 08 specification](docs/curriculum/courses/DA-730/modules/08-time-process-variation-spec.md)
- [Module 08 assessment](courses/data-visualization/modules/08-time-process-variation/assessment.md)
- [Module 08 instructor notes](courses/data-visualization/modules/08-time-process-variation/instructor-notes.md)
- [Module 08 release record](courses/data-visualization/modules/08-time-process-variation/release.json)
- [Module 09: Comparison and small multiples](courses/data-visualization/modules/09-comparison-small-multiples/README.md)
- [Module 09 specification](docs/curriculum/courses/DA-730/modules/09-comparison-small-multiples-spec.md)
- [Module 09 assessment](courses/data-visualization/modules/09-comparison-small-multiples/assessment.md)
- [Module 09 instructor notes](courses/data-visualization/modules/09-comparison-small-multiples/instructor-notes.md)
- [Module 09 release record](courses/data-visualization/modules/09-comparison-small-multiples/release.json)
- [Module 10: Maps, geography, and place](courses/data-visualization/modules/10-maps-geography-place/README.md)
- [Module 10 specification](docs/curriculum/courses/DA-730/modules/10-maps-geography-place-spec.md)
- [Module 10 assessment](courses/data-visualization/modules/10-maps-geography-place/assessment.md)
- [Module 10 instructor notes](courses/data-visualization/modules/10-maps-geography-place/instructor-notes.md)
- [Module 10 release record](courses/data-visualization/modules/10-maps-geography-place/release.json)
- [Module 11: Flow, networks, composition, and hierarchy](courses/data-visualization/modules/11-flow-networks-composition-hierarchy/README.md)
- [Module 11 specification](docs/curriculum/courses/DA-730/modules/11-flow-networks-composition-hierarchy-spec.md)
- [Module 11 assessment](courses/data-visualization/modules/11-flow-networks-composition-hierarchy/assessment.md)
- [Module 11 instructor notes](courses/data-visualization/modules/11-flow-networks-composition-hierarchy/instructor-notes.md)
- [Module 11 release record](courses/data-visualization/modules/11-flow-networks-composition-hierarchy/release.json)
- [Module 12: Dashboards and multi-view composition](courses/data-visualization/modules/12-dashboards-multi-view-composition/README.md)
- [Module 12 specification](docs/curriculum/courses/DA-730/modules/12-dashboards-multi-view-composition-spec.md)
- [Module 12 assessment](courses/data-visualization/modules/12-dashboards-multi-view-composition/assessment.md)
- [Module 12 instructor notes](courses/data-visualization/modules/12-dashboards-multi-view-composition/instructor-notes.md)
- [Module 12 release record](courses/data-visualization/modules/12-dashboards-multi-view-composition/release.json)
- [Week 6 applied visualization portfolio](courses/data-visualization/checkpoints/02-applied-visualization-portfolio/README.md)
- [Week 6 checkpoint specification](docs/curriculum/courses/DA-730/checkpoints/02-applied-visualization-portfolio-spec.md)
- [Week 6 checkpoint instructor notes](courses/data-visualization/checkpoints/02-applied-visualization-portfolio/instructor-notes.md)
- [Week 6 checkpoint release record](courses/data-visualization/checkpoints/02-applied-visualization-portfolio/release.json)
- [Module 13: Audience, annotation, narrative, and capstone](courses/data-visualization/modules/13-audience-annotation-narrative-capstone/README.md)
- [Module 13 specification](docs/curriculum/courses/DA-730/modules/13-audience-annotation-narrative-capstone-spec.md)
- [Module 13 assessment](courses/data-visualization/modules/13-audience-annotation-narrative-capstone/assessment.md)
- [Module 13 instructor notes](courses/data-visualization/modules/13-audience-annotation-narrative-capstone/instructor-notes.md)
- [Module 13 release record](courses/data-visualization/modules/13-audience-annotation-narrative-capstone/release.json)
- [Final decision-story capstone](courses/data-visualization/checkpoints/03-decision-story-capstone/README.md)
- [Final checkpoint specification](docs/curriculum/courses/DA-730/checkpoints/03-decision-story-capstone-spec.md)
- [Final checkpoint instructor notes](courses/data-visualization/checkpoints/03-decision-story-capstone/instructor-notes.md)
- [Final checkpoint release record](courses/data-visualization/checkpoints/03-decision-story-capstone/release.json)
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

1. Build FND-1 as its own straight-through technical foundations course.
2. Build FND-2 Module 04 from the accepted Week 3 checkpoint.
3. Complete the named DA-730 human reviews before alpha promotion.

## Licensing

Original documentation and synthetic data are planned for CC BY 4.0. Teaching and pipeline code are planned for the MIT License. Imported public data retain their source terms. See [LICENSE.md](LICENSE.md) for the scope and complete license links.

## Repository

https://github.com/ShuhanCS/open-clinical-learning-commons
