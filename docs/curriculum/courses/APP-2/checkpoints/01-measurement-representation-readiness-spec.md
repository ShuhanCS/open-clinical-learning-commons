# APP-2 Checkpoint 01: Measurement and representation readiness

## 1. Checkpoint identity and place in the course

- Checkpoint ID: `oclc-app2-cp01`.
- Course: APP-2, Data for Patient Experience and Engagement.
- Due point: end of instructional Week 3.
- Checkpoint version target: 0.1.0.
- Commons release target: 0.58.0.
- Accepted modules: APP-2 Modules 01, 02, and 03.
- Course points: 20.00, awarded by Module 02 exactly once.
- Decision: whether the selected patient-reported measure and response evidence may enter Module 04 linked analysis.

This is the first cumulative release gate. It does not ask learners to upload three unrelated assignments. It freezes one auditable chain from the patient-experience decision through the exact measurement contract and the response and representation audit.

## 2. Decision, readers, and required answer

The checkpoint asks:

> May the accepted Q22 and Q23 discharge-information measure, target population, teaching frame, response evidence, item-missingness evidence, and bounded response adjustment enter linked analysis?

Primary readers are the adult inpatient patient-experience council, a patient or caregiver partner, the APP-2 faculty owner, a measurement reviewer, a survey-methods reviewer, and the future Module 04 analyst.

The answer must be `continue`, `continue with conditions`, `revise`, or `refer`. A continuing answer names the exact accepted artifacts, score, passing gates, remaining conditions, and Module 04 ownership. It never authorizes real fielding, patient targeting, clinical action, hospital ranking, a real patient-experience estimate, or machine-learning response adjustment.

## 3. Accepted Module 01 decision package

The checkpoint accepts APP-2 Module 01 only as:

- module ID `oclc-app2-01`;
- version `0.1.0`;
- Commons release `0.56.0`;
- 25 assembled workspace files;
- 15 immutable manifest rows;
- manifest SHA-256 `c693e04592994f6f7bef14459b83669a5c824d0bf0b027a0624bab12a3cb4862`; and
- zero course points.

The frozen Module 01 evidence includes the decision charter, construct map, patient journey, evidence needs, stakeholder partnership map, claim boundary, public-source feasibility, agent-use record, and progression decision. It establishes the adult inpatient council and prevents later analysis from replacing a patient decision with a convenient available metric.

## 4. Accepted Module 02 measurement package

The checkpoint accepts APP-2 Module 02 only as:

- module ID `oclc-app2-02`;
- version `0.1.0`;
- Commons release `0.57.0`;
- 66 assembled workspace files;
- 52 immutable manifest rows;
- manifest SHA-256 `c261307b45be842c00c9ded66614a3770f379d41a1d7efecb68032f9c090a870`;
- score `20 of 20`;
- 18 of 18 measurement gates passing; and
- progression `continue with conditions`.

The frozen measurement contract is the updated HCAHPS Discharge Information Q22 and Q23 pair. Q21 another health facility makes both items not applicable. Each item uses its own answered denominator. The teaching composite is the mean of the two question-level yes proportions. Use remains public-domain HCAHPS-derived, local, unadjusted unless explicitly labeled, and unofficial.

## 5. Accepted Module 03 response package

The checkpoint accepts APP-2 Module 03 only as:

- module ID `oclc-app2-03`;
- version `0.1.0`;
- Commons release `0.58.0`;
- 44 assembled workspace files;
- 31 immutable manifest rows;
- manifest SHA-256 `3d7787a975335518cf4a4f50b5561a323707e2acea6bd1724b1c92a565f64a30`;
- 19 of 19 response gates passing; and
- zero additional course points.

The frozen response evidence includes the full five-file MEPS HC-256 source suite, 1,255 public-derived target and frame records, 782 synthetic respondents, item-specific answered sets, 40 subgroup audit rows, 13 response cells, one 3.0 cap hit, weight diagnostics, known-truth comparison, privacy and consent conditions, and an explicit Module 04 progression decision.

## 6. Point architecture and no-double-counting rule

The checkpoint score is 20.00 out of 20.00. All 20 points come from the accepted Module 02 measurement assessment:

- instrument fit and construct or content validity, 4 points;
- scoring correctness and reproduction, 4 points;
- reliability and meaningful interpretation, 4 points;
- language, mode, proxy, access, and burden, 4 points; and
- source, rights, claims, reproducibility, and responsible agent use, 4 points.

