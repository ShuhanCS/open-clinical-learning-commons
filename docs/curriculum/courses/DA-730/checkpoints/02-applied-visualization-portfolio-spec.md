# DA-730 Checkpoint 2: applied visualization portfolio

- Checkpoint ID: DA-730-CP2
- Course: DA-730, Clinical data visualization and decision storytelling
- Due: end of instructional week 6
- Modules included: 07 through 12, with revisions from Checkpoint 1 when useful
- Checkpoint version: 0.1.0
- Commons release: 0.24.0
- Learner workload: included in the module hours for Modules 07 through 12
- Runnable package: `courses/data-visualization/checkpoints/02-applied-visualization-portfolio/`

## 1. Purpose and checkpoint decision

Checkpoint 2 tests whether a learner can move from individual visualization exercises to a governed, reproducible, accessible portfolio that is ready to support a final decision story.

The checkpoint joins six applied competencies:

1. accessible visual communication;
2. time and process variation;
3. aligned multi-group comparison;
4. place and geographic structure;
5. flow, composition, and hierarchy; and
6. dashboard and multi-view composition.

The submission is not six unrelated images placed in one folder. Every artifact must have a named reader task, a defensible visual structure, an exact-value fallback, a complete source record, an accessible alternative, and a decision boundary.

### Checkpoint decision owner

The decision owner is a DA-730 clinical analytics review panel consisting of the course instructor and at least one clinical, quality, research, patient, operational, public-health, or community reviewer appropriate to the learner's proposed capstone.

### Checkpoint decision

Decide whether the learner is ready to enter Module 13 with a feasible, sourced, reproducible, accessible, and decision-limited capstone proposal.

### Available dispositions

- `approve`: the portfolio passes every gate and the capstone proposal is feasible for Module 13;
- `approve with conditions`: the portfolio passes, but one named proposal detail must be resolved before final analysis;
- `revise`: one or more recoverable portfolio or proposal requirements are incomplete; or
- `refer`: a source, privacy, integrity, safety, or restricted-data concern needs program review.

### Supported action

The panel may approve a learner to begin the final capstone, require a bounded revision, narrow the proposed source or decision, or defer the proposal until a named evidence gap is resolved.

### Unsupported action

The checkpoint does not authorize a real clinical intervention, a hospital performance judgment, access to restricted patient records, or a claim that the six portfolio cases describe one population.

### Completion standard

Checkpoint 2 is complete when the folder contract validates, every figure can be regenerated, all six cases have exact tables and source records, accessibility is documented, the critique repairs a reader error, and the review panel records a disposition on a feasible capstone proposal.

## 2. Audience and portfolio argument

### Primary reader

The primary reader is the DA-730 clinical analytics review panel.

The learner may name a second reader who represents the intended capstone audience, such as:

- a clinical service leader;
- a quality director;
- a patient or family partner;
- a population-health program lead;
- a public-health partner;
- a research principal investigator;
- an operational leader;
- a community organization;
- a payer or value leader; or
- an executive sponsor.

### Portfolio question

The portfolio answers:

> Does this learner select, build, reproduce, explain, and limit clinical visual evidence well enough to complete the proposed final capstone responsibly?

### Portfolio argument

The learner must make one readiness argument using six distinct cases. The cases demonstrate transferable judgment, but their populations and findings remain separate.

The learner may not combine:

- CMS hospital readmission estimates;
- CDC jurisdiction-level respiratory reporting;
- CDC county model estimates;
- HRSA shortage-area components;
- Synthea patient pathways; and
- CMS emergency department public reporting

into one clinical or causal conclusion.

### Reader needs

The panel needs to see:

- why each display was selected;
- what task each display supports;
- how the source and population differ;
- whether the source values are preserved;
- whether units, denominators, time windows, and uncertainty are visible;
- whether the display works without color alone;
- whether exact values and text alternatives are available;
- whether the analysis is reproducible;
- whether AI assistance was verified;
- whether the learner can state an action boundary; and
- whether the proposed capstone can be completed with open or synthetic data.

## 3. Competencies assessed

