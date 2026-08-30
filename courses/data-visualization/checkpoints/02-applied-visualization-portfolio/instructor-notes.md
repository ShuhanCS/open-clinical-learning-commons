# Checkpoint 2 instructor notes

## Teaching purpose

Checkpoint 2 decides whether a learner is ready to enter the final DA-730 capstone. It tests the evidence chain from decision through source, definition, analysis, display, exact table, accessible alternative, and action boundary.

The portfolio uses six different public or synthetic cases. The learner must connect them as evidence of readiness without combining their populations into one clinical claim.

## Review decision

The review panel records one disposition:

- `approve`;
- `approve with conditions`;
- `revise`; or
- `refer`.

Approval means the learner has passed every checkpoint gate and has a feasible Module 13 proposal. It does not mean that the proposed analysis or clinical action has been approved for real-world implementation.

## Instructor preparation

1. Run the checkpoint validator self-check.
2. Assemble a starter portfolio into a new temporary folder.
3. Confirm all six PNG files.
4. Confirm all six evidence-table row counts.
5. Confirm all six accessible alternatives.
6. Open all six source records.
7. Run the validator against the incomplete starter and confirm that learner instructions and word counts prevent a false pass.
8. Review the full checkpoint specification.
9. Prepare one example of an approved capstone proposal and one example that requires narrowing.
10. Confirm the official Week 6 due date for the current half-term.

## Reference assembly command

From the repository root:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File courses/data-visualization/checkpoints/02-applied-visualization-portfolio/assemble_checkpoint.ps1 -Target checkpoint-2
```

If needed:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File courses/data-visualization/checkpoints/02-applied-visualization-portfolio/assemble_checkpoint.ps1 -Target checkpoint-2 -RscriptPath "C:\Path\To\Rscript.exe"
```

## Technical answer key

| Artifact | Starting module output | Exact table | Released rows |
|---|---|---|---:|
| Accessible display | `01-color-plus-shape.png` | `accessible_hf_readmission_table.csv` | 65 |
| Time display | `05-exploratory-control-chart.png` | `weekly_time_decision_table.csv` | 94 |
| Comparison display | `01-all-counties-ordered-small-multiples.png` | `comparison_decision_table.csv` | 500 |
| Place display | `03-bivariate-screen-map.png` | `place_decision_table.csv` | 100 |
| Structure display | `01-defined-cohort-flow.png` | `transition-path-decision-table.csv` | 7 |
| Dashboard | `01-minimum-ed-public-reporting-dashboard.png` | `dashboard-decision-table.csv` | 3 |

## Evidence-chain key

### Accessible display

The released view preserves all 65 Massachusetts heart-failure readmission rows and uses color plus shape and direct source status. Too-few and unavailable states remain in the exact table.

Passing interpretation:

- the display does not rely on color alone;
- a contrast calculation is evidence, not complete certification;
- point order is not a league table; and
- source status and intervals constrain the comparison.

### Time display

The released view uses 94 consecutive Massachusetts CDC NHSN weeks. The first 26 weeks form a declared exploratory baseline.

Reference values:

- center: 85.23 percent;
- lower exploratory limit: 80.72 percent; and
- upper exploratory limit: 89.75 percent.

Passing interpretation states that outside-limit weeks are review signals. Changing reporting coverage, reporting hospital mix, aggregate composition, and seasonality weaken formal process assumptions.

### Comparison display

The released view contains 500 rows: 100 North Carolina counties by five measures.

Reference facts:

- 54 counties are above the national age-adjusted point estimate on all five selected measures;
- 9 are at or below it on all five; and
- the profile count is a transparent teaching screen, not a validated score.

Passing interpretation distinguishes model-based small-area estimates from observed diagnoses or direct county survey estimates.

### Place display

The released view uses 100 county rows, 1,546 selected HRSA HPSA component rows, and 7,121 generalized boundary points.

Reference facts:

- 73 counties are above the 17.0-percent national health point;
- 23 meet the declared score-20 HPSA screen; and
- 19 meet both conditions.

Passing interpretation does not call the maximum component score touching a county a county workforce rate. It states what county aggregation hides and keeps a non-map exact-value path.

### Structure display

The released view contains a 374-person adult synthetic acute-transition cohort.

Reference facts:

- 314 emergency index events;
- 60 inpatient index events;
- 374 people conserved at every stage;
- 7 exact path rows; and
- a selected `Inpatient -> No encounter recorded` definition-audit path.

Passing interpretation states that `No encounter recorded` means no qualifying encounter appears in the selected extract and interval. The synthetic case does not estimate real quality, access, utilization, mortality, or readmission.

### Dashboard

The released dashboard contains five views and a three-row exact table for EDV, OP_18b, and OP_22.

Reference facts:

- selected OP-22: 23 percent;
- Massachusetts OP-22 median: 3 percent;
- mock OP-22 review trigger: 10 percent, crossed;
- OP-22 source lag at release: 590 days;
- selected OP_18b: 188 minutes;
- Massachusetts OP_18b median: 211.5 minutes;
- mock OP_18b review trigger: 240 minutes, not crossed; and
- OP_18b source lag at release: 317 days.

Passing interpretation says the state medians are descriptive, the triggers are course assumptions rather than CMS thresholds, and the immediate action is definition validation and current local data.

## Portfolio-index review

Each of the six rows must name:

- one reader;
- one decision or task;
- one source population;
- one finding;
- one supported action; and
- one material limit.

Return the portfolio if the same clinical finding is stretched across all six cases.

## View-purpose audit review

Every artifact needs a unique purpose. Require revision when two rows differ only by chart name.

The dashboard sub-audit must preserve five distinct functions:

1. alert;
2. freshness;
3. OP-22 peer position;
4. OP-18b peer position; and
5. ordered action.

The learner also names one view removed or revised.

## Critique review

The critique must identify a likely reader error and repair the decision contract.

Strong repairs commonly:

- restore an original unit;
- restore a reporting window;
- restore unavailable values;
- add a non-color cue;
- keep comparison scales fixed;
- define a denominator;
- prove flow conservation;
- remove a decorative dashboard view; or
- narrow an unsupported action.

A font, color, or software change alone does not pass.

## Accessibility review

Check all six artifacts for:

- contrast;
- grayscale survival;
- redundant cues;
- direct units;
- readable labels;
- stable reading order;
- exact tables;
- complete accessible alternatives;
- non-hover access; and
- remaining barriers.

Open each accessible alternative beside its figure and exact table. Confirm that the finding, key values, missingness or freshness boundary, and action are equivalent.

## Decision-brief review

The brief must contain 600 to 1,000 words and cite all six artifacts.

The requested decision must be one of:

- approve;
- approve with conditions; or
- revise.

The brief names the strongest remaining weakness. A learner does not need a flawless portfolio to request conditional approval, but every noncompensable gate must pass.

## Capstone-proposal review

The proposal must contain 700 to 1,200 words and define:

- decision owner;
- decision question;
- approved open or synthetic source;
- access rights;
- population;
- unit;
- time window;
- measures and denominators;
- planned analysis;
- primary and supporting displays;
- exact table;
- accessible alternative;
- reproducibility path;
- ethics and equity boundary;
- expected limitation;
- exact deliverables;
- review date; and
- approval request.

### Approve

Use when the source is available, the decision is bounded, the analysis is feasible, and every checkpoint gate passes.

### Approve with conditions

Use when the checkpoint gates pass but one proposal detail needs a named resolution, such as a final source release, measure definition, clinical reviewer, or narrowed subgroup.

### Revise

Use when the proposal remains too broad, exploratory, inaccessible, underdefined, or dependent on unavailable data.

### Refer

Use when the package contains or proposes unapproved patient data, restricted partner data, a rights concern, an integrity concern, or a safety issue that needs program review.

## AI-use review

The record must connect each generated artifact to human verification.

Require evidence that:

- numbers were checked against exact tables;
- definitions were checked against dictionaries or source records;
- URLs were verified;
- figures were visually inspected;
- accessible alternatives were compared with the figures; and
- threshold origins and owners were confirmed.

Do not accept a generic statement that AI output was reviewed.

## Automatic return conditions

Return without scoring when:

- a required artifact is missing;
- an analysis cannot regenerate its evidence chain;
- a source record is incomplete;
- an exact table is missing;
- an accessible alternative is missing;
- a display relies on color alone;
- the time display claims formal special cause without support;
- the place display calls a component score a county workforce rate;
- the flow does not conserve 374 people;
- the dashboard calls a course trigger a CMS threshold;
- a public dashboard value is labeled current;
- a source population is combined into another case;
- the capstone depends on unapproved patient data; or
- the AI-use record omits verification.

## Review record

Record:

| Field | Entry |
|---|---|
| Learner |  |
| Instructor |  |
| Clinical or domain reviewer |  |
| Validator result |  |
| Score |  |
| Gate result |  |
| Disposition |  |
| Conditions |  |
| Condition owner |  |
| Due date |  |
| Module 13 approval |  |

Do not place student identifiers in the public Commons release record.

## Human review before alpha

The checkpoint package still requires named review for:

- DA-730 faculty;
- clinical or health-system relevance;
- public-source fidelity;
- visualization and information design;
- accessibility;
- equity and action language; and
- independent teachability.

## Module 13 handoff

An approved proposal becomes the Module 13 input contract. Measure definitions, source values, uncertainty, rights, accessibility, and action boundaries remain stable unless a recorded review decision changes them.
