# DA-730 Module 07: Color and accessible visual communication

- Course: DA-730, Clinical data visualization and decision storytelling
- Instructional position: week 4, first applied-portfolio module
- Learner time: 7.5 hours
- Module version: 0.1.0
- Target Commons release: 0.18.0
- Primary environment: R and ggplot2
- Data build and validation: Python 3 standard library
- Clinical source: CMS Unplanned Hospital Visits, `READM_30_HF`
- Accessibility authorities: W3C WCAG 2.2, W3C WAI complex images guidance, and CDC COVE Section 508 accessibility guidance
- Public module package: `courses/data-visualization/modules/07-color-accessible-communication/`

## 1. Module identity and place in the course

Module 07 begins the applied visualization portfolio. Modules 01 through 06 established encoding, perception, chart selection, distributions, rates, denominators, adjustment, uncertainty, and missingness. Module 07 asks whether the same finding remains available when a reader cannot distinguish the chosen colors, uses grayscale, enlarges content, reads a printed page, or needs a text and table alternative.

The module reuses the complete 65-row Massachusetts heart failure readmission case from Module 06. Reuse is deliberate. If the clinical data and statistical claim stay fixed, learners can see exactly what an accessibility change repairs and whether the repair accidentally changes the evidence.

Formal concept prerequisites are Modules 01 through 03. The worked case also assumes the Module 06 interpretation boundary. An instructor teaching Module 07 independently must supply the short Module 06 case briefing before the lab.

Accessibility requirements become cumulative after this module. Every figure in Modules 08 through 13 must carry redundant cues, readable contrast, a text alternative, exact values, missingness, and a reproducible source.

## 2. Healthcare decision and audience

### Decision

A clinical quality analyst must decide whether the Massachusetts heart failure readmission display is ready for a committee packet and live meeting.

The release decision has three options:

- ready for committee use;
- revise before use;
- do not use because the source, interpretation, or access path is incomplete.

### Decision owner

The primary decision owner is a clinical staff member or quality committee member reading under time pressure. The audience also includes a reader who:

- cannot distinguish the selected hues;
- uses a monochrome or low-quality display;
- receives a grayscale printout;
- enlarges the chart or reads it on a smaller screen;
- uses a screen reader or text-only workflow;
- needs exact values rather than visual estimates.

### Decision questions

The learner must answer:

1. Can a reader identify comparison status without hue?
2. Do the required text and graphical objects have enough contrast against adjacent colors?
3. Does the chart remain understandable in grayscale and print?
4. Can a reader reach the same finding through short text, a structured long description, and an exact-value table?
5. Are all unavailable and too-few rows still visible in the alternate path?
6. Did any accessibility repair change the source value, category, interval, benchmark, or claim?

### Required decision language

The final recommendation uses one of these forms:

- "Ready for the committee because status is available through [cues], the final contrast checks pass, and the table and text preserve [finding and limits]."
- "Revise before use because [barrier] prevents [reader or task] from recovering [information]."
- "Do not use this display because the missing source or interpretation cannot be repaired by visual changes."

The recommendation does not call a chart accessible because it uses a named palette, passes one simulator, or has an alt attribute.

## 3. Foundation skill revisited or extended

### Foundations I skills revisited

- keep a stable row identifier through a derived release;
- preserve source blanks instead of converting them to zero;
- verify a source checksum before transformation;
- document every added field and calculation;
- provide a machine-readable exact-value file;
- use a predictable reading order and clear column names.

### Foundations II skills revisited

- distinguish a source estimate from a visual encoding;
- retain the national benchmark and source comparison category;
- preserve the lower and higher source estimates without inventing a confidence level;
- keep a point rank separate from evidence of difference;
- keep descriptive overlap separate from a pairwise test;
- match the final claim to the published aggregate data.

### Visualization foundations revisited

- choose marks and channels based on variable type and reader task;
- prefer position and direct labels for important comparisons;
- use perception evidence to reduce legend lookup and hue discrimination;
- select a table or text alternative when a chart cannot carry exact detail;
- test what a summary, rank, or color choice hides.

### New application

The learner moves from general chart judgment to an accessibility release decision. Color, shape, line, text, table structure, contrast, reading order, and alternative descriptions must work as one system.

