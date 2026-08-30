# Final checkpoint instructor notes

## Teaching purpose

The final checkpoint decides whether a learner can release and defend the complete DA-730 competency. It is one stable evidence chain, not a collection of unrelated charts.

The reference case asks a hospital quality committee to authorize an emergency department quality director to conduct a definition and current-data review. The evidence is historical public CMS reporting. It does not authorize an intervention.

## Calendar rule

Use the official last day of the learner's assigned half-term.

Official calendar:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

The curriculum uses 7.5 weeks as a planning model. The 2026-2027 half-terms span 49 to 52 elapsed days. Record the real end date in the learning-management system and `review-disposition.md`.

## Final review decision

Record one disposition:

- `approve`;
- `approve with conditions`;
- `revise`; or
- `refer`.

Only `approve` and `approve with conditions` can become released course evidence. An open condition cannot defer a privacy, rights, evidence-integrity, accessibility, reproducibility, or failed-defense gate.

## Instructor preparation

1. Read the full final checkpoint specification.
2. Confirm the official half-term end date.
3. Review the learner's Checkpoint 2 disposition and conditions.
4. Run the final validator self-check.
5. Assemble a reference starter into a new temporary folder.
6. Confirm both figures and the exact table.
7. Confirm all three packaged data fingerprints.
8. Run the analysis inside the assembled folder.
9. Confirm the starter fails because learner and review work is incomplete.
10. Test the nonempty-target refusal.
11. Prepare faculty, domain, accessibility, and reproducibility reviewers.
12. Schedule an eight-minute presentation and approximately seven-minute question period.

## Reference commands

From the repository root:

```powershell
python courses/data-visualization/checkpoints/03-decision-story-capstone/validate_checkpoint.py --self-check
```

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File courses/data-visualization/checkpoints/03-decision-story-capstone/assemble_checkpoint.ps1 -Target final-capstone
```

Inside the assembled folder:

```powershell
Rscript analysis/analysis.R --output .
```

From the repository root after completion:

```powershell
python courses/data-visualization/checkpoints/03-decision-story-capstone/validate_checkpoint.py final-capstone
```

## Reference outputs

| Artifact | Expected result |
|---|---|
| `figure-primary.png` | Executive three-card story for the hospital quality committee. |
| `figure-supporting.png` | Technical OP-22 peer-position story for the emergency department quality director. |
| `accessible-table.csv` | Three selected-facility rows and 20 exact fields. |
| `data/ma_ed_public_reporting_dashboard_2026.csv` | 186 rows, 31 columns. |
| `data/ed_dashboard_measure_dictionary_2026.csv` | 3 rows, 18 columns. |
| `data/cms_ma_ed_dashboard_source_2026.csv` | 186 rows, 15 columns. |

## Technical answer key

### Source

- Publisher: Centers for Medicare & Medicaid Services.
- Dataset: Timely and Effective Care - Hospital.
- Dataset ID: `yv7e-xc69`.
- CMS release: August 13, 2026.
- Reference facility: Anna Jaques Hospital, CMS ID 220029.

### Exact source fingerprints

| File | SHA-256 |
|---|---|
| Teaching table | `fbfcfcaf10d87cd48236a702622781f559d86d52b8773ca578d72313a9b270fd` |
| Measure dictionary | `2db834a350c0fee342efb30fc4b028053e325b3b357cc1031a11f7c9e9b29412` |
| Source selection | `f28f5d56e5e0e29001c7a275b01306762e673c9a21459dc7a68ff1aea782943b` |

### Selected EDV

- category: Low;
- period: January 1 through December 31, 2024;
- release date: August 13, 2026;
- source lag: 590 days; and
- use: public volume context, not a performance result.

### Selected OP_18b

- value: 188 minutes;
- sample: 422;
- period: October 1, 2024 through September 30, 2025;
- Massachusetts reported count: 54;
- descriptive state median: 211.5 minutes;
- mock trigger: 240 minutes;
- trigger crossed: no;
- source lag: 317 days; and
- immediate action: validate current local throughput definition and recent encounter-level time data before intervention.

### Selected OP_22

- value: 23 percent;
- source sample: 19,211;
- period: January 1 through December 31, 2024;
- Massachusetts reported count: 53;
- descriptive state median: 3 percent;
- unfavorable order: first;
- mock trigger: 10 percent;
- trigger crossed: yes;
- source lag: 590 days; and
- immediate action: validate numerator, denominator, exclusions, source completeness, and current local data.

### Threshold boundary

The 10-percent and 240-minute values are mock QI charter triggers created for teaching. They are not CMS thresholds, targets, or benchmarks.

### Stable supported action

Authorize a local definition and current-data review. Require current local OP-22 and emergency-department time evidence at the next review.

### Stable unsupported conclusions

The reference does not support:

- a current hospital rating;
- causal attribution;
- a staffing conclusion;
- a care-delivery change;
- a subgroup statement;
- an intervention choice; or
- an intervention-effect claim.

## Primary figure review

The executive figure should make three items immediately visible:

1. public signal: 23-percent OP-22;
2. time boundary: 590-day lag; and
3. decision request: authorize review.

Check that it also names:

- the hospital quality committee;
- 53 reporting hospitals;
- the emergency department quality director;
- current local OP-22 and ED-time return evidence;
- the non-CMS trigger boundary; and
- the no-current, no-cause, no-intervention boundary.

Return the figure if urgency design overwhelms the freshness boundary or if the card structure makes the course trigger look official.

## Supporting figure review

The technical figure should:

- preserve all 53 reported OP-22 peers;
- show the selected 23-percent point directly;
- mark the 3-percent descriptive state median;
- mark the 10-percent mock trigger;
- label the trigger as non-CMS;
- show the period and release lag;
- state the validation action; and
- avoid a causal or current-performance title.

The supporting figure passes because it answers the trace-and-validate question. It is not merely a detailed copy of the executive card view.

## Exact-table review

Confirm:

- exactly 20 columns;
- exactly three rows;
- one EDV row;
- one OP_18b row;
- one OP_22 row;
- original units;
- samples and status;
- periods and release date;
- lag fields;
- peer counts and medians;
- scenario triggers;
- threshold origin;
- monitoring-use label; and
- action-if-crossed text.

Do not accept a manually retyped summary table if the analysis can write the exact source-derived table.

## Decision-brief review

The brief contains 600 to 900 words and uses all required headings.

A passing brief:

- names audience authority;
- states one historical finding;
- preserves 23 percent, 53 peers, and 590 days;
- distinguishes the descriptive median from the mock trigger;
- requests definition and current-data review;
- names the owner and next review evidence;
- states the material limitation; and
- excludes current, causal, and intervention claims.

Return a brief that turns a request to validate into a request to intervene.

## Transformation-record review

Every material step appears in code or the transformation record. Check:

- Massachusetts and measure selection;
- selected facility;
- reported-value peer filter;
- unavailable-state handling;
- numeric parsing;
- peer ordering;
- median and trigger use;
- source-lag calculation;
- title and annotation choices;
- audience adaptations;
- manual inspection; and
- export settings.

No key value should exist only because it was typed into a chart editor.

## Audience-adaptation review

The learner must distinguish:

- executive authorization task; and
- technical trace-and-validate task.

The record must show that both versions preserve:

- source;
- facility;
- values;
- units;
- samples;
- dates;
- lags;
- peer references;
- trigger origin;
- material limitation;
- supported action; and
- unsupported conclusions.

Return the work if the executive version quietly removes the historical boundary or if the technical version introduces a different action.

## Accessibility review

Inspect both figures beside the exact table and alt text.

Confirm:

- non-color cues;
- direct values;
- readable labels;
- contrast;
- logical reading order;
- unit and time visibility;
- exact-value access;
- equivalent text;
- accessible PDF structure;
- no color-only references during delivery; and
- remaining barriers are stated.

The structural validator cannot certify PDF tags or the full visual hierarchy. Record the human result.

## Critique-response review

Strong responses repair one of these failures:

- overstated causality;
- hidden freshness;
- annotation misdirection;
- threshold-origin ambiguity;
- missing exact-value access;
- inaccessible color dependence;
- duplicated figure purpose; or
- action beyond evidence.

The learner must show that values and definitions stayed stable during the repair.

## AI-use review

Connect each retained generated artifact to a human check.

Require evidence that:

- numbers were checked against the exact table;
- definitions were checked against source documentation;
- URLs and rights were verified;
- titles and annotations were checked against the claim ladder;
- cross-audience invariants were checked;
- accessibility was checked by a person;
- the learner made the final decisions; and
- the learner accepts responsibility.

If no AI was used, the learner still records manual verification.

## Defense questions and answer boundaries

### 1. Supported decision

Passing answer: authorize the emergency department quality director to validate definitions and review current local data, then return to the quality committee.

### 2. Historical rather than current

Passing answer: the OP-22 period is calendar 2024, CMS released the file in August 2026, and the lag is 590 days. Public aggregate reporting does not describe current operations.

### 3. Median and trigger

Passing answer: 3 percent is a descriptive Massachusetts median among reporting hospitals. Ten percent is a mock course trigger. Neither is an official CMS benchmark.

### 4. Audience adaptation

Passing answer: evidence density, order, terminology, and annotation changed. Source, values, definitions, time, limits, and action did not.

### 5. Supporting figure

Passing answer: the executive view supports authorization. The technical view shows peer position and what needs validation.

### 6. Reproduction

Passing answer: identify packaged data, hashes, editable analysis, commands, expected figures and table, clean run, and validator.

### 7. Equivalent access

Passing answer: describe non-color cues, direct labels, exact CSV, text alternative, accessible PDF, reading order, and remaining barriers.

### 8. AI checks

Passing answer: connect material assistance to number, definition, source, claim, accessibility, and human-responsibility checks.

### 9. Evidence before intervention

Passing answer: current local numerator and denominator definitions, source completeness, monthly OP-22 and ED-time data, appropriate clinical and operational context, and a review design.

### 10. Strongest limitation

Passing answer: the historical public aggregate source cannot establish current conditions or cause. The bounded validation action remains appropriate.

## Scoring

Use the 100-point rubric in the checkpoint specification.

Minimum release score: 80.

The following cannot be compensated by points elsewhere:

- restricted data;
- changed or unverifiable values;
- causal or current-performance inflation;
- official-threshold mislabeling;
- inaccessible evidence;
- irreproducible evidence;
- undisclosed material AI use;
- action beyond authority; or
- failed defense.

## Disposition guidance

### Approve

Use when every gate passes, the score is at least 80, the defense passes, and no material condition remains.

### Approve with conditions

Use when every noncompensable gate passes and one bounded condition has:

- owner;
- due date;
- closure evidence; and
- closure reviewer.

### Revise

Use when a recoverable source, figure, table, prose, access, reproduction, or defense problem remains.

### Refer

Use when the package contains or proposes:

- unapproved patient data;
- restricted partner data;
- unresolved rights;
- fabricated or materially altered evidence;
- a serious safety or professional-boundary concern; or
- another issue requiring program review.

## Common failure patterns

| Failure | Likely reader error | Required repair |
|---|---|---|
| "Our intervention caused improvement" | Committee infers causal evidence. | Restore descriptive design and name evidence needed for causality. |
| "Current OP-22 is 23%" | Reader treats 2024 public reporting as current. | Restore period, release, lag, and current-local-data requirement. |
| "CMS target is 10%" | Reader treats a course trigger as official. | Label mock origin in figure, table, brief, and defense. |
| Median called benchmark | Reader treats a descriptive peer statistic as a target. | Use descriptive median language. |
| Two similar figures | Reader receives no distinct supporting question. | Remove or redesign the supporting view. |
| Missing exact table | Reader cannot audit values. | Restore source-derived three-row CSV. |
| Color-only alert | Some readers cannot distinguish status. | Add direct labels, shape, text, and table path. |
| Hidden manual edit | Another analyst cannot reproduce the claim. | Move the change into editable analysis and document it. |
| Vague AI statement | Reviewer cannot trace generated work. | Link outputs to material prompts, revisions, and checks. |

## Recovery when validation fails

1. Read every validator issue.
2. Fix source or value issues before prose.
3. Regenerate figures and the table from editable analysis.
4. Update transformation and adaptation records.
5. Update text alternatives and decision brief.
6. Recheck PDF accessibility.
7. Rerun from a clean folder.
8. Run the validator again.
9. Record the repair in the critique or review record.
10. Repeat the affected human review.

Do not edit the validator or source fingerprints to make a changed result pass. A real source change requires a new release.

## Human review still required

The package is a runnable release candidate. It does not become alpha until named faculty, domain, source, executive, design, accessibility, equity, and independent-instructor reviewers record decisions and material findings are resolved.
