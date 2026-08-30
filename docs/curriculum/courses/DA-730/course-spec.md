# DA-730: Clinical data visualization and decision storytelling

- Status: course specification complete; module specifications and builds in progress
- Specification version: 0.19.0
- Credits: 3
- Delivery: asynchronous online half-term
- Instructional model: seven weeks mapped to the official half-term dates
- Total learner workload: 112.5 hours
- Position: standalone course outside the 30-credit program sequence
- Default lab environment: R and ggplot2
- Source course: DA-730, Analyzing, Visualizing, and Storytelling with Data
- Source record: `docs/source/ali-goff-da-730-course-redesign.md`
- Existing syllabus redesign: `courses/data-visualization/syllabus-redesign.md`
- Master architecture: `docs/specs/2026-08-29-curriculum-master-architecture-spec.md`

## Course decision

DA-730 remains a separate course. It replaces a Tableau-centered sequence with a concept-first course about how people read healthcare data, how visual choices affect interpretation, and how a display supports a decision.

The course keeps 13 numbered modules so the current public route, the existing Module 04 release, and the seven-week wrapper remain stable. The sequence restores the durable competencies from Ali Goff's redesign and retains useful visual forms from the current public syllabus. Module 04 remains Distributions versus summaries.

The course does not teach Tableau menu recall, dashboard decoration, or one preferred visual style. Tableau remains an allowed tool. R and ggplot2 provide the default reproducible path. Python, Power BI, Observable, and other approved tools are acceptable when the learner submits editable source files and another person can reproduce the result.

## Learners and prerequisites

The primary learner is a health data analytics student who has basic experience with tabular data but may not yet write R independently. The same materials should also work for clinicians, fellows, analysts, instructors, and program adopters who need visualization judgment without local patient data.

Learners should be able to:

- read a table and identify rows, columns, variables, and units;
- calculate or interpret a mean, median, proportion, and rate;
- run a supplied script or notebook;
- save and submit files in a defined folder structure;
- explain a healthcare question in plain language.

An optional week-zero bridge introduces the project workspace, RStudio or Posit Cloud, the small set of data verbs used in the labs, and the required source record. It is support material, not a numbered visualization module.

## Catalog description

This course teaches learners to select, build, critique, and explain data visualizations for clinical care, healthcare operations, research, quality improvement, and population health. Learners work with public or synthetic health data and examine encoding, perception, chart selection, distributions, rates, uncertainty, color, time, comparison, geography, flow, dashboards, accessibility, annotation, and narrative. Every graded display includes reproducible source files, data provenance, an accessible alternative, and a statement of the decision it supports.

## Course outcome

By the end of the course, a learner can produce and defend a healthcare visualization based on the decision, data structure, patient population, audience, uncertainty, and consequences of what the display leaves out.

A polished chart does not pass when the learner cannot explain where the data came from, who is represented, what the chart hides, or what should happen because of the result.

## Course learning outcomes

By the end of DA-730, learners will be able to:

| ID | Learners will be able to |
|---|---|
| CLO-1 | Translate a clinical, operational, research, or population-health question into a suitable chart, table, or justified decision not to visualize. |
| CLO-2 | Explain how variables map to position, length, angle, area, color, shape, and other visual channels. |
| CLO-3 | Select and critique displays using evidence about perception, data type, comparison, distribution, uncertainty, and audience. |
| CLO-4 | Explain how denominators, adjustment, missingness, aggregation, small groups, and uncertainty affect a healthcare interpretation. |
| CLO-5 | Build comparison, distribution, temporal, relationship, flow, network, hierarchical, geographic, and dashboard views with reproducible source files. |
| CLO-6 | Use color, typography, annotation, layout, alt text, data tables, and non-color cues to make a visualization accessible. |
| CLO-7 | Produce a complete source record and transformation record for every graded dataset. |
| CLO-8 | State the finding, intended audience, decision, uncertainty, and material limitation without claiming more than the data support. |

## Concept ownership

DA-730 owns the visualization and communication concepts that applied courses use later:

- visual encoding and the grammar of graphics;
- perception and the accuracy of visual channels;
- chart and table selection;
- distributions and the limits of summary statistics;
- counts, rates, denominators, and adjusted comparisons;
- uncertainty, variation, and small numbers;
- informative and accessible color;
- temporal displays and process variation;
- comparisons, ordering, shared scales, and small multiples;
- maps, geography, aggregation, and place-based interpretation;
- patient flow, networks, composition, and hierarchy;
- dashboards and multi-view composition;
- audience, annotation, narrative, alt text, and decision communication.

Applied courses should use these concepts in their domains. They should not repeat DA-730 as a chart catalog.

DA-730 does not own regression teaching, causal inference, survey methodology, risk adjustment methods, forecasting models, machine-learning development, financial modeling, or clinical implementation science. A visualization module may show those results, but another course owns the method.

## Course design

