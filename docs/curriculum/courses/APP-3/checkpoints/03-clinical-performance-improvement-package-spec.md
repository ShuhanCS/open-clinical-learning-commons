# APP-3 Final checkpoint: Clinical performance improvement package

## 1. Checkpoint identity and official timing

- Checkpoint ID: `oclc-app3-cp03`.
- Checkpoint version: `0.1.0`.
- Commons release target: `0.75.0`.
- Course: APP-3, Data for Clinical Performance and Improvement.
- Due: official last day of the assigned MGH Institute half-term.
- Course weight: 35 percent, or 35 course points.
- Required input: complete APP-3 Module 07 candidate version `0.1.0`.
- Status target: runnable release candidate.

The official calendar controls the submission date:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

The phrase "7.5 weeks" is a planning model. The final checkpoint is due on the published last day of the assigned half-term, not on a date inferred by adding 7.5 weeks.

## 2. Final decisions and receiving audience

The checkpoint records two separate decisions.

Allowed package dispositions are `accept`, `accept with conditions`, `revise`, and `refer`. Only `accept` and `accept with conditions` pass the course package gate.

Allowed clinical performance recommendations are `run bounded prospective improvement test`, `revise before testing`, `refer`, and `stop`.

The reference package disposition is `accept with conditions`. Its separate clinical performance recommendation is `revise before testing`.

The receiving audience is the fictional `CGH-ED-01` clinical performance council and the clinical, safety, operations, workforce, access, measurement, forecasting, model, governance, and independent reviewers who would decide whether a local proposal is ready for design and authorization review. Package acceptance does not authorize clinical action, staffing or schedule change, automation, testing, implementation, production scoring, or model deployment.

## 3. Course-point preservation and score map

Checkpoint 03 records Module 07's draft 35-point component once as the reviewed final course score.

| ID | Recurring criterion | Points |
|---|---|---:|
| E01 | Correct evidence, decision, and claim boundary | 8.00 |
| C01 | Clinical performance reasoning, safety, access, and workforce judgment | 9.00 |
| L01 | Leadership recommendation, feasibility, alternatives, and ownership | 8.00 |
| M01 | Monitoring, stewardship, escalation, disagreement, and communication | 6.00 |
| H01 | Reproducibility, accessibility, responsible agent use, and defense | 4.00 |
| Total |  | 35.00 |

Passing requires at least 28.00 points, all 26 noncompensable gates, an adequate defense, `accept` or `accept with conditions`, and one allowed clinical performance recommendation.

The final checkpoint does not add another 35 points to the Module 07 draft. It replaces the draft with the reviewed course record. APP-3 totals 100 points: 40 at Week 3, 25 at Week 6, and 35 on the official half-term end date.

## 4. Accepted candidate identity

The checkpoint accepts one complete Module 07 candidate with:

- 416 files;
- a 389-row immutable release manifest;
- the complete 153-file Checkpoint 01 package;
- the complete 226-file Checkpoint 02 package;
- exact Checkpoint 01 and Checkpoint 02 release records;
- eight Module 07 controls; and
- 26 completed leadership records.

The accepted Module 07 release record is 4,532 bytes with SHA-256 `5dcec682080346570e89915473a9b2939c15cf57a28a15250137694d056486e2`. Its immutable candidate manifest is 75,470 bytes with SHA-256 `cd88ad1910ca35d231da734f919f58420e2f3f25deda9135ee6ca8c20105d2fc`.

The accepted Checkpoint 01 release SHA-256 is `270b4e49d1c21d8faf7243cd11cef1dddea836d32be551dfe72edac771b31f27`. The accepted Checkpoint 02 release SHA-256 is `b8af80b7e07c2eac2aeb0e9206533bfae134f55d69a5df9038a7a9a915c4dd05`.

## 5. Ownership and out-of-scope boundary

The final checkpoint owns the whole-candidate freeze, 416-row final manifest, accepted release checks, final 35-point score, 26 final gates, 14-question final defense, reviewer and independence record, final reproduction, audit, conditions, package disposition, clinical performance recommendation, course-completion statement, and proposed tag.

