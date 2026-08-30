# FND-2 Module 07: Model cards, governance, and defense

## 1. Module identity and place in the course

| Field | Value |
|---|---|
| Module ID | `oclc-fnd2-07` |
| Version | `0.1.0` |
| Commons release | `0.47.0` |
| Course | FND-2: Modeling, Inference, and Reproducible Analytics |
| Source week | 7 |
| Learner work | 16.0 hours |
| Cumulative course work | 112.5 hours |
| Final assessment component | 35 course points |
| Decision owner | Clinical analytics model-risk lead |
| Progression target | Final checkpoint |

Module 07 turns the accepted Week 6 evidence into one reviewer-ready analytics candidate. It does not refit, tune, repair, or improve the accepted model or forecast. It adds governance, monitoring, reproducibility, accessibility, human accountability, and separate package and model-use recommendations.

### Required starting state

Checkpoint 2 version `0.1.0` must validate completely with disposition `accept` or `accept with conditions` and explicit Module 07 permission. Its 130 files, 117-row manifest, source fingerprints, score, gates, defense, conditions, and use boundaries are immutable input.

### Required ending state

The learner releases a 168-file candidate with 143 immutable manifest rows, 24 completed reviewer records, an adequate ten-question defense, at least 28 of 35 points, all 18 gates, an allowed package disposition, and a separately recorded model-use recommendation.

## 2. Technical decision, owner, and audience

### Decision

Can another reviewer reproduce, understand, govern, monitor, stop, and honestly limit the analysis, and what model use is permitted?

### Decision owner

The accountable decision owner is a clinical analytics model-risk lead. Named faculty, biostatistical, clinical-informatics, model-evaluation, forecasting, accessibility, privacy and data-governance, responsible-AI, and independent-reproduction review remains required before alpha.

### Primary audience

The candidate is written for a receiving reviewer who must decide two things independently:

1. whether the technical package is acceptable; and
2. what, if any, model use the evidence supports.

### Package dispositions

- `accept`
- `accept with conditions`
- `revise`
- `refer`

Only `accept` and `accept with conditions` permit final-checkpoint review.

### Model-use recommendations

- `teaching use only`
- `silent prospective validation only`
- `revise before further validation`
- `stop model use`

The public reference recommendation is `teaching use only`. An acceptable package never implies deployment permission.

## 3. Foundation skill and upstream handoff

### Foundation skill

The learner can release and defend a governed analytic package whose evidence, limitations, ownership, monitoring, and stop rules remain inspectable after handoff.

### Checkpoint 2 handoff

Module 07 receives the complete accepted Checkpoint 2 package, including:

- Checkpoint 1 identity and four-outcome test evidence;
- Module 04 DAG, validity, missingness, dependence, censoring, and referral evidence;
- Module 05 complete public data, forecast contract, predictions, errors, coverage, and use limits;
- Module 06 tests, failures, prompt trace, critique, adjudication, independent verification, and sign-off;
- cumulative score, gates, defense, conditions, reviewer evidence, and progression; and
- the exact 117-row immutable Checkpoint 2 manifest.

### Supplementary provenance

Seven exact files preserve the FND-1 handoff, the FND-2 Module 01 source/data contract, and the exact Module 03 performance and subgroup evidence:

- FND-1 final-checkpoint `release.json`;
- FND-1 `reference/handoff-acceptance.md`;
- FND-2 Module 01 `source-record.yml`; and
- FND-2 Module 01 `data-spec.md`;
- Module 03 `test-metrics.csv`;
- Module 03 `subgroup-metrics.csv`; and
- Module 03 `prediction-evaluation-report.md`.

### Final-checkpoint handoff

The final checkpoint receives the exact Module 07 candidate. It may freeze, score, defend, and adjudicate the candidate. It may not silently change model evidence, governance rules, or use recommendation.

## 4. Assessable outcomes

The learner can:

1. assemble accepted evidence without changing it;
2. map every important model-card statement to registered evidence;
3. state purpose, users, target, prediction time, data, model, evaluation, limitations, ethics, and ownership;
4. keep package acceptance separate from model-use permission;
5. present baseline, discrimination, calibration, threshold, confusion, uncertainty, subgroup, validity, and forecast evidence together;
6. preserve four-outcome and sparse-subgroup limits;
7. define input, missingness, population, prevalence, performance, calibration, subgroup, forecast-source, and integrity monitoring signals;
8. give every monitoring signal a denominator, window, trigger, owner, action, and stop condition;
9. distinguish data, label, calibration, concept, workflow, and population drift;
10. require new evidence, comparison, approval, rollback, and semantic versioning before retraining;
11. define safe fallback, notification, investigation, immediate stop, and retirement;
12. reproduce the candidate into two clean targets and compare manifests;
13. disclose material agent assistance and independent checking;
14. deliver an accessible eight-minute handoff;
15. answer ten evidence-based defense questions; and
16. issue a bounded package disposition and separate model-use recommendation.

## 5. Concept ownership and out-of-scope boundaries

### Module 07 owns

- candidate assembly and immutable manifest;
- repository navigation, semantic version, change log, release notes, and proposed tag;
- evidence index and accessible performance appendix;
- model card and subgroup/equity review;
- monitoring signals and simulated governance responses;
- drift, retraining, versioning, rollback, stop, and retirement rules;
- model-use recommendation;
- clean reproduction audit;
- release checklist, score, gates, handoff, defense, reviewer record, conditions, and progression.

### Upstream ownership retained

Modules 01 through 06 and Checkpoints 1 and 2 retain ownership of source values, cohort, split, labels, feature roles, formulas, fitted models, thresholds, metrics, DAG, validity analyses, forecast, tests, failures, trace, and adjudication. Module 07 cites them; it does not revise them.

### Out of scope

- refitting, retuning, threshold changes, or reopening test data;
- acquiring real patient or hospital data;
- claiming deployed monitoring effectiveness;
- authorizing silent prospective validation from the public reference;
- clinical decision support, patient-level action, staffing, capacity, or operations;
- causal-effect, treatment-benefit, fairness-certification, safety, stable-process, or real-population claims;
- inventing monitoring data, alerts, labels, or approvals;
- treating a model card as marketing; and
- treating an agent-produced statement as independent evidence.

## 6. Lesson sequence and learner time

| Lesson | Work | Hours |
|---|---|---:|
| 7.1 | Reconcile Checkpoint 2 evidence and conditions | 1.5 |
| 7.2 | Draft the evidence index and model card | 2.5 |
| 7.3 | Build the accessible performance and subgroup appendix | 1.5 |
| 7.4 | Define monitoring signals and data contracts | 2.5 |
| 7.5 | Define drift, retraining, versioning, rollback, stop, and retirement | 2.0 |
| 7.6 | Assemble and reproduce the candidate in clean targets | 2.0 |
| 7.7 | Complete AI, accessibility, human, reviewer, and release records | 1.5 |
| 7.8 | Deliver handoff and technical defense | 2.0 |
| Total |  | 16.0 |

The eight-minute handoff and defense are included in learner work. Named program review outside the instructional exercise is not charged to the learner.

## 7. Readings and authoritative evidence

Required readings are carried in the repository so the learner can work without a hidden external dependency:

1. FND-2 course specification sections on package dispositions, model-use recommendations, model identity, monitoring, and final release.
2. Checkpoint 1 and Checkpoint 2 durable specifications and release contracts.
3. Module 03 model contract, evaluation report, calibration, threshold, subgroup, and failure evidence.
4. Module 04 causal-claim screen, DAG narrative, validity memo, threat register, and specialist referrals.
5. Module 05 forecast contract, memo, coverage context, failure analysis, and text alternative.
6. Module 06 prompt constraints, trace, critique, adjudication, independent verification, and human sign-off.
7. FND-1 final handoff acceptance and FND-2 Module 01 source/data records.

Instructors may add current governance standards as enrichment, but no external reading may silently change the module's fixed evidence or assessment contract.

## 8. Evidence inventory, provenance, rights, and teaching purpose

### Checkpoint 2 package

The accepted Checkpoint 2 reference contains 130 files. Its generated manifest has 117 rows, 17,699 bytes, and SHA-256 `16733c55e8a9930f4903006c81e5fb1acb9e75386507f1aa46867daac89f6ccc`.

### Key fixed evidence

