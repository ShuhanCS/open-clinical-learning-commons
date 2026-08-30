# APP-3 Checkpoint 01: Measures, variation, and bottleneck readiness

## 1. Checkpoint identity and place in the course

- Checkpoint ID: `oclc-app3-cp01`.
- Course: APP-3, Data for Clinical Performance and Improvement.
- Due point: end of instructional Week 3.
- Checkpoint version: 0.1.0.
- Commons release: 0.69.0.
- Accepted modules: APP-3 Modules 01, 02, and 03.
- Course points: 40.
- Point source: Module 02 contributes 20 points once and Module 03 contributes 20 points once.
- Required zero-point gate: Module 01.
- Decision: whether the accepted service definition, measure system, diagnostic evidence, and human escalation rule may enter Module 04 demand forecasting and capacity analysis.
- Package: `courses/clinical-performance-improvement/checkpoints/01-measures-variation-readiness/`.

This is the first cumulative APP-3 release gate. It is one evidence chain, not a folder containing three unrelated assignments. The checkpoint starts with a fictional service and public-source feasibility decision, follows the exact synthetic event and measure build, and ends with a bounded diagnostic and escalation rule. It freezes those decisions before forecasting begins.

The checkpoint does not recompute an upstream measure, repair a defect, change a baseline, redraw a limit, remove an inconvenient signal, or strengthen a claim. Any correction returns to its owning module, receives a new version, reproduces, and enters a rebuilt checkpoint.

## 2. Decision, readers, and required answer

The checkpoint asks:

> May the accepted `CGH-ED-01` service definition, source roles, measure system, variation and safety evidence, bounded bottleneck diagnosis, and human escalation rule enter demand forecasting and capacity analysis?

Primary readers are the `CGH-ED-01` clinical performance and improvement council, the APP-3 faculty owner, a clinical performance and quality reviewer, an emergency care clinician, a safety reviewer, an equity and access reviewer, a workforce reviewer, and the future Module 04 analyst.

The allowed disposition is `continue`, `continue with conditions`, `revise`, or `refer`. A continuing answer must name:

- the three accepted module identities;
- all 137 accepted candidate files;
- the 40-point source and no-double-counting rule;
- all 45 inherited gates and 18 checkpoint gates;
- the provisional baseline and nine signal records;
- the safety undercapture evidence;
- the bounded stage, shift, and time-window diagnosis;
- unsupported target-window subgroup comparisons;
- E01 ownership and human-only action;
- every unresolved condition; and
- exact Module 04 permission.

A continuing answer opens curriculum construction only. It does not establish a root cause or authorize staffing, scheduling, routing, clinical care, automation, implementation, or a prospective test.

## 3. Accepted Module 01 decision and source package

The checkpoint accepts Module 01 only as:

- module ID `oclc-app3-01`;
- version `0.1.0`;
- Commons release `0.66.0`;
- 25 assembled reference files;
- 14 immutable manifest rows;
- manifest size 1,741 bytes;
- manifest SHA-256 `ecd8400c5e972e7070d64770086d752a89fd8bc659a1c5c1345c612d0236605d`;
- 12 of 12 decision gates passing; and
- zero checkpoint points.

The accepted service is the explicitly fictional `CGH-ED-01` adult emergency service. One synthetic adult emergency encounter from recorded arrival through recorded departure is the unit of flow. The clinical performance and improvement council owns progression.

The public source evidence remains exactly:

| Source | Accepted identity | Rows | Role |
|---|---|---:|---|
| CMS timely and effective care | dataset `yv7e-xc69`, release 2026-08-13 | 138,084 | public measure definitions and aggregate feasibility |
| CMS complications and deaths | dataset `ynj2-r877`, release 2026-08-13 | 95,800 | public outcome and safety measure definitions |
| HHS capacity | dataset `anag-cw7u`, last update 2024-05-03 | 1,045,406 | public capacity definitions and historical aggregate context |

Public data do not become fictional service data. The fictional service has no public hospital linkage. The checkpoint preserves the source inventory, profiles, service declaration, unit of flow, process boundary, measure families, accountability map, claim boundary, AI record, and progression decision.

Module 01 is a required gate because later work is invalid without its service, unit, clock, source-role, owner, and claim decisions. It adds no course points.

## 4. Accepted Module 02 measure and operational package

The checkpoint accepts Module 02 only as:

- module ID `oclc-app3-02`;
- version `0.1.0`;
- Commons release `0.67.0`;
- 58 assembled reference files;
- 43 immutable manifest rows;
- manifest size 5,266 bytes;
- manifest SHA-256 `868f87c365de83e052c3acee6c7742586a8007dd75d9976343b2f06dfbf622e4`;
- score 20 of 20;
- 15 of 15 measurement gates passing; and
- progression `continue with conditions`.

The frozen local release contains 318,732 raw rows across nine linked synthetic tables. Twelve defects remain auditable in the raw layer and are repaired through declared logic. The accepted analytic population contains 43,628 encounters. It includes 39,975 completed encounters and 3,653 left-before-seen encounters across 1,092 shifts and 52 weeks.

Seventeen measure specifications define the numerator, denominator, unit, time anchor, eligibility, exclusion, unavailable state, aggregation, direction, interpretation limit, source fields, and owner. Thirty exact query checks pass. No record may silently change:

- the encounter status branches;
- a clock or event order;
- a numerator or denominator;
- a defect or repair rule;
- an unavailable value;
- a subgroup support threshold;
- a source identity; or
- the public and synthetic separation.

The Module 02 score contributes 20 checkpoint points exactly once. The checkpoint never adds a second score for accepting the same measure work.

## 5. Accepted Module 03 variation, safety, and bottleneck package

The checkpoint accepts Module 03 only as:

- module ID `oclc-app3-03`;
- version `0.1.0`;
- Commons release `0.68.0`;
- 54 assembled reference files;
- 40 immutable manifest rows;
- manifest size 5,115 bytes;
- manifest SHA-256 `6528e85f2324fd4b2068788598417be96f6c3a699a587a6ef5eb63f176b0242f`;
- score 20 of 20;
- 18 of 18 diagnostic gates passing; and
- progression `continue with conditions`.

The frozen analytic contract declares Weeks 1 through 24 as the provisional baseline and Weeks 25 through 52 as evaluation. Its target window is evening shifts in Weeks 35 through 44. Recovery is evening shifts in Weeks 45 through 52.

The accepted release has four chart contracts:

1. weekly left-before-seen proportion uses a p-chart with week-specific binomial limits;
2. weekly mean of shift median arrival-to-clinician time uses an XmR chart;
3. incident reports per 1,000 completed encounters use an exact low-count Poisson u-chart; and
4. weekly arrivals use a run chart without control limits because Module 04 owns calendar and seasonal adjustment.

Three predeclared rules generate nine signal records. The accepted output retains the Weeks 4 through 11 baseline XmR high run. It also retains the evaluation high run, Week 44 high points, incident-report low run, and arrival runs. A signal opens review. It does not prove cause.

Module 03 contributes its 20 points exactly once.

## 6. Point architecture and no-double-counting rule

The checkpoint score is 40 of 40:

| Source | Points carried |
|---|---:|
| Module 01 decision and source gate | 0 |
| Module 02 measure and operational assessment | 20 |
| Module 03 performance diagnostic | 20 |
| Total | 40 |

Module 02 has five 4-point criteria for measure definitions, event logic and repair, operational metrics, validation and interpretation, and reproducibility and progression. Module 03 has five 4-point criteria for chart selection, signal calculation, safety surveillance, process diagnosis and support, and communication, escalation, and reproduction.

The checkpoint does not rescore those records. It verifies their identities, carries each accepted score once, and determines whether their cumulative chain may progress. It may not:

- assign points to Module 01;
- carry either 20-point score twice;
- add checkpoint points for passing a gate;
- average failed gates into a numeric score; or
- replace one component with stronger performance on the other.

A 40-point score cannot compensate for a broken fingerprint, wrong denominator, altered baseline, failed gate, unsupported claim, incomplete defense, or invalid progression decision.

## 7. Cumulative evidence index and chain of custody

`evidence-index.csv` is the human-readable chain of custody. It has one ordered row for each module and records:

- module ID and title;
- module version and Commons release;
- assembled file and manifest row counts;
- nested manifest bytes and SHA-256;
- checkpoint points;
- gate status;
- progression;
- accepted decision; and
- role in the cumulative release.

Its point column must be `0, 20, 20` and sum to 40. The `candidate-manifest.csv` file is the machine-readable chain of custody. It has 137 sorted rows with relative path, byte count, SHA-256, source module, source version, and role.

Each nested `release-manifest.csv` remains inside its candidate module directory. The outer manifest proves what entered the checkpoint. The nested manifest proves that each module's immutable artifacts still match its accepted workspace. Both layers must pass.