Module 01 and Module 03 are required gates with zero additional points. The checkpoint may not add the Module 02 score again, create shadow points for response work, or average gates into the score. A 20-point score cannot compensate for a failed response, integrity, protection, or progression gate.

## 7. Cumulative evidence index

`evidence-index.csv` is the human-readable chain of custody. It contains one ordered row for each accepted module with:

- module ID and title;
- module version and Commons release;
- assembled file count;
- nested manifest bytes and SHA-256;
- points carried into this checkpoint;
- gate status;
- progression;
- accepted decision; and
- role in the cumulative release.

The point column must sum to 20.00 and contain a nonzero value on the Module 02 row only. The candidate manifest is the machine-readable file-level chain of custody.

## 8. Measurement-readiness review

The cumulative review must state:

- the adult inpatient decision and intended construct;
- the exact updated instrument version and selected Q22 and Q23 items;
- Q21 skip logic and item-specific denominators;
- the local teaching composite rule;
- validity, reliability, and meaningful-interpretation limits;
- language, mode, disability, literacy, proxy, non-digital, burden, and stop conditions;
- public-domain item and CAHPS trademark boundaries;
- the 20.00 of 20.00 score and 18 passing measurement gates; and
- the return trigger for any changed item, score, construct, naming decision, or intended use.

The review may not call the partial local measure official HCAHPS, compare it with an official adjusted hospital score, or invent a meaningful-change threshold.

## 9. Response and representation review

The same cumulative review must state:

- 19,140 public HC-256 source rows and 18,683 positive-person-weight rows;
- the 1,255-person public analytic target and teaching frame;
- the 18,879,474.284615 base-weighted target population;
- complete teaching coverage as a constructed property only;
- 782 synthetic respondents and the 62.31075697 percent unweighted response rate;
- 642 respondent Q21 home records;
- 585 Q22 and 589 Q23 answered records;
- separate total nonresponse, not-applicable, and item-missing states;
- subgroup support and the one-record missing-language cell;
- `PERWT24F` as the official public final person weight;
- 13 teaching response cells, the 3.0 bound, and one bound hit;
- the decline in Kish effective sample size from 548.95483815 to 527.00399458;
- the known-truth comparison; and
- remaining adjusted absolute bias of 3.14500108 points for Q22, 5.26048779 for Q23, and 4.20274444 for the teaching composite.

The review must say that the adjustment helps in this simulation and does not remove bias.

## 10. Data-class and claim boundaries

The checkpoint keeps three classes visible:

1. official public CMS HCAHPS aggregate and instrument evidence from Modules 01 and 02;
2. official public AHRQ MEPS HC-256 data and public-derived grouped fields from Module 03; and
3. synthetic patient-level measurement and response fields used only for procedural teaching.

Public data do not become synthetic because they are used in a teaching package. Synthetic Q21, Q22, Q23, invitation, response, mode, and missingness do not become observed because they are joined to public rows. No checkpoint record may claim a real HCAHPS response rate, hospital performance, access disparity, equity finding, prevalence, causal mode effect, patient benefit, or clinical effect.

## 11. Noncompensable checkpoint gates

Progression requires:

1. exact Module 01, 02, and 03 versions and nested manifests;
2. all 135 accepted component files present and fingerprinted;
3. Module 02 score carried once and totaling 20.00;
4. all 18 Module 02 measurement gates passing;
5. all 19 Module 03 response gates passing;
6. measurement item, skip, scoring, construct, and naming rules unchanged;
7. target, frame, invitation, response, applicability, and item counts reconciled;
8. public, public-derived, and synthetic data classes labeled correctly;
9. base and teaching weights distinguished;
10. bound hit, weight concentration, effective sample size, and remaining bias visible;
11. privacy, consent, access, burden, refusal, retention, and safety-content conditions complete;
12. responsible agent use disclosed and independently checked;
13. no fielding, targeting, ranking, clinical, causal, official-score, or synthetic-as-real overclaim;
14. reproducible assembly and copied validation passing; and
15. an explicit Module 04 permission or refusal consistent with progression.

Any failure returns the checkpoint for revision or referral. Points do not override a gate.

## 12. Checkpoint learner records

The learner completes:

- `README.md`, with the cumulative package identity and run commands;
- `evidence-index.csv`, with one accepted row per module;
- `measurement-representation-review.md`, with one integrated decision review;
- `reproducibility-check.md`, with assembly, manifest, copied-validator, and mutation evidence;
- `ai-use.md`, with accountable agent-use fields; and
- `progression-decision.md`, with the score, gate totals, conditions, and Module 04 permission.

