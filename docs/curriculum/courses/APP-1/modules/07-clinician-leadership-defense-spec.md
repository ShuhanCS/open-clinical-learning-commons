# APP-1 Module 07: Clinician leadership, recommendation, and defense

## 1. Module identity and place in the course

- Module ID: `oclc-app1-07`.
- Module version: 0.1.0.
- Commons release target: 0.55.0.
- Course: APP-1, Data for Clinical Care.
- Block: final clinician-led leadership block.
- Workload: 16.0 hours.
- Course component: 35-point clinical care improvement brief, finalized at Checkpoint 3.
- Required inputs: accepted APP-1 Checkpoints 1 and 2, both version 0.1.0.
- Status target: runnable release candidate.

Module 07 turns the accepted technical case into a bounded organizational recommendation. It does not change the cohort, refit a model, revise accepted findings, award another set of points, or authorize clinical action.

## 2. Decision, audience, and claim boundary

### Decision

What should a hospital medicine care-improvement council do next, who owns that action, how should it be tested, and when must it stop or change?

### Receiving audience

The primary receiver is a hospital medicine medical director or care-improvement council. The panel also includes an improvement lead, clinical operations lead, patient or caregiver partner, scheduling or access lead, equity reviewer, methods reviewer, and data steward.

### Allowed recommendations

- `run bounded prospective improvement test`;
- `revise before testing`;
- `refer`; or
- `stop`.

The reference recommendation is `revise before testing`. The synthetic retrospective evidence supports a testable question and a prospective measurement plan. It does not support implementing a workflow, targeting patients, deploying a model, or claiming benefit.

## 3. Clinician of record and publishable biography

Joe Joseph, MD, SFHM, is the designated clinician of record for this leadership block.

The course uses only dated public facts from Sound Physicians:

- Sound Physicians listed Joe Joseph, MD, as a Fellow in Hospital Medicine in 2015: https://www.soundphysicians.com/press-release/sound-physicians-actively-participating-hospital-medicine-2015/
- Sound Physicians listed Joe Joseph, MD, as a Senior Fellow in Hospital Medicine in 2017: https://www.soundphysicians.com/press-release/sound-physicians-thought-leaders-presenting-at-hospital-medicine-2017-annual-conference/
- Sound Physicians identified Joe Joseph, MD, as a Regional Chief Medical Officer in a 2019 release: https://www.soundphysicians.com/press-release/sound-physicians-acquires-indigo-health-partners/

These sources confirm the intended hospital medicine physician leader. The course makes no claim about his current employer or title. The curriculum sponsor designated him for this block. Direct confirmation of schedule, session format, recording permission, and final biography wording remains a pre-alpha condition.

## 4. Ownership and out-of-scope boundary

### Module 07 owns

- final evidence synthesis;
- bounded clinical recommendation;
- people, equity, safety, workflow, and feasibility review;
- stakeholder roles and decision ownership;
- prospective test design;
- process, outcome, balancing, access, and implementation measures;
- monitoring, reassessment, rollback, stop, and escalation rules;
- leadership reflection;
- accessible technical appendix and evidence index;
- 35-point draft component score and noncompensable gates;
- accountable agent-use record;
- 12-question defense; and
- recommendation and progression decisions.

### Upstream ownership retained

Checkpoints 1 and 2 retain ownership of source identity, phenotype, cohort, time zero, follow-up, censoring, survival evidence, proportional-hazards screen, risk adjustment, site extension, expected outcomes, variation, equity analysis, pathway evidence, improvement draft, and simple-versus-machine-learning comparison.

### Out of scope

- changing an accepted upstream byte without a new version and renewed review;
- fitting, selecting, tuning, recalibrating, or deploying a model;
- creating a patient-level targeting list;
- claiming that scheduled follow-up causes fewer acute returns;
- ranking real clinicians, sites, or demographic groups;
- certifying fairness, quality, access, safety, or clinical value in a real population;
- using real patient, workplace, restricted, identifiable, secret, or credential data; and
- authorizing a live clinical test or workflow change.

