# APP-4 Module 07 specification: Clinician leadership, product brief, and defense

## 1. Module identity and place in the course

- Course: `APP-4`, Data for Clinical Decision Support.
- Module ID: `oclc-app4-07`.
- Title: Clinician leadership, product brief, and defense.
- Module version: `0.1.0`.
- Commons release: `0.85.0`.
- Hours: `16.0`.
- Timing: final clinician-led block before the official half-term end date.
- Course points: `35`.
- Package path: `courses/clinical-decision-support/modules/07-clinician-leadership-product-defense/`.
- Clinician of record: Joe Joseph, MD, SFHM.

Module 07 is the leadership and synthesis unit. It does not add a new cohort, model, threshold, interface behavior, or safety result. It freezes the accepted Week 3 and Week 6 packages and asks the learner to make a bounded leadership recommendation from that exact record.

The module completes the 112.5-hour instructional plan. Its 35-point component is new. The accepted Week 3 total of 40 points and Week 6 total of 25 points remain frozen and are not counted again.

## 2. Decision, readers, and allowed recommendations

The decision is:

> Should the fictional governance council recommend seeking local approval for a bounded silent-mode evaluation, require revision first, refer the question, or stop the concept?

The primary readers are the fictional governance council, the APP-4 faculty owner, clinical and operational reviewers, patient and access reviewers, safety and informatics reviewers, and an independent reproducer. The product brief must also support a plain-language explanation to staff and patients who could experience the proposed workflow.

Exactly four recommendation classes are allowed:

1. `recommend seeking local approval for bounded silent-mode evaluation`;
2. `revise before seeking local silent-mode approval`;
3. `refer`; or
4. `stop`.

The reference recommendation is `revise before seeking local silent-mode approval`. The curriculum package status is separately `accept with conditions`. A complete curriculum submission does not make the CDS concept ready for local approval.

## 3. Clinician of record and dated identity boundary

Joe Joseph, MD, SFHM, is the designated clinician of record. The release uses three dated Sound Physicians public records:

- 2015 Fellow in Hospital Medicine announcement: https://www.soundphysicians.com/press-release/sound-physicians-actively-participating-hospital-medicine-2015/
- 2017 Senior Fellow in Hospital Medicine announcement: https://www.soundphysicians.com/press-release/sound-physicians-thought-leaders-presenting-at-hospital-medicine-2017-annual-conference/
- 2019 release identifying him as a Regional Chief Medical Officer: https://www.soundphysicians.com/press-release/sound-physicians-acquires-indigo-health-partners/

These records establish a dated professional identity. They do not establish a current employer, current title, current board status, or current availability. The module does not claim that Dr. Joseph reviewed, endorsed, delivered, or approved this curriculum.

Before alpha, the program must directly confirm participation, schedule, session format, recording permission, accessibility needs, preparation materials, and final biography wording. If he cannot participate, the program must approve a qualified clinician-led substitute who can preserve the same decision and defense outcomes. A substitution must be recorded; it cannot be silently implied.

## 4. Ownership and authority boundary

The learner owns the submitted analysis and recommendation. Faculty own curriculum assessment. Named human reviewers own their review findings. A fictional governance council may accept the curriculum package, require revision, refer, or stop within the case exercise.

A real clinical organization would own any local protocol, approval, data, staffing, safety, privacy, and implementation decision. Clinicians retain review and override. Patient-safety, accessibility, privacy, security, and operations owners may stop an affected route within their authority.

The following are prohibited in this module:

- real-patient scoring;
- acceptance of a clinical threshold;
- clinical alerting or clinical action;
- beginning a silent-mode evaluation;
- implementation;
- a production connection; and
- deployment.

No learner, model, analyst, or agent receives clinical authority or a decision or sign-off right. The module may recommend that a later human council consider a bounded proposal. It may not submit, approve, start, or operate that proposal.

## 5. Assessable learning outcomes

By the end of Module 07, the learner can:

1. preserve exact Week 3 and Week 6 evidence without recomputation or selective omission;
2. distinguish curriculum-package completeness from clinical readiness;
3. state the intended use, intended user, workflow moment, possible action, nonaction, and prohibited action in one coherent product brief;
4. explain what the public, synthetic, modeled, sandbox, safety, monitoring, and ML evidence can and cannot establish;
5. preserve the absence of an accepted clinical threshold;
6. translate alert burden, access, equity, disability, language, privacy, workflow, override, and hidden-work findings into leadership consequences;
7. describe the prototype accurately without claiming interoperability, accessibility, local validity, safety, or utility;
8. build a safety case with human ownership, independent failure detection, fallback, stop, restart, and retirement;
9. propose the evidence and governance needed before a later local silent-mode request could be considered;
10. compare progression alternatives and choose one with an explicit evidence chain;
11. record disagreement without treating silence as agreement;
12. communicate the same decision in technical and accessible forms;
13. disclose material agent use and reject unsupported claims;
14. defend the recommendation under structured questioning; and
15. state exactly what remains outside course authority.

## 6. Sixteen-hour clinician-led sequence

The module uses four clinician-led segments of four hours each.

| Segment | Focus | Work product | Clinician contribution |
|---:|---|---|---|
| 1 | Clinical purpose, uncertainty, and evidence chain | intended-use brief and evidence synthesis | tests whether the proposed support serves a defensible clinical moment |
| 2 | Workflow, burden, access, staff voice, and patient consequences | workflow brief, prototype disclosure, and disagreement record | probes hidden work, override, trust, exclusion, and practical failure |
| 3 | Safety, monitoring, governance, and future evaluation | safety case, monitoring plan, conditions, and evaluation proposal | challenges ownership, stop authority, silence detection, and reconsideration evidence |
| 4 | Recommendation, communication, and defense | final recommendation, accessible communication, and 14-question defense | leads the decision conference and tests the boundary between analysis and authorization |

Each segment combines evidence review, a case conference, structured critique, revision, and a short defense rehearsal. The clinician does not replace methods, interoperability, accessibility, privacy, safety, or patient review. The clinician helps learners connect those records to clinical judgment and responsibility.

## 7. Accepted checkpoint identities

Module 07 accepts exactly two cumulative inputs.

| Input | Version | Commons release | Files | Candidate-manifest SHA-256 | Accepted points |
|---|---|---:|---:|---|---:|
| `oclc-app4-cp01` | `0.1.0` | `0.80.0` | 263 | `4e78d2313ce324fd372e6fc187afee333b27ed0cc0270c6ab8c08354dd5c3151` | 40 |
| `oclc-app4-cp02` | `0.1.0` | `0.84.0` | 1,047 | `14ac12dd890045dce21cdc44a9b614770b8b2428bd71a1d4f5eb9cc9de63d642` | 25 |

The accepted Checkpoint 01 release record has SHA-256 `8f637bef551ebe5cb91e93b3b91fef51f25736d07168b904851405c703b62c03`. The accepted Checkpoint 02 release record has SHA-256 `05e65b59f0d4c4b33dc341256141e39c02cfffc32e22aca546dbb85384cb1221`.

The assembler rebuilds each accepted reference package through its own builder, invokes its validator, verifies file count and manifest identity, and then copies every file. This is chain of custody, not a selective export.

## 8. Immutable clinical, evidence, and threshold facts

The continuing fictional service is `CGH-GIM-01`. The intended use is a nonbinding advisory asking the clinician responsible for the current adult encounter to consider confirmatory HbA1c testing after required information is available and before encounter close.

The advisory does not diagnose diabetes, order testing, change treatment, deny care, target a patient for nonclinical action, or act without clinician review.

The accepted historical evidence contains:

- 16 complete NHANES XPT files;
- 34,221,200 raw bytes and 145,563 component rows;
- 14,892 age-eligible audit rows;
- 7,544 fixed model rows and 328 observed HbA1c outcomes;
- 3,652 development rows and 156 outcomes;
- 1,806 temporal-holdout rows and 97 outcomes; and
- 2,086 transport-stress rows and 75 outcomes.

