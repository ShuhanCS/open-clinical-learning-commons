# APP-3 Week 6 checkpoint build plan

## Goal and release boundary

Build `oclc-app3-cp02`, the cumulative forecast, scenario, evaluation, and monitoring release, as a deterministic checkpoint package at version `0.1.0` and Commons release `0.73.0`.

The checkpoint is due at the end of instructional Week 6. It carries the accepted Module 05 score of 25 points exactly once. Module 04 and Module 06 are required zero-point gates. The checkpoint may permit Module 07 clinician leadership and defense with conditions. It may not select a failed scenario, accept the ML challenger, claim safety or causal effect, authorize staffing, start a test, route a patient, implement a workflow, or deploy a model.

## Accepted component identities

The assembler must build and freeze complete reference workspaces from:

| Component | Version | Commons | Files | Nested manifest rows | Nested manifest bytes | Nested manifest SHA-256 | Points |
|---|---|---|---:|---:|---:|---|---:|
| `oclc-app3-04` | 0.1.0 | 0.70.0 | 59 | 46 | 5,946 | `e462b470ba6aefa83c50bfdbcc21f8ca3be11dcf8e47ef9c377b820b42571f12` | 0 |
| `oclc-app3-05` | 0.1.0 | 0.71.0 | 68 | 53 | 6,773 | `2c6cddb2d59ba3e5d3eb67023c68756f9c2cd50144ba7e699fcf1cde8bfc4104` | 25 |
| `oclc-app3-06` | 0.1.0 | 0.72.0 | 82 | 64 | 8,672 | `7f81c00961f783c81e3f2b9d77b3a82b7e2d422860efb19e27ae55eb50b9ef85` | 0 |

The candidate contains 209 immutable component files. Each candidate row records the checkpoint-relative path, bytes, SHA-256, source module, source version, and role. The assembler must reject an existing destination and reproduce the same candidate manifest across learner and reference builds.

## Point and gate contract

The exact point map is:

- Module 04 forecast and capacity: 0 points;
- Module 05 scenario and evaluation: 25 points once;
- Module 06 feasibility, monitoring, and embedded ML: 0 points;
- cumulative Week 6 total: 25 of 25.

Inherited gates remain required:

- Module 04: 18 of 18;
- Module 05: 20 of 20;
- Module 06: 22 of 22; and
- checkpoint integrity: 20 of 20.

No point can compensate for a failed inherited or checkpoint gate.

## Accepted forecast evidence

The checkpoint must retain:

- target: accepted arrivals per eight-hour shift;
- issue time: end of the final shift in each completed week;
- horizon: 21 shifts over 7 days;
- folds: F01 through F28;
- common evaluation rows: 588 per method;
- accepted method: seasonal exponential smoothing;
- accepted MAE: 5.937283 arrivals per shift;
- accepted RMSE: 7.307180 arrivals per shift;
- accepted bias: 0.008215 arrivals per shift;
- accepted WAPE: 15.141268 percent;
- Week 53 point: 876.924084 arrivals;
- lower planning value: 805.136639 arrivals;
- upper planning value: 970.733035 arrivals;
- Little's Law equilibrium: not established; and
- staffing recommendation: not authorized.

The accepted difficult folds and failure evidence remain visible.

## Accepted scenario and evaluation evidence

The checkpoint must retain:

- four scenarios S00 through S03;
- five conditions C01 through C05;
- 4,000 paired simulation runs;
- 20 scenario-condition summaries;
- 15 paired option effects;
- six null or failed comparisons;
- no selected option;
- S01 point-demand P90 improvement 21.244986 minutes with a failed median rule;
- S02 point-demand median worsening 5.803341 minutes and P90 worsening 41.617987 minutes;
- S02 stress median worsening 86.671644 minutes;
- S03 point-demand median improvement 0.316383 minutes and P90 improvement 14.547388 minutes, both below their rules;
- 12 prospective evaluation measures;
- eight evaluation threats;
- safety and 72-hour return not simulated;
- simulation not causal; and
- implementation not authorized.

The 25-point score and all 20 Module 05 gates are copied without recalculation.

## Accepted feasibility and monitoring evidence

The checkpoint must retain:

- 28 scenario-domain feasibility screens;
- five supported, 18 requires-local-evidence, and five not-supported rows;
- S00 retained as monitoring baseline;
- S01 revised before reconsideration;
- S02 stopped in current form;
- S03 revised before reconsideration;
- 12 monitoring measures;
- nine simulated or modeled planning values;
- three prospectively unavailable values;
- ten escalation and fallback rules;
- zero automatic actions;
- continued no-change monitoring as fallback;
- a static accessible dashboard; and
- human ownership and restart conditions.

All thresholds remain draft planning rules rather than control limits, safe staffing values, clinical orders, or automatic actions.

## Accepted ML evidence

The checkpoint must retain:

- one fixed `GradientBoostingRegressor`;
- random state 7300600;
- no tuning;
- issue-time calendar, shift, lag, and complete-week features only;
- training-fold-only categorical preprocessing;
- 12 passing leakage and environment tests;
- 588 challenger rows identical to the transparent rows;
- challenger MAE 5.205494;
- challenger RMSE 6.554934;
- challenger bias -0.513059;
- challenger WAPE 13.275060 percent;
- challenger weighted-cost improvement 9.403087 percent;
- all four difficult folds passing the no-worse rule;
- Week 53 challenger total 860.277096 inside the accepted range;
- MAE improvement 0.731788 against a required 0.750000;
- seven of eight replacement rules passing; and
- final decision: retain transparent forecast.

The failed MAE rule cannot be rounded away, weakened, or repaired through retuning.

## Checkpoint work records

Reference and learner packages contain nine checkpoint records:

1. `README.md`;
2. `evidence-index.csv`;
3. `forecast-scenario-monitoring-review.md`;
4. `checkpoint-gates.csv`;
5. `checkpoint-defense.md`;
6. `reproducibility-check.md`;
7. `ai-use.md`;
8. `progression-decision.md`; and
9. `module07-handoff.md`.

The reference is complete. The learner version has explicit placeholders in every work record. Neither version edits candidate files.

## Integrated review contract

The cumulative review must answer:

1. What demand is forecast and when is it issued?
2. Which method remains accepted and why?
3. What uncertainty and failure evidence limit capacity use?
4. Did any scenario qualify?
5. Which scenario results failed or traded off?
6. What remains unmodeled or prospectively unavailable?
7. What is each scenario's feasibility disposition?
8. Which measures, owners, cadence, and escalation rules support monitoring?
9. What does the dashboard permit and prohibit?
10. Did the ML challenger use comparable rows and information?
11. Which replacement rule failed?
12. What changes, if anything, for Module 07?

The supported answer is that the evidence package is complete enough for clinician leadership review, but no scenario, staffing action, test, implementation, or ML replacement is authorized.

## Checkpoint integrity gates

1. exact 209-file candidate identity;
2. Module 04 release, 18 gates, and zero points retained;
3. Module 05 release, 20 gates, and 25 points retained;
4. Module 06 release, 22 gates, and zero points retained;
5. 25 points counted once;
6. exact target, issue time, folds, horizon, and 588 rows;
7. accepted transparent method and errors retained;
8. Week 53 point, range, Little's Law, and staffing limits retained;
9. no-selection scenario decision retained;
10. all failed scenario and sensitivity evidence retained;
11. safety, return, causal, and implementation limits retained;
12. all four feasibility dispositions retained;
13. 12 measures and three unavailable states retained;
14. accessible static dashboard and exact table retained;
15. ten human-owned escalation rules and no automatic action retained;
16. comparable fixed ML contract and 12 leakage checks retained;
17. failed R01 and transparent-method decision retained;
18. failure cases, difficult periods, and feature-importance limit retained;
19. defense, AI, reproducibility, and ownership records complete; and
20. progression and Module 07 handoff preserve all authority limits.

## Defense contract

The reference defense contains 14 ordered questions. Every question includes an answer, exact evidence, a decision consequence, and a limit. The questions cover target and issue time, temporal evaluation, accepted errors, capacity limit, scenarios, failed evidence, feasibility, prospective measures, escalation, dashboard, ML comparability, failed rule, points and gates, and Module 07 authority.

## Progression and Module 07 handoff

Allowed progression values are `continue`, `continue with conditions`, `revise`, and `refer`.

The supported reference is `continue with conditions`. Module 07 clinician leadership and defense are permitted only when:

- the 209 candidate files verify;
- the total remains 25 points once;
- all 18, 20, 22, and 20 gates pass;
- no scenario is selected;
- the transparent forecast remains accepted;
- the failed R01 rule remains visible;
- all prospective gaps remain visible; and
- clinical, staffing, testing, automated, implementation, and deployment authority remain absent.

## Deterministic assembly and validation

The package contains:

- seven immutable checkpoint control files;
- nine work records;
- one 209-row candidate manifest; and
- 209 candidate artifacts.

The exact assembled file count is 226.

The validator must check file sets, candidate path and hash identity, nested module manifests, releases, scores, gates, exact analytic evidence, no-selection status, dispositions, monitoring, dashboard, ML row comparability, failed R01, point accounting, defense, AI, progression, and authority limits. It must run from a copied package.

The self-check must assemble two reference packages and one learner package, prove byte-identical candidate manifests, validate reference and learner packages, run the copied validator, reject an existing target, and reject at least 20 changed, missing, duplicated, incomplete, unsafe, or invalid routes.

## Integration and release steps

1. Write the 17-section checkpoint specification.
2. Build checkpoint controls and learner/reference records.
3. Assemble the 209-file candidate and freeze its exact manifest identity.
4. Run builder and validator self-checks.
5. Update the release record with measured counts and manifest identity.
6. Advance Commons from 0.72.0 to 0.73.0.
7. Update the APP-3 course, root catalog, build ledger, and curriculum checker.
8. Run the checkpoint, APP-3, and remaining curriculum checks.
9. Commit, push, and verify the remote branch.

After Checkpoint 02, build Module 07 clinician leadership and defense.