| Module | Required portfolio evidence | Readiness claim |
|---|---|---|
| 07. Color and accessible visual communication | `accessible-display.png`, exact table, text alternative, and accessibility evidence | The learner communicates status without relying on color alone. |
| 08. Time and process variation | `time-display.png`, weekly table, and process-limit statement | The learner distinguishes chronology, smoothing, reporting context, and exploratory process signals. |
| 09. Comparison and small multiples | `comparison-display.png`, complete decision table, and fixed comparison rules | The learner compares many groups without changing scale, order, denominator, or reference meaning. |
| 10. Maps, geography, and place | `place-display.png`, all-county table, and aggregation statement | The learner uses geography only when place changes the decision and states what aggregation hides. |
| 11. Flow, networks, composition, and hierarchy | `structure-display.png`, exact path table, and conservation statement | The learner defines the unit, stages, denominators, and absence state before using a structural display. |
| 12. Dashboards and multi-view composition | `dashboard.png`, exact decision table, and view-purpose audit | The learner coordinates the minimum views needed for one owner, alert, freshness boundary, and action. |

### Integrated competencies

The checkpoint also assesses whether the learner can:

1. keep six source populations separate;
2. select one evidence type for each reader task;
3. preserve exact values outside the figure;
4. preserve source definitions and checksums;
5. provide equivalent text communication;
6. state what each artifact cannot support;
7. repair a display at the decision-contract level;
8. document AI assistance and verification;
9. propose a feasible final capstone; and
10. reproduce the entire package from a clean checkout.

## 4. Required folder contract

The default R path uses these exact names:

```text
checkpoint-2/
  README.md
  portfolio-index.md
  view-purpose-audit.md
  figures/
    accessible-display.png
    time-display.png
    comparison-display.png
    place-display.png
    structure-display.png
    dashboard.png
  analysis/
    accessible-display.R
    time-display.R
    comparison-display.R
    place-display.R
    structure-display.R
    dashboard.R
  evidence-tables/
    accessible-display.csv
    time-display.csv
    comparison-display.csv
    place-display.csv
    structure-display.csv
    dashboard.csv
  source-records/
    accessible-display-source.yml
    time-display-source.yml
    comparison-display-source.yml
    place-display-source.yml
    structure-display-source.yml
    dashboard-source.yml
  alt-text/
    accessible-display.md
    time-display.md
    comparison-display.md
    place-display.md
    structure-display.md
    dashboard.md
  critique-and-repair.md
  accessibility-report.md
  decision-brief.md
  capstone-proposal.md
  ai-use.md
```

### Alternative tools

An approved alternative tool may replace an `.R` file with `.py`, `.ipynb`, `.twb`, `.pbix`, `.ps1`, or another editable source file. The base name must stay the same.

For example, `dashboard.py` may replace `dashboard.R`. `final-dashboard.py` may not.

### Exact-name rule

Do not rename the six figures, tables, source records, or accessible alternatives. The validator connects each artifact by base name.

### No hidden dependencies

The folder may not depend on:

- a local patient spreadsheet;
- an uncommitted extract;
- a hidden Tableau extract;
- a manually edited final PNG;
- a private cloud notebook;
- restricted partner data;
- an undocumented package; or
- a file available only on the learner's computer.

## 5. Six-artifact evidence contract

### `accessible-display.png`

Starting evidence: Module 07 `01-color-plus-shape.png`.

Source: the released 65-row Massachusetts CMS heart-failure readmission teaching table.

Reader task: distinguish source reporting status and point estimates without relying on color alone.

Required evidence:

- direct status text;
- redundant shape, symbol, line, position, or pattern cues;
- readable foreground contrast;
- unavailable and too-few states retained;
- exact 65-row table;
- text alternative; and
- a statement that accessibility is more than a calculated contrast ratio.

Required limit: the source estimates do not justify a simple point-rank league table.

### `time-display.png`

Starting evidence: Module 08 `05-exploratory-control-chart.png`.

Source: the released 94-week Massachusetts CDC NHSN teaching series.

Reader task: identify weeks for review while preserving reporting coverage, seasonality, and exploratory process assumptions.

Required evidence:

- chronological order;
- time unit and period;
- raw values;
- declared baseline when process limits are used;
- reporting-coverage context;
- exact 94-row table;
- text alternative; and
- a statement that outside-limit weeks are review signals, not automatically formal special causes.

Required limit: the aggregate reporting hospital mix and coverage may change.

### `comparison-display.png`