Each module follows the same learning sequence:

1. A named healthcare stakeholder has a decision to make.
2. The learner inspects the source and identifies what the data can support.
3. A short concept core explains the visual judgment without relying on software.
4. A worked healthcare example shows the decision and its consequences.
5. The learner runs, modifies, or authors a reproducible display.
6. The learner diagnoses and repairs flawed examples.
7. The learner submits the display, source files, provenance, accessible alternative, and decision note.

Misleading charts, ethics, equity, accessibility, and small-cell protection are threaded through the course. They are not saved for one closing lecture.

## Scaffold levels

Every lab has three support levels that use the same competency and dataset:

| Level | Learner action | Intended use |
|---|---|---|
| Run | Execute a complete script, inspect the outputs, and answer interpretation questions. | Learners new to R or the selected tool. |
| Modify | Change specified encodings, scales, grouping, labels, or layout and explain what improved or worsened. | Default starting level for the transitional cohort. |
| Author | Build the display from the data and decision question, then justify the design. | Learners ready for independent work. |

The support level may change without changing the module competency or grading standard.

## Schedule and workload

The course totals 112.5 learner hours. Official start and end dates come from the Institute half-term calendar. The final submission is due on the official last day.

| Week | Modules | Hours | Cumulative hours | Required course event |
|---:|---|---:|---:|---|
| 1 | 01 and 02 | 15.0 | 15.0 | Workspace and first source record complete |
| 2 | 03 and 04 | 16.0 | 31.0 | First worked healthcare case complete |
| 3 | 05 and 06 | 16.5 | 47.5 | Checkpoint 1: visualization judgment dossier |
| 4 | 07 and 08 | 16.0 | 63.5 | Accessible temporal display complete |
| 5 | 09 and 10 | 16.0 | 79.5 | Comparison and place-based interpretation complete |
| 6 | 11 and 12 | 16.5 | 96.0 | Checkpoint 2: applied visualization portfolio |
| 7 | 13 | 16.5 | 112.5 | Final checkpoint: decision-story capstone and defense |

## Module sequence

| ID | Module | Week | Hours | Primary decision |
|---|---|---:|---:|---|
| 01 | Encoding and the grammar of graphics | 1 | 7.0 | Which visual channels faithfully represent the variables in this healthcare question? |
| 02 | Perception and visual accuracy | 1 | 8.0 | Which display will the audience read most accurately and quickly? |
| 03 | Chart selection in practice | 2 | 8.0 | Should this question use a chart, table, multiple views, or no display? |
| 04 | Distributions versus summaries | 2 | 8.0 | Does the summary hide a patient group or operational tail that changes the decision? |
| 05 | Rates, denominators, and adjustment | 3 | 8.0 | Does the comparison remain meaningful after population size and denominator differences are made visible? |
| 06 | Uncertainty, variation, and small numbers | 3 | 8.5 | How much confidence should the audience place in the difference or trend? |
| 07 | Color and accessible visual communication | 4 | 7.5 | Can every learner and decision owner distinguish the information without relying on color alone? |
| 08 | Time and process variation | 4 | 8.5 | Is the observed change a trend, seasonal pattern, signal, or ordinary variation? |
| 09 | Comparison and small multiples | 5 | 7.5 | How can groups be compared without hiding scale, order, denominators, or within-group variation? |
| 10 | Maps, geography, and place | 5 | 8.5 | Does geography help answer the decision, and what does aggregation conceal? |
| 11 | Flow, networks, composition, and hierarchy | 6 | 8.0 | Which structure best represents a pathway, relationship, or part-to-whole question? |
| 12 | Dashboards and multi-view composition | 6 | 8.5 | What minimum set of views allows a named audience to monitor and act? |
| 13 | Audience, annotation, narrative, and capstone | 7 | 16.5 | How should sourced evidence be communicated so a named healthcare audience can make and revisit a decision? |

## Module 01 brief: Encoding and the grammar of graphics

- Prerequisites: week-zero bridge or equivalent workspace skills.
- Competency: Given a healthcare question and tabular data, map variables to suitable visual channels and explain why the resulting display has its form.
- Concepts: data types, marks, position, length, angle, area, color, shape, aesthetics, geometries, scales, coordinate systems, labels, and layers.
- Primary case: hospital patient-experience measures from CMS HCAHPS.
- Decision owner: hospital patient-experience director.
- Core source: https://data.cms.gov/provider-data/dataset/dgck-syfz
- Lab: rebuild one comparison from table to layered chart and trace each variable-to-channel mapping.
- Critique: diagnose a chart that maps an ordered measure to unordered color and a chart that uses area for a precise comparison.
- Submission: `module-01/encoding-map.md`, `module-01/analysis.R`, `module-01/figure.png`, `module-01/source-record.yml`, `module-01/alt-text.md`, and `module-01/decision-note.md`.
- Full specification: `docs/curriculum/courses/DA-730/modules/01-encoding-grammar-spec.md`.
- Runnable package: `courses/data-visualization/modules/01-encoding-grammar/`.
- Handoff: Module 02 tests whether those encodings can be read accurately.

