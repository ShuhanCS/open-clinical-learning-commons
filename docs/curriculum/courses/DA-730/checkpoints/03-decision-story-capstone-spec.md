# DA-730 Final Checkpoint: Decision-Story Capstone and Defense

- Checkpoint ID: DA-730-CP3
- Course: DA-730, Clinical Data Visualization and Decision Storytelling
- Due: official last day of the assigned MGH Institute half-term
- Modules included: 01 through 13, with required resolution of Checkpoint 2 conditions
- Checkpoint version: 0.1.0
- Commons release: 0.26.0
- Learner workload: included in the 16.5 hours assigned to Module 13
- Runnable package: `courses/data-visualization/checkpoints/03-decision-story-capstone/`
- Official calendar: https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

## 1. Purpose, decision, and completion meaning

### Purpose

The final checkpoint is the complete DA-730 performance assessment. It asks a learner to release and defend one sourced, reproducible, accessible, and action-bounded clinical decision story.

The checkpoint brings the course sequence together:

1. represent variables faithfully;
2. choose perceptually accurate encodings;
3. select a display for a reader task;
4. preserve distributions and missingness;
5. preserve rates, denominators, and adjustment;
6. communicate uncertainty and small numbers;
7. provide non-color and text access;
8. preserve time and reporting context;
9. compare groups on common scales;
10. use geography only when place matters;
11. define flow, composition, and absence states;
12. coordinate the minimum views for a decision; and
13. adapt one stable evidence chain for two audiences.

This is not a folder-completion exercise. The learner must show that the evidence, display, prose, exact table, action request, accessibility path, and oral answers all describe the same bounded decision.

### Final decision owner

The final decision owner is a DA-730 review panel with:

- the course instructor;
- at least one clinical, quality, operational, research, patient, public-health, or community reviewer appropriate to the case;
- an accessibility reviewer or a faculty reviewer applying the accessibility contract; and
- a reproducibility reviewer or second instructor.

One person may fill more than one role when the program documents the role and the conflict is acceptable. The learner may not be the final reviewer of their own release.

### Final checkpoint decision

Decide whether the learner has demonstrated the full DA-730 competency and may release the decision-story capstone as course evidence.

### Release dispositions

| Disposition | Meaning | Release result |
|---|---|---|
| `approve` | All pass gates are satisfied and no material condition remains. | The capstone may be released as completed DA-730 evidence. |
| `approve with conditions` | All noncompensable gates pass and a named bounded condition has an owner, date, and closure test. | The release may proceed only under the recorded condition. |
| `revise` | One or more recoverable requirements are incomplete or inconsistent. | The release does not pass until resubmitted and re-reviewed. |
| `refer` | A privacy, rights, integrity, safety, restricted-data, or professional-boundary concern needs program review. | The release is held outside the public Commons workflow. |

The package validator accepts only `approve` or `approve with conditions` as a released final package. A `revise` or `refer` record remains useful evidence of the review but does not pass the release gate.

### Supported course action

The panel may award the DA-730 final checkpoint, require a bounded revision, narrow the public release, or refer the work for program review.

### Unsupported course action

Course approval does not authorize:

- a real clinical intervention;
- a current hospital performance rating;
- a staffing or care-delivery change;
- release of restricted patient or partner data;
- use of a mock course trigger as an official benchmark;
- a causal conclusion from descriptive public reporting; or
- institutional endorsement by CMS, MGH Institute, a hospital, or a data publisher.

### Completion statement

The checkpoint is complete only when the folder validates, the score is at least 80, every noncompensable gate passes, the oral defense passes, required reviewers record their findings, and the disposition is `approve` or `approve with conditions`.

## 2. Calendar rule, due date, and workload

### Planning model

DA-730 uses a 7.5-week instructional design model. That phrase describes workload planning. It does not create a universal 52.5-day academic term.

The official 2026-2027 MGH Institute calendar labels these offerings as half-terms and gives the dates below.

| Half-term | First day | Last day | Elapsed span |
|---|---|---|---:|
| Fall 2026 half-term 1 | September 8, 2026 | October 27, 2026 | 49 days |
| Fall 2026 half-term 2 | October 28, 2026 | December 18, 2026 | 51 days |
| Spring 2027 half-term 1 | January 11, 2027 | March 2, 2027 | 50 days |
| Spring 2027 half-term 2 | March 3, 2027 | April 24, 2027 | 52 days |
| Summer 2027 half-term 1 | May 10, 2027 | June 29, 2027 | 50 days |
| Summer 2027 half-term 2 | June 30, 2027 | August 20, 2027 | 51 days |

The official source is:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

### Due-date rule

The final checkpoint is due on the official last day of the learner's assigned half-term. The course schedule must write the real date into `review-disposition.md` and the learning-management system.

Do not publish a due date calculated as:

- start date plus 52 or 53 days;
- seven full weeks plus a fixed half week;
- the nearest Friday;
- the date used by another half-term; or
- a date copied from this specification without checking the current official calendar.

### Workload placement

The final checkpoint does not add hours beyond the course total. Its work is contained in Module 13's 16.5 hours.

