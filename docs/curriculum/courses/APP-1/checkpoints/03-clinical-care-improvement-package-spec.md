# APP-1 Final checkpoint: Clinical care improvement package

## 1. Checkpoint identity and official timing

- Checkpoint ID: `oclc-app1-cp03`.
- Checkpoint version: 0.1.0.
- Commons release target: 0.55.0.
- Course: APP-1, Data for Clinical Care.
- Due: official last day of the assigned MGH Institute half-term.
- Course weight: 35 percent, or 35 course points.
- Required input: complete APP-1 Module 07 candidate version 0.1.0.
- Status target: runnable release candidate.

The official calendar controls the submission date:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

The phrase "7.5 weeks" is a planning model. The final checkpoint is due on the published last day of the assigned half-term, not on a date inferred by adding 7.5 weeks.

## 2. Final decisions and receiving audience

The checkpoint records two separate decisions.

### Package disposition

- `accept`;
- `accept with conditions`;
- `revise`; or
- `refer`.

Only `accept` and `accept with conditions` pass the course package gate.

### Clinical recommendation

- `run bounded prospective improvement test`;
- `revise before testing`;
- `refer`; or
- `stop`.

The reference package disposition is `accept with conditions`. Its separate clinical recommendation is `revise before testing`.

The decision owner is a hospital medicine medical director or care-improvement council role. The receiver is an organization considering whether the proposal is ready for local design and authorization review. Package acceptance does not authorize clinical implementation, model deployment, patient targeting, or a claim of benefit.

## 3. Course-point preservation and score map

The checkpoint records Module 07's draft 35-point component once as the final course score.

| ID | Recurring criterion | Points |
|---|---|---:|
| C01 | Correct evidence, decision, and claim boundary | 8.00 |
| R01 | Reproducible evidence, package, and handoff | 5.00 |
| L01 | Sound clinical reasoning, equity, safety, and feasibility | 10.00 |
| A01 | Clear and action-guiding recommendation, ownership, and monitoring | 8.00 |
| H01 | Responsible agent use, accessibility, and defense | 4.00 |
| Total |  | 35.00 |

Passing requires at least 28.00 points, every noncompensable gate, an adequate defense, `accept` or `accept with conditions`, and an explicit allowed clinical recommendation.

The final checkpoint does not add 35 points to the Module 07 draft. It replaces the draft score with the reviewed course record. APP-1 then totals 100 points: 20 at Week 3, 45 at Week 6, and 35 at the official half-term end.

## 4. Accepted candidate identity

The checkpoint accepts one complete Module 07 candidate with:

- 236 files;
- a 214-row immutable release manifest;
- the complete 91-file Checkpoint 1 package;
- the complete 113-file Checkpoint 2 package;
- exact Checkpoint 1 and Checkpoint 2 release records;
- eight Module 07 controls; and
- 21 completed leadership records.

The accepted Module 07 release record is 4,198 bytes with SHA-256 `939fc4c08f46974e3d7db1c2b387f2c7251287cdba2317e2867ce326edbac933`. Its immutable candidate manifest is 40,140 bytes with SHA-256 `2c90713fb220b6fdc1af492898e89605051b0dffed44b2fb2883b2942aefde62`.

## 5. Ownership and out-of-scope boundary

### Final checkpoint owns

- whole-candidate freeze and 236-row final candidate manifest;
- accepted Checkpoint 1, Checkpoint 2, and Module 07 release identity checks;
- final 35-point score;
- 24 final gates;
- 12-question final defense record;
- reviewer and independence record;
- final reproduction and audit records;
- conditions and owners;
- package disposition;
- separate clinical recommendation;
- course-completion statement; and
- proposed tag record.

### Module 07 ownership retained

Module 07 owns the evidence synthesis, recommendation, stakeholder roles, workflow, prospective-test plan, measures, monitoring, stop rules, leadership reflection, technical appendix, evidence index, accessibility record, AI record, draft score, gates, conditions, defense, reviewers, and progression decision.

### Upstream ownership retained

Checkpoints 1 and 2 retain all accepted analytic evidence. The final checkpoint freezes and adjudicates the package. It does not recompute or silently edit that evidence.

### Out of scope

- changing the cohort, source, time zero, event, censoring, model, threshold, site extension, subgroup rule, or accepted output;
- fitting or deploying another model;
- authorizing a clinical workflow or prospective test;
- creating a patient-level targeting list;
- claiming causation, efficacy, fairness, quality, access, safety, or real-population performance; and
- creating an annotated tag before named human acceptance of the exact reviewed commit.

## 6. Final workflow and workload

The checkpoint uses work already included in Module 07's 16 hours:

1. validate the complete Module 07 candidate;
2. assemble it into a protected final target;
3. verify the 236-row candidate manifest;
4. confirm all three accepted release identities;
5. complete the final score, 24 gates, reviewer, reproduction, audit, conditions, and decisions;
6. deliver the accessible council handoff;
7. answer all 12 final defense questions;
8. record package disposition and clinical recommendation separately;
9. rerun complete validation;
10. commit the exact reviewed state; and
11. create the proposed annotated tag only after named human authorization.

## 7. Final package architecture

The final assembler copies all 236 Module 07 candidate files without modification and adds 15 files under `final-review/`:

- `CHECKPOINT-VERSION`;
- `checkpoint1-release.json`;
- `checkpoint2-release.json`;
- `module07-release.json`;
- `candidate-manifest.csv` with 236 sorted rows; and
- ten final-review records.

The complete final package contains exactly 251 files. No accepted candidate file is overwritten by the final review.

The generated 236-row final candidate manifest is 38,238 bytes with SHA-256 `aab1eef0c746700b6322ac1300c5dac3571d861f0fb283c86a0602e3dad9a54b`.

## 8. Ten final-review records

1. `submission-record.md` records repository, full source commit, versions, fingerprints, due-date rule, validator result, submitter, and proposed tag.
2. `final-score.csv` records the five fixed criteria and exact 35-point total.
3. `gate-results.csv` records all 24 gates, evidence, reviewer, result, and condition.
4. `final-defense.md` records direct answers to all 12 questions and adequacy.
5. `reviewer-record.md` records required roles, independence, evidence, dates, decisions, and acknowledgments.
6. `final-reproduction.md` records clean checkout, environment, commands, manifest comparison, validators, reproducer, and unresolved conditions.
7. `conditions-register.csv` records carried and new conditions, owners, due points, evidence, verifiers, status, and escalation triggers.
8. `final-audit.md` combines source, rights, integrity, privacy, accessibility, agent-use, evidence-index, and prohibited-data checks.
9. `final-decision.md` records score, gates, defense, package disposition, clinical recommendation, authorization boundary, and course status separately.
10. `release-acceptance.md` states what the receiver gets, allowed use, prohibited use, conditions, support owner, change rule, stop triggers, and tag status.

## 9. Final reviewer roles

Required review coverage includes:

- APP-1 faculty owner;
- hospital medicine clinical decision owner;
- improvement science reviewer;
- biostatistical methods reviewer;
- clinical informatics reviewer;
- equity reviewer;
- accessibility reviewer;
- privacy and data-governance reviewer;
- responsible-AI reviewer; and
- independent reproducer.

One person may cover more than one role when qualifications and independence are recorded. The learner cannot be the clinical decision owner or independent reproducer.

Reference construction may use role-based pending conditions. It cannot represent a completed learner defense, clinical authorization, or named program approval.

## 10. Twenty-four final gates

1. exact Checkpoint 1, Checkpoint 2, and Module 07 release identities;
2. exact 236-file candidate and 236-row final manifest;
3. exact 214-row Module 07 immutable manifest;
4. repository, full commit, versions, release records, and proposed tag;
5. source rights, synthetic status, and prohibited-data scan complete;
6. accepted cohort, time zero, follow-up, event, and censoring facts unchanged;
7. proportional-hazards failure and count-first survival interpretation visible;
8. risk adjustment, variation, subgroup, and residual-confounding limits visible;
9. machine learning does not change the decision and is not deployed;
10. every material claim traces to exact accepted evidence;
11. package disposition and clinical recommendation are separate;
12. clinical recommendation belongs to the allowed set and states its authorization boundary;
13. people affected, equity, safety, burden, and exclusion are addressed;
14. stakeholder roles and decision authority are complete;
15. workflow and capacity assumptions are explicit;
16. prospective-test plan has eligibility, comparison, duration, and learning aim;
17. process, outcome, balancing, access, implementation, and data-quality measures are complete;
18. monitoring, reassessment, pause, stop, rollback, and escalation rules are complete;
19. exact tables and equivalent access routes are complete;
20. clean reproduction and nested validation pass;
21. agent trace, independent material checks, and human accountability are complete;
22. all 12 defense answers are adequate;
23. reviewer roles and condition ownership are complete; and
24. package acceptance does not authorize implementation, targeting, model deployment, causation, efficacy, or fairness claims.

Any failed gate returns the package for revision or referral. Numeric strength cannot waive a changed immutable byte, an unsupported claim, hidden assistance, inaccessible evidence, incomplete safety rule, or absent decision owner.

## 11. Final defense questions

1. What exact council decision does this package support?
2. Which evidence is strongest, and which condition most narrows it?
3. Why does the failed proportional-hazards screen change the survival summary?
4. What does risk adjustment support, and what remains confounded?
5. Why does machine learning not change the clinical recommendation?
6. Who may benefit, carry burden, or be missed?
7. Why is universal offer and prospective measurement favored over patient targeting?
8. What local workflow and capacity evidence remains missing?
9. Which measures show delivery, outcomes, burden, access, implementation, and data quality?
10. Which trigger would pause or stop the work first?
11. What did an agent contribute, and how was the material contribution checked independently?
12. Why can the package be accepted while the recommendation remains `revise before testing`?

