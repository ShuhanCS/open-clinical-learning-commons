# Clinical data visualization and decision storytelling

This course teaches people to choose, build, critique, and explain visualizations for healthcare decisions. The organizing question is not "How do I make this in Tableau?" It is "What must a clinician, operational leader, researcher, or community partner see to make a sound decision?"

- Source course: DA-730, Analyzing, Visualizing, and Storytelling with Data
- Format: three credits, seven weeks, asynchronous online
- Course status: all 13 module specifications and all three checkpoint packages are runnable release candidates
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

| Week | Module | Hours | Primary decision |
|---|---|---:|---|
| 1 | 01. Encoding and the grammar of graphics | 7.0 | Which visual channels faithfully represent the variables in this healthcare question? |
| 1 | 02. Perception and visual accuracy | 8.0 | Which display will the audience read most accurately and quickly? |
| 2 | 03. Chart selection in practice | 8.0 | Should this question use a chart, table, multiple views, or no display? |
| 2 | 04. Distributions versus summaries | 8.0 | Does the summary hide a patient group or operational tail that changes the decision? |
| 3 | 05. Rates, denominators, and adjustment | 8.0 | Does the comparison remain meaningful after population size and denominator differences are visible? |
| 3 | 06. Uncertainty, variation, and small numbers | 8.5 | How much confidence should the audience place in the difference or trend? |
| 4 | 07. Color and accessible visual communication | 7.5 | Can every decision owner distinguish the information without relying on color alone? |
| 4 | 08. Time and process variation | 8.5 | Is the observed change a trend, seasonal pattern, signal, or ordinary variation? |
| 5 | 09. Comparison and small multiples | 7.5 | How can groups be compared without hiding scale, order, denominators, or within-group variation? |
| 5 | 10. Maps, geography, and place | 8.5 | Does geography help answer the decision, and what does aggregation conceal? |
| 6 | 11. Flow, networks, composition, and hierarchy | 8.0 | Which structure best represents a pathway, relationship, or part-to-whole question? |
| 6 | 12. Dashboards and multi-view composition | 8.5 | What minimum set of views allows a named audience to monitor and act? |
| 7 | 13. Audience, annotation, narrative, and capstone | 16.5 | How should sourced evidence help a named healthcare audience make and revisit a decision? |

Total learner time is 112.5 hours. The complete course, checkpoint, data, accessibility, AI, and release contracts are in the [DA-730 course specification](../../docs/curriculum/courses/DA-730/course-spec.md).

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

## Available modules and tools

- [Clinical visualization chart atlas in R](chart_gallery.R)
- [Module 01: Encoding and the grammar of graphics](modules/01-encoding-grammar/README.md)
- [Module 01 specification](../../docs/curriculum/courses/DA-730/modules/01-encoding-grammar-spec.md)
- [Module 01 release record](modules/01-encoding-grammar/release.json)
- [Module 02: Perception and visual accuracy](modules/02-perception-accuracy/README.md)
- [Module 02 specification](../../docs/curriculum/courses/DA-730/modules/02-perception-accuracy-spec.md)
- [Module 02 release record](modules/02-perception-accuracy/release.json)
- [Module 03: Chart selection in practice](modules/03-chart-selection/README.md)
- [Module 03 specification](../../docs/curriculum/courses/DA-730/modules/03-chart-selection-spec.md)
- [Module 03 release record](modules/03-chart-selection/release.json)
- [Module 04: Distributions versus summaries](modules/04-distributions-vs-summaries/README.md)
- [Module 04 specification](../../docs/curriculum/courses/DA-730/modules/04-distributions-summaries-spec.md)
- [Module 04 original build record](../../docs/specs/2026-08-15-ali-goff-module-04-build-spec.md)
- [Module 05: Rates, denominators, and adjustment](modules/05-rates-denominators-adjustment/README.md)
- [Module 05 specification](../../docs/curriculum/courses/DA-730/modules/05-rates-denominators-adjustment-spec.md)
- [Module 05 release record](modules/05-rates-denominators-adjustment/release.json)
- [Module 06: Uncertainty, variation, and small numbers](modules/06-uncertainty-variation-small-numbers/README.md)
- [Module 06 specification](../../docs/curriculum/courses/DA-730/modules/06-uncertainty-variation-small-numbers-spec.md)
- [Module 06 release record](modules/06-uncertainty-variation-small-numbers/release.json)
- [Week 3 visualization judgment checkpoint](checkpoints/01-visualization-judgment-dossier/README.md)
- [Week 3 checkpoint specification](../../docs/curriculum/courses/DA-730/checkpoints/01-visualization-judgment-dossier-spec.md)
- [Module 07: Color and accessible visual communication](modules/07-color-accessible-communication/README.md)
- [Module 07 specification](../../docs/curriculum/courses/DA-730/modules/07-color-accessible-communication-spec.md)
- [Module 07 release record](modules/07-color-accessible-communication/release.json)
- [Module 08: Time and process variation](modules/08-time-process-variation/README.md)
- [Module 08 specification](../../docs/curriculum/courses/DA-730/modules/08-time-process-variation-spec.md)
- [Module 08 release record](modules/08-time-process-variation/release.json)
- [Module 09: Comparison and small multiples](modules/09-comparison-small-multiples/README.md)
- [Module 09 specification](../../docs/curriculum/courses/DA-730/modules/09-comparison-small-multiples-spec.md)
- [Module 09 release record](modules/09-comparison-small-multiples/release.json)
- [Module 10: Maps, geography, and place](modules/10-maps-geography-place/README.md)
- [Module 10 specification](../../docs/curriculum/courses/DA-730/modules/10-maps-geography-place-spec.md)
- [Module 10 release record](modules/10-maps-geography-place/release.json)
- [Module 11: Flow, networks, composition, and hierarchy](modules/11-flow-networks-composition-hierarchy/README.md)
- [Module 11 specification](../../docs/curriculum/courses/DA-730/modules/11-flow-networks-composition-hierarchy-spec.md)
- [Module 11 release record](modules/11-flow-networks-composition-hierarchy/release.json)
- [Module 12: Dashboards and multi-view composition](modules/12-dashboards-multi-view-composition/README.md)
- [Module 12 specification](../../docs/curriculum/courses/DA-730/modules/12-dashboards-multi-view-composition-spec.md)
- [Module 12 release record](modules/12-dashboards-multi-view-composition/release.json)
- [Week 6 applied visualization portfolio](checkpoints/02-applied-visualization-portfolio/README.md)
- [Week 6 checkpoint specification](../../docs/curriculum/courses/DA-730/checkpoints/02-applied-visualization-portfolio-spec.md)
- [Week 6 checkpoint release record](checkpoints/02-applied-visualization-portfolio/release.json)
- [Module 13: Audience, annotation, narrative, and capstone](modules/13-audience-annotation-narrative-capstone/README.md)
- [Module 13 specification](../../docs/curriculum/courses/DA-730/modules/13-audience-annotation-narrative-capstone-spec.md)
- [Module 13 release record](modules/13-audience-annotation-narrative-capstone/release.json)
- [Final decision-story capstone](checkpoints/03-decision-story-capstone/README.md)
- [Final checkpoint specification](../../docs/curriculum/courses/DA-730/checkpoints/03-decision-story-capstone-spec.md)
- [Final checkpoint release record](checkpoints/03-decision-story-capstone/release.json)
- [Syllabus redesign](syllabus-redesign.md)
- [Course redesign plan](../../docs/plans/2026-08-26-clinical-data-visualization-course-redesign-plan.md)

