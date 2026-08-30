# DA-730: Clinical data visualization and decision storytelling

- Document status: redesign draft `0.1.0`
- Source: Fall 2025 syllabus supplied by Shuhan He
- Credits: 3
- Format: seven-week asynchronous online course
- Course number note: the source DOCX lists DA-830, while its filename and existing course records use DA-730. Confirm the official number before release.

## Catalog description

This course teaches the design and interpretation of data visualizations for clinical care, healthcare operations, research, quality improvement, and population health. Learners work with sourced public or synthetic health data and choose among comparison, distribution, temporal, relationship, uncertainty, flow, network, hierarchical, geographic, and dashboard displays. They produce reproducible visualizations and explain the healthcare decision each display supports, the population it represents, and the evidence it may hide.

The course is software independent. R starter files provide the first reproducible path. Learners may use Python, Tableau, Power BI, Observable, or another approved tool when they submit the source file and document the workflow.

## Learning outcomes

By the end of the course, learners will be able to:

1. Translate a clinical, operational, research, or population-health question into a suitable display and explain why that display fits the decision.
2. Build and critique comparison, distribution, time, relationship, uncertainty, flow, network, hierarchy, geographic, and dashboard visualizations.
3. Explain how patient mix, denominators, missing data, uncertainty, aggregation, and small groups affect a healthcare interpretation.
4. Identify which patients, staff, or care processes may disappear when a chart compresses or combines data.
5. Use color, annotation, typography, layout, and accessible alternatives to communicate with clinical, executive, patient, and public audiences.
6. Produce a source record and reproducible workflow for every visualization.
7. State a decision, uncertainty, and limitation without claiming more than the data support.

## Data and software

Every graded dataset comes from the [course source register](data-source-register.md). Public aggregate data, Synthea records, and documented synthetic teaching releases are allowed. Real MGB patient records, restricted partner data, and any other protected health information are outside the public course.

R and ggplot2 starter files are supplied. Flow and interactive assignments may also use ggalluvial, Plotly, networkD3, Python, Tableau, or another approved tool. Students are graded on visualization judgment, healthcare interpretation, provenance, reproducibility, and communication rather than vendor-specific menu recall.

## Required submission package

Unless an assignment says otherwise, submit:

1. the final visualization in a portable format;
2. the script, notebook, or workbook used to create it;
3. a source record with the full URL, retrieval date, terms, variables, and transformations;
4. one or two sentences of alt text;
5. a short note naming the healthcare finding, audience, decision, and limitation.

## Grading

| Activity | Percent |
|---|---:|
| Weekly clinical visualization labs | 35% |
| Chart critique and repair briefs | 15% |
| Data provenance and transformation records | 10% |
| Clinical visualization portfolio and capstone | 40% |

A polished visualization cannot pass if the data source is missing, the healthcare interpretation is unsupported, or the display hides a material subgroup without explanation.

## Course schedule

| Week | Module and visual forms | Healthcare application | Assignment and source |
|---|---|---|---|
| 1 | From question to display: tables, bars, dots, lollipops | Compare patient-experience measures while retaining survey counts and response rates. | Build and critique a hospital comparison using CMS HCAHPS. |
| 1 | Categories and comparisons: grouped bars, dumbbells, slopegraphs | Show differences across hospitals, measures, or reporting periods without turning rank into quality. | Repair a misleading hospital scorecard using CMS HCAHPS. |
| 2 | Patient distributions: histogram, density, box, violin, ridgeline | Find long waits and different care processes hidden by a department-wide average. | Complete Module 04 with the synthetic emergency-department release and its source note. |
| 2 | Change over time: line, slope, run, control, calendar heatmap | Decide whether a quality or access measure changed beyond ordinary variation. | Build a sourced time view from CMS timely care or CDC WONDER. |
| 3 | Relationships: scatter, bubble, hexbin, regression | Examine associations among access, outcomes, volume, and community context without claiming causation. | Join CDC PLACES to Census ACS and write an interpretation limit. |
| 3 | Uncertainty: confidence intervals, forest, caterpillar, funnel | Compare estimates while accounting for sample size and uncertainty. | Build an interval or funnel display from ClinicalTrials.gov or CMS. |
| 4 | Patient journeys: Sankey, alluvial, cohort funnel, state transition | Show where a cohort waits, transfers, leaves a pathway, or reaches an outcome. | Build a sourced patient-flow diagram from Synthea encounters. |
| 4 | Clinical networks: node-link, matrix, chord | Examine condition, service, trial-site, or sponsor relationships without implying referral or causation that the data do not contain. | Create a network from ClinicalTrials.gov or Synthea and document each edge definition. |
| 5 | Composition and hierarchy: stacked bars, treemap, sunburst | Explain how causes, services, or reported events contribute to a total. | Compare a stacked bar with a treemap using CDC WONDER or openFDA. |
| 5 | Equity comparisons: small multiples, diverging bars, dumbbells, ridgelines | Compare populations without hiding denominators, uncertainty, or within-group variation. | Build an equity comparison using CDC PLACES and ACS. |
| 6 | Place and access: choropleth, proportional symbol, bivariate map | Identify geographic patterns in health, access, and workforce while avoiding causal or stigmatizing claims. | Combine CDC PLACES, Census ACS, and HRSA AHRF. |
| 6 | Clinical dashboards: KPI cards, sparklines, heatmaps, tables | Monitor one care process for a named audience without collapsing every question into one score. | Build a small CMS hospital dashboard and defend every included measure. |
| 7 | Annotation, narrative, and capstone | Communicate sourced evidence to a clinical, operational, research, patient, or public audience. | Submit a portfolio and one decision-ready capstone from an approved source. |

## Capstone

Choose one approved public or synthetic healthcare source. Define the population, care process, audience, and decision before choosing the display. The capstone must include one primary visualization and may add one supporting view only when it answers a different question.

Submit the visual, reproducible source, data extract or retrieval script, provenance record, alt text, and a two-paragraph decision brief. The brief must distinguish the finding from its interpretation and state one material limitation.

## Weekly critique questions

Every critique asks:

- What healthcare question does this display answer?
- Which patient group, clinical process, or denominator is easy to miss?
- What decision could change because of that omission?
- What display or annotation would repair the problem?
- Does the source support the claim being made?

## Generative AI

Generative AI may support brainstorming, code explanation, debugging, and copy editing. Students remain responsible for every data transformation, chart choice, interpretation, citation, and submitted sentence. Any AI use must follow the current Institute academic-integrity policy and the assignment disclosure instructions.

## Accessibility and responsible communication

Visualizations must not rely on color alone. Labels and scales must be readable, alt text must state the finding, and a table must be available when exact values affect the decision. Learners must follow source suppression rules, avoid re-identification, and distinguish association from causation.

## Institutional policy sections to retain

The final Institute syllabus should carry forward the current approved language and URLs for accessibility accommodations, academic integrity, health equity, course-material use, student support, grading, and course evaluation. Faculty should review those sections against the current Institute catalog before release.

Current catalog: https://mghihp.smartcatalogiq.com/en/current/catalog/

## Decisions to confirm before publication

1. Confirm whether the official course number is DA-730 or DA-830.
2. Confirm the term and instructor information.
3. Approve the replacement of three Tableau exams with weekly labs, source records, critiques, and a capstone portfolio.
4. Confirm R as the default starter environment and the policy for alternative tools.
5. Name the faculty, clinical, accessibility, and independent-instructor reviewers.
