# APP-2 Checkpoint 02 specification: Linked evidence and patient voice release

## 1. Checkpoint identity and place in the course

- Checkpoint ID: `oclc-app2-cp02`.
- Version: `0.1.0`.
- Commons release: `0.62.0`.
- Course: APP-2, Data for Patient Experience and Engagement.
- Timing: end of instructional Week 6.
- Course points: 45.
- Package path: `courses/patient-experience-engagement/checkpoints/02-linked-evidence-patient-voice-release/`.
- Status: runnable release candidate after all checks in this specification pass.

This checkpoint is the cumulative technical case for Modules 04 through 06. It freezes accepted evidence and asks for one integrated readiness decision. It does not create a new analysis or rescore a completed component.

## 2. Decision, readers, and required answer

The learner must answer:

> Is the linked patient-experience case strong enough to enter clinician and patient leadership review for a bounded prospective improvement proposal?

The answer is read by the APP-2 faculty owner, patient or caregiver partner, patient-experience measurement reviewer, survey-methods reviewer, health-services data reviewer, qualitative-methods reviewer, equity and accessibility reviewer, model reviewer, governance reviewer, and Module 07 clinician lead.

The learner must choose `continue`, `continue with conditions`, `revise`, or `refer`. A continuation permits Module 07 curriculum work only. It does not authorize contact, fielding, official reporting, patient targeting, clinical action, implementation, or model deployment.

## 3. Accepted Week 3 identity

Checkpoint 02 retains the accepted Week 3 checkpoint as an immutable identity:

- ID: `oclc-app2-cp01`;
- version: `0.1.0`;
- Commons release: `0.58.0`;
- accepted component files: 135;
- candidate manifest SHA-256: `5734df858d79721f3efd6766df6299f56d0df49c0aee8b8728b22c284255c903`;
- score: 20.00 of 20.00, already counted at Week 3; and
- progression: `continue with conditions`.

Checkpoint 02 records this identity but does not copy or rescore the Week 3 candidate. Its open measurement, response, data-class, protection, and reviewer conditions remain active.

## 4. Accepted Module 04 linked-evidence package

The checkpoint assembles the complete accepted Module 04 reference workspace:

- ID: `oclc-app2-04`;
- version: `0.1.0`;
- Commons release: `0.59.0`;
- assembled files: 65;
- workspace manifest: 52 rows, 6,529 bytes;
- workspace manifest SHA-256: `bc0592acd18b8524be907fd42483e85af4180e0b6f6de35d40e82ea3eae46aa8`;
- Week 6 points: 25, counted once; and
- linkage gates: 20 of 20 pass.

The accepted package preserves the full 25-file AHRQ MEPS source suite, 19,140 person rows, 174,231 event rows, one-to-one event linkage, the 1,255-person target, 28,455 linked target events, denominator decisions, access and communication measures, digital-channel evidence, service-use evidence, source identities, and claim limits.

## 5. Accepted Module 05 patient-voice and equity package

The checkpoint assembles the complete accepted Module 05 reference workspace:

- ID: `oclc-app2-05`;
- version: `0.1.0`;
- Commons release: `0.60.0`;
- assembled files: 49;
- workspace manifest: 33 rows, 4,598 bytes;
- workspace manifest SHA-256: `6f3d93a1a08458cb39fa8d321a67f10dad1ee45b2a8a2742a969ab969f35c8fa`;
- Week 6 points: 20, counted once; and
- patient-voice and equity gates: 22 of 22 pass.

The accepted package preserves the 782 synthetic comment opportunities, 420 generated comments, eight-theme codebook, 120-record double-coding benchmark, agreement results, assisted-classification audit, prespecified group plan, support decisions, suppressed estimates, channel-exclusion audit, responsible claims, and progression record.

## 6. Accepted Module 06 partnership, improvement, and ML package

The checkpoint assembles the complete accepted Module 06 reference workspace:

- ID: `oclc-app2-06`;
- version: `0.1.0`;
- Commons release: `0.61.0`;
- assembled files: 46;
- workspace manifest: 28 rows, 4,361 bytes;
- workspace manifest SHA-256: `0cb7f2d0ffc6d5ae8cbcd0cf206a61f143dcd603b5b34eb312972d2ecc2f0938`;
- additional points: zero; and
- partnership, improvement, and ML gates: 24 of 24 pass for curriculum construction.