## 5. Learning outcomes

By completing the module, the learner can:

1. state the decision, population, pathway, evidence, and claim boundary in clinical language;
2. distinguish a package decision from a clinical recommendation;
3. explain the strongest evidence and the condition that most narrows it;
4. explain why the failed proportional-hazards screen prevents a constant hazard ratio from leading the case;
5. interpret risk-adjusted and variation evidence without treating adjustment as causal proof;
6. explain why the machine-learning extension does not change the improvement decision;
7. identify people who may benefit, carry burden, or be missed;
8. define a bounded prospective test with a comparison and learning aim;
9. assign accountable, responsible, consulted, and informed roles;
10. define measures with denominators, sources, cadence, owners, and triggers;
11. state when the work must pause, stop, roll back, or be referred;
12. provide equivalent access to every decision-relevant display and table;
13. separate agent assistance from verified evidence and human ownership; and
14. defend a specific recommendation under clinical and operational questioning.

## 6. Sixteen-hour clinician-led sequence

| Segment | Hours | Main work | Clinician role |
|---|---:|---|---|
| Clinical decision conference | 4.0 | Read the accepted evidence as a medical director; define the decision and claim boundary | Leads case conference and tests clinical meaning |
| People, workflow, and stakeholder lab | 4.0 | Map affected people, burden, roles, workflow, safety, feasibility, and missing local evidence | Leads tradeoff and ownership review |
| Recommendation and monitoring studio | 4.0 | Draft the prospective test, measures, triggers, stop rules, and council brief | Challenges recommendation and monitoring logic |
| Council defense and feedback | 4.0 | Deliver the accessible handoff and answer 12 questions | Chairs defense and records clinical conditions |

The clinician of record leads the leadership framing and defense standard. Faculty may support data, methods, access, and assessment work. If a live session is unavailable, an approved recorded case conference plus a qualified clinician-led synchronous defense preserves the same standard.

## 7. Accepted evidence and immutable facts

### Accepted release identities

| Unit | Version | Commons release | Accepted fingerprint |
|---|---:|---:|---|
| Checkpoint 1, longitudinal and survival readiness | 0.1.0 | 0.51.0 | release SHA-256 `ef2ee1dd1fcac47dda2efd680b9605862a0006962867d59a836dec4c276b090c` |
| Checkpoint 2, adjusted variation and feasible improvement | 0.1.0 | 0.54.0 | release SHA-256 `58cc270fad6649feec5e958b0850ea3dff3a8119599c30f2e900d68ad5f591da` |

Checkpoint 1 assembles 91 files and freezes a 78-row candidate manifest with SHA-256 `ef5ace3d6b450473f5b7ab8c1b53bf24f63aa42910b1fdab5d72c617f4f57860`.

Checkpoint 2 assembles 113 files and freezes a 100-row candidate manifest with SHA-256 `f5f892c2b5f6c193f5389c10f7e60df81b1400ca5a163734a103efa745c54ed1`.

### Case facts that must remain visible

- 518 people enter the initial cohort and 476 enter the day-30 landmark cohort.
- The landmark cohort has 87 acute-return events and 389 administrative censors.
- The scheduled-follow-up group has 129 people; the no-recorded-scheduled-follow-up group has 347.
- The proportional-hazards screen p-value is 0.00636020 and fails the declared screen.
- The reference analysis therefore leads with count-first Kaplan-Meier and fixed-time evidence, not one constant hazard ratio.
- The transparent benchmark has held-out Brier score 0.09609243 and AUC 0.66363212.
- The bounded random forest has held-out Brier score 0.10745654 and AUC 0.62371615.
- At the educational threshold, the transparent benchmark flags 25 people with weighted error cost 44; the random forest flags 60 with weighted cost 67.
- Machine learning does not change the improvement decision.
- Offer, preference, acceptance, appointment status, completion, barriers, and burden are not observed in the retrospective source.
- The source is synthetic. No estimate is a real prevalence, effect, quality, access, equity, site, or deployment result.