## Module 02 brief: Perception and visual accuracy

- Prerequisites: Module 01.
- Competency: Compare plausible encodings using evidence about perceptual accuracy and select the one the audience can read with the least avoidable error.
- Concepts: position, length, angle, area, volume, color intensity, preattentive features, ordering, clutter, and audience effort.
- Primary case: comparison of hospital survey measures and response rates.
- Decision owner: health-system quality committee.
- Core source: https://data.cms.gov/provider-data/dataset/dgck-syfz
- Lab: compare a bar chart, dot plot, pie chart, and table for the same task and record accuracy, time, and interpretation errors.
- Critique: repair a pie chart with close values and a bubble chart whose areas exaggerate small differences.
- Submission: `module-02/perception-test.md`, `module-02/analysis.R`, `module-02/selected-display.png`, `module-02/source-record.yml`, `module-02/alt-text.md`, and `module-02/decision-note.md`.
- Full specification: `docs/curriculum/courses/DA-730/modules/02-perception-accuracy-spec.md`.
- Runnable package: `courses/data-visualization/modules/02-perception-accuracy/`.
- Handoff: Module 03 turns perception evidence into a repeatable chart-selection method.

## Module 03 brief: Chart selection in practice

- Prerequisites: Modules 01 and 02.
- Competency: Select and justify a chart, table, coordinated pair of views, or decision not to visualize based on the question, data structure, audience, and required precision.
- Concepts: comparison, distribution, time, relationship, part-to-whole, flow, geography, lookup tasks, exact values, and chart-selection failure modes.
- Primary case: choose a display for hospital leaders comparing patient experience, response rate, and survey volume.
- Decision owner: hospital executive team.
- Core source: https://data.cms.gov/provider-data/topics/hospitals
- Lab: complete ten question-to-display decisions, build two, and justify one case where a table is better.
- Critique: diagnose a dashboard that uses one visual form for every question.
- Submission: `module-03/selection-matrix.md`, `module-03/analysis.R`, `module-03/figures/`, `module-03/source-record.yml`, `module-03/alt-text.md`, and `module-03/decision-note.md`.
- Full specification: `docs/curriculum/courses/DA-730/modules/03-chart-selection-spec.md`.
- Runnable package: `courses/data-visualization/modules/03-chart-selection/`.
- Handoff: Module 04 shows why a valid summary and plausible chart may still conceal the decision-relevant structure.

## Module 04 brief: Distributions versus summaries

- Prerequisites: Modules 01 through 03 and basic summary statistics.
- Competency: Determine whether a summary statistic faithfully represents a distribution, choose a display that exposes consequential structure, and state what decision changes.
- Concepts: skew, multimodality, unequal group sizes, consequential tails, aggregation, mean, median, quantiles, box plots, violin plots, histograms, densities, and ECDFs.
- Primary case: synthetic emergency-department length of stay after a fast-track pathway.
- Decision owner: emergency-department operations leader.
- Core sources: https://data.cms.gov/provider-data/dataset/yv7e-xc69 and `courses/data-visualization/modules/04-distributions-vs-summaries/data/ed_los_2026.csv`.
- Lab: run the existing tiered R lesson and produce the four required views.
- Critique: repair a bar of means, a box plot that hides the second mode, and an average-of-averages comparison.
- Submission: `module-04/distribution-audit.md`, `module-04/analysis.R`, `module-04/figures/`, `module-04/source-record.yml`, `module-04/alt-text.md`, and `module-04/decision-note.md`.
- Full specification: `docs/curriculum/courses/DA-730/modules/04-distributions-summaries-spec.md`.
- Runnable package: `courses/data-visualization/modules/04-distributions-vs-summaries/`.
- Handoff: Module 05 asks whether the rates and denominators behind subgroup comparisons are stable and comparable.

## Module 05 brief: Rates, denominators, and adjustment

- Prerequisites: Modules 01 through 04 and basic proportions.
- Competency: Distinguish counts from rates, select the correct denominator, and explain when crude comparisons mislead.
- Concepts: numerator, denominator, prevalence, incidence, crude and adjusted rates, standardization, survey denominators, suppression, instability, and the ecological fallacy.
- Primary case: North Carolina adult diabetes-prevention partnership using every national CDC PLACES county `DIABETES` row, Census ACS adult-population context, and generalized county boundaries.
- Decision owner: population-health program director.
- Core sources: https://data.cdc.gov/d/fu4u-a9bh, https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b01001.dat, and https://tigerweb.geo.census.gov/arcgis/rest/services/Generalized_ACS2024/State_County/MapServer
- Lab: compare modeled counts, crude prevalence, age-adjusted prevalence with denominators and intervals, and the resulting county rank changes.
- Critique: repair a raw-count choropleth and a rate chart that omits the denominator and uncertainty.
- Submission: `module-05/rate-audit.md`, `module-05/analysis.R`, `module-05/figure.png`, `module-05/source-record.yml`, `module-05/alt-text.md`, and `module-05/decision-note.md`.
- Full specification: `docs/curriculum/courses/DA-730/modules/05-rates-denominators-adjustment-spec.md`.
- Runnable package: `courses/data-visualization/modules/05-rates-denominators-adjustment/`.
- Handoff: Module 06 adds uncertainty and small-number stability to the comparison.