- Modeling cohort: 374 synthetic rows.
- Split: 224 train, 75 validation, 75 test.
- Test positives: four.
- Selected model: `ML01`.
- Threshold: 0.08513264.
- Confusion: 48 TN, 23 FP, 2 FN, 2 TP.
- Test ROC AUC: 0.58802817 with stratified-bootstrap interval 0.26760563 to 0.91549296.
- Five of ten subgroup rows are suppressed.
- Selection case: 111 timing rows and 263 structural blanks.
- Full CDC release: 6,208 rows and 67 jurisdictions.
- Massachusetts forecast: 94 weeks.
- Candidate forecast MAE: 14.99587157 across 20 common targets.
- Accepted tests: 18; seeded failures: ten; independent checks: three; adjudicated claims: four.

### Rights and privacy

The modeling evidence is synthetic. The forecast evidence is public CDC jurisdiction-level aggregate data. No direct identifier, patient record, restricted workplace data, secret, key, token, or credential is permitted. Source and rights records remain immutable evidence.

### Teaching purpose

The candidate supports technical education, reproducibility practice, and governance reasoning. It is not a clinical product, operational model, safety case, or prospective-validation authorization.

## 9. Exact candidate and integrity contract

### Assembly input

Reference mode creates and validates the accepted Checkpoint 2 reference. Learner mode requires a complete assembled Checkpoint 2 directory. Both modes verify the exact nested file count, contract, manifest fingerprint, progression, and evidence identities before creating the candidate.

### Immutable inputs

The candidate manifest freezes:

- all 130 Checkpoint 2 files under `evidence/checkpoint2/`;
- seven supplementary provenance files under `evidence/provenance/`; and
- six Module 07 controls.

The manifest therefore has exactly 143 rows.

### Manifest schema

```text
relative_path,source_unit,source_version,bytes,sha256,role
```

Rows are unique, safe, and sorted. The manifest is generated after copying and is not self-listed.

### Protected target

Assembly refuses any existing target. It never merges with or cleans a prior submission.

### Candidate tree

```text
candidate/
  .gitattributes
  .gitignore
  VERSION
  README.md
  CHANGELOG.md
  release-notes.md
  governance-contract.json
  assessment.md
  validate_candidate.py
  release-manifest.csv
  environment-and-commands.md
  evidence-index.csv
  model-card.md
  performance-appendix.csv
  subgroup-equity-review.md
  monitoring-plan.csv
  drift-retraining-versioning.md
  rollback-stop-retirement.md
  model-use-recommendation.md
  reproducibility-audit.md
  accessibility-review.md
  ai-use.md
  human-sign-off.md
  handoff-brief.md
  technical-defense.md
  component-score.csv
  gate-results.csv
  release-checklist.csv
  conditions-register.csv
  reviewer-record.md
  progression-decision.md
  evidence/
    checkpoint2/
    provenance/
```

### Counts

The candidate contains 168 files: 143 manifest members, 24 editable records, and one generated manifest.

### Change control

An immutable change returns to its owning upstream unit. A governance-record change after review requires a Module 07 version decision and a new candidate assembly. Retraining always creates a new model version.

## 10. Worked example and instructor walkthrough

The instructor starts with a tempting but unsupported statement: "The package passed, so the model can be deployed." The class separates five questions:

1. Did immutable evidence validate? Yes.
2. Did the candidate meet the technical release contract? The reference does.
3. Does four-outcome test evidence establish stable performance? No.
4. Do sparse subgroup rows establish fairness? No.
5. What use is supportable? Teaching use only.

The instructor then traces the model-card claim through the performance appendix to Checkpoint 2 and Module 03 evidence, shows how Gate 18 blocks deployment claims, and demonstrates that a package can be acceptable while model use remains restricted.

The monitoring walkthrough uses a simulated trigger, not invented live data. A changed source fingerprint triggers quarantine, owner notification, investigation, and immediate stop. No claim is made that real monitoring has occurred.

## 11. Guided practice

### Practice 1: Evidence reconciliation

Map every Checkpoint 2 condition to a Module 07 record, owner, next check, and return trigger.

### Practice 2: Model-card trace

For ten model-card claims, cite the exact nested evidence path and classify the claim as supported, bounded, unsupported, or prohibited.

### Practice 3: Baseline and model appendix

Present training prevalence, baseline, selected model, discrimination, calibration, threshold, exact confusion counts, and uncertainty without hiding the four outcomes.

### Practice 4: Subgroup restraint

Explain why five suppressed rows and sparse outcomes prevent a fairness ranking or certification.

### Practice 5: Monitoring contract

Complete ten simulated signals with denominator, window, trigger, owner, action, and stop condition.

### Practice 6: Drift and retraining