The package preserves the simulated partnership record, 12 partnership requirements, disagreements, universal-offer workflow, 14-measure registry, feedback and accountability plan, fixed response-model split, transparent benchmark, one bounded random forest, calibration, error costs, weight stability, known-truth recovery, subgroup support, failure cases, and the prespecified model decision.

## 7. Point architecture and no-double-counting rule

The Week 6 checkpoint contains 45 course points:

| Scored source | Points | Treatment |
|---|---:|---|
| Module 04 linked-evidence analysis | 25 | Count exactly once at Checkpoint 02 |
| Module 05 equity and patient-voice memo | 20 | Count exactly once at Checkpoint 02 |
| Module 06 partnered improvement and embedded ML | 0 | Required gate, no added points |
| Total | 45 | No duplicate points |

The accepted Week 3 score is visible for continuity but is not part of the 45-point Week 6 sum. No checkpoint narrative, gate, or record adds bonus points.

## 8. Cumulative evidence index

`evidence-index.csv` must contain exactly four ordered identities: Checkpoint 01, Module 04, Module 05, and Module 06. It records version, Commons release, candidate directory, assembled file count, workspace manifest SHA-256, points, score treatment, gate treatment, and progression.

The three module candidate directories contain 160 immutable files in total. Their generated `candidate-manifest.csv` records relative path, bytes, SHA-256, source module, source version, and role for every file. Any changed, omitted, extra, or relabeled candidate file fails the checkpoint.

## 9. Linked-evidence review requirements

The integrated review must state:

1. the five accepted public MEPS products and their source role;
2. the 1,255-person target and 28,455 linked target events;
3. one-to-one event reconciliation and the 12 inpatient carry-in starts;
4. aligned denominator, period, grain, and weight rules;
5. the 80.78856833 percent usual-source estimate;
6. the 52.44065366 percent after-hours-difficulty estimate;
7. the 7.61893012 percent delayed-for-cost estimate;
8. the 7.37866394 percent linked telehealth-event estimate;
9. the limited-support 45-record provider-language result; and
10. the absence of a portal-preference measure.

Telehealth is a service channel, not proof of portal access, preference, engagement, quality, or intervention benefit. Linked patterns are descriptive teaching evidence and cannot become causal or clinical claims.

## 10. Patient-voice, group, and equity review requirements

The integrated review must preserve these facts:

- all 420 comments are generated teaching text, not patient testimony;
- the codebook contains eight themes;
- 120 simulated records were double coded;
- overall agreement is 80.00000000 percent and Cohen's kappa is 0.77142857;
- the fixed phrase rule has 0.78333333 benchmark accuracy and cannot replace human review;
- 35 of 52 group estimates and 19 of 36 contrasts meet the support rule;
- unsupported estimates remain blank without merging source categories;
- the lower-income delayed-cost contrast is 4.02137981 percentage points;
- the lower-income telehealth contrast is -6.88053616 percentage points; and
- a supported contrast retains an equity question but does not prove inequity, discrimination, preference, cause, fairness, or a group trait.

Comment counts do not estimate prevalence or saturation. The learner must carry the missing-voice and channel-exclusion questions into partnership and improvement design.

## 11. Partnership and improvement review requirements

The checkpoint must distinguish the simulated construction reference from actual patient or caregiver participation. The reference contains no actual patient statement and cannot satisfy the alpha gate.

The review must name the universal-offer population, language and format choices, non-digital alternatives, proxy and interpreter support, contact choice, understanding check, follow-up routes, burden protection, safety routing, feedback, accountable owners, 14-measure registry, and stop rules. The proposal advances only as a bounded design question.

Named patient or caregiver partnership, compensation, access needs, authority, participation terms, disagreement rights, and final review remain required before alpha.

## 12. Transparent-versus-ML review requirements

Both response methods must retain the same three eligible fields, fixed 878-row training set, fixed 377-row evaluation set, 235 held-out respondents, 0.60 threshold, and factors bounded from 1.0 through 3.0.