`LBXGH >= 6.5%` is an observed laboratory cut-point indicator for this teaching analysis. It is not a clinical diagnosis. NHANES supports historical teaching evidence but cannot establish local validity, clinical utility, causal benefit, workflow fit, or implementation readiness.

Six candidate thresholds remain unaccepted: `0.020`, `0.030`, `0.040`, `0.050`, `0.075`, and `0.100`. The Module 02 `0.20` value remains a rejected mechanics fixture. Module 07 cannot select or accept a threshold.

## 9. Immutable workflow, prototype, safety, monitoring, and ML facts

Module 04 generated 1,200 synthetic encounter opportunities and 7,200 candidate event rows. `panel-t003` is a passive contextual-panel mechanics fixture, not an accepted clinical design. `0.03000000` was used only to produce bounded sandbox cases.

The local sandbox contains 31 cases, 184 FHIR R4-shaped prefetch resources, 31 response envelopes, and 61 trace events. Seventeen inherited failure modes remain visible. Independent ledgers detect one seeded silent failure. One malformed-card accessibility defect is blocked from release.

The safety and monitoring package contains:

- 22 retained hazards;
- 20 accepted monitoring measures;
- eight seeded monitoring scenarios;
- 12 human-owned escalation routes; and
- zero automatic clinical actions.

Monitoring thresholds are teaching triggers, not validated clinical control limits. FHIR R4 and CDS Hooks artifacts are teaching message shapes, not evidence of conformance or production interoperability.

The fixed gradient-boosted challenger uses the same 7,544 rows, target, predictors, analytic weights, splits, missing-input rule, threshold candidates, and alert budgets as the transparent model. Eight of 11 replacement rules pass. R03 fails with temporal-holdout AUC difference `-0.00743486`. R04 fails with transport-stress AUC difference `-0.01928938`. R08 fails with worst supported subgroup AUC degradation `0.10385240`. The transparent model remains retained.

## 10. Reference leadership conclusion

The reference curriculum-package status is `accept with conditions`. The 35-point Module 07 component scores 35.00 of 35.00, all 26 noncompensable gates pass, and the defense is adequate for curriculum construction.

The separate CDS recommendation is `revise before seeking local silent-mode approval` because:

- no clinical threshold is accepted;
- the malformed-card accessibility defect remains blocked;
- a silent failure was detected and requires local independent reconciliation and ownership;
- FHIR and CDS Hooks artifacts remain teaching shapes;
- local clinical, workflow, burden, access, equity, privacy, security, safety, and utility evidence is absent; and
- R03, R04, and R08 fail, so the challenger does not replace the transparent model.

The final checkpoint is permitted for curriculum construction only. Real-patient scoring, clinical threshold acceptance, clinical alerting or action, silent-mode evaluation, implementation, production connection, and deployment remain prohibited.

## 11. Candidate package architecture

The deterministic learner and reference candidates each contain 1,347 files:

| Layer | Files | Manifest treatment |
|---|---:|---|
| Module 07 immutable controls | 8 | hashed and versioned |
| Accepted Checkpoint 01 package | 263 | copied byte for byte and hashed |
| Accepted Checkpoint 02 package | 1,047 | copied byte for byte and hashed |
| Accepted checkpoint release records | 2 | copied byte for byte and hashed |
| Leadership records | 26 | editable and excluded from the immutable manifest |
| Generated release manifest | 1 | sorted identity of immutable content |
| Total | 1,347 | 1,320 immutable rows |

The release manifest is 319,268 bytes with SHA-256 `8fc03ea9a7ebce8e0e4bf350b2699c5f74ec4a9c5ae493f25f26c94be8c2cea9`.

Reference and learner candidates contain the same immutable evidence. They differ only in the 26 leadership records. Reference records are complete teaching examples. Learner records contain visible placeholders and cannot pass complete validation.

## 12. Required leadership records

Every submission includes these 26 records:

1. `README.md`: package identity, disposition, boundaries, and navigation.
2. `product-brief.md`: intended use, user, workflow moment, action, nonaction, prohibited action, and recommendation.
3. `evidence-synthesis.md`: exact accepted evidence and limits.
4. `logic-input-threshold.md`: rule, inputs, timing, terminology, unavailable states, and unaccepted threshold record.
5. `workflow-patient-consequences.md`: alert burden, hidden work, access, equity, trust, override, and staff voice.
6. `prototype-disclosure.md`: sandbox scope, tests, failures, accessibility block, and interoperability limits.
7. `safety-case.md`: hazards, controls, owners, escalation, fallback, stop, restart, and retirement.
8. `monitoring-silent-failure-plan.md`: measures, independent reconciliation, unavailable states, human notice, and zero automation.
9. `evaluation-proposal.md`: current no-request disposition and evidence required for a later bounded proposal.
10. `stewardship-governance-retirement.md`: lifecycle ownership and decision rights.
11. `stakeholder-roles.csv`: 17 roles with accountability, decision right, consultation, and status.
12. `recommendation-and-alternatives.md`: package status, CDS recommendation, alternatives, fallback, and return path.
13. `disagreement-record.md`: five structured unresolved disagreements and escalation routes.
14. `leadership-reflection.md`: uncertainty, competing priorities, responsibility, and learning.
15. `accessible-communication.md`: staff and patient explanation without unsupported reassurance.
16. `technical-appendix.md`: exact numerical, threshold, prototype, safety, monitoring, and ML evidence.
17. `evidence-index.csv`: accepted checkpoint identities, file counts, hashes, points, and dispositions.
18. `reproducibility-check.md`: commands, package identity, manifest identity, and pending independent reproduction.
19. `responsible-claims-audit.md`: supported, bounded, and rejected claims.
20. `ai-use.md`: material agent use, data boundary, verification, revision, and human accountability.
21. `component-score.csv`: five criteria plus exact 35-point total.
22. `gate-results.csv`: 26 ordered noncompensable gates.
23. `conditions-register.csv`: 16 open conditions with owner and evidence needed.
24. `technical-defense.md`: 14 ordered questions with answer, evidence, consequence, and limit.
25. `reviewer-record.md`: 14 reviewer roles and explicit pending status.
26. `progression-decision.md`: curriculum status, CDS recommendation, final-checkpoint handoff, and prohibited authority.

## 13. Product brief, recommendation, alternatives, and revision path

The product brief must make the clinical purpose understandable without overselling the evidence. It states who receives the advisory, at what moment, with what information, and what the person may consider. It also states what the tool does not do.

The recommendation record separates two judgments:

- Is the curriculum package complete enough to assess and carry forward?
- Is the CDS concept ready to support a local silent-mode approval request?

The alternatives analysis must consider all four allowed recommendations. It must explain why each rejected option is not selected from the accepted record. A selected revision path names the unresolved condition, accountable owner, evidence needed, independent check, and decision body that may reconsider it.

A later silent-mode proposal would need explicit population, duration, data minimization, no-care-action controls, independent reconciliation, safety oversight, patient and staff protections, analysis, stopping, reporting, and retirement. Module 07 describes those requirements but does not submit or approve the protocol.

## 14. People, workflow, access, equity, and communication

Leadership analysis must address:

- whether the clinical moment is appropriate;
- what work appears before, during, and after the advisory;
- who receives visible work and who inherits hidden follow-up work;
- whether alert burden is proportionate;
- how clinicians review, override, defer, or decline;
- what patients may understand, fear, expect, or be unable to access;
- language, disability, digital, transportation, cost, and follow-up barriers;
- whether staff can raise a concern without blame or retaliation;
- what happens when a resource, terminology, unit, time, interface, or monitoring signal is unavailable; and
- who may pause or stop the affected route.

The accessible explanation must say that no patient is being scored, no tool is being used in care, no threshold is accepted, and the malformed-card fixture remains blocked. It cannot claim that the prototype is accessible, interoperable, safe, effective, or locally useful.

