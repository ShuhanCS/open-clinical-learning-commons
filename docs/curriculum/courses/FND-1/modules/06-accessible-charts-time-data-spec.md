# FND-1 Module 06: Accessible charts and time-indexed data

## 1. Module identity and place in the course

- Course: FND-1, Healthcare Data Foundations.
- Module: 06 of 07.
- Instructional week: 6.
- Learner work: 16.0 hours.
- Module version: 0.1.0.
- Commons release: 0.34.0.
- Status target: runnable release candidate.
- Decision owner: data-quality review panel.
- Checkpoint role: completes the cumulative Week 6 evidence package.
- Core inputs: exact Module 04 quality evidence and Module 05 descriptive release.
- Downstream receiver: Week 6 checkpoint, then Module 07 handoff and AI audit.

Module 06 teaches learners to create three accessible inspection views without changing an accepted number or implying cause. It is a focused foundations application, not a substitute for the separate DA-730 visualization course.

## 2. Technical decision and named audience

### Decision

Can every reviewer inspect the quality, descriptive, and time-indexed evidence through figures, exact tables, and equivalent text without hidden values, inaccessible cues, or unsupported causal or trend language?

### Decision owner

A data-quality review panel owns the decision. The panel includes a clinical analytics reviewer, accessibility reviewer, and technical reproducibility reviewer.

### Receiving audience

- a clinical analytics lead reviewing exact evidence;
- a colleague using screen magnification or a screen reader;
- a reviewer printing in grayscale;
- an instructor checking chart mapping and claim boundaries;
- the Week 6 checkpoint panel; and
- the Module 07 toolkit recipient.

### Allowed dispositions

- `accept`;
- `accept with conditions`;
- `revise`; or
- `refer` for accessibility, source, privacy, rights, integrity, or governance review.

Only `accept` and `accept with conditions` permit the Week 6 checkpoint to pass.

## 3. Foundation skill and handoff

### Foundation skill

The learner maps exact tables to accessible figures, preserves an equivalent nonvisual path, and states what a time pattern can and cannot mean. The goal is inspection and communication, not decoration.

### Upstream handoff

Module 04 provides:

- `missingness-profile.csv`, 29 rows, SHA-256 `46e9c4dd268db223fac3cd0f01e65e050a3d44f6a28e0babcfb7bd5b552b5ba5`;
- accepted versus defective missing counts;
- N01 through N08 quality conditions; and
- `proceed with conditions` after deterministic restoration.

Module 05 provides:

- `rates.csv`, six rows, SHA-256 `2398b283e449d6f876a3a3ea123e7905c637ba222f56c6aa03882cfc158942f3`;
- `denominator-registry.csv`, 27 rows, SHA-256 `e13bd0e1cf0716b912476fd81c7e4dd8bc827b2df468421aa2efc33f1f234be6`;
- the 374-row resolved analytic table, SHA-256 `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a`;
- six exact descriptive CSV outputs; and
- `accept with conditions` for visual handoff.

### Downstream handoff

The Week 6 checkpoint receives:

- three 300-DPI PNG figures;
- three vector SVG figures;
- three exact evidence tables;
- three structured text alternatives;
- a figure registry linking source, table, figure, alt text, caption, and claim limit;
- accessibility and resize checks;
- the unchanged resolved table, quality profile, and descriptive outputs;
- the Module 04 quality decision and Module 05 interpretation memo; and
- a panel disposition.

Module 07 receives the accepted package without recalculating figure values.

## 4. Assessable outcomes

By the end of Module 06, the learner can:

1. verify all upstream fingerprints;
2. state the question before selecting a chart;
3. map each displayed mark to an exact table field;
4. use a zero baseline for bars;
5. use direct labels and units;
6. use colorblind-safe color without making color the only cue;
7. add hatching, line style, marker shape, or direct text as redundant encoding;
8. retain readable text at final display size;
9. export a lossless 300-DPI PNG and vector SVG;
10. provide the exact data behind every figure;
11. write an equivalent structured text alternative;
12. preserve Wilson interval meaning in the rate view;
13. distinguish selected cohort index counts from operational service volume;
14. avoid a causal, intervention, process-control, or forecast claim;
15. test grayscale, reduced size, file identity, and reading order;
16. document material AI assistance and human verification; and
17. make an allowed Week 6 readiness disposition.

