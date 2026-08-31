# APP-4 Checkpoint 03 specification: Clinical Decision Support package

## 1. Checkpoint identity and official timing

- Course: `APP-4`, Data for Clinical Decision Support.
- Checkpoint ID: `oclc-app4-cp03`.
- Title: Clinical Decision Support package.
- Version: `0.1.0`.
- Commons release: `0.86.0`.
- Timing: official last day of the assigned MGH Institute half-term.
- Course points: `35`.
- Package path: `courses/clinical-decision-support/checkpoints/03-clinical-decision-support-package/`.
- Required input: accepted `oclc-app4-07@0.1.0` reference candidate.

The published academic calendar controls the actual due date:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

The curriculum uses seven instructional weeks plus the official half-term end date as its planning model. The observed 2026-2027 half-terms span approximately seven to seven and a half weeks, not one universal duration. Checkpoint 03 is therefore tied to the published last day rather than a hard-coded day count.

## 2. Final decisions and receiving audience

The final checkpoint records two different judgments:

1. Is the APP-4 curriculum package complete enough to accept, accept with conditions, revise, or refer?
2. Should the fictional governance council recommend seeking local approval for a bounded silent-mode evaluation, require revision first, refer, or stop?

The reference curriculum disposition is `accept with conditions`. The separate CDS recommendation is `revise before seeking local silent-mode approval`.

The receivers are the APP-4 faculty owner, Joe Joseph, MD, SFHM, as designated clinician of record, a local clinical decision owner role, clinical informatics and interoperability reviewers, patient-safety and workflow reviewers, patient and access reviewers, survey-methods and model-risk reviewers, accessibility, privacy, security, responsible-AI reviewers, and an independent reproducer.

Package acceptance cannot become threshold acceptance, approval to score a patient, permission to begin silent mode, or authorization to implement or deploy.

## 3. Course-point preservation and score map

The course total is:

`40 + 25 + 35 = 100`

| Cumulative checkpoint | Accepted source | Course points | Final handling |
|---|---|---:|---|
| Week 3 | Checkpoint 01 | 40 | frozen and not rescored |
| Week 6 | Checkpoint 02 | 25 | frozen and not rescored |
| Official end date | Module 07 final component | 35 | reviewed and counted exactly once |
| Total |  | 100 | zero duplicated points |

The final component retains five criteria: E01 evidence integrity for 8 points, C01 clinical CDS judgment for 9, L01 leadership and evaluation readiness for 8, G01 governance and communication for 6, and H01 reproducibility and defense for 4. Passing requires at least 28 of 35 plus every noncompensable gate and an adequate defense.

The reference score is 35.00 of 35.00. A numeric score cannot compensate for a changed candidate byte, accepted threshold without authority, hidden failure, waived accessibility block, missing owner, incomplete reviewer state, unsupported claim, or expanded clinical authority.

## 4. Accepted candidate identity

Checkpoint 03 accepts exactly one Module 07 candidate identity:

- Module: `oclc-app4-07@0.1.0`.
- Commons release: `0.85.0`.
- Candidate files: `1,347`.
- Immutable manifest rows: `1,320`.
- Immutable manifest bytes: `319,268`.
- Immutable manifest SHA-256: `8fc03ea9a7ebce8e0e4bf350b2699c5f74ec4a9c5ae493f25f26c94be8c2cea9`.
- Module release bytes: `4,590`.
- Module release SHA-256: `8e2eada4dadc30d92976963bc8bd01639ea851b88e115464801ee9900ed6e7cd`.
- Accepted Checkpoint 01 release SHA-256: `8f637bef551ebe5cb91e93b3b91fef51f25736d07168b904851405c703b62c03`.
- Accepted Checkpoint 02 release SHA-256: `05e65b59f0d4c4b33dc341256141e39c02cfffc32e22aca546dbb85384cb1221`.

The final assembler rebuilds the Module 07 reference candidate through its own deterministic assembler, invokes complete Module 07 validation, verifies the immutable manifest and all three accepted release identities, and copies all 1,347 files byte for byte. Checkpoint 03 cannot select a subset or repair an upstream record.