Silence from staff or patients is not agreement. Missing feedback is not evidence of acceptability. A disagreement record must preserve the concern even when the curriculum recommendation can proceed with conditions.

## 15. Safety, monitoring, governance, disagreement, and retirement

The safety case retains all 22 hazards and all 20 monitoring measures. It connects each hazard to detection, control, accountable human, escalation, fallback, stop, restart, and retirement. It cannot close a hazard by assertion or treat unavailable monitoring as a passing result.

Silent-failure detection requires independent request, response, terminal-trace, and human-notice evidence. A missing output cannot silently become a negative result. Every monitoring action remains human owned; automatic actions total zero.

Governance must assign stewardship for intended use, logic, terminology, historical evidence, models, threshold and alert budget, interface and accessibility, safety, monitoring, privacy, security, and the released candidate. Any material change requires a new version and renewed review.

The concept must be stopped or retired when no defensible intended use or accountable owner remains, required data or controls cannot be maintained, independent failure detection is unavailable, burden or exclusion cannot be addressed, benefit cannot justify harm, or safe fallback and stop authority cannot be guaranteed.

## 16. Accessibility, reproducibility, privacy, and responsible claims

Every quantitative or visual claim needs an exact structured alternative. Meaning cannot depend on color alone. Evidence tables preserve denominator, outcome count, missingness, support, uncertainty, suppression, source, time, and limit when relevant.

The repository contains public historical data and explicitly synthetic workflow data. It must not receive protected or identifiable patient, clinician, employee, or workplace data. No credential or production endpoint belongs in the package or an external agent prompt.

Reproduction requires a clean rebuild of both accepted checkpoints, an exact 1,320-row immutable manifest, 1,347 candidate files, complete reference validation, and an independent human record before alpha.

Responsible claims distinguish among observed public evidence, synthetic mechanics, modeled estimates, sandbox tests, governance proposals, and authorization. Package acceptance is not clinical authorization. A passing sandbox test is not interoperability. A threshold table is not threshold approval. A silent-mode proposal is not permission to score patients.

## 17. Thirty-five-point assessment

| Criterion | ID | Points | Evidence |
|---|---|---:|---|
| Evidence integrity and synthesis | E01 | 8 | accepted identities, exact facts, limits, and no upstream rewrite |
| Clinical product judgment | C01 | 9 | intended use, workflow, patient consequence, recommendation, and alternatives |
| Leadership and communication | L01 | 8 | uncertainty, burden, access, staff voice, disagreement, and accessible explanation |
| Governance, safety, and stewardship | G01 | 6 | ownership, monitoring, failure detection, stop, reconsideration, and retirement |
| Handoff, reproducibility, and defense | H01 | 4 | release identity, AI disclosure, reviewer state, and technical defense |
| Total |  | 35 |  |

The minimum numeric score is 28 of 35, but all noncompensable gates must also pass. The reference earns 35.00 of 35.00. Points cannot compensate for changed upstream evidence, a falsely accepted threshold, hidden failure, lost accessibility block, unsupported clinical claim, absent human owner, expanded authority, or incomplete defense.

## 18. Twenty-six noncompensable gates

The gate record contains ordered IDs `G01` through `G26`:

1. accepted Checkpoint 01 identity;
2. accepted Checkpoint 02 identity;
3. complete immutable manifest;
4. unchanged evidence and point history;
5. bounded intended use and prohibited action;
6. no accepted clinical threshold;
7. design and sandbox mechanics disclosed;
8. all visible and silent failures retained;
9. malformed-card accessibility defect remains blocked;
10. all 22 hazards retained;
11. all 20 monitoring measures retained;
12. independent silent-failure detection preserved;
13. all escalation and stop routes are human owned;
14. automatic clinical actions remain zero;
15. fixed ML comparison and failed rules remain exact;
16. transparent model remains retained;
17. patient, access, equity, privacy, and staff consequences addressed;
18. clinical override and hidden work addressed;
19. disagreement recorded without invented consensus;
20. stewardship and retirement assigned;
21. evaluation proposal remains a future human-governance request;
22. accessible communication is accurate and bounded;
23. responsible claims and material agent use are disclosed;
24. 16 open conditions remain owned and unresolved;
25. reviewer and reproduction state remain explicit; and
26. no clinical, silent-mode, implementation, production, or deployment authority is added.