The checkpoint never treats an outer fingerprint as evidence that the semantic contract is correct by itself. The validator also inspects scores, gates, population counts, query checks, signal count, safety values, stage evidence, subgroup support, escalation language, defense, and progression.

## 8. Integrated measure-readiness review

`measures-variation-readiness-review.md` must connect the service decision to the measure system. It states:

- `CGH-ED-01` is fictional;
- one synthetic adult emergency encounter is the unit of flow;
- public sources provide definitions and aggregate context only;
- public hospital linkage is prohibited;
- the raw synthetic release has 318,732 rows;
- 12 declared repairs remain auditable;
- the accepted population has 43,628 encounters;
- 39,975 encounters are completed and 3,653 are left before seen;
- the release spans 1,092 shifts and 52 weeks;
- 17 measure specifications are complete;
- 30 query checks pass; and
- any changed measure rule returns to Module 02.

The review does not compress unavailable clocks into zero, remove an encounter from conservation, combine event and reporting time, borrow subgroup support, or infer a clinical result from a process measure.

The review names the 20-point Module 02 score and all 15 gates. It also states that point acceptance is separate from permission to diagnose or act.

## 9. Variation and safety readiness

The cumulative review preserves these exact chart values:

| Contract | Accepted value |
|---|---:|
| p-chart center | 8.13767 percent |
| XmR center | 97.636958 minutes |
| XmR lower limit | 90.485606 minutes |
| XmR upper limit | 104.788311 minutes |
| incident u-chart center | 9.895751 per 1,000 completed encounters |
| arrivals run-chart median | 853 |
| signal records | 9 |

It explains why each chart matches its data type, denominator, exposure, and temporal structure. It keeps the provisional baseline instability visible. It does not redraw the baseline after seeing the target window or remove a signal because the generated truth says no cause was seeded there.

The safety review preserves:

- 894 known true events;
- 673 trigger true positives;
- 358 incident true positives;
- 379 reviewed non-events or trigger false positives;
- trigger sensitivity 75.2796 percent;
- incident capture 40.0447 percent; and
- trigger specificity 99.0302 percent.

Known truth, triggers, incident reports, false positives, and reviewed non-events remain separate. The incident chart has no exact Poisson limit breach. The Weeks 33 through 42 low run remains a review prompt. It is not evidence that harm prevalence fell or safety improved.

## 10. Bounded bottleneck, subgroup, and escalation readiness

The only accepted bottleneck statement is:

> The fictional release supports a roomed-to-clinician constraint on evening shifts in Weeks 35 through 44.

The declared stage medians are:

| Comparison group | Roomed-to-clinician median |
|---|---:|
| baseline evening, Weeks 1 through 24 | 49 minutes |
| target evening, Weeks 35 through 44 | 66 minutes |
| contemporaneous day and night, Weeks 35 through 44 | 44 minutes |
| recovery evening, Weeks 45 through 52 | 49 minutes |

Queue, wait, throughput, staffing exposure, balancing, and recovery evidence support the bounded stage and time-window diagnosis. They do not establish root cause, staffing adequacy, clinician productivity, or a required intervention.

The full release supports all three declared access groups. The target window does not. Language-support has 401 eligible encounters and mobility-support has 242, both below the 1,000-encounter teaching threshold. A target-window cross-group claim is not supported. Full-release support cannot be borrowed for a narrower comparison.

E01 requires a high clinician-delay signal plus a same-period left-before-seen signal or queue corroboration. It opens human clinical, flow, access, and safety review within one business day. Serious-harm candidates can enter immediate human safety review regardless of chart status.

E01 does not select staff, change a schedule, route a patient, alter care, implement a test, or authorize any automated action.

## 11. Noncompensable inherited and checkpoint gates

The checkpoint inherits 45 module gates:

- 12 Module 01 decision, source, and claim gates;
- 15 Module 02 measure, event, repair, output, and progression gates; and
- 18 Module 03 chart, safety, bottleneck, support, escalation, and progression gates.

It adds 18 integrity gates:

1. exact Module 01 through Module 03 identities;
2. all 137 candidate files present and fingerprinted;
3. all nested manifest row counts, bytes, and SHA-256 values exact;
4. Module 01 retained as a zero-point gate;
5. Module 02 20 points carried once;
6. Module 03 20 points carried once;
7. checkpoint total of 40 without duplication;
8. all 45 inherited gates passing;
9. service, source roles, and unit of flow unchanged;
10. denominators, clocks, repairs, and unavailable states unchanged;
11. baseline, chart contracts, rules, and nine signals unchanged;
12. safety truth, triggers, reports, false positives, and low-count limits separate;
13. diagnosis bounded to one stage, shift, and time window;
14. unsupported target-window subgroup comparisons unavailable;
15. E01 retained as human review only;
16. root-cause, staffing, clinical, causal, automated, and implementation claims prohibited;
17. complete defense, reproduction, accessibility, and accountable agent records; and
18. progression and Module 04 permission consistent with named conditions.

Any failure produces `revise` or `refer`. Points never override a gate.

## 12. Learner records and defense contract

The learner completes eight checkpoint records:

- `README.md`, with checkpoint identity, run commands, evidence classes, score, and decision;
- `evidence-index.csv`, with one exact row per accepted module;
- `measures-variation-readiness-review.md`, with one cumulative interpretation;
- `checkpoint-gates.csv`, with all 18 integrity gates, evidence, owners, and status;
- `checkpoint-defense.md`, with 12 answers, evidence paths, and limits;
- `reproducibility-check.md`, with build, copied-validation, and mutation evidence;
- `ai-use.md`, with accountable agent use; and
- `progression-decision.md`, with points, gates, conditions, and Module 04 permission.

The 12 defense questions cover:

1. decision and unit of flow;
2. public and synthetic evidence separation;
3. measure readiness;
4. chart-family selection;
5. baseline instability;
6. safety undercapture;
7. bounded bottleneck diagnosis;
8. unsupported subgroup comparison;
9. E01 authorization and limits;
10. 40-point accounting;
11. chain of custody and reproduction; and
12. Module 04 ownership.

Every answer must name accepted evidence and one material limit. A fluent answer without evidence fails. A correct number paired with an unsupported action also fails.

Candidate module workspaces are immutable. Learners do not edit a candidate file inside the checkpoint.

## 13. Deterministic assembly contract

`build_checkpoint.py` imports the three accepted module workspace builders and creates their complete reference workspaces. It copies every file into:

- `candidate/module-01/`;
- `candidate/module-02/`; and
- `candidate/module-03/`.

It verifies expected module file counts of 25, 58, and 54 before copying. It then writes the 137-row candidate manifest. The builder:

- uses only the Python standard library;
- sorts manifest paths;
- hashes file bytes with SHA-256;
- keeps learner and reference candidates byte-identical;
- refuses any existing target;
- excludes transient `__pycache__` files; and
- proves two independent reference assemblies match.

Each assembled checkpoint has:

- 137 candidate files;
- seven immutable checkpoint controls;
- eight editable checkpoint records;
- one candidate manifest; and
- 153 files total.

The builder does not copy `release.json` into the learner workspace because release metadata belongs to the package. The assembled checkpoint contains the contract, assessment, instructor notes, builder, validator, version, and line-ending rules needed to reproduce and validate it elsewhere.

## 14. Validation, copied execution, and mutation rejection

`validate_checkpoint.py` checks:

- exact file membership and count;
- all 137 outer manifest rows;
- every candidate byte count and SHA-256;
- source module and version on every row;
- all three nested manifests and their immutable artifacts;
- checkpoint contract, point source, and gate totals;
- evidence-index identities, counts, hashes, points, and gate results;
- accepted Module 01 service and claim boundary;
- accepted Module 02 score, gates, population, and query results;
- accepted Module 03 score, gates, nine signals, safety evidence, target-stage median, subgroup support, and E01;
- exact cumulative review values and prohibited-claim absence;
- 18 passing checkpoint gates;
- 12 complete defense answers;
- reproduction and AI records; and
- progression, action boundaries, and eight owned conditions.

Reference validation passes 742 checks. Learner validation passes 700 structural and immutable-evidence checks while requiring visible prompts in all eight editable records. The copied validator runs from the assembled checkpoint, not only from the repository package.

The self-check rejects 18 failure routes:

1. changed candidate;
2. missing candidate;
3. changed Module 01 points;
4. duplicate Module 02 points;
5. duplicate Module 03 points;
6. wrong checkpoint total;
7. failed inherited gate;
8. failed checkpoint gate;
9. changed signal count;
10. signal presented as cause;
11. staffing recommendation;
12. unsupported subgroup claim;
13. automated escalation;
14. incomplete defense;
15. invalid progression permission;
16. missing AI accountability field;
17. missing reproduction route; and
18. starter records submitted as complete.