## 8. Reference leadership conclusion

The reference package recommends `revise before testing`.

The council should retain the question of whether a universal discharge follow-up scheduling offer is feasible and acceptable. Before any live test, the organization must supply a local workflow map, service capacity, named clinical and operational owners, prospective offer and preference fields, appointment and completion states, safety and workload measures, a patient-partner review, and local governance approval.

The reference package rejects model-based targeting. The bounded random forest does not improve the held-out decision evidence enough to justify its larger flag burden, and the source cannot establish clinical utility.

## 9. Candidate package architecture

The assembler creates a protected candidate with:

- eight immutable Module 07 controls;
- the complete 91-file accepted Checkpoint 1 package;
- the complete 113-file accepted Checkpoint 2 package;
- exact copies of both checkpoint release records;
- 21 editable leadership records; and
- one generated immutable release manifest.

The release manifest has 214 sorted rows: eight controls plus 206 accepted evidence files. It is 40,140 bytes with SHA-256 `2c90713fb220b6fdc1af492898e89605051b0dffed44b2fb2883b2942aefde62`. The complete candidate has 236 files. Checkpoint packages are nested under `evidence/checkpoint1/` and `evidence/checkpoint2/`. Release records are nested under `evidence/provenance/`.

## 10. Required leadership records

1. `README.md` identifies the decision, audience, status, and ordered workflow.
2. `evidence-synthesis.md` traces the strongest evidence, discordant evidence, uncertainty, and claim boundary.
3. `improvement-recommendation.md` records one allowed recommendation and its rationale.
4. `people-equity-safety.md` identifies benefit, burden, exclusion, safety, and equity questions.
5. `stakeholder-roles.csv` assigns accountable, responsible, consulted, and informed roles.
6. `workflow-feasibility.md` defines the current and proposed workflow, capacity questions, and failure points.
7. `bounded-test-plan.md` defines setting, eligibility, intervention, comparison, duration, learning aim, and authorization boundary.
8. `measures-monitoring.csv` defines process, outcome, balancing, access, implementation, and data-quality measures.
9. `stop-escalation-rules.csv` defines triggers, actions, owners, and restart requirements.
10. `leadership-reflection.md` explains the learner's decision role, tradeoffs, and accountability.
11. `technical-appendix.md` preserves exact analytic facts and limitations.
12. `evidence-index.csv` maps every material claim to an exact evidence path and owner.
13. `accessibility-review.md` records equivalent access routes.
14. `reproducibility-check.md` records package validation and immutable evidence comparison.
15. `ai-use.md` records agent use, independent checks, corrections, and human owner.
16. `component-score.csv` contains the draft 35-point source score.
17. `gate-results.csv` records all 24 noncompensable gates.
18. `conditions-register.csv` assigns every open condition, owner, due point, verifier, and escalation trigger.
19. `technical-defense.md` answers all 12 defense questions.
20. `reviewer-record.md` records roles, independence, evidence, and decision scope.
21. `progression-decision.md` records package status, recommendation, final-checkpoint permission, and prohibited use separately.

## 11. Recommendation and prospective-test contract

A recommendation must state:

- the exact clinical and operational decision;
- eligible population and exclusions;
- proposed workflow change;
- universal or targeted reach;
- comparison or baseline;
- test duration and review cadence;
- named accountable and responsible owners;
- capacity and training requirements;
- patient and caregiver involvement;
- process, outcome, balancing, access, implementation, and data-quality measures;
- stop, rollback, escalation, and reassessment rules;
- evidence that would support continuation, revision, or termination; and
- what remains unauthorized.

The reference proposal is universal offer and prospective measurement, not model targeting. It remains a proposal until local leaders, patient partners, operations owners, and governance reviewers authorize a specific protocol.