## 5. Ownership and out-of-scope boundary

The learner owns the submission. Faculty own course assessment and curriculum disposition. Named human reviewers own their findings. A fictional governance council receives the separate CDS recommendation.

A real clinical organization would own any local purpose, threshold, protocol, patient-data, privacy, security, staffing, safety, implementation, or deployment decision. Clinicians retain review and override. Patient-safety, accessibility, privacy, security, and operational owners may stop an affected route within their authority.

Checkpoint 03 prohibits:

- real-patient scoring;
- clinical threshold acceptance;
- clinical alerting;
- clinical action;
- silent-mode evaluation;
- implementation;
- production connection; and
- deployment.

No learner, analyst, model, interface, dashboard, or agent receives clinical authority or a decision or sign-off right.

## 6. Final workflow and workload

The final checkpoint is an adjudication workflow, not a new analytic assignment.

1. The learner identifies one clean Module 07 candidate and source commit.
2. The assembler reconstructs and validates the accepted candidate.
3. The final manifest freezes every copied file.
4. The learner submits the ten final-review records.
5. Faculty and reviewers inspect score, gates, conditions, claims, reproduction, and defense.
6. The clinician-led panel tests clinical meaning, uncertainty, burden, access, failure response, stop authority, and absent authority.
7. The faculty owner records package disposition separately from the CDS recommendation.
8. The release remains a construction candidate until named review, independent reproduction, and exact-commit authorization are complete.

The checkpoint adds review and defense time only within the course's existing 112.5-hour plan. It does not extend the course or introduce a fourth graded component.

## 7. Final package architecture

The final learner and reference packages each contain 1,362 files.

| Layer | Files | Treatment |
|---|---:|---|
| Frozen Module 07 candidate | 1,347 | copied byte for byte and represented in final manifest |
| Checkpoint version | 1 | copied into `final-review/` |
| Accepted Checkpoint 01 release | 1 | copied and hash verified |
| Accepted Checkpoint 02 release | 1 | copied and hash verified |
| Accepted Module 07 release | 1 | copied and hash verified |
| Final candidate manifest | 1 | generated from all 1,347 frozen files |
| Final-review records | 10 | complete reference or visible learner prompts |
| Total | 1,362 | 1,347 manifest rows plus 15 review files |

The final candidate manifest is 295,377 bytes with SHA-256 `217a64aad1cbaf5bde9fb2e9a1bd5325140b6a82f20541818b7e1cfd170d17b3`.

The final-review files are outside the frozen candidate manifest so they can record that manifest's measured identity without self-reference. Learner and reference packages have the same frozen candidate and differ only in the ten final-review records.

## 8. Ten final-review records

1. `submission-record.md` records repository, commit state, versions, release identities, final manifest identity, calendar rule, validation, submitter, and proposed tag.
2. `final-score.csv` records the five criteria and exact 35-point result.
3. `gate-results.csv` records 26 ordered gates, evidence, reviewer, and condition links.
4. `final-defense.md` records 14 ordered questions with exact answer, evidence, consequence, and limit.
5. `reviewer-record.md` records all 14 required roles and truthful pending status.
6. `final-reproduction.md` records candidate, manifest, release, validator, two-build, refusal, and independent-human status.
7. `conditions-register.csv` records 16 open conditions, owners, due points, evidence, verifiers, and escalation triggers.
8. `final-audit.md` checks identity, evidence, threshold, failure, accessibility, safety, monitoring, ML, score, decisions, claims, agents, and authority.
9. `final-decision.md` records the final score, gates, defense, separate decisions, threshold, design, model, conditions, authority, course status, and tag state.
10. `release-acceptance.md` explains what the receiver gets, allowed use, prohibited use, change and stop rules, owners, and tag authorization.

Every learner template contains a visible completion prompt. Complete validation rejects any remaining `REPLACE`, `TODO`, or `TBD` marker.

## 9. Final reviewer roles

The final record requires 14 roles:

1. APP-4 faculty owner;
2. Joe Joseph, MD, SFHM, clinician of record;
3. local clinical decision owner;
4. patient-safety reviewer;
5. workflow and human-factors reviewer;
6. patient or caregiver reviewer;
7. equity, language, and disability-access reviewer;
8. clinical informatics and interoperability reviewer;
9. survey-methods and calibration reviewer;
10. model-risk and biostatistics reviewer;
11. accessibility reviewer;
12. privacy, data-governance, and security reviewers;
13. responsible-AI reviewer; and
14. independent reproducer.

One qualified person may cover multiple roles only when the record states qualifications, conflicts, and independence. Construction does not imply sign-off. The reference claims no completed named review, no current clinical authorization, and no clinician participation or endorsement.

## 10. Twenty-six final gates

The 26 final gates cover:

1. all three accepted release identities;
2. exact 1,347-file candidate and final manifest;
3. exact 1,320-row Module 07 immutable manifest;
4. commit, versions, releases, and proposed tag;
5. source, data-class, fictional-service, and prohibited-data boundaries;
6. intended use, action, nonaction, timing, and prohibited action;
7. six unaccepted thresholds and rejected `0.20` fixture;
8. `panel-t003` and `0.03000000` as mechanics fixtures only;
9. all 17 failures;
10. the blocked accessibility defect;
11. all 22 hazards and safety life cycle;
12. all 20 measures and unavailable states;
13. 12 human escalation routes and zero automatic actions;
14. historical evidence limits and absent local evidence;
15. workflow burden, hidden work, override, staff voice, and blame protection;
16. patient access, language, disability, cost, privacy, equity, and recourse;
17. fixed ML comparison and failed R03, R04, and R08;
18. retained transparent model and no accepted threshold;
19. exact point accounting;
20. separate package and CDS decisions;
21. future evaluation as a local human-governance proposal;
22. ownership, disagreement, stop, restart, and retirement;
23. accessibility, claims, AI disclosure, and reproduction;
24. all 16 open conditions;
25. all 14 defense answers and reviewer roles; and
26. course completion, tag state, decisions, and authority prohibitions.

Every gate must be `pass` or `pass with condition`. Any linked condition must be one of C01 through C16. A failed gate stops final acceptance regardless of score.

## 11. Final defense questions

The defense asks 14 questions about:

1. the exact decision;
2. strongest evidence and greatest limitation;
3. intended and prohibited actions;
4. absent threshold acceptance;
5. sandbox meaning and limits;
6. accessibility and silent failure;
7. safety-case meaning;
8. silent and unavailable monitoring;
9. failed ML replacement rules;
10. patient and staff consequences;
11. disagreement without blame;
12. evidence for reconsideration;
13. material agent use and verification; and
14. why curriculum acceptance can coexist with a revise recommendation.

Each response must include the exact answer, accepted evidence path, decision consequence, and limit. The reference is adequate for curriculum construction. A live or approved equivalent clinician-led defense remains pending before alpha and cannot be fabricated by the construction record.

## 12. Learner and reviewer workflows

The learner starts from a complete Module 07 candidate and the ten prompted final-review records. The learner may not edit a frozen candidate file. Any candidate change requires a new Module 07 version and rebuilt final package.

Faculty first verify identity and point accounting. Domain reviewers then assess their assigned gates and conditions. The clinician-led review tests clinical meaning and decision ownership. The independent reproducer verifies clean assembly, copied release identities, exact manifests, and complete validation.

Reviewers record disagreements and conditions rather than forcing consensus. Silence is not agreement. A reviewer may withhold acceptance within their domain. The faculty owner cannot convert a pending clinical, safety, accessibility, privacy, or independent review into an approval claim.

## 13. Automated validation and failure routes

`assemble_final.py` uses the Python standard library. It rebuilds and validates Module 07, verifies release fingerprints, copies 1,347 files, generates the final manifest, renders measured manifest identity into review records, refuses existing targets, and refuses a target inside the candidate.

To stay within local storage limits, production assembly still makes real byte copies, while disposable self-check trees try standard-library hard links and fall back to real copies on volumes that do not support them. A repository test runner supplies the same fallback to frozen upstream validators without changing their accepted bytes. Every path, byte count, and SHA-256 is still validated. Mutation clones are removed as soon as their route is checked, and the final validator detaches each changed file before mutation and restores the clean source afterward, so the 20 negative routes never alter the reference.