Classify six change scenarios and decide whether to observe, investigate, stop, retire, or begin a new versioned validation cycle.

### Practice 7: Rollback and stop

Write a safe fallback that uses no model or forecast and identify notification and evidence-preservation steps.

### Practice 8: Reproduction

Assemble two clean reference targets, compare manifests byte for byte, validate each, and confirm existing-target refusal.

### Practice 9: Agent accountability

Trace one retained, one modified, and one rejected claim through assistance, independent evidence, human action, and final wording.

### Practice 10: Decision separation

Record package disposition and model-use recommendation on different machine-readable lines and explain why they differ.

## 12. Independent exercise

The learner receives an accepted Checkpoint 2 directory and creates a new Module 07 candidate without using the reference records. The submission must:

1. assemble into a new target;
2. preserve all 143 immutable members;
3. complete all 24 records;
4. cite checkpoint-relative evidence;
5. score the exact six-row rubric;
6. pass all 18 gates;
7. complete ten defense responses;
8. name actual human accountability for the learner submission;
9. validate without `--starter`;
10. propose but not create the annotated tag;
11. recommend package disposition and model use separately; and
12. carry an accepted candidate to the final checkpoint.

The exercise returns automatically if the learner edits accepted evidence, hides sparse results, claims monitoring occurred, or expands use beyond the data.

## 13. Visualization and communication requirements

### Accessible performance appendix

The exact CSV appendix includes measure, value, denominator, interval or comparator, source path, and interpretation limit. No summary chart may replace the exact table.

### Handoff brief

The eight-minute handoff follows this order:

1. decision and use boundary;
2. source, grain, target, prediction time, and split;
3. baseline, selected model, test counts, and uncertainty;
4. calibration, threshold, subgroup, and validity limits;
5. distinct public forecast and its coverage limits;
6. tests, failures, agent audit, and independent checks;
7. monitoring, stop, rollback, retirement, and safe fallback; and
8. separate package and model-use recommendations.

### Communication boundary

No visual or prose may omit denominators, four test outcomes, suppressed subgroup rows, public-aggregate forecast unit, or teaching-only use. Color cannot be the only encoding. All paths are candidate-relative.

## 14. Exact submission package

### Module source package

The repository module contains:

- `README.md`;
- `VERSION`;
- `.gitattributes` and `.gitignore`;
- `governance-contract.json`;
- `assessment.md`;
- `instructor-notes.md`;
- `assemble_candidate.py`;
- `validate_candidate.py`;
- `release.json`;
- 24 learner templates; and
- 24 complete reference records.

### Learner candidate records

The 24 editable records are:

1. `README.md`;
2. `CHANGELOG.md`;
3. `release-notes.md`;
4. `environment-and-commands.md`;
5. `evidence-index.csv`;
6. `model-card.md`;
7. `performance-appendix.csv`;
8. `subgroup-equity-review.md`;
9. `monitoring-plan.csv`;
10. `drift-retraining-versioning.md`;
11. `rollback-stop-retirement.md`;
12. `model-use-recommendation.md`;
13. `reproducibility-audit.md`;
14. `accessibility-review.md`;
15. `ai-use.md`;
16. `human-sign-off.md`;
17. `handoff-brief.md`;
18. `technical-defense.md`;
19. `component-score.csv`;
20. `gate-results.csv`;
21. `release-checklist.csv`;
22. `conditions-register.csv`;
23. `reviewer-record.md`; and
24. `progression-decision.md`.

### Submission identity

The learner submits the exact candidate directory, full repository commit, semantic version `0.1.0`, and proposed tag `fnd2-governed-candidate-v0.1.0`. The tag is not created before final-checkpoint acceptance.

## 15. Rubric, gates, and pass conditions

### Thirty-five-point rubric

| ID | Criterion | Points |
|---|---|---:|
| M01 | Aim, target, prediction time, model design, and baseline | 5.00 |
| R01 | Reproducible pipeline, environment, manifest, tests, and exact refit contract | 6.00 |
| E01 | Evaluation, calibration, thresholds, subgroup evidence, and failure analysis | 7.00 |
| V01 | Validity, uncertainty, data limits, forecast limits, and claim boundary | 5.00 |
| G01 | Model card, monitoring, drift, retraining, rollback, stop, retirement, and use decision | 6.00 |
| H01 | Responsible-agent evidence, accessible handoff, defense, reviewers, and disposition | 6.00 |
| Total |  | 35.00 |