## 4. Assessable learning outcomes

By the end of the module, a learner can:

1. classify a palette as sequential, diverging, qualitative, or inappropriate for the data structure;
2. explain why clinical red, amber, and green conventions are not self-interpreting or accessible by default;
3. calculate relative luminance and contrast ratio for named foreground and background colors;
4. apply the correct 4.5:1, 3:1, or context-specific check without treating it as the only accessibility test;
5. encode source status through at least one non-color cue;
6. test a static visualization in color, grayscale, print, and a smaller viewing context;
7. write short alternative text that identifies a complex chart and its main finding;
8. write a structured long description that preserves chart structure, values, uncertainty, missingness, and the decision boundary;
9. provide a complete exact-value table and downloadable CSV;
10. repair a color-only status chart and a low-contrast heatmap;
11. preserve all source values and comparison categories during the repair;
12. record tool use, human checks, remaining risks, and the release decision.

### Mastery threshold

The learner earns at least 80 percent overall and passes every noncompensable condition in Section 15. A visually polished figure fails when color carries status alone, missing rows disappear, exact values change, the alternative path is incomplete, or the final claim exceeds the source.

## 5. Concept ownership and boundaries

### Concepts owned here

- sequential, diverging, and qualitative color selection;
- relative luminance and contrast ratio;
- WCAG 2.2 use-of-color, text-contrast, and non-text-contrast application to a teaching chart;
- redundant visual encoding;
- direct labels and reduced legend dependence;
- grayscale and print checks;
- short alt text for a complex chart;
- structured long description;
- accessible exact-value table and CSV alternative;
- explicit record of accessibility tests and remaining risk.

### Concepts carried in

- marks, channels, and variable types from Module 01;
- graphical perception and decoding accuracy from Module 02;
- chart, table, paired-view, and no-display selection from Module 03;
- distributions and hidden subgroups from Module 04;
- rates, denominators, and adjustment from Module 05;
- source intervals, benchmark categories, unavailable values, and claim boundaries from Module 06.

### Concepts introduced but completed later

- keyboard operation, focus order, and interactive-state access in Module 12 dashboard work;
- reflow and responsive layout in Module 12;
- audio, live-region, and dynamic update patterns in Module 12 when interactive tools are used;
- audience-specific narrative sequencing in Module 13;
- organizational accessibility governance in the final capstone.

### Explicit exclusions

This module does not:

- certify a website, product, document, or organization as WCAG or Section 508 compliant;
- replace review by disabled users or accessibility professionals;
- simulate every color-vision condition, visual disability, screen, printer, browser, or assistive technology;
- teach a complete interactive visualization engineering stack;
- treat one color-blind simulator as proof;
- assign a universal meaning to red, amber, green, blue, or gray;
- change the CMS model, interval, comparison category, or missingness rule;
- infer patient-level experience or causal quality from aggregate public data.

## 6. Lesson sequence and learner time

| Activity | Hours | Learner work | Evidence |
|---|---:|---|---|
| Entry check | 0.25 | Read the Module 06 display in color and grayscale. | Barrier note |
| Concept lesson | 1.00 | Classify palettes, calculate contrast, and map redundant cues. | Concept responses |
| Standards and source reading | 0.75 | Read W3C, CDC, and CMS records for the exact tasks. | Reading notes |
| Guided lab | 1.50 | Build color, grayscale, status, cue-key, table, and text outputs. | Lab output folder |
| Critique and repair | 1.00 | Diagnose and repair two inaccessible displays. | Critique record |
| Independent build | 1.50 | Produce the final figure, table, and editable analysis. | Submission draft |
| Accessibility audit | 0.75 | Record contrast, grayscale, print, small-view, text, and table checks. | Audit draft |
| Exit and handoff | 0.75 | Complete the decision note, AI-use record, and Module 08 handoff. | Final package |

Total: 7.5 hours.

### Scaffold levels

- Run: execute the supplied Python and R files and inspect the outputs.
- Modify: change labels, cue combinations, ordering, or layout while preserving the source fields and claim.
- Create: build an approved alternative in R, Python, Tableau, Power BI, Observable, or another tool with editable source, equivalent outputs, and the same checks.