Module 01 contains a pinned public CMS HCAHPS extract and an encoding lab. Module 02 reuses that release for a scored graphical-perception exercise. Module 03 uses the same source to choose among comparison, lookup, relationship, and no-display responses through a 10-case matrix. Module 04 uses every national CMS OP_18b hospital row to anchor an explicitly synthetic emergency-department distribution exercise. Module 05 uses complete national CDC PLACES diabetes rows, ACS county population context, and North Carolina boundary data to teach counts, crude prevalence, adjustment, and denominators. Module 06 uses every national CMS heart failure readmission row, the national benchmark, and official footnotes to show why point ranks exceed evidence of separation. Module 07 preserves that exact 65-hospital case while adding color, shape, text, grayscale, contrast, table, and long-description access paths. Module 08 preserves a 6,208-row CDC NHSN jurisdiction release and uses 94 consecutive Massachusetts weeks to teach raw time views, seasonality, smoothing, reporting context, and exploratory process limits. Module 09 preserves 31,450 CDC PLACES rows and uses 500 complete North Carolina county-measure rows to teach fixed scales, shared order, consistent references, crude-versus-adjusted dumbbells, and transparent review rules. Module 10 adds 1,546 public HRSA primary-care HPSA rows and reuses 7,121 Census boundary points to compare a health map with an all-county non-map view, then records why direct HPSA data were redistributable while AHRF clinician fields were not. Module 11 preserves all 53,346 encounters from the selected Synthea sample fields and builds a one-person-per-index transition cohort, conserved flow, exact matrix, and endpoint composition. Module 12 preserves 186 public CMS rows for 62 Massachusetts hospitals and three emergency department measures, then builds a five-view historical public-reporting dashboard with separate units, visible lag, mock-trigger ownership, an exact table, and an ordered review action. Module 13 reuses that exact evidence to produce technical and executive decision stories while holding values, definitions, time, trigger origin, and action constant. The Week 3 package renders one comparison, distribution, rate, and uncertainty figure from the first six releases. The Week 6 package renders six applied artifacts with matching analyses, exact tables, source records, text alternatives, review documents, and a capstone approval proposal. The final package creates a portable three-file evidence release, requires complete provenance and accessibility records, and ends with a scored oral defense and reviewer disposition. All thirteen modules and all three checkpoints remain candidates until their required human reviews are recorded.

## Source record

Ali Goff's full DA-730 redesign is preserved as a [Markdown source record](../../docs/source/ali-goff-da-730-course-redesign.md). The Fall 2025 syllabus supplied for this redesign remains outside the public repository. The [course foundation](../../docs/specs/2026-08-15-data-visualization-course-foundation.md) records the original module contract and the decision to keep the concept core independent of software.