At least 28.00 points are required.

### Eighteen noncompensable gates

1. Accepted Checkpoint 1 and Checkpoint 2 identities are preserved.
2. Exact source, cohort, split, label, feature, and pipeline identities remain fixed.
3. No leaked, post-index, or future predictor is permitted.
4. Baseline and untouched-test evidence remain visible.
5. Exact metric numerators, denominators, and uncertainty remain visible.
6. Calibration and threshold evidence are present.
7. Four test outcomes and sparse subgroup evidence are visible.
8. Validity conditions and specialist boundaries carry forward.
9. The forecast remains a separate public aggregate case.
10. All 18 tests pass and all ten seeded failures reject for intended reasons.
11. AI trace, material audit, independent evidence, and human owner are complete.
12. The model card states synthetic source and prohibited use.
13. Monitoring, retraining, rollback, stop, and retirement have owners and actions.
14. Accessible exact tables and structured alternatives accompany displays.
15. Clean reproduction and the 143-row immutable manifest pass.
16. The ten-question defense is adequate.
17. Package disposition and model-use recommendation are separate.
18. No deployment, clinical efficacy, causal effect, fairness certification, stable-process, or real-population claim is made.

### Automatic return

Return without scoring for changed immutable evidence, missing records, invalid arithmetic, a failed gate, inadequate defense, incomplete human ownership, simulated signature, unverified claim, hidden dependency, prohibited data, created-before-acceptance tag, or model-use recommendation implied by package acceptance.

## 16. Common failures and instructor interventions

| Failure | Instructor intervention |
|---|---|
| Model card reads like marketing | Require every claim to cite exact evidence and limitation. |
| Package pass becomes deployment language | Separate disposition and model-use fields; fail Gate 17. |
| Four outcomes disappear from summary | Return E01 and Gate 7. |
| Suppressed subgroup rows become fairness claims | Restore counts, suppression, uncertainty, and no-ranking boundary. |
| Monitoring has no denominator or owner | Return G01 and Gate 13. |
| Threshold is presented as validated utility | Reopen the exact 48/23/2/2 consequences and sparse outcome limit. |
| Forecast becomes a hospital staffing model | Restore jurisdiction aggregate, reporting coverage, and prohibited use. |
| Retraining is described as an automatic refresh | Require new data, comparison, approval, rollback, and new version. |
| Rollback means using an older unvalidated model | Use the safe fallback: no model or forecast action. |
| Agent critique is treated as evidence | Map claim to independent rows or reject it. |
| Reproduction overwrites an old target | Require clean target and existing-target refusal. |
| Proposed tag is created early | Delete or invalidate the tag and return release identity for review. |

## 17. Accessibility, equity, privacy, and claim checks

### Accessibility

The candidate provides descriptive headings, readable tables, non-color encoding, exact CSV evidence, structured DAG routes, forecast text alternative, keyboard-readable decisions, and plain-language handoff. The validator confirms required equivalent paths, while a named human checks rendered delivery before alpha.

### Equity and subgroup evidence

The ten subgroup rows retain counts, outcomes, missing metrics, and five suppressions. The model card may describe limited evidence; it may not rank groups, certify fairness, infer absence of harm, or recommend differential action.

### Privacy and security

Only synthetic and public aggregate evidence is permitted. The candidate rejects personal absolute paths, hidden dependencies, secrets, credentials, keys, tokens, restricted data, identifiable data, workplace-confidential data, and caches.

### Claim boundary

Technical validation means declared files and contracts agree. It does not establish clinical validity, causal identification, fairness, external validity, deployment safety, prospective performance, or monitoring effectiveness.

## 18. AI policy, disclosure, and verification

### Permitted uses

An agent may help inventory evidence, check consistency, draft bounded prose, propose monitoring questions, inspect accessibility, or suggest tests using only allowed data classes.

### Prohibited uses

An agent may not receive restricted data, invent evidence, choose the final disposition, sign for a human, authorize use, rewrite failed tests, or silently alter a source, metric, threshold, condition, or model card.

### Required record

`ai-use.md` names the tool, task, data class, prompt or instruction reference, output used, output rejected or corrected, independent evidence, human owner, and prohibited-data confirmation.

### Material audit

At least one material agent-assisted claim must be traced to independent row-level or artifact-level evidence. Repeating the same prompt to the same system is not independent verification.