The software is not the learning outcome. The evidence must still be reproducible and reviewable.

## 7. Authoritative readings and public clinical sources

### Required accessibility sources

1. WCAG 2.2: https://www.w3.org/TR/WCAG22/
2. Understanding Success Criterion 1.4.1, Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color
3. Understanding Success Criterion 1.4.3, Contrast Minimum: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum
4. Understanding Success Criterion 1.4.11, Non-text Contrast: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast
5. W3C WAI Complex Images tutorial: https://www.w3.org/WAI/tutorials/images/complex/
6. CDC COVE Section 508 Accessibility: https://www.cdc.gov/cove/about/section-508-accessibility.html

### Required clinical source

- CMS Unplanned Hospital Visits, Hospital: https://data.cms.gov/provider-data/dataset/632h-zaca
- CMS Unplanned Hospital Visits, National: https://data.cms.gov/provider-data/dataset/cvcs-xecj
- CMS Footnote Crosswalk: https://data.cms.gov/provider-data/dataset/y9us-9xdf
- CMS Hospital data dictionary: https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/hospital/HOSPITAL_Data_Dictionary.pdf

### Required reading questions

- What information does WCAG 1.4.1 prohibit from being carried by color alone?
- Which contrast threshold applies to normal text, large text, and required graphical objects?
- Why does a long description need structure for a complex chart?
- What does CDC COVE use as an alternate path for visualization information?
- Which parts of this static module fall outside a complete web or interactive accessibility review?
- Which CMS values and statuses may not change during the repair?

### Reading rule

The learner cites the specific criterion or guidance used for a specific check. A general citation to "WCAG" does not explain whether the issue is use of color, contrast, non-text content, structure, reflow, keyboard access, or another requirement.

## 8. Dataset inventory, provenance, rights, and teaching purpose

### Upstream Module 06 release

`ma_hf_readmission_uncertainty_2026.csv` contains all 65 Massachusetts rows from the pinned CMS heart failure readmission measure. Its SHA-256 is:

```text
33e6284a1064bb12600903526e4e65c009f875d9e6f6a3f25783d3a9a4b00727
```

The Module 07 build stops if that checksum changes.

### Module 07 teaching release

`accessibility_hf_readmission_2026.csv` contains 65 rows and 27 columns. Its SHA-256 is:

```text
b58168d9002a3e489213b0fafde1eca76f5b1a426c71ea3d61551671d76a49c2
```

The build preserves source fields and adds status labels, symbols, shapes, line types, foreground colors, contrast ratios, reading order, and row-level text alternatives.

### No new clinical source

Module 07 does not download another clinical dataset. That is a feature of the lesson, not a data gap. Reusing the fixed Module 06 release isolates accessibility work from clinical and statistical changes.

### Rights and redistribution

- CMS files are public U.S. government reporting data. Preserve attribution and do not imply federal endorsement.
- W3C and CDC documents are cited as standards and guidance. They are not copied into the teaching release.
- Commons documentation is CC BY 4.0.
- Commons code is MIT licensed.
- No patient-level record, MGB record, restricted partner file, or MIMIC row enters this module.

### Teaching purpose

The data are used to test equivalent access to a public aggregate finding. They are not used to rank clinicians, infer individual outcomes, reconstruct CMS risk adjustment, or make a real hospital intervention decision.

## 9. Data dictionary and expected analytic structure

### Source fields preserved exactly

The release preserves:

```text
facility_id
facility_name
city
county
measure_id
measure_name
denominator
score
lower_estimate
higher_estimate
start_date
end_date
estimate_status
source_comparison_group
footnote_text
source_release
```

The validator compares every one of these values with the Module 06 source by `facility_id`.

### Accessibility fields

| Field | Meaning |
|---|---|
| `display_status` | Reported source comparison or explicit unavailable status. |
| `display_label` | Full text label for the status. |
| `display_symbol` | Short redundant text cue. |
| `display_shape` | Human-readable shape name. |
| `display_shape_code` | R and ggplot2 shape code. |
| `display_line_type` | Solid, dashed, or dotted line cue. |
| `display_color_hex` | Foreground color tested by the build. |
| `contrast_on_white` | Relative-luminance contrast against white. |
| `contrast_on_black` | Relative-luminance contrast against black. |
| `reading_order` | Complete 1 through 65 order. |
| `short_alt_row` | Row-level text representation. |

