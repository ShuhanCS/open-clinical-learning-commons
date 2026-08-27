# Clinical data visualization and decision storytelling

This course teaches people to choose, build, critique, and explain visualizations for healthcare decisions. The organizing question is not "How do I make this in Tableau?" It is "What must a clinician, operational leader, researcher, or community partner see to make a sound decision?"

- Source course: DA-730, Analyzing, Visualizing, and Storytelling with Data
- Format: three credits, seven weeks, asynchronous online
- Course status: redesign draft; Module 04 is the first runnable candidate
- Default reproducible lab: R and ggplot2
- Tool policy: Tableau, Python, Power BI, Observable, and other approved tools may be used when the source file is submitted and the result can be reproduced

## Course outcome

By the end of the course, a learner can select and defend a healthcare visualization based on the decision, data structure, patient population, audience, uncertainty, and consequences of what the display leaves out.

A technically polished chart does not meet the outcome if the learner cannot explain:

- whose care or work is represented;
- which clinical or operational process produced the data;
- what decision the display supports;
- where the data came from;
- what the chart may conceal.

## Source-first data rule

Every assignment must include a data-source record. The record names the publisher, full URL, retrieval date, terms, variables used, transformations, and known limits.

The public course may use openly available aggregate health data, Synthea records, or a synthetic teaching dataset calibrated to a named public source. No real MGB patient record, partner dataset, or restricted clinical file enters this repository.

See the [course data-source register](data-source-register.md) for approved starting points and module assignments.

## Seven-week course structure

| Week | Module | Visualizations | Clinical application | Primary source |
|---|---|---|---|---|
| 1 | 01. From healthcare question to display | Tables, bars, dots, lollipops | Compare hospital performance while keeping denominators and sample size visible. | CMS HCAHPS |
| 1 | 02. Categories and comparisons | Grouped bars, dumbbells, slopegraphs | Compare patient experience or quality measures across hospitals and groups. | CMS HCAHPS |
| 2 | 03. Patient distributions | Histograms, density, box, violin, ridgeline | Find long waits, multiple care processes, and patient experiences hidden by an average. | Synthea plus the Module 04 teaching release |
| 2 | 04. Change over time | Line, slope, run, control, calendar heatmap | Separate a sustained process change from ordinary variation and seasonality. | CMS timely care or CDC WONDER |
| 3 | 05. Relationships | Scatter, bubble, hexbin, regression | Examine relationships among access, outcomes, volume, and community context without implying causation. | CDC PLACES plus Census ACS |
| 3 | 06. Uncertainty and benchmarking | Intervals, forest plots, caterpillar plots, funnel plots | Show how much confidence a clinical result or hospital comparison deserves. | ClinicalTrials.gov or CMS hospital quality data |
| 4 | 07. Patient journeys and clinical flow | Sankey, alluvial, cohort funnel, state transition | Show where patients wait, transfer, leave a pathway, or reach an outcome. | Synthea encounters |
| 4 | 08. Clinical networks | Node-link, adjacency matrix, chord diagram | Examine relationships among conditions, services, trial sites, or referral patterns. | ClinicalTrials.gov or Synthea |
| 5 | 09. Composition and hierarchy | Stacked bars, treemap, sunburst | Explain how diagnoses, services, or causes contribute to a total without confusing area with rate. | CDC WONDER or openFDA |
| 5 | 10. Equity and subgroup comparisons | Small multiples, diverging bars, dumbbells, ridgelines | Compare care or outcomes across populations while preserving denominators and uncertainty. | CDC PLACES plus Census ACS |
| 6 | 11. Place and access | Choropleth, proportional symbol, bivariate map | Locate access gaps and decide where outreach, workforce, or services may be needed. | CDC PLACES, Census ACS, and HRSA AHRF |
| 6 | 12. Clinical dashboards | KPI cards, sparklines, heatmaps, tables, coordinated views | Monitor a defined care process without compressing every question into one score. | CMS hospital datasets |
| 7 | 13. Annotation, narrative, and capstone | Annotated figure, board-ready display, accessible table | Communicate sourced evidence and a recommendation to a named healthcare audience. | One approved source from the register |

## Learning design

Each module follows the same sequence:

1. A healthcare stakeholder asks a decision question.
2. The learner inspects the source and decides what the data can support.
3. The learner chooses or critiques a visualization.
4. The learner identifies the patient group or care process that could be hidden.
5. The learner submits the visual, reproducible source, alt text, provenance record, and a short decision note.

## Assessment

| Work | Weight |
|---|---:|
| Weekly clinical visualization labs | 35% |
| Chart critique and repair briefs | 15% |
| Data provenance and transformation records | 10% |
| Clinical visualization portfolio and capstone | 40% |

Vendor-specific menu recall is not a standalone course outcome. A learner may use an approved tool, but the submission must remain reproducible and the visualization must support the stated healthcare decision.

## Available module

- [Clinical visualization chart atlas in R](chart_gallery.R)
- [Module 04: Distributions versus summaries](modules/04-distributions-vs-summaries/README.md)
- [Module 04 build specification](../../docs/specs/2026-08-15-ali-goff-module-04-build-spec.md)
- [Syllabus redesign](syllabus-redesign.md)
- [Course redesign plan](../../docs/plans/2026-08-26-clinical-data-visualization-course-redesign-plan.md)

Module 04 contains a synthetic emergency-department dataset, generator, validation checks, R lab, critique charts, assessment, answer key, and release record. It remains a candidate until faculty, emergency department, accessibility, and independent-instructor reviews are recorded.

## Source record

Ali Goff's full DA-730 redesign is preserved as a [Markdown source record](../../docs/source/ali-goff-da-730-course-redesign.md). The Fall 2025 syllabus supplied for this redesign remains outside the public repository. The [course foundation](../../docs/specs/2026-08-15-data-visualization-course-foundation.md) records the original module contract and the decision to keep the concept core independent of software.
