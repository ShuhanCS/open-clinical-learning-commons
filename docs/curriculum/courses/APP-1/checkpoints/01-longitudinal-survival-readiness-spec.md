# APP-1 Checkpoint 1: Longitudinal and survival readiness

## 1. Checkpoint identity and timing

- Checkpoint ID: `oclc-app1-cp01`.
- Course: APP-1, Data for Clinical Care.
- Timing: end of instructional Week 3.
- Version target: 0.1.0.
- Commons release target: 0.51.0.
- Course points: 20.
- Decision: may the accepted longitudinal cohort and survival evidence enter adjusted comparison?

The official academic calendar controls the submission date. The 7.5-week phrase remains a planning model; this package is due at the end of the third instructional week assigned to the course.

## 2. Accepted component identities

The checkpoint accepts exactly:

- Module 01 `oclc-app1-01` version 0.2.0 at Commons 0.49.1;
- Module 01 workspace-manifest SHA-256 `4f57b0bbf3e510967c5e42691eee990ce523974b7f6ea877f15f46903aa8c147`;
- Module 02 `oclc-app1-02` version 0.1.0 at Commons 0.50.0;
- Module 02 workspace-manifest SHA-256 `9d78f888753b39797ad421d2576eef377ba0bc01fcca02d9ef3c9da388057c10`;
- Module 03 `oclc-app1-03` version 0.1.0 at Commons 0.51.0; and
- Module 03 workspace-manifest SHA-256 `067e1953d7fe7bcfaf878880bef2edf44788b846f71c478282ebe34f1a5d4d52`.

The assembler creates each accepted reference workspace with its own builder, copies it without mutation, and fingerprints every candidate file.

## 3. Decision and readers

The checkpoint asks:

> Is the clinical question measurable, is the day-30 landmark cohort valid, and is the survival evidence transparent enough to begin risk adjustment?

Primary readers are the APP-1 faculty owner, hospital medicine phenotype reviewer, survival-methods reviewer, and learner. The package must let each reader trace the decision from source feasibility through the survival assumption response.

## 4. Frozen clinical question and claim boundary

The clinical question remains whether a hospital medicine council should continue developing a prospective pathway to increase scheduled follow-up within 30 days after an adult's first qualifying acute-care discharge.

The checkpoint is synthetic observational teaching evidence. It supports curriculum progression only. It does not establish access, completion, quality, benefit, harm, equivalence, causation, efficacy, prevalence, fairness, real-site performance, or implementation readiness.

## 5. Cohort and event conservation

The cumulative package must preserve:

- 518 initial index people;
- 9 index deaths;
- 8 early post-discharge deaths;
- 25 early acute returns;
- no overlap among exclusion branches;
- 476 landmark-eligible people;
- 129 scheduled-follow-up and 347 no-recorded-follow-up people;
- 87 later acute returns, divided into 25 and 62 by exposure;
- 389 administrative censors;
- no pre-event competing-death censor; and
- three later deaths after first event.

No checkpoint file may change a person, exposure, event, observed time, censoring reason, site assignment, or field class.

## 6. Required Module 01 evidence

The package freezes the accepted 19-file Module 01 reference workspace. It includes the decision contract, source and feasibility evidence, pathway charter, outcome and evidence standards, stakeholders, improvement options, AI-use record, progression decision, and its own manifest.

Module 01 proves that the question is measurable and identifies the day-30 landmark, early-event exclusions, sparse source organizations, and synthetic claim limits.

## 7. Required Module 02 evidence

The package freezes the accepted 30-file Module 02 reference workspace. It includes the source and extension contracts, four SQL files, phenotype and transformation records, ten released outputs, 20-point assessment, accountable records, and its own manifest.

Module 02 proves the corrected denominator, event-time fields, six-site teaching extension provenance, and survival-ready analysis cohort.

## 8. Required Module 03 evidence

The package freezes the accepted 29-file Module 03 reference workspace. It includes the source and analysis contracts, environment, Python and R code, eight completed work records, eleven survival outputs, assessment gates, and its own manifest.

Module 03 proves the risk tables, fixed-time estimates, log-rank and Cox calculations, failed proportional-hazards screen, death audit, accessible alternative, and required survival-methods referral.

## 9. Exact checkpoint work records

Checkpoint-owned records are:

- `README.md`;
- `evidence-index.csv`;
- `survival-readiness-review.md`;
- `reproducibility-check.md`;
- `ai-use.md`; and
- `progression-decision.md`.

