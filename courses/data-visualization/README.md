# Clinical data visualization and decision storytelling

This course teaches people to choose, build, critique, and explain visualizations for healthcare decisions. The organizing question is not "How do I make this in Tableau?" It is "What must a clinician, operational leader, researcher, or community partner see to make a sound decision?"

- Source course: DA-730, Analyzing, Visualizing, and Storytelling with Data
- Format: three credits, seven weeks, asynchronous online
- Course status: full course specification complete; Modules 01, 02, and 04 are runnable release candidates
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
- [Module 04: Distributions versus summaries](modules/04-distributions-vs-summaries/README.md)
- [Module 04 build specification](../../docs/specs/2026-08-15-ali-goff-module-04-build-spec.md)
- [Syllabus redesign](syllabus-redesign.md)
- [Course redesign plan](../../docs/plans/2026-08-26-clinical-data-visualization-course-redesign-plan.md)

Module 01 contains a pinned public CMS HCAHPS extract and an encoding lab. Module 02 reuses that release for a scored graphical-perception exercise. Module 04 contains the equivalent teaching package around a synthetic emergency-department dataset. All three remain candidates until their required human reviews are recorded.

## Source record

Ali Goff's full DA-730 redesign is preserved as a [Markdown source record](../../docs/source/ali-goff-da-730-course-redesign.md). The Fall 2025 syllabus supplied for this redesign remains outside the public repository. The [course foundation](../../docs/specs/2026-08-15-data-visualization-course-foundation.md) records the original module contract and the decision to keep the concept core independent of software.
