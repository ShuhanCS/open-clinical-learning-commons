# APP-3 Module 03 build plan

## Objective

Build the 16.5-hour APP-3 Module 03 package, `Variation, safety signals, and bottlenecks`, from the accepted Module 02 release. The module must support one bounded process diagnosis and one human escalation rule without turning a chart signal into cause, a staffing recommendation, or clinical action.

## Fixed upstream contract

- Upstream module: `oclc-app3-02` version `0.1.0`.
- Commons input release: `0.67.0`.
- Service: fictional `CGH-ED-01` adult emergency service.
- Accepted encounters: 43,628.
- Completed encounters: 39,975.
- Left before seen: 3,653.
- Valid event sequences: 43,627.
- Module 02 query checks: 30 of 30 pass.
- Module 02 score: 20 of 20 with 15 of 15 gates.
- Module 03 permission: permitted for curriculum construction.

Module 03 will freeze the exact Module 02 contract, source manifest, safety source, encounter output, shift output, weekly output, safety diagnostics, subgroup support, query checks, build report, measure specifications, event validation, progression decision, and release record.

## Predeclared analytic contract

### Baseline and evaluation

- Baseline: Weeks 1 through 24.
- Evaluation: Weeks 25 through 52.
- The baseline is declared before signal calculation.
- Module 02 denominators, clocks, repair rules, and unavailable states cannot be changed.

### Chart families

1. Weekly mean of shift medians for arrival-to-clinician time: XmR chart.
2. Weekly left-before-seen proportion: p-chart with week-specific binomial limits.
3. Weekly incident reports per 1,000 completed encounters: u-chart with exact Poisson count limits because counts are low and exposure varies.
4. Weekly arrivals: run chart with a baseline median and no control limits because calendar and seasonal structure remains for Module 04.

### Signal rules

- R1: one point outside the declared control limits.
- R2: eight consecutive points strictly above or below the centerline.
- R3: six consecutive strictly increasing or decreasing points.

A signal opens review. It does not prove cause. Known truth is disclosed only after the independent signal and bottleneck review.

### Process comparison

The process-stage comparison uses four predeclared groups:

1. baseline evening shifts, Weeks 1 through 24;
2. target evening shifts, Weeks 35 through 44;
3. contemporaneous day and night shifts, Weeks 35 through 44; and
4. recovery evening shifts, Weeks 45 through 52.

It reports arrival-to-triage, triage-to-roomed, roomed-to-clinician, clinician-to-disposition, and disposition-to-departure support, median, and mean. Reconciliation also uses queue, throughput per clinician hour, clinician staff-hours per arrival, overtime, left-before-seen, and recovery evidence.

### Bounded diagnosis

The expected reference diagnosis is limited to the fictional release: evening shifts in Weeks 35 through 44 contain a roomed-to-clinician constraint. The reference must show a median increase from 49 to 66 minutes, contemporaneous shift evidence, queue and throughput evidence, and recovery to 49 minutes in Weeks 45 through 52. Staffing data are descriptive and do not establish cause or authorize a staffing change.

### Safety surveillance

Safety evidence keeps generated truth, triggers, incident reports, reviewed non-events, error, near miss, adverse event, and harm separate. The release must report 894 known true events, 673 trigger true positives, 358 incident true positives, 379 trigger false positives, 75.2796 percent trigger sensitivity, 40.0447 percent incident capture, and 99.0302 percent trigger specificity.

### Support and escalation

Full-release subgroup support remains visible. Narrow target-window support is recalculated and cannot borrow the full-release threshold. Unsupported comparisons remain unavailable.

The escalation rule sends a signal to human clinical-performance and safety review. It cannot automate staffing, scheduling, routing, care, or implementation.

## Deterministic evidence outputs

`build_diagnostic.py` will write:

1. `variation-series.csv`;
2. `control-limits.csv`;
3. `signal-audit.csv`;
4. `weekly-safety.csv`;
5. `safety-surveillance.csv`;
6. `process-stage-comparison.csv`;
7. `bottleneck-reconciliation.csv`;
8. `subgroup-window-support.csv`;
9. `diagnostic-findings.json`;
10. `weekly-arrival-to-clinician-xmr.svg`;
11. `weekly-left-before-seen-p-chart.svg`;
12. `weekly-incident-report-u-chart.svg`; and
13. `process-stage-comparison.svg`.

The builder will use the Python standard library, produce stable bytes, reject nonempty targets, and verify a committed release against a clean rebuild.

## Learner and reference records

- four editable Python/SQL-free analysis contracts are not needed because Module 02 owns source construction;
- `process-map.csv`;
- `chart-selection.csv`;
- `signal-rules.csv`;
- `performance-diagnostic.md`;
- `safety-interpretation.md`;
- `bottleneck-interpretation.md`;
- `subgroup-support-interpretation.md`;
- `escalation-rule.md`;
- `week3-score.csv`;
- `gate-results.csv`;
- `ai-use.md`;
- `progression-decision.md`; and
- `reproducibility-check.md`.

The package will also include a base-R verification script for learners to read and run. Python remains the release validator because R is not installed in the construction environment.

## Assessment and progression

- Module 03 component: 20 points across five 4-point criteria.
- Week 3 total: Module 02 20 points plus Module 03 20 points equals 40 points.
- Module 01 remains a required zero-point gate.
- Planned noncompensable gates: 18.
- Reference progression: `continue with conditions`.
- Next permission: Week 3 checkpoint construction.
- Next durable unit: `checkpoints/01-measures-variation-readiness`.

## Validation routes

The validator will check complete and starter modes, rebuild evidence, compare every accepted output, and reject at least:

1. changed Module 02 evidence;
2. missing upstream evidence;
3. changed baseline;
4. wrong chart family;
5. changed control limit;
6. missing low-count handling;
7. signal-as-cause language;
8. staffing recommendation;
9. unsupported subgroup claim;
10. changed diagnosis;
11. invalid score or failed gate;
12. invalid progression;
13. missing record; and
14. incomplete starter submitted as complete.

## Version decision

- Module version: `0.1.0`.
- Commons release: `0.67.0` to `0.68.0` because this adds a complete runnable module and the Week 3 diagnostic handoff.

## Definition of done

- 21-section durable specification exists.
- Exact upstream identities reproduce.
- All 13 analytic outputs reproduce byte for byte.
- Reference and starter workspaces validate.
- Twenty points and 18 gates reconcile.
- Week 3 handoff is explicit and does not double count Module 01.
- Root course records, ledger, checker, and semver are updated.
- Repository-wide curriculum checks pass.
- Task files are committed and pushed on `feat/roadmap-course-catalog`.
