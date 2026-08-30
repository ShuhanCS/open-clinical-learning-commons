# APP-1 Checkpoint 2: Adjusted variation and feasible improvement

## 1. Identity, timing, and role

- Checkpoint ID: `oclc-app1-cp02`.
- Version: `0.1.0`.
- Commons release: `0.54.0`.
- Timing: end of instructional Week 6.
- Course points: 45.
- Package path: `courses/clinical-care/checkpoints/02-adjusted-variation-improvement-release/`.
- Decision owner: clinical care analytics lead with methods, improvement, and equity reviewers.

This is the cumulative technical checkpoint for APP-1. It freezes accepted Modules 04 through 06 without recomputing their evidence and decides whether the case may enter Module 07 clinician leadership review.

## 2. Decision and allowed use

The checkpoint asks: is the analytic case strong enough to support a draft improvement recommendation and Module 07 leadership review?

The package may advance a bounded prospective test proposal for leadership review. It may not authorize a test, implement a workflow, change care, rank a site or group, apply a group-specific threshold, or deploy a model.

## 3. Accepted Week 3 identity

Checkpoint 2 accepts, but does not duplicate or rescore, APP-1 Checkpoint 1:

- ID `oclc-app1-cp01`;
- version `0.1.0`;
- Commons `0.51.0`;
- 78 accepted candidate files; and
- candidate manifest SHA-256 `ef5ace3d6b450473f5b7ab8c1b53bf24f63aa42910b1fdab5d72c617f4f57860`.

The accepted Week 3 package carries the 476-person day-30 cohort and the failed proportional-hazards screen. Its open survival and reviewer conditions remain visible.

## 4. Accepted Module 04 through Module 06 identities

| Module | Version | Commons | Files | Workspace manifest SHA-256 | Points |
|---|---|---|---:|---|---:|
| `oclc-app1-04` | 0.1.0 | 0.52.0 | 32 | `5eaf8ba19e965b437cd4c586a1811b6d4aeb0f5cc82ea585dae2405432c9a8bb` | 25 |
| `oclc-app1-05` | 0.1.0 | 0.53.0 | 30 | `7106a0ec0b412c61768eff72f03062e60cb3d9dfc0a887bb81be8f4475e7363e` | 20 |
| `oclc-app1-06` | 0.1.0 | 0.54.0 | 38 | `b7127dbfac9e7a9549ea682499a1ca5d368a4acbbc20da2e307324be5813b978` | 0 |

The candidate contains exactly 100 accepted component files. A changed nested file, size, hash, version, manifest, source identity, or file count fails the checkpoint.

## 5. Score contract

The 45 course points are assigned exactly once:

| Scored source | Points |
|---|---:|
| Module 04 survival and risk-adjusted outcome analysis | 25.00 |
| Module 05 clinical variation memo | 20.00 |
| Module 06 equity, improvement, and embedded-ML gate | 0.00 |
| Total | 45.00 |

Module 06 is required but not separately scored. Checkpoint 1 is an accepted prerequisite and is not rescored. A 44-, 46-, or double-counted score fails.

## 6. Required survival and risk-adjustment evidence

The package must retain:

- 476 accepted people, 87 later acute returns, and 389 administrative censors;
- log-rank p-value `0.67258471`, which does not prove equivalence;
- unadjusted Cox hazard ratio `1.10542457`;
- failed PH-screen p-value `0.00636020` and the fixed-time/count-first interpretation;
- the four-feature baseline case-mix contract;
- apparent Brier score `0.13490621` and AUC `0.66585409`;
- expected events totaling `87.00000000`;
- adjusted exposure odds ratio `1.16353250`, interval `0.67665877` to `2.00072462`, and p = `0.58392672`;
- standardized, O/E, calibration, bootstrap, and support evidence; and
- synthetic-site provenance, fixed site order, and known direct effect zero.

This evidence is observational and synthetic. It cannot establish benefit, causal effect, fairness, real-site performance, or clinical use.

## 7. Required variation evidence

The package must retain:

- exact treatment-record, procedure, utilization, outcome, clinical-subgroup, site, and time evidence;
- recorded-follow-up range `0.22988506` to `0.37804878`;
- absolute synthetic-site spread `0.14816372`;
- global p-value `0.27993975` and measurement-question conclusion;
- later scheduled-record exposure difference `-0.13129147`;
- medication-record exposure difference `-0.01713469`;
- procedure-record exposure difference `-0.18597949`;
- clinical-composition and residual-confounding review; and
- the rule that medication records are treatment exposure, never adherence.

The checkpoint cannot turn clinical significance into statistical proof or a source-record difference into quality or causal evidence.

## 8. Required equity and accessible-pathway evidence

The checkpoint requires the fixed 12-group equity review with:

- group counts and source-field missingness;
- recorded-follow-up numerators, denominators, Wilson intervals, and process support;
- outcome counts, Wilson intervals, expected events, O/E ratios, and outcome support;
- Native and other race process suppression;
- Asian, Native, and other race outcome suppression;
- no merging of small groups;
- no result-based sorting, ranking, fairness score, or proof-of-inequity claim; and
- conclusion `question retained`.