## 12. People, equity, safety, and stakeholder requirements

The learner must identify:

- people eligible for the proposed workflow;
- people likely to be missed by the source or workflow;
- who receives benefit, burden, added work, or delayed care;
- language, disability, transportation, technology, scheduling, and caregiver needs;
- groups that require count and missingness review before comparison;
- safety risks and unintended consequences;
- the person with authority to authorize, pause, or stop the work; and
- the patient or caregiver role in design and review.

Small groups stay separate and unsupported estimates stay suppressed. A synthetic subgroup result may retain a question. It cannot certify fairness or inequity.

## 13. Measures and monitoring contract

Every measure records:

- measure ID and family;
- operational definition;
- numerator and denominator;
- unit and direction;
- source and collection timing;
- review cadence;
- accountable owner;
- baseline status;
- trigger and action;
- subgroup support rule; and
- missingness rule.

The reference package includes at least two process measures, one outcome measure, two balancing measures, two access measures, one implementation measure, and two data-quality measures. Retrospective synthetic evidence cannot populate the prospective baseline.

## 14. Stop, escalation, rollback, and reassessment

The package must pause or stop for:

- a serious or unexpected patient-safety concern;
- loss of required oversight or accountable ownership;
- material workflow delay or workload beyond declared capacity;
- missing or invalid denominator data beyond the declared trigger;
- a new access burden or unsupported group-specific action;
- unauthorized patient-level targeting or model use;
- a privacy, rights, integrity, or security concern;
- a material mismatch between the reviewed protocol and delivered workflow; or
- evidence that the test cannot answer its learning question.

Each rule names the immediate action, notification route, reviewer, evidence needed to restart, and final authority.

## 15. Accessibility and equivalent defense routes

- Every display has an exact table and structured text alternative.
- The technical appendix identifies the exact evidence paths used in the defense.
- CSV files have headers and one declared row grain.
- Color is never the only carrier of meaning.
- The council brief uses plain clinical language and defines technical terms in place.
- A live, recorded, written, or supported oral defense may be used when the same 12 questions, evidence standard, and follow-up challenge are preserved.

## 16. Responsible agent use and human accountability

The agent record names the tool, date, purpose, request, data classes shared, output used or rejected, material claims, independent check, corrections, retained limits, and human owner.

Agent output is not evidence. A material claim needs a different verification route, such as an exact accepted table, source comparison, validator, independent code path, or qualified human review. No patient, restricted, identifiable, credential, secret, or identity-expanding data may be shared with an external agent.

The learner owns the recommendation. The clinician of record and council own clinical review. The course package does not transfer clinical authority to an agent, learner, analyst, or model.

## 17. Thirty-five-point assessment

Module 07 drafts the final source assessment. Checkpoint 3 records it once as the course grade.

| ID | Recurring criterion | Points |
|---|---|---:|
| C01 | Correct evidence, decision, and claim boundary | 8.00 |
| R01 | Reproducible evidence, package, and handoff | 5.00 |
| L01 | Sound clinical reasoning, equity, safety, and feasibility | 10.00 |
| A01 | Clear and action-guiding recommendation, ownership, and monitoring | 8.00 |
| H01 | Responsible agent use, accessibility, and defense | 4.00 |
| Total |  | 35.00 |

Passing construction review requires at least 28.00 points, all 24 gates, an adequate defense, and a recommendation from the allowed set. A strong brief cannot compensate for changed evidence, an unsupported causal claim, missing safety rules, inaccessible evidence, absent ownership, or hidden agent assistance.

The complete reference drafts 35.00 of 35.00 points because it meets the package standard while recommending revision before a live test.

## 18. Twenty-four noncompensable gates