## 5. Concept ownership and out-of-scope boundaries

### Module 06 owns

- chart-question fit for three defined views;
- exact mark-to-field mapping;
- accessible categorical color;
- redundant visual cues;
- zero-based bar axes;
- line and marker distinctions;
- direct labels;
- readable hierarchy and final-size typography;
- 300-DPI PNG and SVG export;
- exact CSV alternatives;
- structured text alternatives;
- selected-quarter indexing;
- uncertainty labels already calculated in Module 05;
- false-cause avoidance; and
- the Week 6 visual inspection gateway.

### Module 06 does not own

- the complete grammar, perception, chart-selection, mapping, dashboard, or storytelling curriculum in DA-730;
- new statistical estimates;
- p-values or significance marks;
- causal inference;
- regression, prediction, or machine learning;
- process-control limits;
- forecasting or trend tests;
- risk adjustment;
- operational demand estimation from the selected cohort;
- clinical recommendations; or
- real-population inference from synthetic data.

### No invented uncertainty

The rate view may display the six Wilson intervals released by Module 05. The quality and quarterly-count views have no approved uncertainty estimate, so no error bar or confidence band is added. Absence of an error bar is documented rather than filled with an invented one.

## 6. Lesson sequence and learner time

| Learning activity | Hours | Evidence |
|---|---:|---|
| Source and figure-contract verification | 1.00 | fingerprint record |
| Accessible chart mapping and critique | 1.75 | mapping notes |
| Quality and missingness view | 2.00 | exact table, PNG, SVG, alt text |
| Descriptive rate and interval view | 2.25 | exact table, PNG, SVG, alt text |
| Time-indexed cohort-count view | 2.25 | exact table, PNG, SVG, alt text |
| Color, redundant cues, and grayscale checks | 1.50 | accessibility checks |
| Typography, resize, labels, and export | 1.25 | export record |
| Guided notebook or script reproduction | 1.50 | clean render |
| Claim limits and Week 6 review | 1.25 | review disposition |
| Reproduction and AI audit | 1.25 | final records |
| Total | 16.00 | complete release |

### Feedback checkpoints

1. Faculty approves each question-to-chart mapping before rendering.
2. A peer reads the exact table and alt text without seeing the figure.
3. A peer views grayscale and reduced-size figures without the table.
4. The panel checks one visible value against its upstream result ID.
5. The learner revises any claim that treats selected indexes as service volume or a trend.

## 7. Readings and authoritative sources

### Required Commons records

1. Module 04 missingness profile and quality decision.
2. Module 05 rate table, denominator registry, interpretation memo, and release record.
3. DA-730 Modules 01, 02, 03, 07, and 08 as optional depth rather than duplicated graded work.
4. This specification and figure registry.

### Public references

- W3C images tutorial: https://www.w3.org/WAI/tutorials/images/
- W3C complex images: https://www.w3.org/WAI/tutorials/images/complex/
- W3C table concepts: https://www.w3.org/WAI/tutorials/tables/
- WCAG 2.2 non-text contrast: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- Matplotlib accessibility discussion: https://matplotlib.org/stable/users/explain/colors/colormaps.html
- Synthea downloads: https://synthea.mitre.org/downloads

### Reading questions

- What information disappears if color is removed?
- Which values can be recovered exactly from the figure and which require the table?
- What must an alt text user learn about structure, finding, and limit?
- Why does a line across quarters invite a trend claim even when none is tested?
- When is no error bar more honest than an unsupported error bar?

## 8. Dataset inventory, provenance, rights, and teaching purpose

### Inputs

