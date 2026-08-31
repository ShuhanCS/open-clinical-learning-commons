# APP-3 Checkpoint 02: Forecast, scenario, evaluation, and monitoring release

## 1. Checkpoint identity and place in the course

- Checkpoint ID: `oclc-app3-cp02`.
- Course: APP-3, Data for Clinical Performance and Improvement.
- Due point: end of instructional Week 6.
- Course points: 25.
- Point source: Module 05 25 points once.
- Module 04 points: 0.
- Module 06 points: 0.
- Checkpoint version: `0.1.0`.
- Commons release: `0.73.0`.
- Package: `courses/clinical-performance-improvement/checkpoints/02-forecast-scenario-monitoring-release/`.
- Decision: is the cumulative analytic case complete and bounded enough for Module 07 clinician leadership review?

The checkpoint freezes the accepted forecast, scenario, evaluation, feasibility, monitoring, dashboard, and embedded-ML releases. It does not recompute or improve them. Its job is to prove that the evidence chain remains intact, that the 25 points are counted once, that failed and unavailable evidence remains visible, and that leadership receives the exact decisions and limits produced by Modules 04 through 06.

Checkpoint acceptance does not authorize a scenario, staffing change, schedule change, clinical action, test, automated action, implementation, production scoring, or model deployment.

## 2. Decision, readers, and required answer

The primary readers are the APP-3 faculty owner, Joe Joseph, MD, the clinical performance council, a clinical and safety reviewer, an operations and workforce reviewer, a measurement and forecasting reviewer, an equity and accessibility reviewer, and an independent reproducer.

The checkpoint must answer:

1. what demand target and issue time were accepted;
2. how the transparent forecast performed and where it failed;
3. what capacity inference is and is not supported;
4. whether any scenario qualified;
5. which scenario effects failed, traded off, or remained unmodeled;
6. which option dispositions survived feasibility review;
7. what will be monitored, by whom, and how often;
8. which thresholds trigger investigation, pause review, clinical review, or an interpretability gate;
9. whether the dashboard is accessible and bounded;
10. whether the ML challenger used the same target rows and information;
11. which replacement rule failed;
12. how the 25 points and 80 required gates are counted; and
13. what Module 07 may and may not decide.

The supported reference answer is `continue with conditions`. The package is ready for clinician leadership review. No redesign qualified, the transparent forecast remains accepted, and implementation remains unauthorized.

## 3. Accepted Module 04 forecast and capacity package

The assembler creates the exact `oclc-app3-04` version `0.1.0` reference workspace from Commons `0.70.0`.

| Identity item | Accepted value |
|---|---:|
| Assembled files | 59 |
| Nested immutable rows | 46 |
| Nested manifest bytes | 5,946 |
| Nested manifest SHA-256 | `e462b470ba6aefa83c50bfdbcc21f8ca3be11dcf8e47ef9c377b820b42571f12` |
| Course points | 0 |
| Gates | 18 of 18 |

The checkpoint retains:

- accepted arrivals per eight-hour shift as the target;
- end of the final shift in each completed week as the issue time;
- 21 forecast shifts over 7 days;
- Weeks 1 through 24 as the initial training period;
- F01 through F28 and Weeks 25 through 52 for evaluation;
- 588 exact target shifts per method;
- last value, seasonal naive, and seasonal exponential smoothing comparisons;
- seasonal exponential smoothing as the accepted method;
- MAE 5.937283 arrivals per shift;
- RMSE 7.307180 arrivals per shift;
- bias 0.008215 arrivals per shift;
- WAPE 15.141268 percent;
- Week 53 point forecast 876.924084 arrivals;
- empirical actual-equivalent range 805.136639 to 970.733035 arrivals;
- accepted difficult folds and failure periods;
- Little's Law equilibrium not established;
- capacity values as planning implications only; and
- staffing recommendation not authorized.

The checkpoint may not change the target, folds, method, error record, uncertainty range, or capacity claim boundary.

## 4. Accepted Module 05 scenario and evaluation package

The assembler creates the exact `oclc-app3-05` version `0.1.0` reference workspace from Commons `0.71.0`.

| Identity item | Accepted value |
|---|---:|
| Assembled files | 68 |
| Nested immutable rows | 53 |
| Nested manifest bytes | 6,773 |
| Nested manifest SHA-256 | `2c6cddb2d59ba3e5d3eb67023c68756f9c2cd50144ba7e699fcf1cde8bfc4104` |
| Course points | 25 |
| Gates | 20 of 20 |

The checkpoint retains:

- S00 through S03;
- C01 through C05;
- 200 replications per scenario-condition cell;
- 4,000 paired runs;
- 20 scenario-condition summaries;
- 15 paired option effects;
- six null or failed option-condition comparisons;
- no option qualified for feasibility review;
- S01 P90 improvement 21.244986 minutes with median improvement only 1.958703 minutes;
- S02 median worsening 5.803341 minutes and P90 worsening 41.617987 minutes at point demand;
- S02 median worsening 86.671644 minutes under slower-service stress;
- S03 median improvement 0.316383 minutes and P90 improvement 14.547388 minutes at point demand;
- 12 prospective evaluation measures;
- eight evaluation threats;
- safety and 72-hour return not simulated;
- simulated flex hours separated from staffing recommendations;
- causal effect not established by simulation;
- Module 05 score 25 of 25 once; and
- implementation authority not authorized.

The checkpoint cannot select the least unfavorable option, drop a failed condition, lower a selection rule, or treat a simulation as observed intervention evidence.

## 5. Accepted Module 06 feasibility, monitoring, and ML package

The assembler creates the exact `oclc-app3-06` version `0.1.0` reference workspace from Commons `0.72.0`.

| Identity item | Accepted value |
|---|---:|
| Assembled files | 82 |
| Nested immutable rows | 64 |
| Nested manifest bytes | 8,672 |
| Nested manifest SHA-256 | `7f81c00961f783c81e3f2b9d77b3a82b7e2d422860efb19e27ae55eb50b9ef85` |
| Course points | 0 |
| Gates | 22 of 22 |

The checkpoint retains:

- 28 scenario-domain feasibility rows;
- five supported, 18 requires-local-evidence, and five not-supported rows;
- S00 retained as monitoring baseline;
- S01 revised before reconsideration;
- S02 stopped in current form;
- S03 revised before reconsideration;
- 12 owned monitoring measures;
- nine simulated or modeled planning values;
- three prospectively unavailable values;
- ten human-owned escalation and fallback rules;
- zero automatic actions;
- continued no-change monitoring as the fallback;
- one static accessible dashboard with an exact table;
- one fixed gradient-boosted challenger with seed 7300600 and no tuning;
- 588 common challenger rows;
- 12 passing leakage and environment tests;
- challenger MAE 5.205494;
- challenger RMSE 6.554934;
- challenger bias -0.513059;
- challenger WAPE 13.275060 percent;
- 9.403087 percent lower weighted error cost;
- four of four difficult folds passing their no-worse rule;
- Week 53 challenger total 860.277096;
- MAE improvement 0.731788 against the required 0.750000;
- seven of eight replacement rules passing; and
- final ML decision `retain transparent forecast`.

The failed MAE rule remains a failure. No rounding exception, post-hoc threshold, added model, or retuning is allowed inside the checkpoint.

## 6. Point architecture and no-double-counting rule

| Component | Accepted points | Checkpoint treatment |
|---|---:|---|
| Module 04 forecast and capacity | 0 | required gate, not scored |
| Module 05 scenarios and evaluation | 25 | counted once |
| Module 06 feasibility, monitoring, and ML | 0 | required gate, not scored |
| Checkpoint integrity | 0 | required gate, not scored |
| Cumulative Week 6 package | 25 | exact total |

The Module 05 score is copied, not rescored. Its criterion rows and total must remain exact. A duplicated Module 05 total, a new dashboard score, a new ML score, or points for a gate fail the release.

The 25-point checkpoint remains separate from the 40-point Week 3 checkpoint and the future 35-point final package. Course points remain `40 + 25 + 35 = 100`.

## 7. Cumulative evidence index and chain of custody

`evidence-index.csv` contains three ordered module rows with title, version, Commons release, assembled files, nested manifest rows, bytes, SHA-256, checkpoint points, gates, progression, accepted decision, and checkpoint role.

The assembler generates a 209-row `candidate-manifest.csv`. Each row contains:

- checkpoint-relative path;
- bytes;
- SHA-256;
- source module;
- source version; and
- role.

The accepted candidate manifest is 36,654 bytes with SHA-256 `4f2a303bc5626ea58139aa935da157f524db1d25b5a158a927ef5daec197958a`.

The candidate paths are under `candidate/module-04/`, `candidate/module-05/`, and `candidate/module-06/`. Paths are sorted, relative, portable, and free of traversal. Every nested module manifest must reproduce its own immutable files.

The learner and reference checkpoint packages use the same 209 candidate files and the same candidate manifest. Only the nine checkpoint work records differ.

## 8. Integrated forecast, scenario, and monitoring review

`forecast-scenario-monitoring-review.md` synthesizes the accepted packages without creating a new analytic result.

The forecast section names the target, issue time, horizon, folds, common rows, accepted method, error measures, Week 53 point and range, failure evidence, Little's Law status, and staffing limit.

The scenario section names the four scenarios, five conditions, 4,000 runs, no-selection result, six failed rows, point-demand tradeoffs, stress failure, prospective measures, threat count, and causal and safety limits.