### Reference audit

The reference retains the bounded lower-aggregate-MAE statement, modifies the residual-independence statement, and rejects staffing-readiness and leaked-model claims. Human ownership applies to curriculum construction only until a live learner and reviewer sign.

## 19. Answer key and instructor materials

The reference candidate provides:

- a complete model card with teaching-only recommendation;
- a 17-row accessible performance appendix;
- ten complete simulated monitoring signals;
- drift, retraining, rollback, stop, and retirement rules;
- exact package and model-use lines;
- a two-target clean-reproduction audit;
- six complete score rows and 18 passing gates;
- a ten-question technical defense;
- a release checklist and condition register; and
- an `accept with conditions` curriculum-construction progression record.

Instructor notes identify high-value probes, automatic returns, scoring boundaries, and the distinction between reference construction sign-off and live learner assessment.

The answer key may demonstrate completeness but cannot substitute for learner reasoning, live defense, named program review, or independent reproduction before alpha.

## 20. Runnable acceptance checks

### Assembler self-check

The assembler:

1. creates and validates the accepted Checkpoint 2 reference;
2. assembles two complete Module 07 references and one learner starter;
3. verifies 143 immutable rows and 168 total files;
4. verifies byte-identical manifests across repeated assembly;
5. verifies all seven supplementary provenance fingerprints;
6. confirms learner templates contain prompts; and
7. rejects an existing target.

### Validator self-check

The validator:

1. validates complete and starter candidates;
2. validates the nested Checkpoint 2 package;
3. checks all manifest members and fixed evidence;
4. independently recounts 48/23/2/2 and recalculates forecast MAE/RMSE;
5. checks the six-row score, 18 gates, ten monitoring signals, checklist, conditions, ten defense answers, human scope, disposition, and use recommendation;
6. rejects a complete-mode learner starter;
7. rejects missing immutable evidence;
8. rejects an invalid score;
9. rejects a failed gate;
10. rejects missing monitoring ownership; and
11. rejects a package/use decision contradiction.

### Commands

```powershell
python courses/modeling-inference-reproducible-analytics/modules/07-model-cards-governance-defense/assemble_candidate.py --self-check
python courses/modeling-inference-reproducible-analytics/modules/07-model-cards-governance-defense/validate_candidate.py --self-check
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/check-curriculum-specs.ps1
```

### Technical acceptance

All commands exit zero, all deliberate failure cases reject for their intended reason, the manifest is deterministic, learner-facing records contain no local absolute path or Unicode dash, and the whole-repository curriculum gate recognizes Commons `0.47.0`.

## 21. Release status, reviewers, version, and known issues

### Semantic-version decision

Module 07 starts at `0.1.0` as its first runnable contract. The Commons advances from `0.46.0` to `0.47.0` because a new final-candidate unit is added without breaking prior releases.

### Status

Status is `runnable-release-candidate`. The reference is intended for continued curriculum construction and final-checkpoint development, not clinical or operational use.

### Measured runnable release

- Immutable manifest rows: 143
- Editable records: 24
- Assembled files: 168
- Manifest bytes: 27,316
- Manifest SHA-256: `ab2537e278ea549b8152434df0a21438394d28caa6031b03e9a570a27db07c1b`
- Complete reference checks: 880
- Learner starter checks: 831

### Required human reviewers

- FND-2 faculty owner;
- biostatistical methods;
- clinical informatics;
- model evaluation and model risk;
- forecasting;
- accessibility;
- privacy and data governance;
- responsible AI; and
- independent reproduction.

### Known issues

- Named program review, live learner defense, and live learner/reviewer sign-off remain pending before alpha.
- The test set has four outcomes and wide uncertainty.
- Five of ten subgroup rows are suppressed; no fairness conclusion is supportable.
- Module 04 fixtures are synthetic, and paired R reconciliation remains pending.
- The CDC forecast is a changing-reporting jurisdiction aggregate and loses one fold to last-value.
- Monitoring is a governed teaching simulation, not observed production evidence.
- The proposed tag cannot be created until final-checkpoint acceptance identifies the exact reviewed commit.

### Context-safe handoff

After Module 07 is validated, versioned, committed, and pushed, resume with FND-2 Final Checkpoint 3. Freeze this exact candidate, score the final 35-point map, adjudicate 27 gates and 15 defense questions, record package disposition and model-use recommendation separately, then define the annotated tag target.