| Input | Rows | Teaching role |
|---|---:|---|
| Module 04 missingness profile | 29 | accepted, defective, and structural missingness |
| Module 05 rates | 6 | exact proportions and Wilson intervals |
| Module 05 denominator registry | 27 | meaning and claim limits |
| Module 05 resolved analytic table | 374 | selected index quarter counts |

### Derived exact tables

| Table | Rows | Grain |
|---|---:|---|
| quality-missingness.csv | 8 | one field with accepted or seeded missingness |
| descriptive-rates.csv | 6 | one Module 05 rate |
| quarterly-index-counts.csv | 20 | one calendar quarter from 2015 Q1 through 2019 Q4 |

### Rights and safety

All row-level records are synthetic. Learners may not substitute workplace or patient data. Exact small cells remain internal teaching evidence and carry N07/N08 cautions.

### Teaching purpose

The figures test accessible evidence inspection. They do not measure a real hospital, service, patient population, clinical outcome, or time trend.

## 9. Exact figure contracts

### Figure 1: Quality and missingness

- ID: F01.
- Question: Which fields have accepted structural missingness or seeded missingness that required restoration?
- Exact table: `tables/quality-missingness.csv`.
- Figure: `figures/quality-missingness.png` and `.svg`.
- Chart: grouped horizontal bars for accepted versus defective missing percent.
- Fields: eight fields with accepted missingness or a positive seeded delta.
- Baseline: zero.
- Encoding: accepted uses blue with diagonal hatch; defective uses orange with cross hatch; direct percent labels remain visible.
- Caption boundary: defective counts are deterministic teaching defects, and accepted optional missingness is not error.
- No uncertainty mark is supported.

### Figure 2: Descriptive rates

- ID: F02.
- Question: What selected 30-day and 90-day events are recorded for the synthetic cohort?
- Exact table: `tables/descriptive-rates.csv`.
- Figure: `figures/descriptive-rates.png` and `.svg`.
- Chart: horizontal point-and-interval display.
- Marks: point is Module 05 percent; line is Module 05 Wilson 95-percent interval.
- Baseline and scale: zero through a fixed upper limit sufficient for RT01.
- Encoding: one blue point-and-line style with direct count/denominator labels, so category distinction does not depend on color.
- Caption boundary: RT01 contains RT02 through RT04; rates are not mutually exclusive across 30-day and 90-day measures; intervals are descriptive for synthetic data.

### Figure 3: Time-indexed selected cohort counts

- ID: F03.
- Question: How are the 374 selected index encounters distributed across calendar quarters in the pinned synthetic cohort?
- Exact table: `tables/quarterly-index-counts.csv`.
- Figure: `figures/quarterly-index-counts.png` and `.svg`.
- Chart: three lines for total, emergency, and inpatient selected indexes.
- Encoding: black solid circles for total, blue dashed squares for emergency, orange dotted triangles for inpatient.
- Baseline: zero.
- Direct labels: final series labels and total cohort count.
- Caption boundary: one index per person and cohort selection mean these are not hospital volumes, rates, forecasts, or evidence of a change in demand.
- No uncertainty band, process limit, or fitted trend is supported.

## 10. Worked example and instructor walkthrough

### Missingness example

Death date is blank for 343 of 374 accepted rows. The defective layer adds five duplicate rows, so its blank count is 348 of 379. A longer bar in the defect layer does not prove bad death data; the accepted blank is structural and D01 changes the denominator.

### Rate example

RT06 is 8 of 374, or 2.139037 percent, with a Wilson interval of 1.087782 to 4.163484 percent. The point, interval, and direct count label all come from the exact Module 05 row. No significance symbol is added.

### Time example

The selected cohort includes 38 index encounters in 2015 Q1 and 3 in 2019 Q3. Joining those points with a line helps read sequence but does not prove a decline in real service demand. The title and alt text name selected cohort indexes.

### Equivalent access example

A reviewer who cannot see F03 can recover:

- three series and their line/marker cues;
- the 2015 Q1 maximum total of 38;
- the 2019 Q3 minimum total of 3;
- all 20 exact quarterly values from CSV;
- the one-index-per-person construction; and
- the no-volume/no-trend claim limit.

