# APP-3 Checkpoint 03 build plan

## Objective

Build `oclc-app3-cp03`, the final clinical performance improvement package, as a deterministic runnable release candidate at version `0.1.0` and Commons release `0.75.0`.

The checkpoint closes the 7.5-week course for curriculum construction. It freezes the exact Module 07 candidate, records the 35-point component once, adjudicates the package, and keeps clinical test authorization separate and prohibited.

## Accepted input

| Input | Version | Commons | Files | Immutable manifest | Manifest SHA-256 | Release SHA-256 |
|---|---:|---:|---:|---:|---|---|
| `oclc-app3-07` | 0.1.0 | 0.74.0 | 416 | 389 rows | `cd88ad1910ca35d231da734f919f58420e2f3f25deda9135ee6ca8c20105d2fc` | `5dcec682080346570e89915473a9b2939c15cf57a28a15250137694d056486e2` |

The accepted Module 07 release record is 4,532 bytes. Checkpoint 03 also pins the accepted Checkpoint 01 release SHA-256 `270b4e49d1c21d8faf7243cd11cef1dddea836d32be551dfe72edac771b31f27` and Checkpoint 02 release SHA-256 `b8af80b7e07c2eac2aeb0e9206533bfae134f55d69a5df9038a7a9a915c4dd05`.

## Timing and score

- Due point: official last day of the assigned MGH Institute half-term.
- Calendar: https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf
- Planning language: 7.5 weeks.
- Final component: 35 points.
- Minimum passing score: 28 points.
- Course total: `40 + 25 + 35 = 100`.
- Double-counted components: zero.

Checkpoint 03 replaces Module 07's draft score with the reviewed final record. It does not add another 35 points.

## Package architecture

The final assembler copies all 416 Module 07 candidate files without modification. It adds 15 files under `final-review/`:

1. `CHECKPOINT-VERSION`;
2. `checkpoint1-release.json`;
3. `checkpoint2-release.json`;
4. `module07-release.json`;
5. `candidate-manifest.csv` with 416 sorted rows;
6. `submission-record.md`;
7. `final-score.csv`;
8. `gate-results.csv`;
9. `final-defense.md`;
10. `reviewer-record.md`;
11. `final-reproduction.md`;
12. `conditions-register.csv`;
13. `final-audit.md`;
14. `final-decision.md`; and
15. `release-acceptance.md`.

The complete package contains 431 files. Its 416-row final candidate manifest is 70,531 bytes with SHA-256 `b41acddef7397f9e55deee99f815b3d586d246f2353bbd92cf0873654499e8b6`.

## Score contract

| ID | Criterion | Points |
|---|---|---:|
| E01 | Correct evidence, decision, and claim boundary | 8.00 |
| C01 | Clinical performance reasoning, safety, access, and workforce judgment | 9.00 |
| L01 | Leadership recommendation, feasibility, alternatives, and ownership | 8.00 |
| M01 | Monitoring, stewardship, escalation, disagreement, and communication | 6.00 |
| H01 | Reproducibility, accessibility, responsible agent use, and defense | 4.00 |
| Total |  | 35.00 |

## Decision contract

Allowed package dispositions are `accept`, `accept with conditions`, `revise`, and `refer`.

Allowed clinical performance recommendations are `run bounded prospective improvement test`, `revise before testing`, `refer`, and `stop`.

The reference decisions are:

- package disposition: `accept with conditions`;
- clinical performance recommendation: `revise before testing`;
- selected scenario: `none`;
- accepted forecast: `seasonal exponential smoothing`;
- ML decision: `retain transparent forecast`;
- course status: `complete for curriculum construction only`;
- tag status: `proposed - not created`; and
- clinical action, staffing and schedule changes, automated action, test start, implementation, production scoring, and model deployment: `prohibited`.

## Final gates

The 26 final gates retain the Module 07 gate architecture while adding final release, commit, score, reviewer, reproduction, condition, decision, and tag adjudication. A score cannot compensate for a failed gate.

The gates protect:

- all three release identities;
- the exact 416-file candidate and final manifest;
- the 389-row Module 07 immutable manifest;
- repository, version, source commit, and tag status;
- fictional-service, public-source, synthetic, and no-linkage boundaries;
- unchanged measures, signals, safety limits, diagnosis, forecast, scenario failures, feasibility, monitoring, and ML decision;
- exact 40, 25, and 35-point accounting;
- claim traceability and responsible agent use;
- people, access, equity, safety, workforce, burden, ownership, and disagreement;
- stewardship, escalation, fallback, communication, accessibility, and reproduction;
- 14 adequate defense answers;
- complete reviewers and 12 open conditions; and
- separate package and clinical decisions with every action boundary preserved.

## Defense contract

The 14 final defense questions retain the Module 07 decision topics and require final-review answers about release identity, strongest and weakest evidence, signal and cause, forecast and staffing, scenario failure, feasibility, unavailable evidence, monitoring, ML non-adoption, people and burden, disagreement, ownership, responsible agent use, and the separation between package acceptance and clinical authorization.

Every answer cites an exact package path or registered fact, explains the practical consequence, and states a limit.

## Reviewer and condition contract

Required review coverage includes:

- APP-3 faculty owner;
- Joe Joseph, MD, SFHM, as clinician of record;
- local clinical decision owner;
- safety reviewer;
- improvement and simulation reviewer;
- operations and capacity reviewer;
- workforce reviewer;
- access and equity reviewer;
- measurement and statistical-process reviewer;
- forecasting reviewer;
- responsible-AI and ML reviewer;
- accessibility and communication reviewer; and
- independent reproducer.

The 12 Module 07 conditions carry into final review with explicit owners, due points, evidence, verifiers, open status, and escalation triggers. Reference construction does not claim any pending human review occurred.

## Validation contract

The assembler must:

- validate the Module 07 candidate before copying;
- verify its 416 files and 389-row manifest;
- verify Module 07 and both checkpoint release hashes;
- refuse an existing target;
- refuse a target inside the candidate;
- copy every accepted byte;
- write a sorted 416-row final manifest; and
- produce the same package identity twice.

The validator must check:

- the exact 431-file tree;
- all 416 final-manifest rows, bytes, SHA-256 values, and roles;
- the 389-row Module 07 manifest and its exact fingerprint;
- all three copied release identities;
- reconstructed Module 07 validation;
- exact course score and no duplication;
- 26 gates and 12 conditions;
- 14 substantive defense answers;
- all 13 reviewer roles;
- reproduction, audit, decision, and acceptance records;
- proposed tag status;
- placeholders, portable paths, and ASCII punctuation; and
- deterministic mutation and incomplete-package failures.

## Failure routes

Self-checks reject changed candidate evidence, changed copied release identity, invalid score, failed gate, early tag creation, changed recommendation, false test authorization, changed accepted forecast, selected scenario drift, hidden unavailable evidence, missing reviewer, closed pending condition, incomplete defense, hidden agent use, duplicate final scoring, and a complete-mode learner template. Complete validation passes 2,177 checks and learner validation passes 2,131 checks. All 15 failure routes and complete-mode learner rejection pass.

## Semver and integration

1. Write the durable 17-section specification.
2. Build the contract, controls, ten reference records, and ten learner templates.
3. Assemble the exact Module 07 candidate twice and measure the final manifest.
4. Pass final reference, learner, copied, and failure-route validation.
5. Record exact package and validation identities in release metadata and docs.
6. Advance Commons from 0.74.0 to 0.75.0.
7. Update the APP-3 course package, course spec, root catalog, ledger, and curriculum checker.
8. Run APP-3 and full curriculum regressions.
9. Commit, push, and verify the remote commit before moving to APP-4.

## Completion definition

Checkpoint 03 is complete only when the package is deterministic, all validation gates pass, the course closes for curriculum construction, all pre-alpha human conditions remain honest, the tag remains uncreated, no clinical authority is granted, and the exact commit is pushed and verified.