Starting evidence: Module 09 `01-all-counties-ordered-small-multiples.png`.

Source: the released 500-row North Carolina CDC PLACES comparison table.

Reader task: compare five county health measures on stable scales and a shared order without inventing a composite score.

Required evidence:

- all 100 counties or a justified decision subset with the full table retained;
- five declared measures;
- fixed measure-specific scales;
- shared county order;
- national descriptive references;
- reported uncertainty fields retained in the table;
- exact 500-row table;
- text alternative; and
- a statement that the profile count is a transparent teaching screen, not a validated score.

Required limit: PLACES values are model-based small-area estimates, not observed county diagnoses or direct county survey estimates.

### `place-display.png`

Starting evidence: Module 10 `03-bivariate-screen-map.png`.

Sources: the released CDC PLACES, HRSA HPSA, and Census boundary teaching files.

Reader task: identify whether a place-based pattern changes which counties should be reviewed together.

Required evidence:

- map purpose;
- geographic unit;
- all-county exact table;
- declared screen conditions;
- direct explanation of the HPSA component score;
- non-map exact-value fallback;
- text alternative; and
- a statement of what county aggregation hides.

Required limit: the highest HPSA component score touching a county is not a county workforce rate or proof that the whole county is designated.

### `structure-display.png`

Starting evidence: Module 11 `01-defined-cohort-flow.png`.

Source: the released 374-person adult synthetic acute-transition cohort.

Reader task: audit a path definition while preserving cohort conservation, stage meaning, and absence language.

Required evidence:

- one declared unit;
- index cohort definition;
- mutually exclusive stage states;
- ribbon or path weight definition;
- 374 people at every stage;
- exact seven-row path table;
- text alternative; and
- a statement that `No encounter recorded` means no qualifying encounter appears in the selected extract and interval.

Required limit: the synthetic paths do not estimate real care quality, access, utilization, mortality, or readmission.

### `dashboard.png`

Starting evidence: Module 12 `01-minimum-ed-public-reporting-dashboard.png`.

Source: the released 186-row Massachusetts CMS emergency department public-reporting teaching table.

Reader task: decide whether a public OP-22 signal should open a local definition and current-data review.

Required evidence:

- one dominant alert;
- visible reporting periods and source lag;
- separate percent and minutes scales;
- descriptive peer references;
- mock trigger origin and owner;
- exact three-row decision table;
- ordered action path;
- text alternative; and
- a statement that the dashboard is historical public-reporting review, not real-time operations.

Required limit: the public value alone does not authorize an operational or clinical intervention.

### Revision rule

Learners may revise any starting figure. A revision must preserve source values, definitions, units, time windows, uncertainty, and interpretation boundaries. The matching analysis file must regenerate the submitted artifact and exact table.

## 6. Exact tables and source records

### Evidence-table row contract

| Table | Expected released rows | Minimum purpose |
|---|---:|---|
| `accessible-display.csv` | 65 | Preserve every Massachusetts status and exact source value used by the accessibility case. |
| `time-display.csv` | 94 | Preserve every consecutive Massachusetts week and reporting context field. |
| `comparison-display.csv` | 500 | Preserve 100 counties by five measures with crude, adjusted, uncertainty, and reference context. |
| `place-display.csv` | 100 | Preserve every North Carolina county and the map-to-non-map decision fields. |
| `structure-display.csv` | 7 | Preserve every released path and its exact denominator and percentage. |
| `dashboard.csv` | 3 | Preserve EDV, OP_18b, and OP_22 for the selected facility. |

The released starter must contain exactly these row counts. A learner revision may change a row count only when the portfolio index and source record explain why the source, cohort, or decision changed and the instructor approves the change.

### Source-record keys

Every source record contains these top-level keys:

```yaml
publisher: "..."
landing_page: "https://..."
retrieved_at: "YYYY-MM-DD"
released: "YYYY-MM-DD or source label"
data_path: "repository-relative path"
analysis_path: "analysis/accessible-display.R"
figure_path: "figures/accessible-display.png"
table_path: "evidence-tables/accessible-display.csv"
alt_text_path: "alt-text/accessible-display.md"
sha256: "64 lowercase hexadecimal characters"
transformations:
  - "..."
known_limits:
  - "..."
```

### Checksum meaning