| Final work | Planned hours | Evidence |
|---|---:|---|
| Confirm Checkpoint 2 conditions and evidence invariants | 1.0 | condition closure and invariant audit |
| Regenerate and inspect the two audience figures | 2.5 | primary and supporting PNG files |
| Complete exact table, source, and transformation records | 2.0 | CSV, YAML, and transformation record |
| Complete decision brief and adaptation record | 3.0 | two completed Markdown records |
| Complete accessibility and text-equivalence work | 2.0 | alt text, table, figure, and PDF evidence |
| Run clean reproduction and validator | 1.5 | reproducibility record |
| Resolve critique and document AI use | 1.5 | critique response and AI-use record |
| Prepare and rehearse the defense | 2.0 | accessible slides and written responses |
| Complete oral defense and review handoff | 1.0 | defense result and disposition |
| Total | 16.5 | Module 13 and final checkpoint |

### Holiday and scheduling rule

The offering-specific schedule may redistribute work around holidays or Institute closures. It may not remove a competency, reduce the exact final folder, or move the official final due date beyond the published half-term without program approval.

## 3. Prerequisites, entry gate, and scaffold paths

### Required prerequisites

Before final assembly, the learner must have:

- completed Modules 01 through 13;
- submitted Checkpoint 1;
- received a Checkpoint 2 disposition;
- resolved every Checkpoint 2 condition that affects source, scope, reproducibility, privacy, accessibility, or feasibility;
- identified two audiences with different tasks or technical needs;
- identified one stable decision;
- obtained approval for the public or synthetic source; and
- confirmed that no restricted data will enter the public folder.

### Entry gate

The instructor checks five items before allowing final review:

1. the source remains available and its rights remain compatible with release;
2. the proposed decision still fits the available variables and time window;
3. the analysis can be completed and reproduced inside the remaining course time;
4. the action remains inside the authority of the named audience; and
5. the learner has a clinical or domain reviewer appropriate to the case.

### Scaffold paths

All scaffold paths meet the same outcomes and rubric.

| Path | Starting point | Required learner authorship | Best fit |
|---|---|---|---|
| Run | Released Module 13 CMS reference case | Regenerate, inspect, rewrite the brief, complete all records, prepare the defense, and answer every question. | Learner who needs a complete technical starting point. |
| Modify | Released source and values with a changed audience, narrative, or supporting view | Preserve invariants while making and defending a meaningful adaptation. | Default transitional path. |
| Author | Approved Checkpoint 2 capstone proposal and approved open or synthetic source | Build the complete evidence chain and all release records. | Learner ready for independent work. |

### Equality of standard

The Run path is not a lower grading standard. A learner who uses the reference analysis must still:

- explain the source and every key definition;
- verify all values;
- write original audience-specific prose;
- complete the transformation and adaptation records;
- demonstrate equivalent access;
- document all AI use;
- reproduce the release; and
- defend the decision and limit without relying on the supplied answer key.

### Alternative-source approval

An Author-path source must be:

- publicly downloadable or explicitly synthetic;
- compatible with redistribution in the Commons;
- documented with a full HTTPS landing page and exact access path;
- small enough to package or reproducibly retrieve;
- free of direct and indirect identifiers that violate the public-release boundary;
- sufficiently defined to support an exact table; and
- sufficiently stable to reproduce the final release.

## 4. Competencies and observable outcomes

### Final competency

Produce and defend one source-faithful, audience-specific, reproducible, accessible, and action-bounded clinical decision story.

### Observable outcomes

By the final checkpoint, the learner can:

1. name two audiences and distinguish their authority;
2. state one decision in terms the decision owner can act on;
3. distinguish finding, interpretation, recommendation, and action;
4. preserve the source population, unit, denominator, status, and time window;
5. state uncertainty, freshness, missingness, and aggregation limits;
6. choose one primary figure that carries the decision;
7. use one supporting figure only when it answers a different necessary question;
8. write a finding-led title without causal or current-performance inflation;
9. use annotation to expose values, source boundaries, and action ownership;
10. preserve exact decision-changing values in an accessible table;
11. provide equivalent text communication for both figures;
12. document every material transformation;
13. document what changed across audiences and what stayed invariant;
14. reproduce outputs from the packaged source and editable analysis;
15. verify and disclose AI assistance;
16. resolve one critique at the decision-contract level;
17. create and deliver an accessible eight-minute defense;
18. answer source, method, access, limit, and action questions; and
19. state what the evidence does not support.

### Competency evidence map

| Competency | Primary evidence | Corroborating evidence |
|---|---|---|
| Audience and authority | README and decision brief | adaptation record and defense |
| Source fidelity | source record and data fingerprints | exact table and reproducibility record |
| Visual judgment | primary and supporting figures | transformation record and critique response |
| Claim integrity | title, brief, and requested action | oral answers and review disposition |
| Exact-value access | accessible table | alt text and defense slides |
| Reproducibility | editable analysis and packaged data | clean-run record and validator result |
| Accessibility | non-color figures, alt text, table, accessible PDF | accessibility reviewer result |
| AI accountability | AI-use record | learner explanation during defense |
| Clinical boundary | supported and unsupported action statements | clinical review and defense |

### Noncompensable outcomes

A high total score cannot compensate for:

- restricted or unidentified data;
- unverifiable or altered key values;
- a causal claim without a causal design;
- a historical value presented as current;
- a scenario trigger presented as official;
- an action outside the named audience's authority;
- missing exact-value or text access;
- irreproducible evidence;
- undisclosed material AI assistance; or
- failure to complete the oral defense.

## 5. Exact final folder contract

### Required structure

```text
final-capstone/
  README.md
  decision-brief.md
  figure-primary.png
  figure-supporting.png
  accessible-table.csv
  alt-text.md
  analysis/
    analysis.R
  data/
    ma_ed_public_reporting_dashboard_2026.csv
    ed_dashboard_measure_dictionary_2026.csv
    cms_ma_ed_dashboard_source_2026.csv
  source-record.yml
  transformation-record.md
  audience-adaptation-record.md
  reproducibility-check.md
  critique-response.md
  ai-use.md
  review-disposition.md
  defense/
    slides.pdf
    slides-outline.md
    questions-and-responses.md
```

### Exact-name rule

The validator connects evidence by exact name. Do not rename:

- the two figure files;
- the exact table;
- the top-level records;
- the analysis base name;
- the three reference data files; or
- the defense PDF and written response.

### Alternative analysis tools

An approved alternative may replace `analysis/analysis.R` with exactly one of:

- `analysis/analysis.py`;
- `analysis/analysis.ipynb`;
- `analysis/analysis.twb`;
- `analysis/analysis.pbix`;
- `analysis/analysis.ps1`; or
- another approved editable source using the `analysis` base name.

The alternative tool does not change the figure, table, source, accessibility, transformation, AI, or defense contract.

### File-purpose map

| File | Required purpose |
|---|---|
| `README.md` | Release identity, audiences, decision, reproduction, folder map, review, and limits. |
| `decision-brief.md` | The 600-to-900-word decision request. |
| `figure-primary.png` | Main finding for the decision owner. |
| `figure-supporting.png` | A different necessary question for the second audience or technical review. |
| `accessible-table.csv` | Every exact value that changes the decision. |
| `alt-text.md` | Equivalent text communication for both figures. |
| `analysis/analysis.*` | One editable source that regenerates the evidence. |
| `data/` | Exact source or released teaching data used by the analysis. |
| `source-record.yml` | Publisher, URLs, rights, fingerprints, fields, filters, and limits. |
| `transformation-record.md` | Every material selection, recode, calculation, threshold, annotation, and export. |
| `audience-adaptation-record.md` | What changed across audiences and what remained invariant. |
| `reproducibility-check.md` | Clean-run environment, commands, fingerprints, outputs, inspection, and result. |
| `critique-response.md` | One repaired decision-contract problem and its review. |
| `ai-use.md` | Material AI assistance and human verification. |
| `review-disposition.md` | Score, defense result, reviewer results, conditions, and final disposition. |
| `defense/slides.pdf` | Accessible eight-minute defense deck. |
| `defense/slides-outline.md` | Editable content outline or source companion. |
| `defense/questions-and-responses.md` | Written answers to the final defense questions. |

### No hidden dependencies

The final folder may not depend on:

- an uncommitted local extract;
- a private patient spreadsheet;
- a hidden Tableau extract;
- a manually edited final value;
- a cloud notebook the reviewer cannot open;
- a package absent from the environment record;
- a local absolute path;
- a file available only on the learner's computer; or
- a credential needed to reproduce already-released outputs.

## 6. Reference source and evidence chain

### Publisher and dataset

Publisher: Centers for Medicare & Medicaid Services.

Dataset: Timely and Effective Care - Hospital.

Dataset landing page:

https://data.cms.gov/provider-data/dataset/yv7e-xc69

Pinned complete CSV:

https://data.cms.gov/provider-data/sites/default/files/resources/0437b5494ac61507ad90f2af6b8085a7_1785189967/Timely_and_Effective_Care-Hospital.csv

Hospital data dictionary:

https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/hospital/HOSPITAL_Data_Dictionary.pdf

Measure periods:

https://data.cms.gov/provider-data/topics/hospitals/measures-and-current-data-collection-periods

### Complete source fingerprint

| Attribute | Value |
|---|---|
| Release date | 2026-08-13 |
| Rows | 138,084 |
| Columns | 16 |
| Bytes | 34,150,899 |
| SHA-256 | `1e5a1ca803c2b09468fe3ae3fe60fef3e910f5f5300630a24791c88a1abff516` |

### Packaged releases

| File | Rows | Columns | SHA-256 |
|---|---:|---:|---|
| `ma_ed_public_reporting_dashboard_2026.csv` | 186 | 31 | `fbfcfcaf10d87cd48236a702622781f559d86d52b8773ca578d72313a9b270fd` |
| `ed_dashboard_measure_dictionary_2026.csv` | 3 | 18 | `2db834a350c0fee342efb30fc4b028053e325b3b357cc1031a11f7c9e9b29412` |
| `cms_ma_ed_dashboard_source_2026.csv` | 186 | 15 | `f28f5d56e5e0e29001c7a275b01306762e673c9a21459dc7a68ff1aea782943b` |

### Reference population

The teaching release contains 186 hospital-measure rows:

- 62 Massachusetts facilities;
- three measures or categories per facility;
- EDV as an emergency-department volume category;
- OP_18b as median emergency-department time before admission; and
- OP_22 as the percent leaving before being seen.