### Encoding map

| Status | Text | Symbol | Shape | Line | Color | White contrast |
|---|---|---|---|---|---|---:|
| Better | Better than national | B | square | solid | `#1B7837` | 5.54:1 |
| No different | No different from national | N | circle | solid | `#2166AC` | 5.90:1 |
| Worse | Worse than national | W | triangle | solid | `#B2182B` | 6.87:1 |
| Too few | Too few cases | T | x | dashed | `#4D4D4D` | 8.45:1 |
| Not available | Not available | NA | plus | dotted | `#111111` | 18.88:1 |

Better is defined for reuse but has zero Massachusetts rows in this release. The lab may show the cue in a key. It may not add a better hospital to the source case.

### Missing-value contract

- Reported rows have a score and lower and higher estimates.
- Too-few and not-available rows retain blank score and interval fields.
- Blank values never become zero.
- Unavailable rows receive a text status and table row, not a position on the score axis.
- The national rate of 21.3 is a reference, not an imputed hospital value.

### Contrast calculation

The Python build uses the WCAG relative-luminance formula. It records contrast to two fixed backgrounds. Learners test the final chart again because font rendering, antialiasing, transparency, line width, and adjacent colors can affect real use.

## 10. Worked example and instructor walkthrough

### Reproduce the data

From the module folder:

```powershell
python build_accessibility_case.py
python validate_accessibility_case.py
```

The expected validator result is 66 passing checks, 65 rows, and the release checksum in Section 8.

### Reproduce the lab

```powershell
Rscript lab.R
```

The lab creates four PNGs, one 65-row CSV, and one Markdown text alternative.

### Source facts that must remain unchanged

| Fact | Value |
|---|---:|
| Massachusetts rows | 65 |
| Reported rows | 53 |
| No different from national | 52 |
| Worse than national | 1 |
| Too few | 2 |
| Not available | 10 |
| National rate | 21.3 |
| Reported score range | 19.7 to 25.2 |
| Reported denominator range | 30 to 2,088 |

### Color and shape figure

The reference plot uses blue circles for no-different rows and a dark red triangle for the worse row. Gray interval lines and a black dashed benchmark do not depend on color. The legend names the CMS comparison rather than using unlabeled good and bad colors.

### Grayscale figure

The grayscale version turns all marks dark and preserves status through shape and a W or N prefix. This tests the finding without hue. The figure is not a complete screen-reader alternative, which is why the module also provides text and a table.

### Reporting-status figure

The direct-label bar chart shows 1 worse, 52 no different, 2 too few, and 10 not available. One dark fill is sufficient because labels and counts carry the meaning.

### Cue key

The key shows all five reusable statuses, their text, shape, symbol, color, and white-background contrast. It demonstrates that a palette is only one layer of the encoding.

### Instructor interpretation

The committee can focus a source review on the one worse-classified row while treating 52 reported rows as no different from national and 12 unavailable rows as missing evidence. The accessible display must not turn the one triangle into a causal verdict or the 52 circles into proof of equality.

## 11. Guided practice

### Part A: Inventory information carried by color

Open the Module 06 interval figure. List every meaning associated with hue, including comparison status, emphasis, selection, missingness, and reference lines. Separate meaningful hue from decoration.

### Part B: Calculate contrast

For each proposed color:

1. record the exact hex or RGB value;
2. record the adjacent background;
3. calculate relative luminance;
4. calculate the ratio;
5. name whether the object is normal text, large text, or a required graphical object;
6. record the threshold and result;
7. inspect the exported mark at its real size.

### Part C: Add redundant cues

Pair status color with at least one of:

- shape;
- direct text;
- line type;
- position in a labeled panel;
- a stable symbol;
- an exact status column in the adjacent table.

Learners explain why the cue works for this reader task. Shape may distinguish a few categories, but it is not a good replacement for twenty categories.

### Part D: Reduce legend dependence

Test whether a reader must look back and forth between marks and a legend. Add direct labels or a short status symbol when that reduces decoding effort without cluttering the chart.