The accessible pathway must reconcile 476 to 129/347 and then 25/104 and 62/285. It must keep offer, preference, appointment status, completion, barriers, and burden visually and textually separate as proposed collection states. Exact node and edge tables and a structured alternative are required.

## 9. Required feasible-improvement evidence

The draft improvement option is a capacity-aware scheduling workflow before discharge. The package requires:

- documented eligibility screening;
- offer and preference;
- acceptance or decline;
- appointment and capacity status;
- safe escalation;
- completion, cancellation, barriers, and burden;
- a driver diagram linking the aim, primary drivers, secondary drivers, and candidate changes;
- implementation, process, outcome, access, safety, and balancing measures;
- feasibility and workflow ownership;
- patient preference and communication support; and
- unintended-consequence review.

Retrospective synthetic data cannot populate the prospective measures. The checkpoint sends the proposal to leadership review with conditions and does not authorize it.

## 10. Required transparent-versus-ML evidence

Both models use the day-30 prediction time, the same four eligible baseline features, the same time-ordered 333/143 split, the same 143 evaluation rows with 17 events, and threshold `0.20`.

Required held-out comparison:

| Evidence | Transparent GLM | Bounded random forest |
|---|---:|---:|
| Brier score | 0.09609243 | 0.10745654 |
| AUC | 0.66363212 | 0.62371615 |
| Log loss | 0.34684826 | 0.37750998 |
| False positives | 17 | 49 |
| False negatives | 9 | 6 |
| People flagged | 25 | 60 |
| Weighted teaching cost | 44 | 67 |

The paired ML-minus-transparent Brier difference is `0.01136411` with 95% interval `-0.00489999` to `0.02602160`. The AUC difference is `-0.03991597` with interval `-0.16059757` to `0.11721522`.

The forest catches three more events but adds 32 false positives and 35 flags. ML does not change the improvement decision. Calibration, support, subgroup suppression, every false negative, aggregate false-positive burden, leakage, test contamination, and deployment failure must remain explicit.

## 11. Checkpoint controls and editable records

Immutable checkpoint controls are:

- `.gitattributes`;
- `VERSION`;
- `checkpoint-contract.json`;
- `assessment.md`;
- `build_checkpoint.py`; and
- `validate_checkpoint.py`.

Editable checkpoint records are:

- `README.md`;
- `evidence-index.csv`;
- `adjusted-variation-improvement-review.md`;
- `reproducibility-check.md`;
- `ai-use.md`; and
- `progression-decision.md`.

Reference records are complete. Learner records contain explicit prompts. Both packages contain the same accepted candidate.

## 12. Assembly contract

The assembler builds fresh reference workspaces for Modules 04 through 06 through their accepted workspace builders. It copies every file to `candidate/module-04`, `candidate/module-05`, and `candidate/module-06`, then records path, bytes, SHA-256, source module, version, and role in a sorted candidate manifest.

The final package contains:

- 100 candidate files;
- 6 immutable checkpoint controls;
- 6 checkpoint work records; and
- 1 candidate manifest;
- 113 total files.

The 100-row manifest is 17,062 bytes with SHA-256 `f5f892c2b5f6c193f5389c10f7e60df81b1400ca5a163734a103efa745c54ed1`. Learner and reference assembly must produce the same candidate identity. Existing targets are never overwritten.

## 13. Validation and mutation rejection

Validation must verify:

- all 113 expected files and no extras;
- all 100 candidate rows, byte sizes, hashes, module IDs, and versions;
- all three nested manifests and every nested immutable artifact;
- exact source evidence, scores, gates, claim boundaries, AI-use fields, and progression values;
- reference work without placeholders;
- learner work with prompts;
- two deterministic builds;
- copied-validator execution;
- candidate mutation rejection;
- 45-point score mutation rejection; and
- invalid progression rejection.

The reference route passes 496 checks and the learner route passes 473 checks at first release.

## 14. Progression and noncompensable gates

The checkpoint has 18 noncompensable integrity gates. A perfect point score cannot compensate for failed equity support, inaccessible figures, incomplete measures, leaked features, test contamination, unsupported claims, missing reproducibility, missing AI accountability, or implementation/deployment language.

Allowed dispositions are `continue`, `continue with conditions`, `revise`, or `refer`. Module 07 construction is permitted only for `continue` or `continue with conditions`. The reference disposition is `continue with conditions`.

## 15. Reviewers, known limits, and completion

Required reviewers before alpha are a hospital medicine clinician, clinical improvement reviewer, survival and health-services methods reviewers, equity reviewer, clinical informatician, accessibility reviewer, privacy reviewer, responsible-AI reviewer, and independent instructor.

Known limits remain open: the source is synthetic; key access states are unobserved; the Week 3 PH screen failed; outcome and subgroup support is limited; apparent Module 04 performance is in-sample; the ML evaluation has 17 events; and the error cost is educational.

Checkpoint 2 is complete only when the durable spec, contract, learner/reference package, 100-file candidate, exact score, validators, release record, Commons `0.54.0` update, build ledger, commit, and push all pass.