## 11. Guided practice

1. Map one bar, point, interval, and line mark to an exact field.
2. Recreate the F01 eight-row filter from the 29-row profile.
3. Explain why hatching is useful when color is unavailable.
4. Check F02 percent and interval against RT01 and RT06.
5. Explain why all F02 categories cannot be summed.
6. Reconcile the 20 F03 totals to 374.
7. Test all three PNGs in grayscale.
8. Test figures at 50-percent width and 200-percent zoom.
9. Read alt text aloud without viewing the figure.
10. Rewrite one false-cause or operational-volume claim.

## 12. Independent exercise

The learner independently:

1. verifies all four upstream files;
2. renders into a new target;
3. checks three exact tables;
4. checks three PNG and three SVG files;
5. completes three structured alt-text records;
6. completes the figure registry;
7. records contrast, redundant-cue, grayscale, resize, and reading-order checks;
8. reruns the notebook or renderer;
9. documents material AI use; and
10. records an allowed panel disposition.

The learner may redesign visual styling only if mapping, exact values, accessibility gates, filenames, source links, and claim limits remain compatible.

## 13. Visualization and communication requirements

### Common figure requirements

- 7 by 4 inch final canvas;
- PNG at 300 DPI;
- SVG vector companion;
- sans-serif type at 8 points or larger at final size;
- sentence-case title and labels;
- explicit units;
- no 3D, gradients, shadows, or decorative marks;
- zero-based bars;
- colorblind-safe blue `#0072B2`, orange `#E69F00`, and black;
- redundant hatch, line, marker, or direct label cues;
- exact CSV linked in registry and caption;
- structured text alternative; and
- visible synthetic-data or selected-cohort claim boundary.

### Alt-text structure

Each record names figure purpose, chart structure, axes and units, series and redundant cues, exact high and low values, main pattern, uncertainty meaning when present, source and period, and material interpretation limit.

### Figure registry

Required fields are figure ID, question, source paths and fingerprints, exact table, PNG, SVG, alt text, width, height, DPI, color palette, redundant cue, uncertainty definition, caption, and claim limit.

## 14. Exact submission package

```text
module-06-submission/
  VERSION
  README.md
  source-record.yml
  figure-spec.md
  render_figures.py
  data/
    missingness-profile.csv
    rates.csv
    denominator-registry.csv
    resolved-analytic-table.csv
  tables/
    quality-missingness.csv
    descriptive-rates.csv
    quarterly-index-counts.csv
  figures/
    quality-missingness.png
    quality-missingness.svg
    descriptive-rates.png
    descriptive-rates.svg
    quarterly-index-counts.png
    quarterly-index-counts.svg
  alt-text/
    quality-missingness.md
    descriptive-rates.md
    quarterly-index-counts.md
  figure-registry.csv
  accessibility-check.md
  transformation-record.md
  reproducibility-check.md
  ai-use.md
```

Required tag: `fnd1-accessible-charts-v0.1.0`.

## 15. Rubric and pass conditions

| Criterion | Points |
|---|---:|
| Source and exact-table verification | 10 |
| Quality and missingness view | 15 |
| Rate and interval view | 15 |
| Time-indexed cohort-count view | 15 |
| Accessibility and equivalent alternatives | 20 |
| Claim limits and Week 6 decision | 10 |
| Reproduction, provenance, and AI accountability | 15 |
| Total | 100 |

Passing requires at least 80 points and every gate below.

### Noncompensable gates

- all upstream fingerprints exact;
- three exact tables reconcile;
- three PNG files at 300 DPI;
- three valid SVG files;
- exact table linked for each figure;
- structured text alternative for each figure;
- no meaning depends on color;
- readable final-size text;
- zero baseline for bars;
- F02 interval definition preserved;
- no invented uncertainty;
- F03 counts sum to 374;
- no operational-volume, trend, causal, process-control, forecast, or real-population claim;
- N01 through N08 retained;
- clean reproduction;
- material AI use disclosed and verified; and
- allowed panel disposition.

