# APP-2 Final checkpoint: Patient-experience and engagement package

## 1. Checkpoint identity and official timing

- Checkpoint ID: `oclc-app2-cp03`.
- Checkpoint version: 0.1.0.
- Commons release target: 0.64.0.
- Course: APP-2, Data for Patient Experience and Engagement.
- Due: official last day of the assigned MGH Institute half-term.
- Course weight: 35 percent, or 35 course points.
- Required input: complete APP-2 Module 07 candidate version 0.1.0.
- Status target: runnable release candidate.

The official calendar controls the submission date:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

The phrase "7.5 weeks" is a planning model. The final checkpoint is due on the published last day of the assigned half-term, not on a date inferred by adding 7.5 weeks.

## 2. Final decisions and receiving audience

The checkpoint records a package disposition and a separate organizational recommendation.

Allowed package dispositions are `accept`, `accept with conditions`, `revise`, and `refer`. Only `accept` and `accept with conditions` pass the course package gate.

Allowed organizational recommendations are `run bounded prospective measurement and improvement test`, `revise before testing`, `refer`, and `stop`.

The reference package disposition is `accept with conditions`. Its organizational recommendation is `revise before testing`.

The receiving audience is the clinical service, patient advisory group, patient-experience leaders, and governance reviewers who would decide whether a local proposal is ready for design and authorization review. Package acceptance does not authorize contact, fielding, official HCAHPS reporting, patient or group targeting, clinical implementation, or model deployment.

## 3. Course-point preservation and score map

The checkpoint records Module 07's draft 35-point component once as the final course score.

| ID | Recurring criterion | Points |
|---|---|---:|
| M01 | Correct measurement, response, linked-evidence, and model reasoning | 7.00 |
| P01 | Patient partnership, equity, access, and shared authority | 8.00 |
| L01 | Leadership recommendation, feasibility, safety, and ownership | 8.00 |
| A01 | Patient-facing communication, monitoring, feedback, and accountability | 7.00 |
| H01 | Reproducibility, accessibility, responsible agent use, and defense | 5.00 |
| Total |  | 35.00 |

Passing requires at least 28.00 points, every noncompensable gate, an adequate defense, `accept` or `accept with conditions`, and one allowed organizational recommendation.

The final checkpoint does not add another 35 points to the Module 07 draft. It replaces the draft with the reviewed course record. APP-2 totals 100 points: 20 at Week 3, 45 at Week 6, and 35 on the official half-term end date.

## 4. Accepted candidate identity

The checkpoint accepts one complete Module 07 candidate with:

- 358 files;
- a 334-row immutable release manifest;
- the complete 149-file Checkpoint 01 package;
- the complete 174-file Checkpoint 02 package;
- exact Checkpoint 01 and Checkpoint 02 release records;
- nine Module 07 controls; and
- 23 completed leadership records.

The accepted Module 07 release record is 5,032 bytes with SHA-256 `2a30f59869be0041b813ce6005c226a9bcd3cd28632222464a5defc1586ca317`. Its immutable candidate manifest is 64,149 bytes with SHA-256 `53bd306692145df85d1b2a709615000f80829099a916659c6a8cfd3bd994697f`.

## 5. Ownership and out-of-scope boundary

The final checkpoint owns the whole-candidate freeze, 358-row final manifest, accepted release checks, final score, 26 gates, 14-question defense, reviewer and independence record, final reproduction, audit, conditions, package disposition, organizational recommendation, course-completion statement, and proposed tag.

Module 07 retains ownership of the evidence synthesis, patient-facing summary, partnership record, recommendation, stakeholder roles, workflow, bounded plan, measures, feedback, stop rules, reflection, appendix, evidence index, accessibility, agent use, draft score, gates, conditions, defense, reviewers, and progression decision.

Checkpoints 01 and 02 retain all accepted technical evidence. The final checkpoint freezes and adjudicates the package. It does not recompute or silently edit that evidence.

The checkpoint does not change an instrument, score, frame, response mechanism, weight, linkage rule, denominator, comment corpus, codebook, group-support rule, model, threshold, partnership statement, or accepted output. It cannot authorize contact, fielding, official reporting, targeting, implementation, or deployment. It cannot create an accepted tag before named human authorization of the exact reviewed commit.