Module 07 retains ownership of the evidence synthesis, briefs, recommendation and alternatives, people review, stakeholder roles, workflow feasibility, revision plan, stewardship, monitoring, escalation, disagreement, reflection, appendix, evidence index, accessibility, reproducibility, claims audit, agent-use record, draft score, gates, conditions, defense, reviewers, and progression decision.

Checkpoints 01 and 02 retain all accepted analytic evidence. Checkpoint 03 freezes and adjudicates the package. It does not recompute or silently edit that evidence.

The checkpoint does not change a source, service, unit of flow, measure, denominator, clock, signal rule, safety interpretation, diagnosis, subgroup support rule, forecast target, fold, method, scenario, threshold, feasibility disposition, monitoring definition, escalation rule, ML decision, or accepted output. It cannot create an accepted tag before named human authorization of the exact reviewed commit.

## 6. Final workflow and workload

The checkpoint uses work already included in Module 07's 16 hours:

1. validate the complete Module 07 candidate;
2. assemble it into a protected final target;
3. verify the 416-row candidate manifest;
4. confirm all three accepted release identities;
5. complete the final score, 26 gates, reviewer, reproduction, audit, conditions, and decisions;
6. deliver the accessible clinical performance leadership handoff;
7. answer all 14 final defense questions;
8. record package disposition and clinical performance recommendation separately;
9. rerun complete validation;
10. commit the exact reviewed state; and
11. create the proposed annotated tag only after named human authorization.

## 7. Final package architecture

The final assembler copies all 416 Module 07 candidate files without modification and adds 15 files under `final-review/`:

- `CHECKPOINT-VERSION`;
- `checkpoint1-release.json`;
- `checkpoint2-release.json`;
- `module07-release.json`;
- `candidate-manifest.csv` with 416 sorted rows; and
- ten final-review records.

The ten records are `submission-record.md`, `final-score.csv`, `gate-results.csv`, `final-defense.md`, `reviewer-record.md`, `final-reproduction.md`, `conditions-register.csv`, `final-audit.md`, `final-decision.md`, and `release-acceptance.md`.

The complete final package contains exactly 431 files. No accepted candidate file is overwritten by final review. The 416-row final candidate manifest is 70,531 bytes with SHA-256 `b41acddef7397f9e55deee99f815b3d586d246f2353bbd92cf0873654499e8b6`.

## 8. Ten final-review records

1. `submission-record.md` records repository, source commit, versions, fingerprints, due-date rule, validator result, submitter, and proposed tag.
2. `final-score.csv` records the five fixed criteria and exact 35-point total.
3. `gate-results.csv` records all 26 gates, evidence, reviewer, result, and condition.
4. `final-defense.md` records direct answers to all 14 questions and adequacy.
5. `reviewer-record.md` records required roles, independence, evidence, decisions, and acknowledgments.
6. `final-reproduction.md` records clean checkout, environment, commands, manifest comparison, nested validators, reproducer, and unresolved conditions.
7. `conditions-register.csv` carries 12 conditions with owners, due points, evidence, verifiers, status, and escalation triggers.
8. `final-audit.md` combines source, rights, data-class, integrity, privacy, accessibility, agent-use, evidence-index, and prohibited-use checks.
9. `final-decision.md` records score, gates, defense, package disposition, clinical performance recommendation, authorization boundary, and course status separately.
10. `release-acceptance.md` states what the receiver gets, allowed use, prohibited use, conditions, support owner, change rule, stop triggers, and tag status.

## 9. Final reviewer roles

Required coverage includes the APP-3 faculty owner; Joe Joseph, MD, SFHM, as clinician of record; a local clinical decision owner; safety reviewer; improvement and simulation reviewer; operations and capacity reviewer; workforce reviewer; access and equity reviewer; measurement and statistical-process reviewer; forecasting reviewer; responsible-AI and ML reviewer; accessibility and communication reviewer; and independent reproducer.

