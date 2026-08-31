# APP-4 Checkpoint 01 build plan

## Purpose

Build `oclc-app4-cp01`, Logic, evidence, calibration, and validation readiness, as the cumulative end-of-Week-3 release at Checkpoint version `0.1.0` and Commons release `0.80.0`.

The checkpoint asks whether the accepted use case, logic, historical evidence, calibration, threshold comparisons, and claim limits may enter Module 04 curriculum work. It does not select a clinical threshold, authorize a prototype, permit real-patient scoring, display an alert, diagnose, order, implement, or deploy.

## Accepted module identities

The builder must assemble complete reference workspaces from the accepted module builders. It must not copy only selected outputs or reconstruct a module from memory.

| Module | Version | Commons release | Assembled files | Immutable rows | Manifest bytes | Manifest SHA-256 | Week 3 points |
|---|---:|---:|---:|---:|---:|---|---:|
| `oclc-app4-01` | 0.1.0 | 0.77.0 | 41 | 29 | 3,404 | `40ff7384d227a38b0f93832731d984098e6e6f3324a958dafc2319d23f282b45` | 0 |
| `oclc-app4-02` | 0.1.0 | 0.78.0 | 86 | 73 | 10,564 | `bf3a30d66944a799a1dcbb3bc971bbcc81a6a3986e3e08cacf26fac41ecb9ded` | 20 |
| `oclc-app4-03` | 0.1.0 | 0.79.0 | 118 | 102 | 16,354 | `e67f20599704f83ec1e695f23f571fb57c558109bde3bcc676a64afc3dcf8e22` | 20 |
| Total |  |  | 245 | 204 | 30,322 |  | 40 |

Module 01 remains a required zero-point gate. Module 02 contributes 20 points once, and Module 03 contributes 20 points once. No criterion or component may be rescored or duplicated.

## Fixed cumulative evidence

The checkpoint must preserve these accepted facts:

- 16 complete official NHANES XPT sources, 145,563 component rows, 34,221,200 raw bytes, and 3,149,043 deterministic gzip bytes;
- fictional service `CGH-GIM-01`, its clinician user, encounter moment, nonbinding confirmatory-testing concept, explicit nonaction, stop rights, and prohibited actions;
- a 1,000-adult Synthea 4.0.0 release with 25 FHIR files, 811,803 resource rows, zero parse failures, and 11,109 retained duplicate provider or organization IDs;
- 16 deterministic mechanics cases with passing ordered traces;
- a Module 02 mock score and `0.20` branch value that remain rejected mechanics fixtures;
- 14,892 age-eligible historical audit rows and 7,544 model rows with 328 observed HbA1c outcomes;
- 3,652 development rows with 156 outcomes, 1,806 untouched temporal-holdout rows with 97 outcomes, and 2,086 separate transport-stress rows with 75 outcomes;
- one fixed survey-weighted binomial GLM fit only on development evidence;
- temporal-holdout and transport performance, calibration, subgroup support, and uncertainty records;
- evidence candidates `0.02`, `0.03`, `0.04`, `0.05`, `0.075`, and `0.10`, all unselected and unaccepted; and
- no diagnostic, clinical, real-patient, implementation, or deployment authority.

## Checkpoint records

The learner and reference workspaces require nine checkpoint records:

1. `README.md`;
2. `evidence-index.csv`;
3. `logic-evidence-readiness-review.md`;
4. `checkpoint-score.csv`;
5. `checkpoint-gates.csv`;
6. `checkpoint-defense.md`;
7. `reproducibility-check.md`;
8. `ai-use.md`; and
9. `progression-decision.md`.

The evidence index must name all three accepted modules and their exact nested manifests. The score must preserve the six Module 02 criteria and 11 Module 03 criteria for a total of 40 points. The checkpoint must add no new course points.

## Checkpoint integrity gates

All 20 gates are noncompensable:

1. all three accepted module identities and complete reference workspaces are exact;
2. the 245-row candidate manifest is sorted and complete;
3. all 204 nested immutable rows match their accepted manifests;
4. Module 01 source identities, completeness, intended use, and authority limits remain exact;
5. the service remains fictional and the concept remains nonbinding;
6. the complete synthetic source identity, duplicate count, and limitations remain visible;
7. all 16 mechanics cases and ordered traces pass;
8. the Module 02 score and `0.20` value remain rejected mechanics fixtures;
9. the historical target remains an observed laboratory cut-point indicator, not a diagnosis;
10. development, temporal holdout, and transport partitions remain separate, with zero holdout or transport fitting;
11. survey weights, strata, PSUs, and the transport phlebotomy weight remain explicit;
12. model coefficients, performance, calibration, and evidence identities reproduce;
13. all six evidence thresholds remain present, unselected, and unaccepted;
14. threshold burden, missed-case, and decision-curve quantities remain descriptive and do not prove benefit;
15. the 2021-2023 release remains a separate transport stress test;
16. unsupported subgroup performance remains suppressed and no group action is authorized;
17. Module 01 contributes zero points, and Modules 02 and 03 contribute 20 points once each;
18. all 12 Module 01, 12 Module 02, 12 Module 03, and 20 checkpoint gates pass;
19. the defense, reproduction, AI, claims, ownership, and condition records are complete; and
20. progression permits only bounded Module 04 curriculum construction while every clinical-use and deployment route remains prohibited.

Any failed inherited or checkpoint gate forces `revise` or `refer` regardless of the numeric score.

## Progression contract

The reference decision is `continue with conditions`.

Module 04 may compare the six unaccepted evidence thresholds, candidate-card burden, missed eligible cases, human-factors risks, equity and access consequences, a less interruptive alternative, and no alert. A qualified human governance process may develop a candidate-design recommendation inside Module 04, but this checkpoint accepts no clinical threshold and grants no real-use authority.

Module 05 prototype construction remains gated by Module 04. Module 06 safety, monitoring, governance, and embedded ML work remains gated by Modules 04 and 05. Live scoring, clinical alerting, ordering, treatment, implementation, production connection, and deployment remain prohibited.

## Verification and release

1. Assemble two reference workspaces and require identical candidate manifests.
2. Assemble and validate the incomplete learner workspace.
3. Verify every candidate file against the 245-row manifest and every nested immutable file against its module manifest.
4. Run the accepted Module 01 profiler and validator, Module 02 release and logic verifiers, and Module 03 evidence and workspace verifiers from the checkpoint test path.
5. Validate the exact 40-point score, 56 inherited gates, 20 checkpoint gates, 14-question defense, AI record, progression, and authority boundaries.
6. Reject changed or missing candidates, manifest drift, duplicated points, failed gates, promoted `0.20`, an accepted threshold, diagnosis language, retuning, unsupported subgroup claims, incomplete defense, copied answers, invalid Module 04 permission, and deployment claims.
7. Write the durable 17-section checkpoint specification and the protected Module 04 handoff.
8. Advance Commons from `0.79.0` to `0.80.0`.
9. Run the complete curriculum regression.
10. Commit, push, and remote-verify Checkpoint 01 before building Module 04.