### Part E: Test color, grayscale, print, and small view

Record the tool or method, the defect found, the repair, and the final result. At minimum:

- view the PNG in full color at 100 percent;
- view or export it in grayscale;
- print or create a print preview;
- inspect it at a smaller width or zoom;
- inspect the exact-value table independently of the chart.

### Part F: Write text alternatives

Draft one or two short sentences that identify the chart and finding. Then write a structured long description with purpose, structure, main finding, values, uncertainty, missingness, decision boundary, and table path.

### Part G: Compare access paths

Ask one reader to use the figure, one to use the long description, and one to use the table. Each should reach the same source-supported finding and see the same unavailable rows. Record any mismatch.

## 12. Independent exercise

### Prompt

Prepare a release candidate for a clinical quality committee. The package must work during a meeting and during later exact-value review.

### Required analysis

1. Read the released Module 07 table.
2. Confirm row count, measure, period, benchmark, statuses, and missingness.
3. Choose the smallest useful display for the committee task.
4. Define color and non-color cues.
5. calculate and record contrast in the final context.
6. Render the final figure from code or an editable workbook.
7. Export the complete exact-value table.
8. Write short and long text alternatives.
9. run color, grayscale, print, and small-view checks.
10. repair defects and record the final release decision.

### Required answer

The learner states:

- who reads the display and under what conditions;
- what the one strongest source-supported finding is;
- which status cue works without color;
- which contrast thresholds were tested and passed;
- where a reader finds exact values and unavailable rows;
- which source and accessibility limits remain;
- what the committee should review, monitor, or defer.

### Approved alternatives

The final figure may be a caterpillar plot, labeled comparison panel, paired chart and table, or another defensible form. A learner may conclude that a chart should be replaced by a table for a specific task. The conclusion must still provide an accessible overview and exact values.

### Prohibited shortcuts

- naming a palette as the entire accessibility audit;
- using color alone after changing the hues;
- pasting alt text that only says "chart" or repeats the title;
- listing all 65 rows in an unstructured paragraph;
- omitting unavailable rows because they have no score;
- recoloring a point and changing its source category;
- recalculating a binomial interval from the denominator;
- using interval overlap as a pairwise significance test;
- manually editing only the exported PNG;
- submitting a simulator result without human interpretation or a final-context check.

## 13. Visualization and communication requirements

### Final figure

`figure.png` must:

- show every reported point and source interval used in the decision;
- label the national rate of 21.3 directly;
- preserve the source comparison category;
- pair color with a non-color cue;
- keep line work and labels readable against the final background;
- remain interpretable in grayscale;
- name `READM_30_HF`, Massachusetts, and 2023-07-01 through 2025-06-30;
- state that lower and higher estimates come from CMS;
- state that pairwise hospital difference is not tested;
- provide a clear route to missing statuses and exact values;
- avoid verdict language.

### Color

- Use qualitative color for categories, sequential color for ordered magnitude, and diverging color only around a meaningful reference.
- Do not use a diverging midpoint merely because a number is average.
- Do not assume green means safe or red means harmful.
- Use a named exact color value, not "dark enough."
- Test the actual foreground against the actual adjacent background.
- Keep the meaning available without hue.

### Text and labels

- Use plain labels for source categories.
- Keep measure units, dates, and geography close to the chart.
- Expand or define abbreviations.
- Place the main finding before secondary detail.
- Avoid rotated labels when a table or different orientation reads better.

### Exact-value alternative

`data-table.csv` contains all 65 rows and the required columns in the assessment. The delivery version also needs a semantic table or document structure with a caption, column headers, and clear reading order.

### Short alternative

Short text identifies:

- the chart type or purpose;
- the population and measure;
- the main comparison finding;
- where the long description or table is located.

### Long description

The long description contains headings for purpose and structure, main finding, values and uncertainty, missing and unavailable results, decision boundary, and exact-value table. It preserves relationships and trends, not decorative color names.

### Decision note

The note leads with the reader, finding, and action. It explains the access path and the main uncertainty. It does not turn accessible presentation into stronger clinical evidence.

## 14. Exact submission package and filenames

```text
module-07/
  accessibility-audit.md
  analysis.R
  figure.png
  data-table.csv
  alt-text.md
  decision-note.md
  ai-use.md
```