One person may cover more than one role when qualifications and independence are recorded. The learner cannot be the clinical decision owner or independent reproducer.

Reference construction may use role-based pending conditions. It cannot represent a completed learner defense, current clinical authorization, named program approval, or completed review that did not occur.

## 10. Twenty-six final gates

The 26 final gates require:

1. exact Checkpoint 01, Checkpoint 02, and Module 07 release identities;
2. exact 416-file candidate and 416-row final manifest;
3. exact 389-row Module 07 manifest and fingerprint;
4. repository, source commit, versions, release records, and proposed tag;
5. source, rights, data-class, fictional-service, synthetic, and prohibited-data review;
6. measure, denominator, clock, unavailable, and source limits unchanged;
7. baseline instability, nine signals, and signal-not-cause rule visible;
8. safety undercapture and incident-report limits visible;
9. bounded bottleneck diagnosis, root-cause limit, and subgroup support retained;
10. forecast target, cutoffs, folds, rows, errors, failures, point, and range unchanged;
11. Little's Law and staffing limits retained;
12. scenario register, runs, effects, failures, and no-selection result retained;
13. safety, return, causal, workforce, and implementation limits retained;
14. four feasibility dispositions and evidence statuses retained;
15. 12 measures, three unavailable values, ten escalation rules, no-change fallback, and zero automatic actions retained;
16. static accessible dashboard and equivalent evidence routes retained;
17. fixed comparable ML, leakage checks, failed R01, and transparent forecast retained;
18. Week 3 40 points, Week 6 25 points, and final 35 points counted exactly once;
19. every material final claim traces to accepted evidence;
20. package disposition and clinical recommendation remain separate and allowed;
21. people, burden, exclusion, access, equity, safety, workforce, and blame addressed;
22. ownership, decision rights, reviewer independence, and disagreement route complete;
23. revision, stewardship, monitoring, escalation, fallback, reassessment, and conditions complete;
24. exact tables, frontline communication, accessibility, reproduction, claims, and responsible agent use complete;
25. all 14 defense answers are adequate and all required reviewer roles are present; and
26. course completion, tag status, package acceptance, clinical recommendation, and every prohibited use remain consistent.

Any failed gate returns the package for revision or referral. Numeric strength cannot waive a changed byte, unsupported claim, hidden failure, unavailable-as-zero claim, inaccessible evidence, hidden agent use, missing owner, or false authorization.

## 11. Final defense questions

1. What exact council and course decision does this package support?
2. Which evidence is strongest, and which condition most narrows action?
3. Why do the accepted signals and bottleneck evidence not establish root cause?
4. What does the forecast support, and why does it not define staffing?
5. Why did no scenario qualify, and which failed result matters most?
6. What do the four feasibility dispositions require next?
7. Which safety, return, access, and workforce evidence remains unavailable or unsupported?
8. What do monitoring, escalation, fallback, and zero automatic actions authorize and prohibit?
9. Why does the ML challenger not replace the transparent forecast?
10. Who may benefit, carry burden, be excluded, or face safety or access risk?
11. How can frontline staff raise safety, burden, access, workflow, or disagreement concerns without blame?
12. Who owns revision, review, pause, referral, stop, restart, and final authorization?
13. What did an agent contribute, and how was each material contribution checked?
14. Why can the curriculum package pass while the clinical recommendation remains `revise before testing`?

An adequate answer cites an exact package path or registered fact, explains its practical clinical or operational meaning, and states the decision limit.

## 12. Learner and reviewer workflows

The learner freezes the complete Module 07 candidate at a full commit, assembles Checkpoint 03 into a new target, verifies the final manifest, completes the ten review records, delivers an accessible handoff, answers all 14 questions, corrects findings in the owning record without changing accepted evidence, reruns validation, obtains separate decisions, and commits the exact reviewed package.

