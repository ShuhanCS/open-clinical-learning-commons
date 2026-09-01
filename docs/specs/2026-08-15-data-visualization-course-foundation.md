# Open Clinical Learning Commons: data visualization course foundation

- Status: active draft; Module 04 runnable release candidate complete, human review pending
- Date: 2026-08-15
- Source course: DA-730, Analyzing, Visualizing, and Storytelling with Data

## Decision

Use the DA-730 redesign as the first working application of the Open Clinical Learning Commons.

The first build should be one complete module, not the full course and not the full synthetic health system. Module 04, Distributions versus summaries, is the vertical slice because Ali Goff's source document already defines its competency, data requirements, lab, critique exercises, assessments, and instructor notes.

This first module will test whether a teaching unit can move between Health Data Analytics courses, emergency medicine education, and another institution without rewriting the concept or exposing patient data.

## Source material

This specification draws from three documents supplied for the project:

- Ali Goff's redesign of DA-730, including a complete Module 04 example;

The original DOCX and fellowship PDFs are not copied into this public repository. Course authors should confirm permission and attribution before publishing adapted instructional text.

The Word document has now been converted to a public [Markdown source record](../source/ali-goff-da-730-course-redesign.md) at Shuhan He's direction. The separate [Module 04 record](../../courses/data-visualization/modules/04-distributions-vs-summaries/README.md) adapts that source into the Commons module contract. The [Module 04 build specification](2026-08-15-ali-goff-module-04-build-spec.md) defines the runnable package, validation rules, assessment, review gates, and release criteria.

## Implementation status

| Artifact | Status |
|---|---|
| Ali Goff course document in Markdown | Complete |
| Data visualization course landing page | Complete |
| Module 04 content record | Complete |
| Module 04 implementation and release specification | Complete |
| Synthetic data generator and checks | Complete |
| Learner R lab and critique chart code | Complete |
| Generated dataset and release manifest | Complete |
| Assessment and instructor key | Complete |
| Faculty, clinical, accessibility, and independent-instructor review | Pending |

## Purpose

The Commons will make open and synthetic clinical data teachable. A learner should be able to move from a healthcare decision to data, analysis, a defensible visual, and a recommendation. An instructor should be able to adopt the same material with clear prerequisites, answer keys, data provenance, and reuse terms.

The data visualization course is the first application because it exercises the entire model:

- healthcare data with realistic defects and operational consequences;
- reproducible analysis in code;
- judgment about what a chart reveals or hides;
- communication to clinical, executive, and patient audiences;
- reusable assignments, checks, and contribution records.

The Commons is not a learning management system, a store for restricted data, or a replacement for approved capstone data environments.

## Course outcome

By the end of the bridge course, a learner can choose, build, critique, and explain a healthcare visualization based on the decision, the data structure, the audience, and the consequences of what the display leaves out.

The course should assess judgment, not software menu recall. R and ggplot2 are the first implementation because they match Ali Goff's redesign and the Fall 2026 bridge. The concept core remains tool independent so a later Python lab can use the same module without changing its competency or assessment.

## Course structure

The source design separates four things:

1. The module is the durable unit. It owns one assessable visualization competency.
2. The domain instantiation is a replaceable healthcare case, such as emergency care, oncology, population health, or clinical operations.
3. The wrapper holds the seven-week schedule, discussion prompts, and exam assembly. It may change without changing the modules.
4. The R scaffold supports learners who are still developing coding fluency. It should not be embedded in the concept sequence.

Eleven modules fill thirteen teaching slots:

| Slots | Module | Competency focus |
|---|---|---|
| 1 | Encoding and the grammar of graphics | Map variables to visual channels and explain why a chart has its form. |
| 2 | Perception and accuracy | Compare encodings using evidence about how people read position, length, angle, area, and color. |
| 3-4 | Chart selection in practice | Move from a question and data types to a justified chart, table, or decision not to chart. |
| 5 | Distributions versus summaries | Decide when a summary hides skew, multiple groups, unequal group sizes, or a consequential tail. |
| 6 | Rates, denominators, and adjustment | Distinguish counts from rates and explain when crude comparisons mislead. |
| 7-8 | Uncertainty and variation | Show sampling noise, intervals, small denominators, and signal over time honestly. |
| 9 | Color | Use accessible sequential, diverging, and qualitative color for information rather than decoration. |
| 10 | Time | Display trend, seasonality, indexing, and process variation without distorting change. |
| 11 | Comparison and small multiples | Compare groups with ordering, shared scales, and faceting. |
| 12 | Maps and geography | Use maps only when place matters and handle rates, bins, aggregation, and stigma responsibly. |
| 13 | Audience, annotation, and composition | Turn an analysis into a chart or multi-view display that supports a specific audience and decision. |

Misleading charts, accessibility, equity, ethics, and small-cell protection belong inside the relevant modules rather than in one isolated lecture.

## Module contract

Every module must ship with the same nine parts:

1. One assessable competency statement.
2. Prerequisites within the course and from the foundation courses.
3. A 15 to 25 minute concept core that is independent of tool and clinical domain.
4. One primary healthcare case and at least two alternate domain cases.
5. A dataset specification that states what the data must contain for the lesson to work.
6. One lab with run, modify, and author scaffold levels.
7. Two or three flawed displays for learners to diagnose and repair.
8. Assessment items tagged to the competency and difficulty.
9. Instructor notes covering misconceptions, time cuts, handoffs, and answer-key details.