An adequate answer cites an exact path or registered fact, explains the clinical or operational meaning, and states the decision limit.

## 12. Learner and reviewer workflows

### Learner workflow

1. Freeze the complete Module 07 candidate at a full commit.
2. Assemble the final checkpoint into a new target.
3. Verify the 236-row candidate manifest.
4. Complete submission, reproduction, audit, conditions, score, and gate records.
5. Deliver the accessible handoff and answer all 12 questions.
6. Correct findings in the owning Module 07 or final record without altering accepted evidence.
7. Rerun final validation after every correction.
8. Obtain package disposition and clinical recommendation separately.
9. Commit the exact reviewed 251-file state.
10. Create the annotated tag only when named human authorization is recorded.

### Reviewer workflow

1. Confirm the official due date and exact candidate identity.
2. Scan for prohibited files, data classes, personal paths, secrets, and hidden dependencies.
3. Validate Module 07 and both nested cumulative checkpoints.
4. Trace every material recommendation claim to accepted evidence.
5. Review workflow, people, equity, safety, feasibility, measures, and stop rules.
6. review clean reproduction and exact comparison.
7. conduct the defense and record adequacy.
8. complete all five score rows and 24 gates.
9. record conditions, owners, package disposition, and clinical recommendation.
10. decide course completion and proposed-tag authorization.
11. rerun final validation against the exact reviewed state.

## 13. Automated validation and failure routes

The validator checks:

- exact 251-file tree and safe relative paths;
- exact 236-row final candidate manifest;
- candidate byte and SHA-256 equality;
- exact 214-row Module 07 manifest and accepted fingerprint;
- complete Module 07 validation after reconstructing the candidate without final-review files;
- exact Checkpoint 1, Checkpoint 2, and Module 07 release identities;
- score arithmetic and 28-point minimum;
- all 24 gates and condition ownership;
- all 12 defense answers and adequate status;
- all ten reviewer roles;
- complete reproduction and final audit records;
- separate and consistent package and clinical decisions;
- proposed tag status `proposed - not created`;
- absence of placeholders in complete mode;
- plain ASCII dashes and portable paths; and
- reference, learner, changed evidence, score, gate, tag, and decision failure cases.

The assembler refuses an existing target and a target inside the candidate. It copies accepted bytes, never moves or deletes them.

The complete reference passes 1,276 checks. The learner starter passes 1,231 checks. Self-checks also reject changed candidate evidence, invalid scoring, a failed gate, an early tag, and an inconsistent final decision.

## 14. Reference status

The reference final package records:

- final score: 35.00 of 35.00;
- gates: 24 of 24 pass or pass with an allowed condition;
- defense: adequate;
- package disposition: `accept with conditions`;
- clinical recommendation: `revise before testing`;
- clinical implementation: prohibited;
- model deployment: prohibited;
- proposed tag: `app1-clinical-care-candidate-v0.1.0`;
- tag status: `proposed - not created`; and
- course status: complete for curriculum construction only.

Named program review, actual learner and reviewer acknowledgment, a live or equivalent defense, independent clean reproduction by a person, and final tag authorization remain pending before alpha.

## 15. Release and tag rule

The annotated tag may be created only after:

- an allowed package disposition;
- complete named human approval;
- an adequate learner defense;
- independent clean reproduction;
- confirmation that the tag points to the exact reviewed commit; and
- explicit tag authorization in the final decision.

The tag identifies an accepted curriculum package. It does not authorize a clinical test, implementation, model deployment, patient targeting, or a claim of benefit.

## 16. Completion and next-course handoff

An accepted final package closes APP-1 for curriculum construction and supplies the next course with:

- exact release and commit identity;
- complete accepted technical evidence;
- a bounded leadership recommendation;
- people, workflow, equity, safety, and feasibility conditions;
- measures and stop rules;
- a complete evidence index and accessible appendix;
- agent and human-accountability records; and
- an explicit statement of what remains unauthorized.

The package does not become source evidence for another course unless that course names the accepted release, fingerprints it, and states what it reuses and what it owns.

## 17. Known conditions before alpha

- Joe Joseph, MD confirms participation, schedule, session format, recording permission, and final biography wording.
- Named hospital medicine, improvement, methods, informatics, equity, accessibility, privacy, responsible-AI, and independent-reproduction reviewers complete review.
- A qualified person completes clean reproduction on a supported teaching environment.
- The official section and half-term dates are assigned from the published calendar.
- A live or equivalent learner defense and reviewer acknowledgment workflow is tested.
- No reference package is described as authorization to run a real clinical test.