Complete reference validation passes 6,817 checks. Learner structural validation passes 6,785 checks. Two independent assemblies match. Copied and reconstructed Module 07 validation passes.

Twenty deliberate failure routes are rejected: changed candidate, changed release, invalid score, failed gate, early tag, changed recommendation, false silent-mode authorization, falsely accepted threshold, changed model, waived accessibility defect, hidden failure, missing reviewer, closed condition, incomplete defense, hidden agent boundary, duplicated final score, accepted-design claim, false clinical action, false clinician-participation claim, and changed course status. Complete mode also rejects the learner prompts.

## 14. Reference status

The reference result is:

- final score: `35.00 of 35.00`;
- course score: `40 + 25 + 35 = 100`;
- gates: `26 of 26 pass or pass with an allowed condition`;
- defense: `adequate for curriculum construction`;
- package disposition: `accept with conditions`;
- CDS recommendation: `revise before seeking local silent-mode approval`;
- accepted clinical threshold: `none`;
- selected design: `panel-t003 mechanics fixture only`;
- ML decision: `retain transparent model`;
- open conditions: C01 through C16; and
- course status: `complete for curriculum construction only`.

The reference preserves all 17 failures, the blocked malformed-card accessibility defect, the detected silent failure, 22 hazards, 20 measures, 12 human escalation routes, zero automatic actions, failed R03/R04/R08 rules, and absent local clinical evidence.

## 15. Release and tag rule

The proposed annotated tag is:

`app4-clinical-decision-support-candidate-v0.1.0`

Its status is `proposed - not created`. Construction does not create the tag.

Tag authorization requires named human review, confirmed clinician participation or an approved substitution, clean independent reproduction, an adequate live or approved equivalent defense, resolved release-blocking conditions, and confirmation that the exact reviewed commit contains the validated package.

Any changed frozen candidate byte requires a new Module 07 semantic version and rebuilt Checkpoint 03. Any changed final-checkpoint control or review contract requires a new checkpoint version and new Commons release.

## 16. Completion and next-course handoff

Checkpoint 03 closes APP-4 for curriculum construction. The course catalog may now state that all seven APP-4 modules and all three checkpoints are runnable release candidates.

The next isolated build unit is APP-5 Module 01 under its distinct domain decision and source contract. APP-5 may reuse shared foundations and open-data infrastructure, but it may not inherit APP-4's fictional clinical decision, thresholds, model, prototype, score, or governance conclusion as its own evidence.

APP-4 remains available for named review, learner rehearsal, independent reproduction, and future revision. Closing curriculum construction does not promote it to alpha or authorize clinical evaluation.

## 17. Known conditions before alpha

All 16 conditions remain open:

- confirm Joe Joseph's participation, schedule, format, recording permission, and biography wording;
- confirm the local clinical purpose, action, nonaction, owner, and reconsideration question;
- select and justify any proposed threshold and alert budget through local governance;
- repair and independently verify the malformed-card accessibility defect;
- review local FHIR, CDS Hooks, terminology, units, time, version, suppression, trace, and unavailable-state behavior;
- verify all 22 hazards and complete safety routes locally;
- reproduce silent-failure detection from independent ledgers;
- collect local workflow, burden, hidden-work, override, and staff-voice evidence;
- review patient benefit, harm, language, disability, access, cost, privacy, recourse, and equity;
- approve data minimization, access, retention, security, incident, and credential boundaries;
- independently reproduce historical evidence, calibration, subgroup support, and the ML decision;
- name accountable local owners;
- draft and independently review a separate bounded protocol without starting it;
- complete the live or approved equivalent 14-question defense;
- assign the official APP-4 section and half-term dates; and
- run clean independent assembly and confirm the exact reviewed commit.

Until the applicable conditions are resolved, the tag remains uncreated and real-patient scoring, threshold acceptance, alerting, clinical action, silent-mode evaluation, implementation, production connection, and deployment remain prohibited.