Each public module release should contain four recognizable assets:

- data release;
- assignment pack;
- benchmark and validation results;
- contribution record.

## First vertical slice: Module 04

### Learning decision

The learner must decide whether a summary statistic represents the underlying distribution well enough for the decision, choose a display that exposes any consequential structure, and state what action changes because of the fuller view.

### Clinical case

An emergency department reports that median length of stay fell after a fast-track pathway launched. The same data show that the 90th percentile and the share of stays over eight hours rose sharply as inpatient boarding increased. The learner must produce one chart for leadership and explain why expanding fast track would not address the deteriorating group.

### Data contract

The generator must create synthetic encounter data that meet all six teaching conditions:

| Condition | Required threshold |
|---|---|
| Right-skewed primary outcome | Mean divided by median is at least 1.20. |
| Unequal group sizes | Largest group is at least 2.5 times the smallest comparison group. |
| Hidden second mode | The minority group has a visible second mode that becomes only a weak shoulder when pooled. |
| Opposing trends | Mean changes by less than 6 percent while the 90th percentile rises by more than 40 percent. |
| Small subgroup | At least one clinically meaningful group has fewer than 100 observations. |
| Misleading average of averages | The unweighted group means differ from the pooled mean by at least 30 minutes. |

The generator must support real, null, and clinically trivial effect variants so students cannot assume every assignment contains a hidden crisis.

### Minimum artifacts

- a deterministic R data generator with a documented seed;
- the generated CSV and a data dictionary;
- automated checks for the six data conditions;
- one learner lab with run, modify, and author entry points;
- flawed-chart generation code and repair prompts;
- an assessment and rubric tied to diagnosis, justification, and decision consequence;
- instructor notes and an answer key;
- a release manifest with version, license, row count, checksum, known issues, and source dates.

### Acceptance check

A new instructor can open the module, run the generator and checks, teach the concept without reading the DA-730 source document, and grade a learner's chart and recommendation from the supplied rubric. No real patient record, restricted dataset, or unpublished partner data is required.

## Emergency medicine and Health Data Analytics alignment

| Need | Course contribution | Commons contribution |
|---|---|---|
| R, version control, reproducible work, and software documentation | Learners run and modify versioned analysis code, then justify the result. | Every release carries build code, checks, provenance, and known issues. |
| Work with clinical and operational data | Cases use encounters, length of stay, quality measures, geography, and other healthcare structures. | Synthetic patient data can connect to open CMS, CDC, Census, ClinicalTrials.gov, and OpenAlex context. |
| Statistical judgment and interpretation | Learners examine distributions, rates, uncertainty, small denominators, and time variation. | Dataset specifications create cases with real, null, and clinically trivial findings. |
| Fairness, safety, and responsible communication | Critique tasks ask what is concealed, who may be harmed, and what should replace the display. | The teaching layer documents flaws, small-cell rules, accessibility checks, and limits. |
| Research products and grantsmanship | Learners turn analysis into a decision-focused visual and written recommendation. | Fellows can contribute reviewed datasets, teaching cases, benchmarks, and documentation as reusable scholarly products. |
| A longitudinal project and national development | The course provides a small, complete analytic workflow before a capstone or fellowship project. | Other programs can adopt a versioned module without an IRB, data use agreement, or local patient data. |

Within the revised Health Data Analytics curriculum, the course supplies the visualization and communication thread that begins in Fundamentals I and is reused in each Data for X course and the capstone. Emergency medicine educators and learners can use the same modules as a technical baseline and a contribution path into national teaching infrastructure.

## Data and release rules

- Use synthetic or openly licensed data only. MGB patient data, MIMIC, and partner datasets stay outside the public release.
- Write the pedagogical data specification before choosing or generating the dataset.
- Keep source terms with every imported table. Do not treat public access as a blanket license.
- Record the release version, retrieval dates, licenses, row counts, checksums, build code, and known issues.
- Do not ship an incomplete build or a dataset that fails its teaching checks.
- Original documentation and synthetic data use CC BY 4.0, teaching and pipeline code use MIT, and imported public data keep source-specific terms.
- Require human review before a contributed module, answer key, or benchmark enters a release.

## Planned repository shape

Create this structure only as the corresponding artifacts are built:

```text
courses/data-visualization/
  course.md
  modules/04-distributions-vs-summaries/
    README.md
    data-spec.md
    generate_ed_los.R
    lab.R
    critique_charts.R
    assessment.md
    instructor-notes.md
```

## Release sequence

1. Foundation: approve this course and release contract. The draft is published for review.
2. Vertical slice: the Module 04 runnable candidate is complete; record the four human reviews before alpha.
3. Course shell: add the remaining ten module briefs and assemble the Fall 2026 wrapper.
4. Teaching release: run the course, log defects, and revise the module contract.
5. Commons starter: connect tested modules to a small, versioned synthetic and open data release.

## Deliberate limits for the first build

The first release will not build the full two-hospital synthetic health system, all eleven finished modules, Python mirrors, a learning management system, credentials, or a contribution portal. Add those only after Module 04 proves the release contract.

## Faculty decisions before Module 04 alpha

1. Confirm R and ggplot2 as the Fall 2026 graded environment. The candidate uses them while keeping the concept core tool independent.
2. Confirm whether `boarded`, currently included for the transition cohort, should remain visible in the final learner release.
3. Name the faculty, clinical, accessibility, and independent-instructor reviewers.