The feasibility section names all four dispositions and the required return path for a revised option. It separates local evidence gaps from favorable evidence.

The monitoring section names the 12 measures, three unavailable states, ten escalation rules, zero automatic actions, fallback, owners, cadence, dashboard accessibility, and no-live-system boundary.

The ML section names row comparability, fixed features and model, leakage checks, errors, difficult folds, Week 53 result, all eight rules, failed R01, and the retained transparent method.

The review concludes that the package is complete for leadership interpretation while every action boundary remains in force.

## 9. Failure, unavailable, and uncertainty retention

The checkpoint must foreground evidence that could otherwise be lost during synthesis:

- difficult forecast folds;
- unsupported or limited error slices;
- empirical rather than probabilistic Week 53 range;
- Little's Law equilibrium not established;
- six null or failed scenario comparisons;
- S02 stress failure;
- S01 and S03 missed wait gates;
- safety outcome not simulated;
- return within 72 hours not simulated;
- workforce interruption and perceived-load baseline unavailable;
- implementation feasibility requiring local evidence;
- largest ML underforecasts and overforecasts;
- feature importance not causal;
- one failed ML replacement rule; and
- no fresh confirmation period for a future challenger.

Unavailable is never converted to zero, favorable, safe, or not applicable without evidence. A result may be interesting and still fail the declared decision rule.

## 10. Monitoring, dashboard, escalation, and ownership readiness

Checkpoint readiness requires all 12 measures to retain exact units, values or unavailable states, periods, denominators, directions, displays, thresholds, escalation responses, owners, cadence, and claim limits.

The static dashboard must retain:

- one visible planning-evidence banner;
- the fictional `CGH-ED-01` service label;
- one `h1` and logical headings;
- 12 exact measure cards;
- a complete exact table;
- text states in addition to color;
- narrow-screen support;
- no scripts, external fonts, or external assets;
- no live connection; and
- no automatic alerting.

The ten escalation rules retain a trigger, response level, confirmation owner, decision owner, safeguard, fallback, documentation location, restart condition, and zero automatic action. The fallback remains continued no-change monitoring. A future rollback rule requires a separately authorized test plan.

## 11. Noncompensable inherited and checkpoint gates

The checkpoint carries:

- 18 of 18 Module 04 gates;
- 20 of 20 Module 05 gates;
- 22 of 22 Module 06 gates; and
- 20 of 20 checkpoint integrity gates.

The checkpoint integrity gates cover:

1. exact 209-file candidate identity;
2. Module 04 release, gates, and zero points;
3. Module 05 release, gates, and 25 points;
4. Module 06 release, gates, and zero points;
5. 25 points counted once;
6. exact forecast target, cutoff, folds, horizon, and rows;
7. accepted transparent method and errors;
8. Week 53 range and capacity limits;
9. no-selection scenario result;
10. failed scenario evidence;
11. safety, return, causal, and implementation limits;
12. four scenario dispositions;
13. 12 measures and three unavailable states;
14. accessible static dashboard;
15. ten human-owned escalation rules;
16. comparable fixed ML and 12 leakage checks;
17. failed R01 and retained transparent method;
18. difficult periods and failure evidence;
19. complete defense, AI, reproduction, and ownership records; and
20. bounded progression and Module 07 handoff.

All 80 gates are required. A numeric score cannot compensate for a failed gate.

## 12. Learner records and defense contract

The checkpoint has nine work records:

1. `README.md`;
2. `evidence-index.csv`;
3. `forecast-scenario-monitoring-review.md`;
4. `checkpoint-gates.csv`;
5. `checkpoint-defense.md`;
6. `reproducibility-check.md`;
7. `ai-use.md`;
8. `progression-decision.md`; and
9. `module07-handoff.md`.

Every learner record has explicit placeholders and prompts. Every reference record is complete. Prose uses plain ASCII dashes and contains no personal absolute path.

The defense has 14 ordered questions. Every answer includes an exact answer, evidence path, decision consequence, and limit. Questions cover:

1. target and issue time;
2. temporal evaluation rows;
3. accepted error and uncertainty;
4. capacity and staffing boundary;
5. scenario selection;
6. failed scenario evidence;
7. feasibility dispositions;
8. prospective and unavailable measures;
9. monitoring and escalation;
10. dashboard accessibility and authority;
11. ML comparability and leakage;
12. failed replacement rule;
13. points and gates; and
14. Module 07 permission and absent authority.

## 13. Deterministic assembly contract

`build_checkpoint.py` imports the three accepted workspace builders and creates complete reference workspaces in a temporary directory. It checks each expected file count, then copies every file into the candidate tree while computing the outer manifest.

The package contains:

| File class | Count |
|---|---:|
| Immutable checkpoint controls | 7 |
| Checkpoint work records | 9 |
| Candidate manifest | 1 |
| Module 04 candidate files | 59 |
| Module 05 candidate files | 68 |
| Module 06 candidate files | 82 |
| Total assembled files | 226 |

The assembler refuses any existing destination. Two reference builds and one learner build must produce the same 209-row candidate manifest and candidate bytes. The reference contains no placeholder, while every learner record contains one.

## 14. Validation, copied execution, and mutation rejection

`validate_checkpoint.py` checks:

- exact file set and 226-file count;
- 209 sorted candidate rows;
- portable paths, bytes, SHA-256, module, version, and role;
- checkpoint identity and 0.73.0 Commons release;
- exact module file counts and releases;
- nested manifest identity and every nested immutable hash;
- evidence-index identity;
- exact 0, 25, 0 point map;
- all inherited and checkpoint gates;
- accepted forecast, range, scenario, evaluation, feasibility, monitoring, dashboard, and ML evidence;
- no-selection and transparent-method decisions;
- failed R01 retention;
- 14 complete defense questions;
- accountable AI record;
- complete reproduction record;
- allowed progression and Module 07 permission;
- no clinical, staffing, automated, testing, implementation, or deployment authority; and
- plain ASCII, portable records.

The validator runs from the repository and from an assembled copied package. It rejects candidate mutation, nested manifest mutation, missing candidate files, wrong point maps, duplicate points, failed inherited gates, changed forecast identity, forced scenario selection, hidden failures, invented safety, changed dispositions, unavailable-as-zero, inaccessible dashboard, changed ML rows, leakage failure, moved R01, accepted challenger, incomplete defense, unsupported authority, placeholder reference, and invalid progression.

Reference validation passes 1,102 checks and learner validation passes 1,061 checks. Copied validation passes, and 25 failure routes are rejected.

## 15. Common failure modes and instructor response

| Failure | Why it fails | Instructor response |
|---|---|---|
| Recompute a module inside the checkpoint | breaks accepted release identity | restore the exact candidate package |
| Score Module 04 or Module 06 | duplicates gate work as points | restore 0, 25, 0 point map |
| Select S01 because P90 improves | ignores the failed median rule | retain no selection and revise before reconsideration |
| Hide S02 stress behavior | removes material failure evidence | restore the 86.671644-minute worsening |
| Treat safety unavailable as no events | invents an outcome | restore prospective unavailable status |
| Turn a threshold into an automatic alert | exceeds the approved design | restore human review and zero automatic actions |
| Accept ML because most metrics improve | ignores conjunctive replacement rules | retain failed R01 and transparent method |
| Round 0.731788 to 0.75 | changes the decision after fitting | retain six-decimal comparison |
| Treat feature importance as cause | confuses model allocation with mechanism | restore the noncausal limit |
| Grant implementation in progression | checkpoint acceptance is not action authority | restore the separate governed decision |

The instructor rewards faithful synthesis, not a more favorable conclusion.

## 16. Progression contract and Module 07 handoff

Allowed progression values are `continue`, `continue with conditions`, `revise`, and `refer`.

The supported reference progression is `continue with conditions`. Module 07 is permitted for clinician leadership and defense when:

- all 209 candidate files verify;
- the checkpoint score is 25 of 25 once;
- Module 04 gates are 18 of 18;
- Module 05 gates are 20 of 20;
- Module 06 gates are 22 of 22;
- checkpoint gates are 20 of 20;
- the selected scenario remains none;
- the accepted forecast remains seasonal exponential smoothing;
- the ML decision remains retain transparent forecast;
- safety, access, workforce, and implementation gaps remain visible; and
- all action authority remains absent.

`module07-handoff.md` carries exact release identities, manifest identity, score, gates, forecast and scenario decisions, dispositions, monitoring and escalation facts, ML near miss, open conditions, and authority boundaries. Module 07 may interpret, communicate, assign ownership, recommend revision, or refer. It may not rewrite the candidate.

## 17. Release, review, and exit criteria

The checkpoint is a runnable release candidate when:

- the 17-section specification is complete;
- the builder and validator self-checks pass;
- two reference builds are identical;
- the learner package validates structurally;
- copied validation passes;
- 25 failure routes are rejected;
- the candidate manifest identity is recorded in the release, evidence index, reproduction record, ledger, and checker;
- Commons is advanced to 0.73.0;
- all catalog and course references identify Checkpoint 02 as complete;
- Git records one scoped commit; and
- the feature branch is pushed and remote-verified.

Human review remains required before alpha for the source releases, synthetic operational design, forecasting, scenario assumptions, feasibility dispositions, monitoring thresholds, dashboard accessibility, ML contract and result, safety and workforce language, Joe Joseph participation details, and independent reproduction.

The next durable unit is APP-3 Module 07, clinician leadership, recommendation, and defense.