The required `sha256` identifies the main released analytic input, not the rendered PNG. When an artifact joins multiple released files, the source record lists every additional path and checksum under descriptive keys.

### Public-source diversity

The six records must preserve at least four distinct approved public landing pages. The released starter uses CMS, CDC NHSN, CDC PLACES, HRSA, Census, and Synthea sources.

### Source update

If a learner changes a source, the learner must update:

- landing page;
- release date;
- data path;
- checksum;
- transformations;
- known limits;
- analysis path if needed;
- table;
- figure;
- text alternative; and
- portfolio explanation.

## 7. README and reproduction contract

The checkpoint README contains these exact headings:

- `# Checkpoint 2: applied visualization portfolio`
- `## Review decision`
- `## Portfolio findings`
- `## Reproduce this portfolio`
- `## Folder map`
- `## Known limits`

### Review decision

Name the review panel, requested disposition, any proposed condition, and the capstone decision being requested.

### Portfolio findings

Write one supported sentence for each artifact. The sentence must include the measure or structure, population or setting, time when relevant, and action boundary.

### Reproduce this portfolio

List:

- operating system;
- R or approved-tool version;
- package versions;
- repository commit;
- working directory;
- exact commands;
- expected figures;
- expected tables;
- expected accessible alternatives; and
- validation command.

A new user starting from a clean checkout must be able to regenerate the six artifacts without guessing paths.

### Folder map

Explain how each figure connects to its editable analysis, evidence table, source record, and accessible alternative.

### Known limits

State at least one decision-relevant limit for each source case. Do not use one generic limitations paragraph for all six.

## 8. Portfolio index and view-purpose audit

### `portfolio-index.md`

The index contains exactly one row per required artifact:

| Artifact | Module | Reader | Decision or task | Source population | Finding | Supported action | Material limit |
|---|---:|---|---|---|---|---|---|
| `accessible-display.png` | 07 | | | | | | |
| `time-display.png` | 08 | | | | | | |
| `comparison-display.png` | 09 | | | | | | |
| `place-display.png` | 10 | | | | | | |
| `structure-display.png` | 11 | | | | | | |
| `dashboard.png` | 12 | | | | | | |

The index keeps populations separate and makes the readiness argument visible.

### `view-purpose-audit.md`

The audit contains exactly one row per portfolio artifact:

| Artifact | Question answered | Unit and denominator | Time window | Visual structure | Exact-value fallback | Action enabled | Why another artifact cannot answer it |
|---|---|---|---|---|---|---|---|

### Dashboard sub-audit

The dashboard row also links to a five-view sub-audit containing:

| Dashboard view | Question answered | Measure | Unit | Window | Action enabled | Unique role |
|---|---|---|---|---|---|---|

### Selection standard

Every artifact must have a unique purpose. Phrases such as `shows the data`, `looks better`, or `for stakeholders` do not meet the standard.

### Removal evidence

The audit names at least one candidate view removed from the dashboard or one portfolio artifact revised because it did not serve the task.

## 9. Analysis and reproducible assembly

### Analysis requirements

Each editable analysis file must:

1. read a committed Commons release or documented approved source;
2. stop with a clear error when required input is missing;
3. preserve unavailable, suppressed, and absent states;
4. make transformations visible in code or call a released module lab explicitly;
5. write its matching PNG with the exact name;
6. write or copy its matching exact table;
7. write or copy its matching text alternative;
8. run without manual chart editing; and
9. exit nonzero when the released module lab fails.

### Default analysis wrappers

The released starter analysis files call the corresponding tested module lab, copy one selected figure, copy the exact table, and copy the reference accessible alternative.

The wrappers are a reproducible starting point. A learner who changes a figure may replace the wrapper with a complete approved analysis file.

### Assembly command

From the repository root:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File courses/data-visualization/checkpoints/02-applied-visualization-portfolio/assemble_checkpoint.ps1 -Target checkpoint-2
```

If `Rscript` is not on the command path:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File courses/data-visualization/checkpoints/02-applied-visualization-portfolio/assemble_checkpoint.ps1 -Target checkpoint-2 -RscriptPath "C:\Path\To\Rscript.exe"
```

### Safe target behavior

The assembler refuses to write into a nonempty target. It does not overwrite learner work.

### Assembly outputs

The assembler:

1. creates the exact folder tree;
2. copies eight learner writing templates;
3. copies six prefilled source records;
4. copies six tested analysis wrappers;
5. executes every wrapper;
6. creates six PNGs;
7. creates six exact CSV tables;
8. creates six accessible alternatives; and
9. prints the validation command.

### Completed-folder validation

```powershell
python courses/data-visualization/checkpoints/02-applied-visualization-portfolio/validate_checkpoint.py checkpoint-2
```

The validator checks structure. It does not replace instructor review of clinical meaning, source fit, decision logic, accessibility quality, or capstone feasibility.

## 10. Critique and repair

The learner selects one deliberately flawed display from Modules 07 through 12 or one instructor-approved public example.

`critique-and-repair.md` contains:

- `## Original display and reader task`
- `## Decision-contract failure`
- `## Evidence from Modules 07 through 12`
- `## Repair implemented`
- `## Verification`
- `## Remaining limit`

### Acceptable critique targets

- color-only status;
- low contrast;
- hidden reporting coverage;
- unsupported control limits;
- changing comparison scales;
- inconsistent group order;
- misleading choropleth classification;
- numerator-only map;
- changing flow denominator;
- node-link hairball;
- area-rate conflict;
- wall of KPIs;
- mixed units and windows; or
- decorative widgets.

### Required diagnosis

The critique identifies:

- intended reader;
- likely reader error;
- data or decision-contract failure;
- affected action;
- repair principle; and
- evidence that the repair works.

### Required repair

The repair must appear in one submitted artifact or in a clearly identified supporting comparison. The learner must state which analysis file regenerates it.

### Non-passing repairs

- changing only color;
- changing only font;
- adding decoration;
- hiding unavailable values;
- changing the source values;
- changing the denominator silently;
- removing source windows;
- converting a scenario threshold into an official target; or
- claiming certainty the source does not support.

## 11. Accessibility report and alternatives

`accessibility-report.md` contains:

- `## Scope and readers`
- `## Color and contrast`
- `## Redundant cues`
- `## Reading order and hierarchy`
- `## Exact tables and text alternatives`
- `## Interaction and export`
- `## Checks completed`
- `## Remaining barriers`

### Artifact-by-artifact record

For each of the six figures, the learner records:

- foreground and background check;
- grayscale result;
- non-color cues;
- unit and abbreviation check;
- reading order;
- label and annotation check;
- exact-table path;
- text-alternative path;
- resize or print check;
- interaction fallback when applicable; and
- remaining barrier.

### Text-alternative contract

Each Markdown alternative must state:

- reader and task;
- figure structure;
- source population;
- measure or state definitions;
- strongest supported finding;
- exact key values;
- uncertainty, missingness, or freshness boundary;
- supported action; and
- unsupported interpretation.

### Dashboard alternative

The dashboard alternative follows the five-view reading order and preserves the alert, freshness, peer positions, action sequence, mock-trigger boundary, and current-local-data requirement.

### No color-only meaning

Every status, threshold, selected point, path, and comparison group remains identifiable through text, shape, line type, position, symbol, or exact table.

### Interaction rule

Essential information cannot depend on hover. An interactive submission must also provide a stable PNG, exact table, keyboard path, and text alternative.

## 12. Decision brief and capstone proposal

### `decision-brief.md`

The brief contains:

- `## Review panel`
- `## Readiness finding`
- `## Evidence across the portfolio`
- `## Requested decision`
- `## Conditions or revisions`
- `## Material limitation`

The brief is 600 to 1,000 words.

It must:

- make one readiness argument;
- cite all six portfolio artifacts;
- keep source populations separate;
- name at least one material improvement since Checkpoint 1;
- identify the strongest remaining weakness;
- request `approve`, `approve with conditions`, or `revise`; and
- end with the next concrete action.

### `capstone-proposal.md`

The proposal contains:

- `## Working title`
- `## Decision owner and audience`
- `## Decision question`
- `## Source and rights`
- `## Population, unit, and time window`
- `## Measures and definitions`
- `## Planned analysis and displays`
- `## Accessibility plan`
- `## Reproducibility plan`
- `## Ethics, equity, and privacy`
- `## Expected limitation`
- `## Deliverables and review date`
- `## Approval requested`

The proposal is 700 to 1,200 words.