## Module 06 brief: Uncertainty, variation, and small numbers

- Prerequisites: Modules 01 through 05 and an introductory understanding of intervals.
- Competency: Display estimate uncertainty and distinguish a stable difference from sampling noise, measurement variation, or a small denominator.
- Concepts: confidence intervals, prediction intervals, margins of error, funnel plots, caterpillar plots, forest plots, control limits, multiplicity, and suppressed or unreliable estimates.
- Primary case: Massachusetts hospital heart failure 30-day readmission estimates from the complete national CMS selected-measure release.
- Decision owner: clinical quality or research review committee.
- Core sources: https://data.cms.gov/provider-data/dataset/632h-zaca, https://data.cms.gov/provider-data/dataset/cvcs-xecj, and https://data.cms.gov/provider-data/dataset/y9us-9xdf
- Lab: compare a 53-position rank chart with CMS source intervals, the 21.3 national rate, denominators, and reporting status across all 65 Massachusetts hospital rows.
- Critique: repair a point-only top-ten league table and a chart that gives small and large denominators equal visual certainty.
- Submission: `module-06/uncertainty-brief.md`, `module-06/analysis.R`, `module-06/figure.png`, `module-06/source-record.yml`, `module-06/alt-text.md`, and `module-06/decision-note.md`.
- Checkpoint contribution: closes the week-3 visualization judgment dossier.
- Full specification: `docs/curriculum/courses/DA-730/modules/06-uncertainty-variation-small-numbers-spec.md`.
- Runnable package: `courses/data-visualization/modules/06-uncertainty-variation-small-numbers/`.
- Handoff: Module 07 tests whether the interval and status display works without relying on color.

## Module 07 brief: Color and accessible visual communication

- Prerequisites: Modules 01 through 03.
- Competency: Use color and non-color cues to encode information accessibly, and provide a text and table alternative that preserves the finding.
- Concepts: sequential, diverging, and qualitative palettes; luminance; contrast; color-vision differences; clinical color conventions; redundant cues; alt text; long descriptions; and data tables.
- Primary case: redesign a clinical quality display for color, print, screen, and assistive-technology access.
- Decision owner: clinical staff member reading the display under time pressure.
- Accessibility sources: https://www.w3.org/TR/WCAG22/, https://www.w3.org/WAI/tutorials/images/complex/, and https://www.cdc.gov/cove/about/section-508-accessibility.html
- Lab: create an accessible palette, add labels or shapes, write alt text, and produce a matching table.
- Critique: repair a red-green status chart and a low-contrast heatmap.
- Submission: `module-07/accessibility-audit.md`, `module-07/analysis.R`, `module-07/figure.png`, `module-07/data-table.csv`, `module-07/alt-text.md`, `module-07/decision-note.md`, and `module-07/ai-use.md`.
- Full specification: `docs/curriculum/courses/DA-730/modules/07-color-accessible-communication-spec.md`.
- Runnable package: `courses/data-visualization/modules/07-color-accessible-communication/`.
- Handoff: accessibility requirements apply to every remaining module.

## Module 08 brief: Time and process variation

- Prerequisites: Modules 01 through 07 and basic time ordering.
- Competency: Display change over time without distorting magnitude and distinguish trend, seasonality, ordinary variation, and a possible process signal.
- Concepts: line and run charts, indexing, baselines, seasonality, missing periods, reporting windows, smoothing, control charts, aspect ratio, and event annotations.
- Primary case: emergency or hospital process measures across reporting periods.
- Decision owner: hospital operations leader.
- Core source: https://data.cdc.gov/Public-Health-Surveillance/Weekly-Hospital-Respiratory-Data-HRD-Metrics-by-Ju/rhwp-grxi
- Lab: build a time view with an honest scale, denominator notes, intervention annotation, and signal interpretation.
- Critique: repair a dual-axis trend, a smoothed line that hides a short deterioration, and a control chart with unsupported limits.
- Submission: `module-08/time-audit.md`, `module-08/analysis.R`, `module-08/run-chart.png`, `module-08/comparison-chart.png`, `module-08/process-chart.png`, `module-08/decision-table.csv`, `module-08/alt-text.md`, `module-08/decision-note.md`, and `module-08/ai-use.md`.
- Full specification: `docs/curriculum/courses/DA-730/modules/08-time-process-variation-spec.md`.
- Runnable package: `courses/data-visualization/modules/08-time-process-variation/`.
- Handoff: Module 09 compares multiple groups or panels without losing the time or uncertainty context.