An approved editable alternative may replace `analysis.R` while keeping the other names.

### `accessibility-audit.md`

```markdown
# Accessibility audit

## Audience, context, and user tasks
## Information carried by color
## Contrast calculations
## Redundant cues
## Color, grayscale, print, and small-view checks
## Text alternative and table
## Repairs made
## Remaining risks and human review
```

### `alt-text.md`

```markdown
# Text alternative

## Short alternative
## Long description
### Purpose and structure
### Main finding
### Values and uncertainty
### Missing and unavailable results
### Decision boundary
### Exact-value table
```

### `decision-note.md`

```markdown
# Decision note

## Reader
## Finding
## Action
## Access path
## Uncertainty
## Evidence needed next
```

### `ai-use.md`

```markdown
# AI-use record

## Tool and model
## Work delegated
## Prompts or instructions
## Verification
## Human decisions
```

If no generative AI was used, state that and describe the manual checks.

## 15. Rubric and pass conditions

| Criterion | Weight | Full-credit evidence |
|---|---:|---|
| Source fidelity and interpretation | 15% | All source values, statuses, dates, benchmark, and claim boundaries remain intact. |
| Color and contrast | 15% | Ratios, thresholds, foregrounds, backgrounds, and final-context checks are correct and documented. |
| Redundant encoding and grayscale | 15% | Status and the main finding survive without hue. |
| Figure design and time-pressured reading | 15% | The reader can find benchmark, status, uncertainty, and next step quickly. |
| Text alternative and exact table | 15% | Short text, structured long description, and the complete table provide equivalent information. |
| Critique and repair | 10% | Both barriers are diagnosed and repaired without changing the evidence. |
| Reproducibility | 10% | Editable analysis regenerates the figure and table. |
| Decision note and AI accountability | 5% | The action fits the evidence and tool use is fully recorded. |

### Noncompensable pass conditions

- Color is not the only status cue.
- Required text and graphical objects pass the documented final-context contrast checks.
- The grayscale check preserves status and finding.
- Every hospital is present in the figure, table, or linked alternate path.
- `data-table.csv` has 65 rows and keeps unavailable values blank.
- Short alt text, structured long description, and exact table are present.
- Source values, intervals, categories, dates, benchmark, and footnotes are unchanged.
- Pairwise significance, equivalence, and causation are not claimed.
- The analysis is editable and reproducible.
- No restricted clinical data are included.
- The AI-use record is complete.

## 16. Common errors, failure modes, and interventions

| Failure | Why it matters | Instructor response |
|---|---|---|
| Swapping red and green for blue and orange | Hue still carries status alone. | Require a non-color cue and grayscale evidence. |
| Treating a palette name as proof | Palette safety depends on context, size, contrast, and task. | Require exact values and final-context checks. |
| Checking only text contrast | Intervals, points, axes, and status marks may disappear. | Inventory required graphical objects and adjacent colors. |
| Checking only color simulation | Simulation does not test text alternatives, tables, structure, zoom, or assistive technology. | Require the complete audit. |
| Writing alt text as a caption | A title does not preserve relationships, values, uncertainty, and missingness. | Separate short text, long description, and exact table. |
| Reading every row in alt text | The result is hard to navigate and duplicates the table. | Summarize structure and finding, then link exact values. |
| Hiding unavailable rows | Readers mistake missing evidence for no events or good performance. | Keep statuses in the table, summary, and long description. |
| Changing categories during repair | The visual change becomes a data change. | Compare every source field by stable ID. |
| Thin pale interval lines | The main uncertainty disappears in print or low contrast. | Increase contrast or weight and retest. |
| Too many shape categories | Shape decoding becomes difficult and cluttered. | Reduce categories, facet, label, or use a table. |
| Clinical traffic-light language | Color implies a verdict beyond the source. | Use source category text and a decision boundary. |
| Claiming compliance | The assignment tests a bounded static package, not full conformance. | Change the claim to named checks and remaining risks. |

## 17. Accessibility, equity, privacy, and responsible claims

### Accessibility

The reference package applies these rules:

- color never acts alone;
- each status has full text, a symbol, and a shape or line cue;
- each defined foreground exceeds 4.5:1 against white;
- grayscale output is a required artifact;
- unavailable rows remain in the table and text;
- the chart has short text, a structured long description, and exact values;
- final review still requires human inspection and context-specific testing.

### Equity

Access barriers affect who can participate in a clinical decision. A color-only or image-only packet can exclude committee members, staff, patients, or community partners even when the statistical work is correct.

Accessible presentation does not fix inequity in the source data or risk model. Public hospital measures may reflect structural differences in access, illness burden, referral patterns, documentation, and resources. Learners do not turn a source classification into a moral label for a hospital or community.

### Privacy

The module uses public hospital aggregate data. No patient-level record is needed. If an instructor substitutes local data, the public package may contain only an approved de-identified or aggregate release. Small cells, suppressed values, restricted identifiers, and data-use terms remain governed by the source.

### Responsible claim template

> The accessible display preserves the CMS comparison and uncertainty for 65 Massachusetts hospital rows. It supports source review and monitoring. It does not establish pairwise hospital difference, equivalence, causation, or patient-level quality.

## 18. AI and agent policy

AI may assist with:

- drafting alternative text for human revision;
- proposing redundant encodings;
- checking code structure;
- summarizing recorded audit results;
- finding missing labels or source fields;
- comparing the figure, table, and description for mismatch.

### Required `ai-use.md`

Record:

- tool and model;
- task assigned;
- prompt or material instruction;
- source data provided;
- output retained or rejected;
- human verification;
- final decisions made by the learner.

### Prohibited AI uses

- inventing a contrast ratio without calculation;
- asserting WCAG or Section 508 compliance without a scoped review;
- changing source values or statuses to fit a chart;
- inventing text for unavailable CMS values;
- writing a stronger clinical conclusion than the public data support;
- using generated alt text without comparing it with the final figure and table;
- uploading restricted patient or partner data to an unapproved service;
- citing an AI summary instead of the W3C, CDC, and CMS sources.

### Verification rule

The learner is responsible for each value, ratio, cue, label, text alternative, table row, source statement, and decision claim. If the figure changes after AI-assisted text is drafted, the text must be checked again.

## 19. Answer key and instructor notes

### Required numeric answers

| Question | Answer |
|---|---:|
| Total rows | 65 |
| Reported rows | 53 |
| No different | 52 |
| Worse | 1 |
| Too few | 2 |
| Not available | 10 |
| National rate | 21.3 |
| Score range | 19.7 to 25.2 |
| Denominator range | 30 to 2,088 |
| Defined status cues | 5 |
| Present statuses | 4 |
| Lowest white-background contrast | 5.54:1 |
| Highest white-background contrast | 18.88:1 |
| Data checks | 66 |

### Interpretation key

- The one worse row remains the only worse row in color and grayscale.
- The 52 no-different rows remain no different. Their unique point ranks do not become unique source categories.
- Too-few and not-available rows stay visible in the status summary, table, and long description.
- The 21.3 line is the source national reference.
- Lower and higher estimates remain CMS source endpoints.
- The reference palette exceeds its stated white-background ratios but does not certify the whole chart.
- Better is a defined reusable cue with zero rows in the case.

### Critique key

The red-green chart fails because hue is the only status cue, identical point shapes require color discrimination, and the legend creates decoding effort. It also omits the source interval and benchmark.

The pale heatmap fails because contrast is weak, hue carries value, separately normalized columns suggest a shared scale, values and units disappear, and the three quantities answer different questions. Replacing the heatmap with a labeled table is acceptable.

### Acceptable release conclusion

The reference package is technically ready for human review. A final learner package passes only after the figure, grayscale output, print or print-preview check, smaller view, table, short text, long description, source fidelity, and decision claim are reviewed together.

### Handoff answer

Module 08 must preserve these standing requirements while adding time and process variation: readable contrast, non-color cues, exact values, missingness, short text, long description or equivalent structured alternative, reproducibility, and a scoped accessibility audit.

## 20. Runnable acceptance checks

### Build checks

From the module folder:

```powershell
python build_accessibility_case.py
```

Pass conditions:

- upstream Module 06 checksum matches;
- output has 65 rows and 27 columns;
- output SHA-256 is `b58168d9002a3e489213b0fafde1eca76f5b1a426c71ea3d61551671d76a49c2`;
- rerunning the build produces the same bytes.

### Data checks

```powershell
python validate_accessibility_case.py
```

Pass conditions:

- 66 checks pass;
- all 65 source IDs and selected values match Module 06;
- status counts reconcile to 53 reported, 2 too few, and 10 not available;
- display counts reconcile to 52 no different, 1 worse, 2 too few, and 10 not available;
- reported points remain inside source intervals;
- unavailable numeric fields remain blank;
- reading order is 1 through 65;
- present status rows use the fixed cue map;
- every defined foreground exceeds 4.5:1 on white;
- every row has an appropriate text alternative.

### R checks

```powershell
Rscript lab.R --output output
Rscript critique_charts.R --output critique-output
```

Pass conditions:

- four lab PNGs open and contain content;
- the accessible table has 65 rows;
- the text-alternative Markdown contains short and long sections;
- two critique PNGs open and are clearly labeled as flawed;
- no unexpected R warning changes the result.

### Visual checks

- The color-plus-shape chart shows the same one worse row as the grayscale chart.
- The grayscale chart uses shape and W or N text cues.
- The status chart shows counts 1, 52, 2, and 10 with direct labels.
- The cue key shows five status definitions and their white-background ratios.
- The benchmark, period, measure, source endpoint note, and pairwise boundary remain visible.
- No output invents a better Massachusetts row.

### Repository checks

- The module specification contains exactly 21 numbered sections.
- Every required package file exists.
- `release.json` reports module 0.1.0 and Commons 0.18.0.
- Root, course, site, and ledger version markers agree at 0.18.0.
- The course checker includes Module 07 and its release metadata.
- JavaScript syntax remains valid.
- No added prose contains a Unicode em dash or en dash.
- `git diff --check` passes.

## 21. Release status, reviewers, version, and known issues

### Version decision

Module 07 adds a complete numbered module and begins the applied portfolio. The Commons version moves from 0.17.1 to 0.18.0. The module package begins at 0.1.0.

### Technical release gate

Technical release-candidate status requires:

- deterministic data build;
- 66 passing data checks;
- four rendered lab figures;
- one complete 65-row table;
- one reference short and long text alternative;
- two rendered critique figures;
- exact assessment and instructor key;
- release metadata and source record;
- passing course and repository checks.

Technical completion does not mark the human reviews complete.

### Required human reviews

| Review | Reviewer | Release question |
|---|---|---|
| Accessibility and assistive technology | Named accessibility reviewer, preferably including a disabled user | Can the figure, text, and table support the stated tasks across the tested access paths? |
| Clinical quality interpretation | Clinician or quality leader | Does the display support focused review without turning a source category into a verdict? |
| Statistical and CMS source fidelity | Named quantitative reviewer | Are values, intervals, benchmark, missingness, and claim boundaries preserved? |
| Visualization teaching quality | Named visualization faculty member | Do the lab and critiques teach color, contrast, redundancy, and alternatives accurately? |
| Independent teachability | Instructor other than the author | Can the module run from a clean checkout with the stated prerequisites? |

### Known issues

- Human reviews remain pending.
- Contrast calculations cover fixed foregrounds on white and black, not every final adjacent color or rendering condition.
- The package does not test every browser, screen reader, color-vision condition, display, printer, reflow setting, or zoom level.
- The reference lab produces static PNG and CSV outputs. A web deployment needs semantic HTML, keyboard, focus, reflow, and dynamic-state review where applicable.
- CMS labels the interval columns Lower Estimate and Higher Estimate; the module does not invent a confidence level.
- The risk-standardized model cannot be reconstructed from the public extract alone.
- Public aggregate data lag current operations and do not establish causal hospital quality differences.
- Technical execution has been tested on Windows. Clean macOS and Linux runs remain a human release check.

### Handoff to Module 08

Module 08 owns time and process variation. It must carry forward the Module 07 access contract while teaching trends, seasonality, special-cause signals, and ordinary variation. A time-series display does not pass if color alone separates lines, the exact time values are unavailable, missing periods disappear, annotations are not available in text, or the process claim exceeds the data.