## 6. Final workflow and workload

The checkpoint uses work already included in Module 07's 16 hours:

1. validate the complete Module 07 candidate;
2. assemble it into a protected final target;
3. verify the 358-row candidate manifest;
4. confirm all three accepted release identities;
5. complete the final score, 26 gates, reviewer, reproduction, audit, conditions, and decisions;
6. deliver the accessible clinician and patient leadership handoff;
7. answer all 14 final defense questions;
8. record package disposition and organizational recommendation separately;
9. rerun complete validation;
10. commit the exact reviewed state; and
11. create the proposed annotated tag only after named human authorization.

## 7. Final package architecture

The final assembler copies all 358 Module 07 candidate files without modification and adds 15 files under `final-review/`:

- `CHECKPOINT-VERSION`;
- `checkpoint1-release.json`;
- `checkpoint2-release.json`;
- `module07-release.json`;
- `candidate-manifest.csv` with 358 sorted rows; and
- ten final-review records.

The complete final package contains exactly 373 files. No accepted candidate file is overwritten by the final review.

The 358-row final candidate manifest is 60,523 bytes with SHA-256 `a3ca6bbacd22ab82d6679feb674f061ee98db9e681fc18deba5cc8ee9a93183b`.

## 8. Ten final-review records

1. `submission-record.md` records repository, source commit, versions, fingerprints, due-date rule, validator result, submitter, and proposed tag.
2. `final-score.csv` records the five fixed criteria and exact 35-point total.
3. `gate-results.csv` records all 26 gates, evidence, reviewer, result, and condition.
4. `final-defense.md` records direct answers to all 14 questions and adequacy.
5. `reviewer-record.md` records required roles, independence, evidence, decisions, and acknowledgments.
6. `final-reproduction.md` records clean checkout, environment, commands, manifest comparison, validators, reproducer, and unresolved conditions.
7. `conditions-register.csv` records carried and final conditions, owners, due points, evidence, verifiers, status, and escalation triggers.
8. `final-audit.md` combines source, rights, data-class, integrity, privacy, accessibility, agent-use, evidence-index, partnership-status, and prohibited-use checks.
9. `final-decision.md` records score, gates, defense, package disposition, organizational recommendation, authorization boundary, and course status separately.
10. `release-acceptance.md` states what the receiver gets, allowed use, prohibited use, conditions, support owner, change rule, stop triggers, and tag status.

## 9. Final reviewer roles

Required coverage includes the APP-2 faculty owner; Joe Joseph, MD, SFHM, as clinician of record; a local clinical decision owner; patient/caregiver co-lead; patient-experience measurement reviewer; survey-methods reviewer; health-services data reviewer; qualitative-methods reviewer; equity reviewer; access and language reviewer; privacy and data-governance reviewer; responsible-AI and model reviewer; improvement and operations reviewer; and independent reproducer.

One person may cover more than one role when qualifications and independence are recorded. The learner cannot be the patient/caregiver co-lead, clinical decision owner, or independent reproducer.

Reference construction may use role-based pending conditions. It cannot represent a completed learner defense, actual patient partnership, organizational authorization, or named program approval.

## 10. Twenty-six final gates

The 26 gates require exact Checkpoint 01, Checkpoint 02, and Module 07 release identities; exact candidate and manifest counts; exact Module 07 manifest identity; repository, commit, version, release, and proposed-tag records; source, rights, data-class, and prohibited-data review; measurement and response boundaries; linked denominators; generated-comment limits; group support; honest partnership status; shared authority; claim traceability; separate decisions; an allowed recommendation and authorization boundary; universal offer without targeting; explicit local workflow assumptions; patient-facing communication; feedback and accountability; 14 measures; transparent model non-adoption; 14 stop rules; access routes; reproduction and responsible agent use; adequate defense, reviewers, and conditions; and a final acceptance that preserves every prohibited use.

Any failed gate returns the package for revision or referral. Numeric strength cannot waive a changed byte, unsupported claim, fabricated patient voice, inaccessible evidence, missing safety route, hidden agent use, or absent decision owner.

## 11. Final defense questions