### Capstone feasibility requirements

The proposal must use:

- one or more approved open or synthetic sources;
- a source accessible without restricted patient records;
- a defined unit and population;
- a bounded time window;
- named measures and denominators;
- a realistic analysis for Module 13;
- an exact-value output;
- a text alternative;
- a reproducible source file; and
- a named reviewer.

### Proposal rejection conditions

The proposal cannot proceed when it:

- depends on unapproved patient data;
- lacks a source URL;
- lacks access rights;
- requires an unavailable extract;
- has no decision owner;
- asks only to explore the data;
- proposes an unsupported causal claim;
- hides a material subgroup or denominator;
- cannot be completed in Module 13;
- lacks an accessibility plan; or
- lacks a reproducibility path.

## 13. AI-use and source-integrity contract

`ai-use.md` contains:

- `## Tool and model`
- `## Work delegated`
- `## Prompts or instructions`
- `## Generated artifacts used`
- `## Number and definition verification`
- `## Accessibility verification`
- `## Human decisions`
- `## Final responsibility statement`

### If AI was not used

State that no generative AI was used and explain how code, values, definitions, prose, and accessibility were checked.

### If AI was used

Record:

- tool and model when known;
- date;
- task;
- prompt or instruction;
- generated code or prose used;
- revisions;
- exact values checked;
- definitions checked;
- source URLs checked;
- visual outputs inspected; and
- human decisions retained.

### Required verification

- Every number is checked against its exact evidence table.
- Every definition is checked against its source record and module dictionary.
- Every source URL is opened or verified from the released record.
- Every generated figure is visually inspected.
- Every accessible alternative is compared with the figure and table.
- Every threshold is checked for origin and ownership.

### Prohibited AI substitution

AI cannot replace:

- source-rights review;
- patient-data screening;
- checksum verification;
- measure-definition review;
- denominator verification;
- cohort conservation;
- clinical interpretation;
- accessibility testing;
- capstone feasibility review; or
- learner oral defense.

## 14. Validator and technical acceptance

### Structural checks

The validator checks:

- the exact folder tree;
- eight required Markdown records;
- required headings;
- unfinished placeholders;
- six PNG files;
- minimum PNG dimensions;
- minimum PNG file size;
- exactly one editable analysis source per base name;
- six evidence tables;
- released starter row counts;
- six source records;
- required source keys;
- full HTTPS landing pages;
- lowercase SHA-256 values;
- matching figure, table, analysis, and alt-text paths;
- at least four distinct landing pages;
- six text alternatives;
- decision-brief word count;
- capstone-proposal word count;
- all six artifacts in the portfolio index;
- all six artifacts in the view-purpose audit;
- all six artifacts in the accessibility report; and
- no obvious unfinished code marker.

### Self-check

```powershell
python courses/data-visualization/checkpoints/02-applied-visualization-portfolio/validate_checkpoint.py --self-check
```

The self-check creates a valid temporary fixture, confirms it passes, removes one required figure, and confirms the invalid fixture fails.

### Assembler acceptance

The assembler passes when it:

- refuses a nonempty target;
- resolves the intended repository;
- resolves Rscript;
- copies every template;
- runs six analysis wrappers;
- produces six nonempty PNG files;
- produces exact table row counts of 65, 94, 500, 100, 7, and 3;
- produces six nonempty accessible alternatives;
- leaves no temporary work directory; and
- prints the completion and validation instructions.

### Repository acceptance

- The 17-section specification exists.
- The package file contract exists.
- Release JSON parses.
- Curriculum checker passes.
- JavaScript syntax passes.
- `git diff --check` passes.
- No local absolute path appears in public records.
- No Unicode em dash or en dash appears in the checkpoint contract.
- No generated learner checkpoint folder is committed.
- No temporary output or bytecode directory is committed.

## 15. Rubric