The reference passes 26 of 26. A single gate failure blocks progression regardless of numeric score.

## 19. Fourteen defense questions

The technical defense contains 14 ordered questions. Every response has an exact answer, evidence path, decision consequence, and limit. The questions cover:

1. exact frozen checkpoint identities;
2. intended use and prohibited action;
3. what NHANES can and cannot establish;
4. why no clinical threshold is accepted;
5. what `panel-t003` and `0.03000000` mean;
6. prototype evidence and interoperability limits;
7. visible, silent, and accessibility failures;
8. hazard, monitoring, escalation, and automatic-action counts;
9. alert burden, hidden work, access, and staff voice;
10. transparent-versus-ML decision and failed rules;
11. package acceptance versus CDS readiness;
12. evidence required before reconsideration;
13. ownership, stop authority, disagreement, and retirement; and
14. exact final-checkpoint permission and absent authority.

An adequate defense is required for curriculum construction. It is not a clinical approval hearing and cannot convert pending human review into authorization.

## 20. Assembly, validation, and failure tests

`assemble_candidate.py` uses only the Python standard library. It:

1. builds both accepted reference checkpoints;
2. invokes each checkpoint validator with its correct command interface;
3. verifies exact file, manifest, and release identities;
4. copies eight controls, 1,310 checkpoint files, and two release records;
5. adds 26 reference or learner leadership records;
6. creates a sorted six-field immutable manifest;
7. refuses an existing target; and
8. proves two reference builds have the same manifest identity.

`validate_candidate.py` verifies safe paths, every manifest byte and SHA-256, provenance, checkpoint identities, clinician boundary, exact evidence, score, gates, conditions, roles, recommendation, defense, reviewer state, reproduction record, and absent authority.

The complete reference passes 9,436 checks. The learner starter passes 9,351 structural and immutable-evidence checks but is rejected as complete. Copied-candidate validation passes. Thirty deliberate failure routes are rejected, including changed checkpoint evidence, altered manifest provenance, false threshold or deployment authority, lost clinician boundary, hidden failure, waived accessibility defect, altered safety or ML evidence, incorrect points or gates, falsely closed conditions, incomplete defense, false review, missing immutable evidence, and unfinished learner work.

## 21. Release gates, conditions, and final-checkpoint handoff

Module 07 is a runnable release candidate when:

- the module and Commons versions are exact;
- all 1,347 files are present;
- all 1,320 immutable rows verify;
- the manifest is 319,268 bytes with SHA-256 `8fc03ea9a7ebce8e0e4bf350b2699c5f74ec4a9c5ae493f25f26c94be8c2cea9`;
- the 35-point score and 26 gates validate;
- all 16 conditions remain explicitly open and owned;
- all 14 defense questions are complete;
- reviewer and clinician participation status remain truthful;
- assembler and validator self-checks pass; and
- every clinical and production boundary remains prohibited.

The final checkpoint may freeze this exact Module 07 candidate, count the 35 points once, require final reviewer and reproduction records, adjudicate the package, and close APP-4 for curriculum construction.

The final checkpoint may not change an accepted upstream byte, recompute evidence, select a threshold, repair or hide a failure, waive the accessibility block, change the retained model, imply clinician endorsement, score a real patient, begin silent mode, alert or act clinically, implement, connect production, or deploy.

Before alpha, the program must confirm Joe Joseph's participation; complete named clinical, informatics, interoperability, safety, workflow, patient, access, equity, accessibility, privacy, security, model-risk, responsible-AI, and independent review; repair and independently verify accessibility; obtain local evidence for any later proposal; complete clean human reproduction; and record the final release authority.

The next isolated build unit is `oclc-app4-cp03`, the official-end-date Clinical Decision Support package.