### Selected facility

The reference final story uses:

- facility: Anna Jaques Hospital;
- CMS facility ID: 220029;
- state: Massachusetts; and
- three selected-facility rows in the exact table.

### Public-use boundary

The data are public U.S. government reporting data. Attribution is required. The release may not imply CMS endorsement.

### Reuse rule

The final checkpoint copies the pinned released tables. It does not silently refresh the CMS dataset. A new CMS release requires a new source record, fingerprints, validation expectations, figures, exact table, and version decision.

## 7. Exact data, table, and invariant contract

### Accessible-table schema

The reference `accessible-table.csv` has exactly these 20 fields in this order:

1. `measure_id`;
2. `display_label`;
3. `score_raw`;
4. `score_numeric`;
5. `unit`;
6. `sample`;
7. `value_status`;
8. `footnote`;
9. `period_start`;
10. `period_end`;
11. `cms_release_date`;
12. `source_lag_days_at_release`;
13. `ma_reported_n`;
14. `ma_median`;
15. `ma_rank_unfavorable`;
16. `scenario_threshold`;
17. `threshold_crossed`;
18. `threshold_origin`;
19. `monitoring_use`; and
20. `action_if_crossed`.

### Required rows

The table contains exactly one row for each:

- `EDV`;
- `OP_18b`; and
- `OP_22`.

### Reference facts

| Item | Required reference value |
|---|---:|
| Massachusetts facilities | 62 |
| Selected ED volume category | Low |
| Selected OP_18b | 188 minutes |
| OP_18b sample | 422 |
| Massachusetts OP_18b reporting hospitals | 54 |
| Massachusetts OP_18b median | 211.5 minutes |
| Mock OP_18b trigger | 240 minutes |
| OP_18b trigger crossed | No |
| OP_18b source lag | 317 days |
| Selected OP_22 | 23 percent |
| OP_22 source sample | 19,211 |
| Massachusetts OP_22 reporting hospitals | 53 |
| Massachusetts OP_22 median | 3 percent |
| Selected unfavorable OP_22 position | 1 |
| Mock OP_22 trigger | 10 percent |
| OP_22 trigger crossed | Yes |
| OP_22 source lag | 590 days |

### Stable supported action

The reference release supports:

> Authorize the emergency department quality director to conduct a definition and current-data review, then return with current local OP-22 and emergency-department time evidence.

### Stable unsupported conclusions

The evidence does not support:

- a current performance rating;
- causal attribution;
- a conclusion about staffing, crowding, patient behavior, or care quality;
- a subgroup disparity statement;
- an intervention choice;
- an intervention-effect claim; or
- a claim that the 10-percent or 240-minute trigger is a CMS standard.

### Cross-audience invariants

These items may not change between the primary and supporting versions:

- source release;
- facility identity;
- population;
- measure definitions;
- values and units;
- samples and status;
- reporting windows;
- release date and lags;
- peer counts and descriptive medians;
- scenario triggers and their non-CMS origin;
- trigger crossing result;
- historical-use label;
- material limitation;
- action owner;
- supported action; and
- unsupported conclusions.

### Adaptable elements

The learner may change:

- title wording within the claim boundary;
- annotation density;
- evidence order;
- terminology defined for the audience;
- which detail appears in the figure, table, caption, or brief;
- narrative sequence;
- visual emphasis;
- supporting evidence depth; and
- presentation pacing.

## 8. Primary figure, supporting figure, and narrative contract

### Primary figure purpose

The reference `figure-primary.png` serves the hospital quality committee. It answers:

> Should the committee authorize a bounded local review of this historical public signal?

It uses three cards:

1. public signal;
2. time boundary; and
3. decision request.

### Primary figure required content

The primary figure must expose:

- the finding-led historical signal;
- the 23-percent OP-22 value;
- the 53-hospital peer context;
- the 590-day time boundary;
- the requested authorization;
- the action owner;
- the evidence expected at return review;
- the non-CMS trigger boundary; and
- the current, causal, and intervention limits.

### Supporting figure purpose

The reference `figure-supporting.png` serves the emergency department quality director. It answers:

> Where does the selected historical OP-22 value sit among reported Massachusetts peers, and what must be validated before action?

### Supporting figure required content

The supporting figure must expose:

- all 53 reported OP-22 peer values;
- an ordered peer structure;
- a direct label at 23 percent;
- the descriptive 3-percent Massachusetts median;
- the mock 10-percent review trigger;
- a statement that the trigger is not CMS;
- the 2024 reporting window;
- the 2026 release and 590-day lag;
- the definition-validation action; and
- the no-intervention boundary.

### Distinct-purpose gate

The supporting figure must answer a different necessary question. It cannot be:

- a recolored copy of the primary figure;
- the same evidence with a different title;
- an extra chart added for visual variety;
- a detail that belongs only in the exact table; or
- a view that creates a second decision.

### Title ladder

The title must stay at the strongest supported level:

| Level | Example | Reference status |
|---|---|---|
| Observation | The public OP-22 value is 23 percent. | Supported. |
| Comparison | The value is highest among 53 reporting Massachusetts hospitals. | Supported as a descriptive comparison. |
| Interpretation | The historical signal warrants validation. | Supported. |
| Recommendation | Authorize a definition and current-data review. | Supported. |
| Cause | Staffing caused patients to leave. | Unsupported. |
| Intervention effect | Adding staff will reduce OP-22. | Unsupported. |

### Annotation rules

Annotations must:

- point to evidence that exists;
- state units;
- expose threshold origin;
- expose freshness when it changes interpretation;
- name the action owner when requesting action;
- avoid emotional or stigmatizing language;
- avoid implying a trend from one period; and
- remain equivalent to the exact table and alt text.

## 9. Learner records and written deliverables

### README

The README contains 350 to 1,300 words and includes:

- release status and official due date;
- learner and version;
- both audiences and their authority;
- one decision;
- source and release;
- strongest finding;
- supported and unsupported actions;
- exact reproduction commands;
- expected outputs;
- folder map;
- reviewer names or roles;
- score, defense result, and disposition; and
- known limits.

### Decision brief

The decision brief contains 600 to 900 words under these headings:

- `## Audience and authority`;
- `## Finding`;
- `## Evidence`;
- `## Requested decision`;
- `## Action owner and next review`;
- `## Uncertainty or freshness`;
- `## Material limitation`; and
- `## Unsupported conclusion`.

The brief must preserve the 23-percent signal, 53 reporting peers, 590-day lag, and definition and current-data review action.

### Transformation record

The record contains 450 to 1,500 words and documents every material:

- input and fingerprint;
- source selection;
- filter and exclusion;
- definition and recode;
- calculation and reference;
- denominator and sample meaning;
- threshold and action rule;
- ordering and annotation;
- audience adaptation;
- manual review; and
- export.

No material transformation may exist only in manual chart editing.

### Audience-adaptation record

The 350-to-1,200-word record covers:

- authority and task;
- title;
- evidence shown;
- evidence moved to the table or note;
- terminology;
- annotation density;
- narrative sequence;
- requested action;
- material limitation; and
- unsupported conclusions.

For every element, state:

1. primary audience version;
2. secondary audience version;
3. what changed;
4. what stayed invariant; and
5. verification evidence.

### Critique response

The 350-to-1,000-word response resolves one Module 13 critique or approved reviewer comment. It includes:

- original problem;
- likely reader error;
- decision affected;
- repair;
- invariant audit;
- accessibility check;
- reviewer response; and
- remaining limit.

A font, color, or software change alone does not satisfy the repair requirement.

### AI-use record

The 350-to-1,200-word record names:

- tool and model;
- date;
- work delegated;
- material prompts or instructions;
- generated artifacts used;
- learner revisions;
- number and definition verification;
- source and rights verification;
- cross-audience verification;
- accessibility verification;
- human decisions; and
- final responsibility.

If no generative AI was used, state that and document the manual checks. A blank record does not pass.

## 10. Reproducibility, analysis, and technical execution

### Reference command