| Criterion | Weight | Full-credit evidence |
|---|---:|---|
| Portfolio decision and selection | 15% | Six artifacts serve distinct tasks and support one readiness decision without joining their populations. |
| Applied visualization judgment | 20% | Time, comparison, place, structure, and dashboard forms preserve the correct units, denominators, windows, and decision boundaries. |
| Accessibility | 15% | Every artifact uses redundant cues, readable hierarchy, exact tables, complete text alternatives, and documented checks. |
| Reproducibility and provenance | 15% | Six editable analyses regenerate six figures and tables; all source records preserve URLs, releases, checksums, transformations, and limits. |
| Clinical and statistical interpretation | 15% | The learner distinguishes descriptive references, modeled values, source intervals, synthetic paths, mock triggers, and current-data needs. |
| Critique and repair | 10% | The learner identifies a reader error, repairs the decision contract, verifies the result, and names the remaining limit. |
| Capstone readiness and AI accountability | 10% | The proposal is feasible and bounded; AI assistance and human verification are complete. |
| Total | 100% |  |

### Passing score

Passing requires at least 80 percent overall and a pass on every noncompensable gate.

### Scoring principle

A polished image cannot compensate for an inaccessible display, missing source, broken reproduction path, hidden denominator, unsupported claim, or infeasible capstone proposal.

### Evidence weighting

Instructors grade the complete evidence chain:

```text
decision -> source -> definition -> analysis -> figure -> exact table -> accessible alternative -> action boundary
```

A defect early in the chain affects the interpretation of every later artifact.

## 16. Noncompensable pass gates

- All six PNG files open and meet minimum dimensions.
- Every figure has exactly one matching editable analysis file.
- Every figure has a matching evidence table.
- Every figure has a matching source record.
- Every figure has a matching accessible alternative.
- At least four distinct approved public landing pages are preserved.
- Missing, unavailable, and suppressed source values are not silently imputed.
- The accessibility artifact does not rely on color alone.
- The time artifact states the exploratory process-limit boundary and reporting-context limit.
- The comparison artifact keeps fixed scales, shared order, and source uncertainty.
- The place artifact does not call a component HPSA score a county workforce rate.
- The structure artifact conserves 374 synthetic people and defines `No encounter recorded` precisely.
- The dashboard labels its scenario triggers as non-CMS and its public values as historical.
- Percent and minutes do not share one numeric scale.
- Every source population remains separate in the portfolio argument.
- The critique repairs a likely reader error, not only appearance.
- The decision brief requests one review disposition.
- The capstone proposal uses approved open or synthetic data and is feasible for Module 13.
- The AI-use record documents number, definition, source, visual, and accessibility checks.
- The submission contains no real patient records or restricted partner data.

### Automatic return

Return the package without scoring when any gate above fails.

The instructor may allow a technical resubmission when the defect is a missing file or path. A source, privacy, integrity, or unsupported clinical claim requires review before resubmission.

## 17. Instructor review, release, and Module 13 handoff

### Instructor review order

1. Run the structural validator.
2. Confirm the six figures and exact tables.
3. Check the six source records and source populations.
4. Review the view-purpose audit.
5. Review the accessibility report and alternatives.
6. Review the critique and repair.
7. Read the decision brief.
8. Review capstone feasibility.
9. Review AI-use verification.
10. Record the disposition and conditions.

### Required review roles

Before the checkpoint package becomes alpha, record named review from:

- DA-730 faculty;
- clinical or health-system relevance;
- public-source fidelity;
- visualization and information design;
- accessibility;
- equity and action language; and
- independent teachability.

One person may cover more than one role, but each role needs an explicit decision.

### Release status

Checkpoint version 0.1.0 is a runnable release candidate in Commons 0.24.0.

### Alpha gate

The checkpoint cannot become alpha until named reviewers complete the required roles and material findings are resolved.

### Version policy

- Patch: wording, typo, or noncontractual correction.
- Minor: compatible template, validator, source, figure, rubric, or assembly change.
- Major: incompatible folder, competency, source, decision, scoring, or pass-gate change.

### Module 13 handoff

An approved learner enters Module 13 with:

- one approved decision owner;
- one approved capstone question;
- one approved open or synthetic source plan;
- a defined population, unit, and period;
- defined measures and denominators;
- a planned primary and supporting display;
- an exact-table plan;
- an accessible-alternative plan;
- a reproducibility plan;
- an ethics and equity boundary;
- a named reviewer;
- a requested final action; and
- any review conditions.

### Final boundary

Checkpoint 2 ends when applied visualization competence and capstone feasibility are demonstrated. Module 13 begins when the learner turns one approved evidence chain into a sourced, reproducible, accessible decision story for two audiences and the final half-term review.