## Module 09 brief: Comparison and small multiples

- Prerequisites: Modules 01 through 08.
- Competency: Compare groups with ordering, shared scales, consistent encodings, and small multiples while preserving denominators and relevant within-group variation.
- Concepts: dot plots, dumbbells, slopes, faceting, shared axes, reference lines, sorting, baselines, panel density, and comparable units.
- Primary case: health outcome or care measure across hospitals, counties, or patient groups.
- Decision owner: quality, equity, or service-line leader.
- Core sources: https://data.cms.gov/provider-data/topics/hospitals and https://data.cdc.gov/d/fu4u-a9bh
- Lab: redesign one overloaded chart as ordered small multiples and test whether each panel supports the same comparison.
- Critique: repair panels with inconsistent scales and a subgroup display that uses a different baseline in each panel.
- Submission: `module-09/comparison-brief.md`, `module-09/analysis.R`, `module-09/figure.png`, `module-09/source-record.yml`, `module-09/alt-text.md`, and `module-09/decision-note.md`.
- Handoff: Module 10 asks whether place adds information or merely turns a comparison into a map.

## Module 10 brief: Maps, geography, and place

- Prerequisites: Modules 01 through 09 and Module 05 in particular.
- Competency: Use a map only when place matters, map rates rather than population size, and state how aggregation, boundaries, uncertainty, and stigma limit interpretation.
- Concepts: choropleths, proportional symbols, bivariate maps, bins, projections, spatial units, modifiable areal unit problem, rurality, access, and place-based language.
- Primary case: county health measure, population context, and health-workforce access.
- Decision owner: regional population-health or access planner.
- Core sources: https://data.cdc.gov/d/fu4u-a9bh, https://www.census.gov/data/developers/data-sets/acs-5year.html, and https://data.hrsa.gov/data/download
- Lab: build a rate map and an alternative non-map display, then choose which better supports the decision.
- Critique: repair a raw-count map, arbitrary bins, and stigmatizing labels.
- Submission: `module-10/place-brief.md`, `module-10/analysis.R`, `module-10/map.png`, `module-10/non-map.png`, `module-10/source-record.yml`, `module-10/alt-text.md`, and `module-10/decision-note.md`.
- Handoff: Module 11 handles structures that ordinary comparisons and maps do not express well.

## Module 11 brief: Flow, networks, composition, and hierarchy

- Prerequisites: Modules 01 through 10.
- Competency: Select and define a flow, network, or hierarchical display when links, states, or part-to-whole structure are central to the decision.
- Concepts: cohort funnels, Sankey and alluvial diagrams, state transitions, node-link diagrams, adjacency matrices, trees, stacked bars, treemaps, edge definitions, and double counting.
- Primary case: synthetic patient encounters and transitions from Synthea.
- Alternate case: sponsor-condition-site relationships from ClinicalTrials.gov.
- Decision owner: care-pathway, research-portfolio, or service-line leader.
- Core sources: https://synthetichealth.github.io/synthea/ and https://clinicaltrials.gov/data-api
- Lab: create one defined cohort flow and audit every node, edge, denominator, and dropped record.
- Critique: repair a Sankey with changing denominators, a hairball network, and a treemap that confuses area with rate.
- Submission: `module-11/structure-definition.md`, `module-11/analysis.R`, `module-11/figure.png`, `module-11/source-record.yml`, `module-11/alt-text.md`, and `module-11/decision-note.md`.
- Handoff: Module 12 decides when several views belong together in a monitoring display.

## Module 12 brief: Dashboards and multi-view composition

- Prerequisites: Modules 01 through 11.
- Competency: Assemble the minimum set of coordinated views needed for a named audience to monitor one care process and act on an exception.
- Concepts: audience tasks, KPI selection, overview and detail, coordinated scales, layout, hierarchy, annotation, sparklines, tables, filters, refresh cadence, thresholds, and dashboard failure modes.
- Primary case: small hospital monitoring dashboard using CMS measures.
- Decision owner: clinical operations or quality leader.
- Core source: https://data.cms.gov/provider-data/topics/hospitals
- Supporting guidance: https://www.ahrq.gov/evidencenow/tools/dashboard-best-practice.html and https://www.ahrq.gov/talkingquality/translate/display/index.html
- Lab: build a three-to-five-view monitoring display, remove any view without a decision purpose, and define the action linked to each threshold.
- Critique: repair a wall of KPIs, inconsistent time windows, and decorative widgets without decision use.
- Submission: `module-12/dashboard-brief.md`, `module-12/analysis.R`, `module-12/dashboard.png`, `module-12/measure-dictionary.csv`, `module-12/source-record.yml`, `module-12/alt-text.md`, and `module-12/decision-note.md`.
- Checkpoint contribution: closes the week-6 applied visualization portfolio.