The candidate module workspaces are immutable. A learner corrects an upstream failure in its owning module and rebuilds the checkpoint. The learner does not edit a candidate file inside the checkpoint to make it pass.

## 13. Assembly contract

`build_checkpoint.py` assembles accepted reference workspaces from the three module builders. It copies every component into:

- `candidate/module-01/`;
- `candidate/module-02/`; and
- `candidate/module-03/`.

It then writes `candidate-manifest.csv` with relative path, bytes, SHA-256, source module, source version, and role. It refuses an existing target. Learner and reference builds contain identical candidates and differ only in the six editable checkpoint records.

The checkpoint does not duplicate release points or recompute an upstream measurement decision. It verifies and freezes accepted upstream work.

## 14. Validation and mutation rejection

`validate_checkpoint.py` must:

- verify every checkpoint control and candidate file;
- verify the 135-row candidate manifest and all nested module manifests;
- require exact module versions, Commons releases, assembled counts, manifest bytes, and manifest hashes;
- confirm the 20-point score appears on Module 02 only;
- inspect the accepted Module 02 measurement score and gates;
- inspect the accepted Module 03 response flow, cells, weight diagnostics, estimates, and gates;
- validate the integrated review and progression record;
- scan editable text for personal paths, unsupported placeholders, and non-ASCII dash characters;
- run from a copied checkpoint workspace;
- reject a candidate mutation;
- reject double-counted points;
- reject a failed gate; and
- reject Module 04 permission that conflicts with progression.

Learner-mode validation checks the complete immutable package and requires visible prompts in every editable record. It does not treat starter prompts as completed work.

## 15. Common failure modes and instructor response

| Failure | Required response |
|---|---|
| One module directory is missing or changed | rebuild from the accepted module release |
| Module 02 points appear twice | restore one 20-point row and a 20.00 total |
| Passing score is used to ignore a failed response gate | return checkpoint for revision |
| Q21, Q22, Q23, or composite rule changes | return to Module 02 |
| Target, frame, or respondent count changes | return to Module 03 and rebuild |
| Public and synthetic evidence are merged without labels | stop release and restore data classes |
| Teaching factor is called official | correct the weight boundary before progression |
| Residual bias is omitted | add the known-truth comparison and remaining error |
| Complete teaching frame is called real coverage | narrow the coverage claim |
| Small subgroup is interpreted as stable evidence | retain support flag and limit the claim |
| Real fielding is authorized | restore the protection and review conditions |
| Candidate file is edited inside checkpoint | correct the owning module and reassemble |
| Module 04 permission conflicts with progression | correct the progression record |

Instructors stop review at the first broken fingerprint, duplicated score, failed noncompensable gate, changed measurement rule, changed denominator, or data-class overclaim.

## 16. Progression contract and Module 04 handoff

A continuing reference decision must carry:

- checkpoint score `20.00 of 20.00`;
- Module 02 measurement gates `18 of 18 pass`;
- Module 03 response gates `19 of 19 pass`;
- checkpoint integrity gates passing;
- progression `continue with conditions`;
- Module 04 permission `permitted for linked analysis`;
- clinical action, hospital ranking, real fielding, and patient targeting `prohibited`; and
- machine learning `reserved for Module 06`.

Module 04 receives the frozen decision, measure, population, response evidence, base weight, teaching response factor, support limits, privacy conditions, and unresolved design-aware uncertainty work. It may not silently change any of them.

## 17. Release, review, and exit criteria

Checkpoint version 0.1.0 exits as a runnable release candidate at Commons 0.58.0 only when two independent assemblies match, the copied validator passes, every candidate and nested manifest matches, the score is carried exactly once, all gates pass, and the whole-curriculum checker passes.

Named APP-2 faculty, patient or caregiver, measurement, survey-methods, accessibility, language-access, privacy, responsible-AI, clinical, and independent reproduction reviews remain required before alpha use. The actual course section must map the due date to the official half-term calendar. The checkpoint is a curriculum construction release, not approval to field a survey or act on a patient result.

The reference release contains 135 accepted candidate files and 149 assembled files. Its candidate manifest is 23,489 bytes with SHA-256 `5734df858d79721f3efd6766df6299f56d0df49c0aee8b8728b22c284255c903`. Reference validation passes 714 checks and learner validation passes 683 checks. Candidate mutation, duplicate points, failed gates, invalid progression, and overwrite routes are rejected.