## 16. Common failures and instructor interventions

| Failure | Intervention | Evidence |
|---|---|---|
| Calls all missingness bad | Return to field and state rules. | N01/N02/N03. |
| Uses color alone | Remove color mentally or print grayscale. | Hatch, line, marker, label. |
| Truncates a bar axis | Restore zero. | F01 axis. |
| Omits small rate | Restore exact internal row. | RT03/RT06 and N08. |
| Sums overlapping rates | Review RT01 parent relation and windows. | Denominator registry. |
| Adds significance stars | Remove unsupported inference. | Descriptive caption. |
| Adds an F03 trend line | Remove unapproved model. | Exact quarterly counts. |
| Calls F03 hospital volume | Restate selected one-per-person indexes. | Source and alt text. |
| Writes decorative alt text | Add structure, values, pattern, and limit. | Required sections. |
| Exports only PNG | Add SVG. | Registry paths. |
| Makes text tiny | Review at final size. | Resize check. |
| Retypes values | Render from exact CSV. | Reproduction hash. |

## 17. Accessibility, equity, privacy, and claim checks

### Accessibility

Every figure has redundant cues, exact CSV, structured text, direct labels, readable hierarchy, and a declared reading order. PNG and SVG are both required because no single format solves every access need.

### Equity

Small source categories and outcomes remain exact in the internal evidence. The module does not label a rare group erroneous or make an equity conclusion from unadjusted synthetic data.

### Privacy

All patient-level data is synthetic. Figures aggregate the accepted cohort and expose no new identity-like field. Learners may not substitute workplace data.

### Claims

- F01 compares accepted and seeded teaching layers, not real data quality.
- F02 describes recorded synthetic events, not clinical performance.
- F03 describes selected cohort indexes, not operational demand.
- A line connecting quarters is not a trend test.
- Wilson intervals are not real-population estimates here.
- No figure supports a causal, intervention, quality, safety, access, equity, or forecasting conclusion.

## 18. AI policy, disclosure, and verification

### Permitted uses

- propose a chart mapping;
- suggest accessible color and redundant cues;
- diagnose rendering code;
- draft alt text;
- check a caption for overclaiming; and
- edit documentation.

### Prohibited uses

- invent a value or uncertainty mark;
- change an upstream table to improve a chart;
- hide a small or unavailable value;
- fabricate contrast or grayscale testing;
- infer a cause or trend;
- replace exact alt text with decorative prose;
- share protected data or credentials; or
- fabricate rendered outputs.

### Required verification

At least one AI-suggested mapping, value label, interval, alt-text fact, color, or claim is checked against exact tables, source rows, contrast calculation, grayscale review, or authoritative accessibility guidance.

## 19. Answer key and instructor materials

### F01 facts

The eight displayed fields are death date, gender, index encounter ID, index reason code, index reason description, next encounter ID, next start, and next elapsed days. The view must preserve accepted versus defective denominators of 374 and 379.

### F02 facts

- RT01: 111 of 374, 29.679144 percent, interval 25.274719 to 34.496768.
- RT02: 92 of 374, 24.598930 percent, interval 20.507004 to 29.207355.
- RT03: 4 of 374, 1.069519 percent, interval 0.416679 to 2.717296.
- RT04: 15 of 374, 4.010695 percent, interval 2.445359 to 6.511164.
- RT05: 36 of 374, 9.625668 percent, interval 7.034020 to 13.038277.
- RT06: 8 of 374, 2.139037 percent, interval 1.087782 to 4.163484.

### F03 facts

Quarterly totals from 2015 Q1 through 2019 Q4 are 38, 30, 28, 22, 22, 19, 10, 29, 24, 21, 24, 15, 15, 14, 13, 12, 13, 11, 3, and 11. They sum to 374. Emergency and inpatient sums are 314 and 60.

### Reference disposition

`accept with conditions` for Week 6 checkpoint assembly. The conditions are exact-table linkage, equivalent text, N01 through N08, unadjusted descriptive language, selected-cohort time wording, and synthetic-data scope.