1. exact accepted Checkpoint 1 identity and 91-file package;
2. exact accepted Checkpoint 2 identity and 113-file package;
3. exact 214-row immutable manifest and protected assembly;
4. repository, version, release, and full candidate identity;
5. synthetic source and rights boundary visible;
6. cohort, time zero, follow-up, event, and censoring facts unchanged;
7. failed proportional-hazards screen and count-first interpretation visible;
8. risk-adjustment, support, and residual-confounding limits visible;
9. variation evidence cannot rank real sites or establish causation;
10. subgroup counts, missingness, uncertainty, and suppression retained;
11. machine learning does not change the decision and is not deployed;
12. every material leadership claim traces to an exact evidence path;
13. one allowed recommendation with explicit authorization boundary;
14. people affected, burden, exclusion, equity, and safety addressed;
15. stakeholder roles include accountable and responsible owners;
16. workflow and capacity assumptions are explicit;
17. bounded test has eligibility, comparison, duration, and learning aim;
18. process, outcome, balancing, access, implementation, and data-quality measures complete;
19. monitoring, reassessment, stop, rollback, and escalation rules complete;
20. exact tables and equivalent accessible routes complete;
21. clean validation and immutable evidence comparison pass;
22. material agent use has an independent check and human owner;
23. all 12 defense answers are adequate; and
24. package status, clinical recommendation, final-checkpoint permission, and prohibited use are separate and consistent.

## 19. Twelve defense questions

1. What exact council decision does this package support?
2. Which evidence is strongest, and which condition most narrows it?
3. Why does the failed proportional-hazards screen change the way you present survival evidence?
4. What does risk adjustment support, and what does it fail to remove?
5. Why does machine learning not change your recommendation?
6. Who may benefit, carry burden, or be missed?
7. Why is the recommendation universal offer and measurement rather than patient targeting?
8. What local workflow and capacity evidence is missing?
9. Which measures would tell you whether the proposed test is being delivered as intended?
10. What would make you pause, stop, roll back, or refer the work?
11. What did an agent contribute, and how did you verify the material contribution?
12. Why can this package pass while the clinical recommendation remains `revise before testing`?

An adequate answer cites a package-specific fact or path, explains its practical meaning, and states the decision limit. Memorized definitions or unsupported confidence are inadequate.

## 20. Assembly, validation, and failure tests

The assembler must:

- refuse an existing target;
- validate both accepted checkpoint packages before copying them;
- copy all accepted bytes without modification;
- verify both release fingerprints and candidate-manifest fingerprints;
- use safe relative paths;
- create a sorted 214-row release manifest; and
- produce deterministic reference and learner candidates.

The validator checks the exact 236-file tree, every immutable byte and SHA-256, nested checkpoint validation, release identity, scoring, 24 gates, 12 defense answers, stakeholder and measure contracts, conditions, recommendation, progression, placeholders, portable paths, and ASCII dashes.

Self-checks must reject an existing target, changed accepted evidence, a changed release identity, an invalid score, a failed gate, an unsupported recommendation, and inconsistent authorization.

The complete reference passes 1,233 checks. The learner starter passes 1,185 checks. The copied candidate validator also passes against the assembled reference.

## 21. Release gates, known conditions, and handoff

The reference package may proceed to final-checkpoint construction as `continue with conditions`. Its clinical recommendation remains `revise before testing`. Clinical implementation and model deployment remain prohibited.

Pre-alpha conditions include:

- Joe Joseph, MD confirms participation, schedule, session format, recording permission, and final biography wording;
- a named hospital medicine clinician reviews the case and reference recommendation;
- named improvement, methods, equity, informatics, accessibility, privacy, responsible-AI, and independent-instructor reviewers complete review;
- a qualified person completes clean reproduction;
- the official course section and half-term dates are assigned; and
- a live or equivalent learner defense and acknowledgment workflow is tested.

The final checkpoint receives the exact complete Module 07 candidate. It may adjudicate the package, score, defense, conditions, and recommendation. It may not silently edit accepted evidence or convert curriculum acceptance into clinical authorization.