The defense asks learners to state the exact leadership decision; strongest and weakest evidence; missing patient and caregiver voice; measurement boundary; linked denominator; generated-comment use; group-support meaning; current partnership status; reason for universal offer; reason ML does not change the decision; local feasibility needs; patient-facing accountability; stop and restart rules; and agent use and the separation between package acceptance and organizational recommendation.

An adequate answer cites an exact path or registered fact, explains its clinical, patient, measurement, or operational meaning, and states the decision limit.

## 12. Learner and reviewer workflows

The learner freezes the complete Module 07 candidate at a full commit, assembles the final checkpoint into a new target, verifies the final manifest, completes the ten review records, delivers an accessible handoff, answers all 14 questions, corrects findings in the owning record without changing accepted evidence, reruns validation, obtains separate decisions, and commits the exact reviewed package.

Reviewers confirm the official due date and candidate identity, scan for prohibited data and hidden dependencies, validate Module 07 and both nested checkpoints, trace claims, review partnership status and shared authority, review workflow and measures, reproduce the package, conduct the defense, complete the score and gates, record conditions and decisions, and rerun validation against the exact reviewed state.

The proposed tag may be created only after the required named humans authorize the exact commit.

## 13. Automated validation and failure routes

The validator checks the exact 373-file tree, safe paths, 358-row final manifest, candidate byte and SHA-256 equality, exact 334-row Module 07 manifest, reconstructed Module 07 validation, all accepted release identities, score arithmetic, 26 gates, eight conditions, 14 defense answers, 14 reviewer roles, reproduction, audit, separate decisions, zero actual patient statements in the reference, tag status, placeholders, plain ASCII dashes, and portable paths.

The assembler refuses an existing target and a target inside the candidate. It copies accepted bytes and never moves or deletes them.

Self-checks cover the reference, learner starter, changed candidate, invalid score, failed gate, early tag, false partnership claim, and inconsistent decision routes.

The complete reference passes 1,890 checks. The learner starter passes 1,841 checks.

## 14. Reference status

The reference records a final score of 35.00 of 35.00, 26 gates that pass or pass with an allowed condition, an adequate construction defense, package disposition `accept with conditions`, organizational recommendation `revise before testing`, and course status `complete for curriculum construction only`.

It proposes tag `app2-patient-experience-engagement-candidate-v0.1.0` with status `proposed - not created`. Contact, fielding, official HCAHPS reporting, targeting, clinical implementation, and model deployment remain prohibited.

Named program review, actual patient/caregiver co-lead participation, clinician confirmation, a live or equivalent defense, independent human clean reproduction, and final tag authorization remain pending before alpha.

## 15. Release and tag rule

The annotated tag may be created only after an allowed package disposition, complete named human approval, direct patient/caregiver co-lead review, adequate learner defense, independent clean reproduction, exact-commit confirmation, and explicit tag authorization.

The tag identifies an accepted curriculum package. It does not authorize patient contact, survey fielding, official reporting, a workflow test, implementation, model deployment, targeting, or a claim of benefit.

## 16. Completion and next-course handoff

An accepted final package closes APP-2 for curriculum construction. It carries exact release and commit identity, accepted technical evidence, a bounded leadership recommendation, patient-facing communication, partnership and disagreement conditions, workflow and access assumptions, measures and stop rules, evidence and accessibility records, agent and human accountability, and an explicit statement of what remains unauthorized.

APP-3 may use the Commons architecture and public-data principles. It does not inherit APP-2's patient-experience case as its evidence base unless its own specification names a release, fingerprints it, and states what it reuses and what it owns.

## 17. Known conditions before alpha

- Joe Joseph, MD, SFHM, confirms participation, schedule, format, recording permission, and final biography wording.
- A named and compensated patient/caregiver co-lead completes direct review under agreed preparation, access, authority, attribution, recording, disagreement, and withdrawal terms.
- Named clinical, measurement, survey, data, qualitative, equity, access, privacy, governance, operations, model, responsible-AI, and independent reviewers complete review.
- A qualified person completes clean reproduction on a supported teaching environment.
- The official section and half-term dates are assigned from the published calendar.
- A live or equivalent learner defense and reviewer acknowledgment workflow is tested.
- No reference package is described as authorization for contact, fielding, reporting, targeting, implementation, or deployment.