The checkpoint must state the exact held-out evidence:

| Result | Transparent | Bounded random forest |
|---|---:|---:|
| Brier score | 0.22962545 | 0.23135127 |
| ROC AUC | 0.54335192 | 0.53869891 |
| Teaching error cost | 227 | 225 |
| Composite absolute bias, percentage points | 2.48289986 | 2.39922466 |

The improvement is 0.08367520 percentage points, below the prespecified 0.50 threshold. Both methods pass weight-stability rules. The random forest does not change the response-adjustment decision, and the transparent benchmark remains the teaching adjustment. Neither method authorizes targeting or deployment.

## 13. Checkpoint learner records

The assembled learner package contains six editable records:

1. `README.md`, the submission map and decision prompt;
2. `evidence-index.csv`, the four accepted identities and score treatment;
3. `linked-evidence-patient-voice-review.md`, the integrated evidence review;
4. `reproducibility-check.md`, the candidate, build, mutation, and independent-check record;
5. `ai-use.md`, the accountable agent-use record; and
6. `progression-decision.md`, the score, gates, conditions, boundaries, and Module 07 permission.

Learners edit only these six files. Candidate files are immutable. A correction to accepted evidence must occur in its owning module and trigger a fresh checkpoint build.

## 14. Assembly contract

`build_checkpoint.py` uses only the Python standard library and the accepted module workspace builders. It must:

- refuse any existing target;
- create reference and learner packages from separate records;
- assemble 65 Module 04 files, 49 Module 05 files, and 46 Module 06 files;
- create a sorted 160-row candidate manifest;
- create exactly 174 files in each assembled package;
- produce identical candidate bytes and manifest identity across two builds; and
- include a copied validator that runs inside the assembled package.

The checkpoint source package does not duplicate the 160 candidate files in Git. It generates them from the accepted module builders.

The first runnable package has a 27,594-byte candidate manifest with SHA-256 `67248e989888cdabeb050c970e85d091ece68018047ef6f0bec7ba26441cfed1`.

## 15. Validation and mutation rejection

`validate_checkpoint.py` checks package shape, every candidate byte count and SHA-256, nested workspace manifests, exact versions, score treatment, gate totals, required facts, claim limits, AI accountability, progression, and prohibited uses.

The self-check must prove:

- two reference builds match;
- learner and reference packages share the same candidate manifest;
- the copied validator passes;
- a changed candidate file rejects;
- a duplicate score rejects;
- a failed checkpoint gate rejects; and
- an invalid progression value rejects.

The repository curriculum checker must require the durable specification, all checkpoint source files, release metadata, and both self-checks.

The first runnable validation passes 826 complete-reference checks and 797 learner checks before exercising the copied and mutation routes.

## 16. Progression contract and Module 07 handoff

All 20 checkpoint gates are noncompensable. Module 07 permission is `permitted for curriculum construction` only when progression is `continue` or `continue with conditions`, the Week 6 score is exactly 45.00 of 45.00, Module 04 passes 20 of 20 gates, Module 05 passes 22 of 22 gates, Module 06 passes 24 of 24 gates, and Checkpoint 02 passes 20 of 20 gates.

The reference progression is `continue with conditions`. Module 07 receives the accepted technical case, unresolved patient-partner requirement, retained equity questions, universal-offer proposal, transparent response adjustment, model non-adoption decision, reviewer conditions, and every prohibition.

## 17. Release, review, and exit criteria

The checkpoint may become a runnable release candidate when:

- all required files exist;
- the builder and validator self-checks pass;
- exact package counts and manifest identity are recorded in `release.json`;
- the full curriculum checker passes;
- Commons advances from 0.61.0 to 0.62.0; and
- the work is committed and pushed.

Named faculty, patient or caregiver, measurement, survey, health-services data, qualitative, equity, accessibility, language-access, privacy, responsible-AI, clinical, governance, model, and independent reproduction reviews remain pending before alpha. No checkpoint acceptance authorizes fielding, patient contact, official HCAHPS reporting, clinical action, targeting, implementation, or model deployment.