## 20. Runnable acceptance checks

The validator must check:

1. four upstream fingerprints;
2. upstream row and field counts;
3. Module 04 and 05 status;
4. protected nonempty target;
5. module version 0.1.0;
6. F01 eight rows and exact values;
7. F02 six rows and exact values;
8. F02 intervals and counts;
9. F03 twenty rows and exact values;
10. F03 quarter continuity;
11. F03 total 374;
12. emergency total 314;
13. inpatient total 60;
14. three unique figure IDs;
15. three PNG paths;
16. three SVG paths;
17. three exact-table paths;
18. three alt-text paths;
19. PNG signature and dimensions;
20. PNG 300-DPI metadata;
21. SVG root and viewbox;
22. fixed 7 by 4 inch canvas;
23. source paths and hashes in registry;
24. Okabe-Ito palette values;
25. redundant cues recorded;
26. uncertainty definition for F02 only;
27. no unsupported uncertainty for F01/F03;
28. zero-baseline records;
29. exact title and unit records;
30. alt text purpose;
31. alt text structure;
32. alt text exact high and low;
33. alt text source and period;
34. alt text material limit;
35. accessibility checks recorded;
36. grayscale result;
37. reduced-size result;
38. zoom result;
39. reading-order result;
40. exact-table equivalence result;
41. N01 through N08 retained;
42. no placeholder in complete submission;
43. no local absolute path;
44. no Unicode dash in contracts;
45. no JPEG output;
46. no 3D or chart-junk configuration;
47. AI verification recorded;
48. allowed disposition;
49. renderer self-check;
50. validator self-check;
51. clean rendering;
52. byte-for-byte tables;
53. deterministic figure fingerprints;
54. incomplete submission rejection; and
55. Week 6 handoff completeness.

Automation proves data, structure, exports, registered accessibility facts, and fingerprints. Human review decides whether figures and alternatives are understandable and equivalent, typography remains readable, grayscale and resize checks are credible, and the claims fit the evidence.

## 21. Release status, reviewers, version, and known issues

### Release identity

- Module ID: `oclc-fnd1-06`.
- Module version: 0.1.0.
- Commons release: 0.34.0.
- Status target: runnable release candidate.
- Repository: https://github.com/ShuhanCS/open-clinical-learning-commons

### Semantic-version decision

Module 0.1.0 establishes the first exact-table-to-figure, accessible-alternative, and selected-time-index handoff contract. Commons 0.34.0 adds the compatible module without changing Modules 01 through 05.

### Required human reviewers

| Role | Reviewer | Status |
|---|---|---|
| FND-1 faculty owner | unassigned | pending |
| Clinical analytics reviewer | unassigned | pending |
| Accessibility | unassigned | pending |
| Data visualization | unassigned | pending |
| Clinical informatics and time meaning | unassigned | pending |
| Python and rendering | unassigned | pending |
| Privacy and data governance | unassigned | pending |
| Responsible AI | unassigned | pending |
| Independent reproduction and teachability | unassigned | pending |

### Release measurements and known issues

1. Three exact tables, six figure exports, three text alternatives, and the 25-field figure registry are fingerprint locked.
2. Every PNG is 2100 by 1200 pixels at 300 DPI; every SVG is 504 by 288 points with the same viewbox.
3. Grayscale, 50-percent-width, 200-percent-zoom, reading-order, and exact-table equivalence checks pass.
4. Blue, orange, and black have white-background contrast ratios of 5.185:1, 2.252:1, and 21.000:1. Orange is never the only cue or small-text color.
5. The validator runs 616 release checks and 615 complete-submission checks.
6. Named human review is pending.
7. macOS and Linux reproduction remain pending.
8. The source is synthetic and older.

### Context-safe handoff

The minimal renderer, exact outputs, learner records, assessment, instructor key, and validator are complete. Integrate the repository checker and Commons 0.34.0, reproduce in the pinned clean environment, commit, and push. Then assemble the cumulative Week 6 checkpoint before Module 07.