Reviewers confirm the official due date and candidate identity, scan for prohibited data and hidden dependencies, validate Module 07 and both nested checkpoints, trace claims, review people and workflow implications, reproduce the package, conduct the defense, complete the score and gates, record conditions and decisions, and rerun validation against the exact reviewed state.

The proposed tag may be created only after the required named humans authorize the exact commit.

## 13. Automated validation and failure routes

The validator checks the exact 431-file tree, safe paths, 416-row final manifest, candidate byte and SHA-256 equality, exact 389-row Module 07 manifest, reconstructed Module 07 validation, all accepted release identities, score arithmetic, 26 gates, 12 conditions, 14 defense answers, 13 reviewer roles, reproduction, audit, separate decisions, tag status, placeholders, plain ASCII dashes, and portable paths.

The assembler refuses an existing target and a target inside the candidate. It copies accepted bytes and never moves or deletes them.

Self-checks cover two-build identity, learner starter, copied validation, changed candidate, changed release, invalid score, failed gate, early tag, changed recommendation, false test authorization, changed forecast, selected scenario drift, hidden unavailable evidence, missing reviewer, closed pending condition, incomplete defense, hidden agent use, duplicate final scoring, and complete-mode template rejection.

Complete validation passes 2,177 checks and learner validation passes 2,131 checks. All 15 failure routes and complete-mode learner rejection pass.

## 14. Reference status

The reference records:

- final score: `35.00 of 35.00`;
- gates: `26 of 26 pass or pass with an allowed condition`;
- defense: `adequate for curriculum construction`;
- package disposition: `accept with conditions`;
- clinical performance recommendation: `revise before testing`;
- selected scenario: `none`;
- accepted forecast: `seasonal exponential smoothing`;
- ML decision: `retain transparent forecast`;
- course status: `complete for curriculum construction only`;
- proposed tag: `app3-clinical-performance-improvement-candidate-v0.1.0`; and
- tag status: `proposed - not created`.

Clinical action, staffing and schedule changes, automated action, test start, implementation, production scoring, and model deployment remain prohibited.

Named program review, Joe Joseph's direct confirmation, actual learner and reviewer acknowledgment, a live or equivalent defense, independent human clean reproduction, official dates, and final tag authorization remain pending before alpha.

## 15. Release and tag rule

The annotated tag may be created only after an allowed package disposition, complete named human approval, an adequate learner defense, independent clean reproduction, confirmation that the tag points to the exact reviewed commit, and explicit tag authorization in the final decision.

The tag identifies an accepted curriculum package. It does not authorize a clinical test, staffing or schedule change, implementation, production scoring, model deployment, or a claim of benefit.

## 16. Completion and next-course handoff

An accepted final package closes APP-3 for curriculum construction and supplies the next course with exact release and commit identity, complete accepted technical evidence, a bounded leadership recommendation, people, workflow, access, equity, safety, workforce, and feasibility conditions, measures and escalation rules, an accessible appendix, responsible agent and human-accountability records, and an explicit statement of what remains unauthorized.

APP-4 may reuse Commons architecture and public-data principles. It does not inherit APP-3's fictional service or evidence unless its own specification names the accepted release, fingerprints it, and states what it reuses and what it owns.

## 17. Known conditions before alpha

- Joe Joseph, MD, SFHM, confirms participation, schedule, session format, recording permission, and final biography wording.
- Named clinical, safety, improvement, simulation, operations, capacity, workforce, access, equity, measurement, statistical-process, forecasting, accessibility, responsible-AI, ML, governance, and independent reviewers complete review.
- A qualified person completes clean reproduction on a supported teaching environment.
- The official section and half-term dates are assigned from the published calendar.
- The committed Module 03 and Module 04 base-R checks receive independent review in an environment with R installed.
- The frontline concern and disagreement route is tested.
- A live or approved equivalent 14-question defense and reviewer acknowledgment workflow are completed.
- The proposed tag remains uncreated until exact-commit authorization.
- No reference package is described as authorization for clinical action, staffing or schedule change, automation, testing, implementation, production scoring, or model deployment.