## Module 13 brief: Audience, annotation, narrative, and capstone

- Prerequisites: Modules 01 through 12 and completed checkpoints 1 and 2.
- Competency: Produce and defend a sourced, reproducible, accessible visualization package that communicates a finding and recommendation to a named healthcare audience.
- Concepts: audience, finding-led titles, annotation, visual sequence, board-ready figures, patient-facing explanation, decision briefs, limitations, implementation questions, and oral defense.
- Primary case: learner-selected source from the approved register.
- Decision owner: named clinical, operational, research, patient, executive, or community audience.
- Lab: revise one analysis for two audiences and document what changes and what must remain stable.
- Critique: diagnose a story that overstates causality, hides uncertainty, or uses annotation to direct attention away from a material subgroup.
- Submission: the final decision-story capstone package defined below.
- Course handoff: the learner's portfolio becomes evidence of visualization competence for later applied or capstone work.

## Required submission package

Every module submission uses this minimum package:

```text
module-<id>/
  README.md
  analysis.R
  figure.png
  source-record.yml
  alt-text.md
  decision-note.md
  ai-use.md
```

An approved alternative tool may replace `analysis.R` with `analysis.py`, `analysis.ipynb`, a Tableau `.twb` workbook, a Power BI `.pbix` file, or another editable source. The instructor may require a PDF or SVG in addition to the PNG. The source record, accessible alternative, decision note, and AI-use record do not change with the tool.

Each module README states how to regenerate the figure from a clean checkout.

## Checkpoint 1: visualization judgment dossier

- Due: end of instructional week 3.
- Modules included: 01 through 06.
- Purpose: prove that the learner can select and defend a display before beginning the larger applied portfolio.

The learner submits:

```text
checkpoint-1/
  README.md
  selection-matrix.md
  figures/
    comparison.png
    distribution.png
    rate.png
    uncertainty.png
  analysis/
    comparison.R
    distribution.R
    rate.R
    uncertainty.R
  source-records/
    comparison-source.yml
    distribution-source.yml
    rate-source.yml
    uncertainty-source.yml
  critique-and-repair.md
  accessibility-check.md
  decision-brief.md
  ai-use.md
```

An approved alternative tool may replace an `.R` file with an editable `.py`, `.ipynb`, `.twb`, or `.pbix` file that keeps the same base name. The decision brief names the audience, finding, decision, uncertainty, and material limitation. The four figures must come from at least two approved public or synthetic sources. A dossier without reproducible source files or complete provenance is incomplete.

- Full checkpoint specification: `docs/curriculum/courses/DA-730/checkpoints/01-visualization-judgment-dossier-spec.md`.
- Runnable assembler, templates, and validator: `courses/data-visualization/checkpoints/01-visualization-judgment-dossier/`.

## Checkpoint 2: applied visualization portfolio

- Due: end of instructional week 6.
- Modules included: 07 through 12 plus revisions from checkpoint 1.
- Purpose: show that the learner can build accessible displays for time, comparison, place, structure, and monitoring.

The learner submits:

```text
checkpoint-2/
  README.md
  portfolio-index.md
  figures/
    accessible-display.png
    time-display.png
    comparison-display.png
    place-display.png
    structure-display.png
    dashboard.png
  analysis/
  source-records/
  critique-and-repair.md
  accessibility-report.md
  portfolio-reflection.md
  capstone-proposal.md
  ai-use.md
```

The capstone proposal fixes the audience, decision, source, population, main outcome or measure, planned display, expected limitation, and reproducibility approach before Module 13 begins.

## Final checkpoint: decision-story capstone

- Due: official last day of the half-term.
- Purpose: demonstrate the complete course outcome with one decision-ready release.

The learner submits:

```text
final-capstone/
  README.md
  decision-brief.md
  figure-primary.png
  figure-supporting.png
  accessible-table.csv
  alt-text.md
  analysis/
  data/
  source-record.yml
  transformation-record.md
  reproducibility-check.md
  critique-response.md
  ai-use.md
  defense/
    slides.pdf
    questions-and-responses.md
```

The supporting figure is optional unless it answers a different question from the primary display. The capstone must not use several views to avoid choosing a clear primary message.

## Assessment weights

| Work | Weight |
|---|---:|
| Module labs | 35% |
| Chart critique and repair briefs | 15% |
| Data provenance and transformation records | 10% |
| Applied portfolio and final capstone | 40% |
| Total | 100% |

The checkpoints package these components but do not replace the course weighting. Instructors must publish the exact points assigned to each included module before the course opens.

## Shared grading criteria

Every graded display uses six criteria:

| Criterion | What passing work demonstrates |
|---|---|
| Source and calculation integrity | The source, filters, denominators, calculations, and values are correct and documented. |
| Visual judgment | The display fits the question, data, comparison, and required precision better than reasonable alternatives. |
| Healthcare interpretation | The learner identifies the population or care process and keeps the claim inside what the evidence supports. |
| Decision consequence | The learner states what a named audience should do, inspect, or decide because of the display. |
| Accessibility and equity | The result does not rely on color alone, includes a useful text or table alternative, and does not hide a material group without explanation. |
| Reproducibility and accountability | The work reruns, the source record is complete, and any AI assistance is disclosed and verified. |

A polished visual cannot pass when source integrity, healthcare interpretation, or decision consequence fails.

## Public and synthetic data portfolio

| Source | Course use | Required caution | Full URL |
|---|---|---|---|
| CMS Provider Data Catalog, hospitals | Patient experience, quality, process, benchmark, time, and dashboard work. | Reporting periods, suppression, measure definitions, and risk adjustment differ by file. | https://data.cms.gov/provider-data/topics/hospitals |
| CMS HCAHPS | Survey comparisons, response rates, denominators, small multiples, and dashboards. | Keep completed-survey counts, response rates, dates, and footnotes. | https://data.cms.gov/provider-data/dataset/dgck-syfz |
| CMS Timely and Effective Care | Emergency and hospital process measures and temporal displays. | Aggregate measures do not reveal patient-level distributions. | https://data.cms.gov/provider-data/dataset/yv7e-xc69 |
| CDC PLACES | County health measures, comparisons, equity, and maps. | Estimates are model based and should not be used to claim that a local intervention caused change. | https://data.cdc.gov/d/fu4u-a9bh |
| Census ACS 5-year | Population denominators, margins of error, and community context. | Keep estimates and margins of error together; current API queries require a key. | https://www.census.gov/data/developers/data-sets/acs-5year.html |
| CDC WONDER | Mortality counts, rates, intervals, causes, place, and time. | Respect suppression, unreliable-rate flags, cause definitions, and denominator choices. | https://wonder.cdc.gov/datasets.html |
| ClinicalTrials.gov API | Trial enrollment, sponsors, locations, conditions, interventions, and results. | Registration and reported results do not establish intervention effectiveness or study quality. | https://clinicaltrials.gov/data-api |
| Synthea | Synthetic patient journeys, encounters, conditions, procedures, and networks. | The records are synthetic; realism depends on the generator version and modules. | https://synthetichealth.github.io/synthea/ |
| openFDA drug adverse events | Reporting patterns, time, hierarchy, networks, and data-quality critiques. | A report does not prove causation; duplicates, missingness, and reporting bias are expected. | https://open.fda.gov/apis/drug/event/ |
| HRSA Area Health Resources Files | Workforce and access comparisons and maps. | Keep the year and source definition for every variable. | https://data.hrsa.gov/data/download |

## Data release rule

Every course dataset receives:

- an immutable raw download when source terms allow redistribution;
- a source record with publisher, complete URL, retrieval date, version, terms, size, and checksum;
- a build script for any filter, join, recode, aggregation, or teaching extract;
- a data dictionary with units and denominators;
- validation checks for row counts, key uniqueness, missingness, expected ranges, and the teaching condition;
- a known-issues record covering suppression, bias, uncertainty, and interpretation limits;
- a small learner extract when the full public source is too large for the lesson;
- a synthetic variant when the lesson requires patient-level structure that public aggregate data cannot provide.

No real patient record, MGB patient data, partner dataset, or restricted clinical file enters the public course.

## Accessibility requirements

Every graded visualization must:

- use labels, position, shape, line style, or another redundant cue when color carries meaning;
- meet readable text and graphical contrast requirements;
- include concise alt text that states the chart type and main finding;
- include a longer description when the relationships cannot fit in short alt text;
- provide an accessible data table when exact values affect the decision;
- remain understandable in grayscale and at increased zoom;
- avoid unexplained abbreviations and internal clinical jargon;
- state suppressed, missing, or unreliable values rather than silently removing them.

Course accessibility references:

- https://www.w3.org/TR/WCAG22/
- https://www.w3.org/WAI/tutorials/images/complex/
- https://www.cdc.gov/cove/about/section-508-accessibility.html

## AI and agent policy

Learners may use AI or coding agents to explain code, diagnose errors, suggest tests, draft documentation, or compare design alternatives. Learners remain responsible for every transformation, visual choice, interpretation, source, citation, and submitted sentence.

Every module includes `ai-use.md` with:

- the tool used;
- the relevant prompts and outputs;
- what the learner accepted, changed, or rejected;
- the checks used to verify code and claims;
- a signed statement that no protected or identifiable patient data entered an outside service.

Submitting unverified output, inventing a source, hiding AI assistance, or using an agent to bypass the assessed judgment does not meet the course standard.

## Instructor interaction and feedback

The asynchronous course includes:

- one recorded concept walkthrough for each module;
- one worked healthcare case for each module;
- a live or recorded lab clinic each week;
- a critique session at the end of weeks 3 and 6;
- targeted feedback on checkpoint 1 before checkpoint 2 closes;
- capstone proposal feedback before Module 13;
- a final defense or structured recorded response;
- a monitored help channel with response expectations published in the syllabus.

Guest clinical speakers may explain the decision context and consequences. They do not replace the instructor's responsibility to teach and assess visual reasoning.

## Instructor package

Each module build must include:

```text
courses/data-visualization/modules/<module-id>-<slug>/
  README.md
  data-spec.md
  data/
  build-data.*
  validate-data.*
  lab.*
  critique.*
  assessment.md
  instructor-notes.md
  release.json
```

The package includes a worked answer, rubric, common misconceptions, expected timing, options for cutting content, alternate domain cases, accessibility notes, data provenance, release checks, and reviewer fields.

## Release maturity

| Stage | Evidence required |
|---|---|
| Specified | Course and module specifications define the competency, source, learner work, instructor package, and checks. |
| Runnable candidate | Data, lab, assessment, instructor notes, and automated checks run from a clean checkout. |
| Alpha | Faculty, clinical, accessibility, and independent-instructor reviews are recorded. |
| Beta | The module has been taught once and timing, defects, and revisions are recorded without student identifiers. |
| Stable | A second instructor or program has taught the module successfully and no release-blocking issue remains. |

Modules 01 through 08 are current runnable candidates. Their human reviews remain pending.

## Module build order

Build one numbered module at a time:

1. Module 01: Encoding and the grammar of graphics.
2. Module 02: Perception and visual accuracy.
3. Module 03: Chart selection in practice.
4. Reconcile and complete the existing Module 04 candidate.
5. Complete the released Module 05 candidate: Rates, denominators, and adjustment.
6. Complete the released Module 06 candidate: Uncertainty, variation, and small numbers.
7. Assemble and test checkpoint 1.
8. Module 07: Color and accessible visual communication.
9. Module 08: Time and process variation.
10. Module 09: Comparison and small multiples.
11. Module 10: Maps, geography, and place.
12. Module 11: Flow, networks, composition, and hierarchy.
13. Module 12: Dashboards and multi-view composition.
14. Assemble and test checkpoint 2.
15. Module 13: Audience, annotation, narrative, and capstone.
16. Assemble and test the final checkpoint and complete course wrapper.

Each completed module updates `docs/curriculum/BUILD-LEDGER.md`, bumps the release version when appropriate, runs its checks, and is committed and pushed before the next module begins.

## Course acceptance checks

Run `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/check-curriculum-specs.ps1` before committing a course-specification change.

- [x] The course has 13 numbered modules across seven instructional weeks.
- [x] Module 04 remains Distributions versus summaries and retains its current runnable package.
- [x] Module 05 has a complete source-first specification and runnable teaching package.
- [x] Module 06 has a complete source-first specification, runnable teaching package, and exact checkpoint handoff.
- [x] Module 07 has a complete accessibility specification, source-preserving teaching table, runnable lab, critique set, assessment, instructor key, and release record.
- [x] Module 08 has a complete time-and-process specification, pinned CDC NHSN releases, runnable lab, critique set, assessment, instructor key, and release record.
- [x] The sequence restores encoding, perception, chart selection, distributions, rates, uncertainty, color, time, comparison, maps, composition, dashboards, audience, and narrative.
- [x] The course totals 112.5 learner hours.
- [x] Checkpoints have exact deliverables at weeks 3, 6, and the official half-term end date.
- [x] Every module brief names a decision, audience, competency, data source, learner work, submission, and handoff.
- [x] R and ggplot2 are the default path without making software syntax the learning outcome.
- [x] Alternative tools require editable source files and reproducibility.
- [x] The public-data portfolio uses authoritative publishers and states important limits.
- [x] Accessibility and AI accountability are graded requirements.
- [ ] Each module has its full specification and runnable teaching package.
- [x] Checkpoint 1 assembly and validator run from a clean checkout.
- [ ] Faculty, clinical, accessibility, and independent-instructor reviews are recorded.
- [ ] The official DA-730 versus DA-830 course number is confirmed for publication.
- [ ] The course has reached at least beta after a taught pilot.

## Publication decisions still required

These decisions do not block module specification and implementation:

1. Confirm whether the catalog number is DA-730 or DA-830. The working number remains DA-730.
2. Confirm the term, instructor, and institutional policy text for the official syllabus.
3. Name the faculty, clinical, accessibility, and independent-instructor reviewers.
4. Confirm whether the first live cohort requires every learner to use R or may select an approved alternative tool.

Joe Joseph, MD, is designated for the leadership block in the applied courses. DA-730 does not include that separate leadership block unless the program later assigns him a visualization-specific role.