The immutable controls are `.gitattributes`, `VERSION`, `checkpoint-contract.json`, `assessment.md`, `build_checkpoint.py`, and `validate_checkpoint.py`.

## 10. Evidence index contract

The evidence index contains one row for each accepted module. Every row records module ID, version, Commons release, candidate subdirectory, assembled files, workspace-manifest bytes and SHA-256, primary decision, score treatment, gate treatment, and progression.

The index must make clear that Module 02 owns all 20 course points and Module 03 owns the noncompensable survival-readiness gate.

## 11. Twenty-point score map

| Criterion | Points |
|---|---:|
| Decision, target population, phenotype, and index | 4 |
| Source, SQL, longitudinal cohort, follow-up, and censoring | 8 |
| Cohort validation, event audit, and reproducibility | 5 |
| Interpretation, access, and accountable agent use | 3 |
| Total | 20 |

The reference carries `20.00 of 20.00` from Module 02. The checkpoint does not rescore Module 01 or add points for Module 03.

## 12. Noncompensable survival-readiness gates

All 16 Module 03 gates must pass. In addition, the checkpoint requires:

1. all three module identities and manifests match;
2. 78 accepted component files are present before checkpoint controls;
3. every candidate file matches the checkpoint manifest;
4. score arithmetic equals 20.00 exactly;
5. the failed PH screen is visible;
6. fixed-time evidence is named as the main survival summary;
7. the R route is marked pending unless executed in a named environment;
8. open conditions have named owners; and
9. Module 04 permission matches the progression value.

Any failed condition returns the checkpoint even when the carried score is passing.

## 13. Learner and reference assembly

Both assembly modes copy the same 78 accepted module files. Reference mode adds completed checkpoint records. Learner mode adds prompted checkpoint records. Neither mode recomputes module evidence.

The assembler refuses an existing target. It creates a sorted candidate manifest with relative path, bytes, SHA-256, source module, source version, and role.

## 14. Validation and mutation rejection

The independent validator must:

- verify exact file count and candidate manifest membership;
- verify every candidate byte count and SHA-256;
- verify the three nested workspace manifests;
- verify exact module versions and key output hashes;
- conserve cohort and survival counts;
- verify the 20-point score and 16 survival gates;
- verify the PH failure and required response;
- verify AI-use and progression fields;
- reject placeholders in reference mode;
- require placeholders in learner mode;
- reject a changed candidate file, score, gate, or progression; and
- verify a copied validator command.

## 15. Accessibility, privacy, and responsible AI

The accessible Kaplan-Meier table remains authoritative. The checkpoint review must identify the exact structured alternative, the zero-to-one y-axis, the group line styles, and the synthetic source note.

Only public repository material and synthetic Synthea-derived records are allowed. No identifiable, restricted, workplace, or patient data may enter the package. Agent-assisted work requires the accountable AI-use record and independent evidence checks.

## 16. Reference progression

The reference disposition is `continue with conditions`. Module 04 is permitted for curriculum construction because the decision, phenotype, cohort, follow-up, event-time evidence, uncertainty, and PH response are explicit.

Conditions include survival-methods review, clinical review, informatics review, accessibility testing, responsible-AI review, independent reproduction, managed R execution, and preservation of fixed-time evidence as the main Module 03 result.

Clinical use remains prohibited.

## 17. Completion, reviewers, version, and handoff

The frozen checkpoint has 78 accepted component files and 91 total files in both reference and learner modes. Its 78-row candidate manifest is 13,195 bytes with SHA-256 `ef5ace3d6b450473f5b7ab8c1b53bf24f63aa42910b1fdab5d72c617f4f57860`. Reference validation passes 394 checks and learner validation passes 379 checks. Two reference builds, learner candidate identity, copied validation, existing-target refusal, candidate-mutation rejection, and invalid-score rejection pass.

The checkpoint is a runnable release candidate after whole-curriculum validation, Commons 0.51.0 update, commit, and push.

Required reviews before alpha are APP-1 faculty, hospital medicine clinician, phenotype and clinical informatics, survival methods, accessibility, privacy, responsible AI, and independent instructor reproduction.

The Module 04 handoff must include the accepted 476-person risk set, fixed-time survival evidence, failed PH screen, open survival-methods condition, synthetic-site provenance, exact checkpoint identity, and prohibition on causal or real-site claims.
