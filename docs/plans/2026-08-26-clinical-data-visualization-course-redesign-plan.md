# Clinical data visualization course redesign plan

- Status: implemented for program review
- Date: 2026-08-26
- Source syllabus: `C:\Users\Shuha\Downloads\DA730_Syllabus_Storytelling_Fall2025.docx`
- Course format: three credits, seven weeks, asynchronous online
- Working course number: DA-730

## Problem

The source syllabus is organized around Tableau operations. Learners move through navigation, joins, level-of-detail expressions, calculations, PDF import, and advanced dashboards. Several exercises use sales, sports, geographic, or unspecified datasets. This structure teaches a software package more directly than it teaches healthcare visualization judgment.

The source document lists the course as DA-830, while its filename and the existing course records use DA-730. Use DA-730 in the redesign draft and confirm the official number before publication.

## Course promise

Learners will choose, build, critique, and explain visualizations for clinical, operational, research, and population-health decisions. Every graded visualization will identify:

- the healthcare question;
- the patient population, care process, or health system being represented;
- the person who must use the display;
- the decision the display supports;
- the source and limits of the data;
- what the chosen display reveals and what it can hide.

Software supports the work but does not determine the module sequence. R starter files are the first reproducible implementation. Python, Tableau, Power BI, or another approved tool may be used when the learner submits the source file and the result can be reproduced.

## Source-first data rule

Every assignment dataset must have a source record with the publisher, full URL, retrieval date, license or terms, variables used, transformation steps, and known limits.

Public patient-level data are not required. A module may use:

1. openly available aggregate healthcare or public-health data;
2. synthetic records from a named public generator such as Synthea;
3. a synthetic teaching dataset calibrated to a named public aggregate source, with the generator and assumptions published.

No real MGB patient records, partner data, or restricted clinical data enter the public course repository. A synthetic dataset cannot be described as evidence about a real hospital or intervention.

## Seven-week sequence

| Week | Modules | Visualization families | Healthcare decision |
|---|---|---|---|
| 1 | 1. Question to display; 2. Categories and comparisons | Tables, bars, dots, lollipops | Compare hospital performance without hiding denominators or sample size. |
| 2 | 3. Patient distributions; 4. Change over time | Histograms, density, box, violin, ridgeline, line, slope, run, and control charts | Detect long waits and distinguish common variation from a meaningful process change. |
| 3 | 5. Relationships; 6. Uncertainty | Scatter, bubble, hexbin, regression, confidence intervals, forest plots, and funnel plots | Examine associations and show how much confidence a clinical or quality estimate deserves. |
| 4 | 7. Patient journeys; 8. Clinical networks | Sankey, alluvial, cohort funnels, state transitions, node-link networks, and chord diagrams | Find where patients leave a pathway, wait, transfer, or move between services. |
| 5 | 9. Composition and hierarchy; 10. Equity comparisons | Stacked bars, treemaps, sunbursts, heatmaps, small multiples, dumbbells, and diverging bars | Allocate resources and compare care across populations without erasing subgroup differences. |
| 6 | 11. Place and access; 12. Clinical dashboards | Choropleths, proportional symbols, bivariate maps, KPI cards, sparklines, tables, and coordinated views | Locate access gaps and assemble a monitoring view for a defined clinical or operational audience. |
| 7 | 13. Annotation, narrative, and capstone | Annotated charts, scrollytelling sequence, board-ready figure, and accessible data table | Turn sourced evidence into a recommendation while stating uncertainty and limits. |

## Assessment model

- Weekly clinical visualization labs: 35 percent.
- Chart critique and repair briefs: 15 percent.
- Data provenance and transformation records: 10 percent.
- Clinical visualization portfolio and capstone: 40 percent.

Each submission includes the visualization, reproducible source, source record, alt text, and a short decision note. Menu recall and vendor-specific syntax are not standalone learning outcomes.

## Initial source register

| Source | Intended use | Full URL |
|---|---|---|
| CMS Provider Data Catalog, hospitals | Hospital quality, patient experience, timely care, readmission, and volume comparisons | https://data.cms.gov/provider-data/topics/hospitals |
| CMS Timely and Effective Care, Hospital | Emergency and hospital process measures | https://data.cms.gov/provider-data/dataset/yv7e-xc69 |
| CMS HCAHPS, Hospital | Patient-experience comparisons, small multiples, and dashboards | https://data.cms.gov/provider-data/dataset/dgck-syfz |
| CDC PLACES, county data | Population-health comparisons and maps | https://data.cdc.gov/d/fu4u-a9bh |
| U.S. Census ACS 5-year API | Population denominators and community context | https://www.census.gov/data/developers/data-sets/acs-5year.html |
| CDC WONDER | Mortality counts and rates by cause, place, population, and time | https://wonder.cdc.gov/datasets.html |
| ClinicalTrials.gov API | Trial portfolios, enrollment, geography, sponsors, conditions, and reported results | https://clinicaltrials.gov/data-api |
| Synthea | Synthetic longitudinal patient records for journeys, Sankey diagrams, and networks | https://synthetichealth.github.io/synthea/ |
| openFDA drug adverse events | Reporting patterns, hierarchy, time, and safety-signal examples with strong non-causality warnings | https://open.fda.gov/apis/drug/event/ |
| HRSA Area Health Resources Files | Health-workforce counts and provider-to-population ratios | https://data.hrsa.gov/data/download |

## Deliverables

- Rewrite the course landing page around visualization families and healthcare decisions.
- Add a course data-source register.
- Add a syllabus redesign in Markdown and Word formats.
- Use Module 04 as the first worked example of the healthcare integration standard.
- Update the beginner UI so the healthcare process and decision are explicit.
- Preserve the source syllabus and create a new redesign file rather than overwriting it.

## Release checks

- Every module row names a visualization family, healthcare use, and data source.
- Every public URL is complete and points to an authoritative publisher or project.
- The syllabus does not require Tableau or any other single vendor.
- The course includes flow, network, uncertainty, distribution, temporal, comparison, hierarchical, geographic, and dashboard displays.
- The Word redesign validates and renders on US Letter pages.
- Module 04 data and chart calculations continue to pass their existing checks.