From the repository root:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File courses/data-visualization/checkpoints/03-decision-story-capstone/assemble_checkpoint.ps1 -Target final-capstone
```

Inside the assembled folder:

```powershell
Rscript analysis/analysis.R --output .
```

Final validation from the repository root:

```powershell
python courses/data-visualization/checkpoints/03-decision-story-capstone/validate_checkpoint.py final-capstone
```

### Reference environment

- Python 3 standard library for validation;
- PowerShell 7 or Windows PowerShell for assembly;
- R 4.6.1 for the tested render;
- ggplot2 4.0.3; and
- Windows as the first clean-run platform.

### Analysis output contract

The editable analysis regenerates only:

- `figure-primary.png`;
- `figure-supporting.png`; and
- `accessible-table.csv`.

It does not overwrite:

- learner prose;
- source records;
- review records;
- defense answers; or
- the defense PDF.

### Reproducibility record

The 350-to-1,200-word record includes:

- clean checkout or isolated folder;
- repository URL and full commit;
- operating system;
- software and package versions;
- exact commands;
- three input checksums;
- output names, dimensions, and row counts;
- visual inspection;
- accessibility inspection;
- validator result;
- tester and date; and
- pass or fail.

### Clean-run meaning

A clean run starts from:

- a fresh repository checkout or isolated copied package;
- no existing target files;
- no hidden source extract;
- no manually edited output;
- the documented dependencies only; and
- the packaged data or a reproducibly retrieved approved source.

### Safe assembler rule

The assembler refuses a nonempty target. It may not overwrite a learner's work. Reassembly uses a new folder.

## 11. Accessibility and equivalent communication

### Accessibility is a pass gate

Accessibility is not optional polish. A capstone without equivalent access does not pass even if the statistical interpretation is correct.

### Figure requirements

Both figures must:

- remain understandable without color alone;
- use sufficient contrast;
- preserve direct labels or keyed redundant cues;
- expose units and time;
- avoid clipped or overlapping text;
- preserve a logical reading order;
- work at the required export size; and
- avoid encoding status only by saturation or hue.

### PNG requirements

Each figure must:

- be a valid PNG;
- be at least 1,000 pixels wide;
- be at least 600 pixels high;
- contain substantive rendered content; and
- differ from the other figure.

### Exact table requirements

The CSV is the exact-value path. It must:

- use a header;
- preserve the 20-field schema;
- preserve the three selected measure rows;
- retain status and footnote fields;
- retain periods and release date;
- retain samples and peer context;
- retain threshold origin;
- retain action and interpretation limits; and
- open without a proprietary tool.

### Text alternative requirements

The 300-to-900-word `alt-text.md` must state for both figures:

- audience;
- decision;
- figure structure;
- source population;
- finding;
- key exact values;
- missingness, uncertainty, or freshness;
- threshold origin;
- action request;
- owner;
- material limitation; and
- unsupported conclusion.

It must preserve 23 percent, 53 reporting peers, the 590-day lag, and the definition and current-data review action.

### Defense PDF requirements

The PDF must:

- contain at least one valid page;
- have readable text and contrast;
- use a logical slide and reading order;
- include alternative text or equivalent speaker text for meaningful visuals;
- identify source and time boundaries;
- avoid color-only references during delivery; and
- remain understandable when reviewed without the live presentation.

The structural validator checks the PDF signature and page marker. The accessibility reviewer checks tags, reading order, contrast, text equivalence, and delivery.

### Remaining-barrier rule

The learner states remaining access barriers. A truthful bounded barrier may be repairable. An omitted known barrier is an integrity problem.

## 12. Clinical, ethical, equity, privacy, and AI boundaries

### Clinical relevance review

The clinical or domain reviewer confirms:

- the audience and authority are plausible;
- the decision question matters;
- the measure definition is not misrepresented;
- the action is operationally coherent;
- the evidence gap before intervention is named; and
- the story does not overstate clinical meaning.

### Ethics and equity review

The release must not:

- stigmatize a facility, clinician, patient group, or community;
- treat modeled or aggregate differences as individual traits;
- imply a subgroup disparity without subgroup evidence;
- erase missing or unavailable values;
- use ranking language as moral judgment;
- shift accountability to patients without evidence;
- recommend enforcement or resource removal from descriptive data; or
- hide who bears the cost of the requested next step.

### Privacy boundary

The public final folder contains only:

- approved open data;
- approved synthetic data;
- learner-created analysis and documentation; and
- review records without student or patient identifiers beyond what the program approves.

Real patient records, restricted partner files, access tokens, private URLs, and local identifiers trigger `refer`.

### AI accountability

AI may assist with:

- code drafting;
- prose drafting;
- transformation explanations;
- chart alternatives;
- alt-text drafting;
- slide organization; or
- defense rehearsal.

The learner remains responsible for:

- every number;
- every definition;
- every URL and right;
- every claim;
- every annotation;
- every accessibility assertion;
- every unsupported-conclusion boundary; and
- every oral answer.

### AI automatic-return conditions

Return the package when:

- material assistance is undisclosed;
- the learner cannot explain submitted work;
- generated values are not checked against the exact table;
- generated definitions are not checked against source documentation;
- a generated citation or URL is unverified;
- generated alt text does not match the figure; or
- a generated recommendation exceeds the evidence.

## 13. Oral defense contract

### Format

The defense contains:

- an accessible presentation no longer than eight minutes; and
- a question period of approximately seven minutes.

The instructor may adapt delivery for approved accommodations without changing the assessed competency.

### Required presentation sequence

1. audience and decision;
2. source and population;
3. finding;
4. primary figure;
5. supporting question;
6. audience adaptation;
7. material limitation;
8. requested action; and
9. reproducibility, accessibility, and AI verification.

### Required written responses

The 600-to-1,500-word written response answers:

1. What decision does this release support?
2. Why is the 23-percent OP-22 value not a current performance rating?
3. What do the 3-percent median and 10-percent trigger mean?
4. What changed across the two audiences, and what could not change?
5. Why is the supporting figure necessary?
6. How can another analyst reproduce and audit the release?
7. How does the release provide equivalent access?
8. How was AI assistance checked?
9. What evidence would be needed before an intervention decision?
10. What is the strongest remaining limitation?

### Defense pass standard

The learner passes when they can:

- explain the source without reading the source record verbatim;
- define OP_22 and the selected population;
- distinguish median, benchmark, and mock trigger;
- explain the 590-day lag;
- trace a figure value to the exact table and source;
- explain why the audiences receive different detail;
- name every stable invariant;
- state the requested action and owner;
- name evidence required before intervention;
- explain the reproduction commands;
- explain accessibility choices; and
- take responsibility for AI-assisted work.

### Defense failure examples

The defense does not pass when the learner:

- calls the 23-percent value current;
- calls the 10-percent trigger a CMS threshold;
- calls the 3-percent median a target or benchmark;
- attributes the signal to staffing or crowding;
- cannot explain the denominator or sample;
- cannot trace a value to the table;
- cannot explain the analysis;
- cannot state what changed across audiences;
- cannot explain the text alternative;
- cannot identify a material limitation; or
- delegates responsibility to an AI tool.

## 14. Review workflow and disposition record

### Review sequence

1. Learner resolves Checkpoint 2 conditions.
2. Learner assembles or creates the final folder.
3. Learner completes all records and exports the defense PDF.
4. Learner runs the analysis from packaged data.
5. Learner completes a clean reproduction check.
6. Learner runs the folder validator.
7. Faculty reviews source, interpretation, and rubric evidence.
8. Domain reviewer checks clinical or operational relevance.
9. Accessibility reviewer checks figures, table, text, PDF, and delivery.
10. Reproducibility reviewer checks inputs, commands, outputs, and fingerprints.
11. Learner completes the oral defense.
12. Instructor records score, pass results, conditions, and disposition.
13. Learner closes any release condition.
14. The approved folder becomes course evidence.

### Review-disposition fields

`review-disposition.md` contains:

- `reviewer`;
- `reviewer_role`;
- `review_date` in `YYYY-MM-DD`;
- `official_half_term_end_date` in `YYYY-MM-DD`;
- numeric `score`;
- `defense_result`;
- `clinical_review`;
- `accessibility_review`;
- `reproducibility_review`; and
- `disposition`.

### Passing field values

For release:

- score is at least 80;
- defense result is `pass`;
- clinical review is `pass`;
- accessibility review is `pass`;
- reproducibility review is `pass`; and
- disposition is `approve` or `approve with conditions`.

### Condition contract

Every condition states:

- the defect or uncertainty;
- why it matters;
- owner;
- due date;
- allowed release status before closure;
- exact closure evidence; and
- person who confirms closure.

An open condition may not contradict a pass gate. Privacy, rights, evidence integrity, inaccessibility, irreproducibility, failed defense, or unsupported action cannot be deferred as a minor condition.

### Reviewer independence

Reviewers disclose material involvement in the work. A person who authored a major portion of the analysis may provide feedback but should not be the only reproducibility or final reviewer.

## 15. Rubric, pass gates, and return conditions

### Rubric

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Audience, authority, and decision | 10 | Two named audiences, realistic authority, and one stable decision. |
| Finding and claim integrity | 15 | Observation, comparison, interpretation, recommendation, and action remain supported and separate. |
| Primary and supporting figures | 15 | The primary carries the decision and the supporting view answers a different necessary question. |
| Audience adaptation | 10 | Adaptable elements change while source, values, definitions, limits, and action remain stable. |
| Annotation and narrative | 10 | Titles and annotations guide attention without causal, freshness, ranking, or threshold distortion. |
| Reproducibility and provenance | 10 | Editable analysis, packaged data, source record, transformation record, and clean-run evidence are complete. |
| Accessibility | 10 | Non-color cues, exact table, equivalent text, readable PDF, and accessible delivery are complete. |
| Clinical, ethical, and equity boundary | 10 | No causal, current, stigmatizing, subgroup, privacy, or unauthorized-action claim. |
| Critique response and AI record | 5 | The repair and AI verification are specific, complete, and evidence-backed. |
| Oral defense | 5 | The learner accurately answers source, method, limit, access, and action questions. |
| Total | 100 |  |

### Score rule

Minimum released score: 80 of 100.

### Pass gates

All are required:

- approved open or synthetic source;
- two named audiences;
- one stable decision;
- one primary figure;
- one distinct supporting figure;
- exact accessible table;
- equivalent text alternative;
- full source record;
- full transformation record;
- full audience-adaptation record;
- clean reproduction;
- material limitation;
- bounded action;
- complete AI record;
- completed critique repair;
- accessible PDF;
- completed oral defense;
- clinical review pass;
- accessibility review pass;
- reproducibility review pass; and
- final approved disposition.

### Automatic return without grading

Return the package when:

- source values differ between audience versions;
- the title claims cause without a causal design;
- a historical value is labeled current;
- a scenario trigger is called official;
- a descriptive peer median is called a benchmark;
- a reporting window, sample, denominator, missingness state, or material limit is hidden;
- the requested action exceeds the evidence;
- the supporting figure repeats the primary question;
- the exact table or text alternative is missing;
- the source or transformation record is incomplete;
- the figures cannot be regenerated;
- the three input fingerprints do not match the release;
- AI-assisted values or definitions are not verified;
- the learner cannot explain submitted code or prose;
- the oral defense is missing; or
- restricted data appear in the public package.

### Revision loop

A revision records:

1. returned requirement;
2. reviewer evidence;
3. learner repair;
4. files changed;
5. invariant check;
6. rerun evidence;
7. new review result; and
8. final disposition.

## 16. Validator, technical QA, and release evidence

### Validator scope

`validate_checkpoint.py` checks:

- required Markdown files and headings;
- absence of unfinished drafting markers;
- document word-count contracts;
- stable evidence language in the brief, alt text, and adaptation record;
- three exact data filenames;
- exact data row and column counts;
- three SHA-256 fingerprints;
- exact 20-field table schema;
- exact three-row measure set;
- required OP_18b and OP_22 values;
- trigger origin and historical-use fields;
- two valid, distinct, sufficiently large PNG files;
- exactly one approved editable analysis source;
- source-record URLs, paths, counts, and fingerprints;
- a nonempty PDF with a page marker;
- required review fields and date forms;
- minimum score and passing review results;
- approved final disposition; and
- reproduction fingerprints and passing result.

### Validator boundary

The validator does not replace human review of:

- clinical relevance;
- causal language that evades simple text checks;
- whether two figures truly answer different questions;
- visual hierarchy;
- color contrast across the complete export;
- PDF tags and reading order;
- ethical or equity implications;
- whether an action is feasible; or
- the learner's oral understanding.

### Validator self-check

Run:

```powershell
python courses/data-visualization/checkpoints/03-decision-story-capstone/validate_checkpoint.py --self-check
```

The self-check:

1. creates a complete temporary fixture;
2. uses the exact released source files;
3. writes a valid three-row table;
4. creates two distinct valid PNG fixtures;
5. creates a minimal PDF fixture;
6. creates complete learner and review records;
7. confirms zero errors; and
8. removes the supporting figure and confirms rejection.

### Assembler QA

The released assembler must:

- run from a clean checkout;
- refuse a nonempty target;
- copy all three exact CSV files;
- copy learner templates and editable analysis;
- create the exact directory tree;
- render both figures;
- write the exact three-row table;
- leave the defense PDF absent;
- leave learner and reviewer instructions visibly incomplete; and
- print the next action.

### Starter expectation

The assembled starter intentionally fails final validation because:

- learner records contain unfinished instructions;
- the defense PDF does not exist;
- defense answers are incomplete;
- clean-run evidence is incomplete;
- review results are incomplete; and
- no final disposition is recorded.

A starter that passes would be a defect because it would confuse generated reference evidence with completed learner performance.

### Repository QA

Before Commons release:

- release JSON parses;
- R analysis completes;
- validator self-check passes;
- full assembler regenerates expected artifacts;
- incomplete starter is rejected;
- nonempty target is protected;
- JavaScript syntax passes;
- curriculum checker passes;
- `git diff --check` passes;
- no local absolute path appears in public files;
- no Unicode em dash or en dash appears in the checkpoint contract;
- no temporary output or bytecode directory is committed; and
- required human reviews remain visibly pending until performed.

### Acceptance facts

- Checkpoint version: 0.1.0.
- Commons release: 0.26.0.
- Required top-level files: 13.
- Required directories: 3.
- Required data files: 3.
- Data rows: 186, 3, and 186.
- Figures: 2.
- Exact table rows: 3.
- Exact table columns: 20.
- Defense PDF: 1.
- Written defense questions: 10.
- Minimum score: 80.
- Stable supported action: definition and current-data review.
- Maximum reference source lag: 590 days.

## 17. Release, handoff, and curriculum reuse

### Release status

Version 0.1.0 is a runnable release candidate in Commons 0.26.0.

### Technical release evidence

The release is ready when:

- validator self-check passes;
- assembler creates the reference starter;
- the analysis renders two visually inspected figures;
- the exact table matches the Module 12 source;
- starter validation fails for the expected completion reasons;
- overwrite protection passes; and
- the curriculum checker recognizes all three DA-730 checkpoints.

### Required human roles

Before alpha promotion, record named reviews for:

- DA-730 faculty;
- emergency-department quality relevance;
- CMS source fidelity;
- executive communication;
- visualization and information design;
- accessibility;
- equity and action language; and
- independent teachability and reproduction.

### Version policy

- Patch: wording, typo, or noncontractual template correction.
- Minor: compatible validation, scaffold, source, audience, or review expansion.
- Major: incompatible source, outcome, folder, scoring, defense, or release-gate change.

### Upstream source change

A new source release requires:

- new source URL and release date;
- new complete-source fingerprint;
- new packaged-table fingerprints;
- new row and column expectations;
- new selected facts;
- regenerated figures and exact table;
- updated brief and adaptation contract;
- updated validator expectations;
- new visual and accessibility inspection;
- version changes; and
- human review.

### Handoff to foundation courses

The approved capstone can become evidence in FND-1 and FND-2 only if the following travel with it:

- source record;
- exact data or reproducible retrieval;
- transformation record;
- editable analysis;
- exact table;
- accessibility path;
- AI-use record;
- material limits; and
- action boundary.

FND-1 may use it for source, table, programming, and provenance work. FND-2 may use it for inference, uncertainty, model checking, and reproducibility work. The foundations remain separate straight-through technical courses rather than pieces embedded inside DA-730.

### Handoff to applied courses

APP-1 through APP-7 may reuse the visualization habits, but each applied course must:

- own a distinct clinical or health-system decision;
- revisit statistics and mathematics in its own way;
- use domain-appropriate public or synthetic data;
- embed its machine-learning extension inside the course;
- define different Week 3, Week 6, and final deliverables; and
- end with clinician-led leadership work.

The DA-730 clinical finding does not automatically become the applied-course finding.

### Handoff to capstones

CAP-0 may reuse the package as evidence of proposal feasibility. CAP-1 may reuse it as a communication component inside a larger learning-health-system project. Both capstones must preserve the source, limits, access path, and decision boundary.

### Archive contents

The course archive retains:

- submitted folder;
- validator output;
- rubric score;
- oral-defense result;
- review disposition;
- condition closure when applicable;
- release version;
- repository commit; and
- approved public-release location.

Do not archive restricted review notes or identifiers in the public Commons.

### Final boundary

DA-730 ends when the learner can make one decision story truthful, exact, reproducible, accessible, audience-specific, and defensible. The next curriculum builds do not repeat this course. They carry these practices into separate technical foundations, distinct applied domains, and the capstones.