These routes test chain of custody and meaning. A candidate checksum alone cannot catch a false cumulative claim written outside the candidate directories.

## 15. Common failure modes and instructor response

| Failure | Required response |
|---|---|
| A module directory is missing or changed | rebuild from the accepted module release |
| Module 01 receives points | restore its zero-point gate role |
| Module 02 or Module 03 points appear twice | restore one 20-point row for each and a 40-point total |
| A passing score is used to ignore a gate | stop progression and revise or refer |
| Source, clock, denominator, repair, or unavailable state changes | return to Module 01 or Module 02 |
| Baseline or control limit changes after seeing results | return to Module 03 and release a reviewed new version |
| A signal is called a cause | restore signal-as-review language |
| Incident reports are treated as prevalence | restore the truth, trigger, report, and undercapture separation |
| The incident low run is called safety improvement | restore the low-count interpretation limit |
| The bounded stage diagnosis becomes a staffing claim | remove the recommendation and return to the evidence boundary |
| Target-window subgroup support is borrowed from the full release | mark the narrow comparison unavailable |
| E01 automates action | restore human review and accountable ownership |
| A candidate is edited inside the checkpoint | correct the owning module and reassemble |
| A defense answer lacks evidence or a limit | return the defense as incomplete |
| Module 04 permission conflicts with progression | correct the progression record |
| Machine learning appears before Module 06 | remove it and preserve the course ownership map |

Instructors stop review at the first broken fingerprint, duplicated point, failed gate, changed analytic rule, unsupported claim, or automated action.

## 16. Progression contract and Module 04 handoff

The reference disposition is:

- checkpoint score `40 of 40`;
- Module 01 decision gates `12 of 12 pass`;
- Module 02 measurement gates `15 of 15 pass`;
- Module 03 diagnostic gates `18 of 18 pass`;
- checkpoint integrity gates `18 of 18 pass`;
- failed gates `none`;
- progression `continue with conditions`;
- Module 04 permission `permitted for demand forecasting and capacity analysis`;
- root cause `not established`;
- staffing change, clinical action, automated action, and implementation `prohibited`; and
- machine learning `reserved for Module 06`.

Module 04 receives the frozen Week 3 service, source roles, population, measures, baseline, chart and signal record, safety limitations, bounded stage diagnosis, support limits, and E01 ownership. Before fitting, Module 04 must declare:

- forecast target and unit;
- issue time and information cutoff;
- horizon;
- calendar assumptions;
- eligible history;
- rolling-origin folds;
- last-value and seasonal-naive benchmarks;
- bounded smoothing model;
- cost of error; and
- capacity decision and owner.

Module 04 may not repair a measure, change a baseline, remove a signal, strengthen a bottleneck claim, recommend staffing, or import machine learning. A necessary upstream change returns to the owning module and invalidates this checkpoint until rebuilt.

Eight open conditions name faculty, clinical performance, safety, equity and access, workforce, independent reproduction, Module 04 analysis, and responsible-AI owners. Independent base-R control-chart reproduction remains pending before alpha.

## 17. Release, review, and exit criteria

Checkpoint version 0.1.0 exits as a runnable release candidate at Commons 0.69.0 only when:

- two independent reference assemblies match;
- learner and reference candidates are identical;
- the existing-target refusal passes;
- all 137 outer fingerprints match;
- all three nested manifests and immutable artifacts match;
- the copied validator passes;
- reference validation passes 742 checks;
- learner validation passes 700 checks;
- all 18 failure routes are rejected;
- the score is 40 with no duplication;
- all 63 inherited and checkpoint gates pass;
- the defense has 12 complete answers;
- the progression record matches Module 04 permission; and
- the whole-curriculum checker passes.

The accepted candidate manifest is 23,862 bytes with SHA-256 `9f4dbbf58fdef8ac0935f298de26ae04b87b8722c3be2d3b2b6e2aefbc147656`.

Named APP-3 faculty, clinician, clinical-performance, safety, equity, access, workforce, accessibility, responsible-AI, and independent reproduction reviews remain required before alpha. The base-R control-chart verification must run independently in an environment with R. The official course section must map the checkpoint to the published academic calendar at https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf before assigning a due date.

The release is a construction candidate. It is not approval to change care, staffing, scheduling, routing, safety policy, or implementation in a real service.
