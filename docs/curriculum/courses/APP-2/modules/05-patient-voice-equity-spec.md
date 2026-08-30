# APP-2 Module 05: Patient voice, group differences, and equity

## 1. Module identity, status, and durable paths

- Module ID: `oclc-app2-05`.
- Course: APP-2, Data for Patient Experience and Engagement.
- Instructional week: 5.
- Learner work: 16.0 hours.
- Course points: 20.
- Module version: 0.1.0.
- Commons release: 0.60.0.
- Package path: `courses/patient-experience-engagement/modules/05-patient-voice-equity/`.
- Specification path: `docs/curriculum/courses/APP-2/modules/05-patient-voice-equity-spec.md`.
- Status: runnable curriculum-construction release candidate.

The 20 points enter the cumulative Week 6 checkpoint exactly once. Module completion does not authorize patient targeting, clinical action, group ranking, a local workflow change, or a claim that an observed difference proves inequity.

## 2. Role in the course and decision

Module 05 revisits qualitative coding, group comparison, uncertainty, and responsible reporting through patient voice. It does not repeat general data cleaning, chart construction, or model training.

The decision is:

> Which patient-voice and group-difference findings are supportable enough to bring to patient partners for co-design, and which findings must be narrowed, suppressed, or left unanswered?

The reference case uses public MEPS-derived linked evidence and a clearly labeled synthetic comment exercise. The comments teach procedure. They are not patient testimony and cannot estimate theme prevalence, patient sentiment, discrimination, or lived experience.

## 3. Accepted Module 04 handoff

Module 05 starts only after Module 04 grants `permitted for patient-voice and equity analysis`.

| Accepted file | Bytes | SHA-256 | Purpose |
|---|---:|---|---|
| `module04-release.json` | 5,063 | `de31b805351946d644dccc5125deffdffdb993470fbdd74670278c2ca6e7e1d0` | Release identity, permissions, and limits |
| `module04-linked-persons.csv` | 476,048 | `3605f17995f4f3020572dd23ac008a17db9ca78980d15d6a2faadb1efd5e8f24` | 1,255-person public-derived analytic target |
| `module04-linked-events.csv` | 4,808,211 | `16cbb65d1dc0925f4257c73b574617803f05feacbebba134fec3396dd5788997` | 28,455 linked service events |
| `module04-source-inventory.csv` | 6,596 | `63060f9773f38c1ff2d72a51b2d6561725d6263685f7eda7f67a0cf5649988b7` | Identity of all 25 official MEPS files |
| `module04-denominator-registry.csv` | 1,773 | `7263d5c2b4add3eef5493f9c499e711b70f2f31edf90ef649fa56d4a5f61d4de` | Accepted person, event, and unavailable denominators |
| Total | 5,297,691 |  | Five immutable handoff files |

The release must still contain 1,255 people, 28,455 linked events, 782 synthetic respondents, a 45-record limited-support provider-language estimate, and a zero-record portal-preference denominator. The accepted Module 04 manifest is `bc0592acd18b8524be907fd42483e85af4180e0b6f6de35d40e82ea3eae46aa8`.

## 4. Ownership and exclusions

Module 05 owns:

- a governed synthetic comment opportunity and return process;
- a transparent patient-voice codebook;
- a stratified double-coding exercise and agreement calculation;
- adjudication and preservation of disagreement;
- one bounded, rules-based assisted classification after human coding;
- prespecified public MEPS group comparisons with survey uncertainty;
- support, suppression, channel-exclusion, and respectful-language decisions; and
- the 20-point equity and patient-voice memo component.

Module 04 retains ownership of person-event linkage, access definitions, event reconciliation, and base denominators. Module 06 owns patient-partner improvement design and the embedded machine-learning comparison. Module 07 owns the clinician and patient leadership decision.

Out of scope are real patient comments, qualitative saturation claims, clinical NLP, machine learning, autonomous coding, sentiment scoring, topic modeling, causal explanation, proof of inequity, group ranking, patient targeting, and implementation.

## 5. Learning outcomes

By the end of the module, learners can:

1. distinguish synthetic patient-voice training data from observed testimony;
2. define a comment opportunity, received-comment denominator, and evidence gap;
3. apply a codebook with inclusion, exclusion, and ambiguity rules;
4. calculate raw agreement and Cohen's kappa from independently coded records;
5. adjudicate disagreement without erasing the original codes;
6. audit a transparent assisted classifier against a human-coded benchmark;
7. prespecify groups, measures, references, and support rules before comparison;
8. calculate survey-weighted group estimates and contrasts with design uncertainty;
9. suppress unsupported estimates without merging people to evade a rule; and
10. write a patient-voice and equity memo that separates a recorded difference, an equity question, and a supportable next step.

## 6. Workload and sequence

| Work block | Hours |
|---|---:|
| Verify the accepted handoff and synthetic-data boundary | 1.5 |
| Read comments, apply the codebook, and preserve ambiguity | 3.0 |
| Double-code, calculate agreement, and adjudicate | 2.5 |
| Audit bounded assisted classification | 2.0 |
| Prespecify and calculate group comparisons | 3.0 |
| Audit support, channel exclusion, and language | 2.0 |
| Complete the memo, reproduction record, and defense | 2.0 |
| Total | 16.0 |

## 7. Synthetic comment design

The build creates one synthetic comment opportunity for each of the 782 accepted Module 04 respondents. It deterministically assigns a teaching collection channel, language-support offer, accessible-format offer, and return score. The return mechanism intentionally creates coverage differences for learners to detect. It does not model a real survey, patient population, or channel preference.

Exactly 420 opportunities become received comments. Each received record contains a sequential comment ID, the released person link, channel and access fields, synthetic flag, and generated English teaching text. No real comment, quotation, name, location, diagnosis, date, or patient identifier appears.

The instructor truth file records one primary theme, an optional secondary theme, ambiguity, generation rule, and source phrase identifiers. It stays outside assembled learner workspaces. The generator and seed contract remain available for audit.

## 8. Comment codebook and qualitative unit

The unit of coding is one received synthetic comment. The eight fixed primary themes are:

1. communication clarity;
2. medication help;
3. warning signs;
4. access after hours;
5. cost barrier;
6. digital channel;
7. respect and involvement; and
8. other or unclear.

The codebook defines inclusion, exclusion, anchor language, close alternatives, and adjudication notes. A comment receives one primary theme and may retain one secondary theme. Coders may mark `unclear` and request adjudication. They may not infer emotion, diagnosis, identity, intent, experience frequency, or clinical risk beyond the text.

## 9. Double coding and agreement

The audit sample contains 120 comments, with 15 sampled from each instructor-truth theme. Two reference training coders code the sample independently before adjudication. These are simulated curriculum records, not evidence that two human reviewers have completed alpha review.

The package retains coder A, coder B, adjudicated code, disagreement type, and adjudication reason. It reports exact agreement and Cohen's kappa overall and by theme where meaningful. Kappa is interpreted with the code distribution and disagreement table. It is not treated as proof that a codebook is valid or that one threshold makes coding safe.

## 10. Bounded assisted classification

Assisted classification begins only after the 120-comment human benchmark is complete. The reference method is a fixed keyword and phrase rule with no training, no external service, and no patient data. It predicts one primary theme and records the matched phrase or `no match`.

The audit compares predictions with adjudicated human codes on the fixed 120-comment sample. It reports accuracy, per-theme recall, macro recall, disagreements, and records requiring human review. The remaining 300 comments may receive suggested labels, but a person remains responsible for accepting, changing, or rejecting every label used in a submission.

This method is not the Module 06 machine-learning extension. It cannot replace the codebook, independent coding, adjudication, or patient-partner interpretation.

## 11. Comment counts and examples

Theme counts use received comments as their denominator. They may be described as counts or shares of this synthetic received-comment set only. They are never survey-weighted and never called patient prevalence, population sentiment, saturation, representativeness, or an intervention effect.

The package retains two synthetic examples per theme with comment ID, channel, primary and secondary code, and a plain statement that the text is generated. Examples preserve enough context for codebook review but never become a patient quotation.

## 12. Prespecified group-comparison contract

The public MEPS-derived group review is fixed before estimates are calculated.

| Dimension | Reference | Compared groups |
|---|---|---|
| Other language spoken at home | No | Yes; missing remains visible |
| Income group | Middle or high income | Lower income |
| Insurance coverage | Any private insurance | Public insurance only; uninsured |
| Race and ethnicity | Non-Hispanic White only | Hispanic; non-Hispanic Black only; non-Hispanic Asian only; non-Hispanic other or multiple races |

The four measures are delayed medical care because of cost, difficult after-hours contact, usually or always involved in decisions, and any linked telehealth event. The first three use their valid person-response denominator. Any telehealth uses one record per person and does not measure portal access or preference.

No group is a biological explanation, a risk score, or a target for different care. The source categories remain visible and are not merged to make a result reportable.

## 13. Survey estimation and contrasts

Public group estimates use `PERWT24F`, `VARSTR`, and `VARPSU` from the accepted linked-person table. Survey-domain variance retains every sampled PSU with a zero contribution outside the analytic domain.

For a supported group, the package reports unweighted valid records, positive and negative records, weighted denominator, weighted percent, standard error, and 95 percent confidence interval. A contrast is the supported group estimate minus its fixed reference estimate. The contrast standard error comes from one joint linearized survey calculation, not from adding two rounded confidence intervals.

Synthetic comment opportunity and return fields are summarized with counts only. They do not use MEPS population weights.

## 14. Support, suppression, and multiplicity

A public group estimate is reportable for teaching only when it has at least 50 valid records, 10 positive records, 10 negative records, and two contributing PSUs. A contrast requires both group estimates to pass. Unsupported rows retain the group, denominator, positive count, support status, and suppression reason while leaving the protected estimate blank.

The four dimensions and four measures produce many descriptive comparisons. The package does not sort them by effect size or statistical significance. It labels the analysis exploratory, reports confidence intervals, and does not convert a confidence interval into proof of no difference or proof of inequity.

## 15. Equity and channel-exclusion interpretation

The equity review separates four statements:

1. what the source records;
2. what difference or missing voice appears in the teaching evidence;
3. what mechanism is unknown; and
4. what patient partners should examine before any proposal is designed.

The channel audit reports the 782 synthetic opportunities and 420 returns by assigned channel, language-support offer, accessible-format offer, and prespecified public group. Because the mechanism is synthetic, it demonstrates how a collection design can shape whose comments appear. It cannot show that any real group prefers, avoids, trusts, or lacks access to a channel.

Learners replace blaming or deficit language with descriptions of the measurement process. A source-recorded group difference may retain an equity question. It cannot be labeled an inequity, disparity cause, fairness failure, or group trait without stronger evidence and patient-partner interpretation.

## 16. Learner deliverables

The learner submits:

1. `comment-provenance.md`;
2. `codebook-decisions.csv`;
3. `double-coding-review.csv`;
4. `agreement-interpretation.md`;
5. `assisted-classification-review.md`;
6. `group-analysis-plan.md`;
7. `group-support-decisions.csv`;
8. `group-difference-interpretation.md`;
9. `channel-exclusion-review.md`;
10. `equity-patient-voice-memo.md`;
11. `responsible-claims.md`;
12. `reproducibility-check.md`;
13. `gate-results.csv`;
14. `ai-use.md`; and
15. `progression-decision.md`.

The memo is the 20-point course component. Supporting records make the reasoning auditable and pass forward to the Week 6 checkpoint.

## 17. Assessment and noncompensable gates

| Criterion | Points |
|---|---:|
| Corpus provenance, opportunity flow, and synthetic boundary | 4 |
| Codebook use, double coding, disagreement, and agreement | 4 |
| Assisted-classification audit and human ownership | 4 |
| Group plan, survey estimates, support, and contrasts | 4 |
| Equity memo, channel exclusion, claims, reproduction, and defense | 4 |
| Total | 20 |

A numeric score cannot compensate for a changed upstream fingerprint, real patient text, hidden synthetic status, missing independent coding, missing adjudication, assisted classification before the human benchmark, an unsupported released estimate, merged groups used to evade suppression, a prevalence claim from comments, a causal or proof-of-inequity claim, patient targeting, missing AI accountability, or failed reproduction.

## 18. Package and validation contract

The module package contains:

- `README.md`, `VERSION`, `.gitattributes`, `assessment.md`, `data-spec.md`, `instructor-notes.md`, `source-record.yml`, and `voice-equity-contract.json`;
- `build_patient_voice.py`, `build_workspace.py`, and `validate_workspace.py`;
- the five fingerprinted Module 04 handoff files and their inventory;
- generated synthetic opportunity and comment tables;
- the instructor truth outside learner assemblies;
- generated qualitative, group, channel, and invariant evidence;
- 15 learner templates and 15 completed references; and
- `build-report.json` and `release.json`.

Validation must prove deterministic generation, exact handoff hashes, exact row counts, no direct MEPS identifiers, no unmarked real-text claim, group support and suppression, design-aware estimates and contrasts, codebook identity, agreement arithmetic, assisted-classification ordering, complete learner and reference records, all gates, progression logic, copied-validator operation, mutation rejection, existing-target protection, and byte-identical independent builds.

The released package has 33 immutable manifest rows, 15 editable records, and 49 assembled files. Its 4,598-byte manifest has SHA-256 `6f3d93a1a08458cb39fa8d321a67f10dad1ee45b2a8a2742a969ab969f35c8fa`. Reference validation passes 217 checks and learner validation passes 199 checks.

The deterministic evidence release contains 19 generated files and 364,354 bytes. All 28 invariants pass. The public group review has 52 estimate rows, of which 35 are supported, and 36 contrast rows, of which 19 are supported. Suppressed estimates and contrasts remain blank.

## 19. Accessibility, privacy, and responsible AI

All text is synthetic English teaching text. The package does not claim translation quality, language concordance, disability access, or channel preference. Tables use plain headers, complete labels, exact denominators, support status, and text explanations. Meaning does not depend on color.

No protected, identifiable, restricted, or real comment text enters the repository or an external agent. The released teaching keys are module-scoped and are not a claim that the original MEPS public-use data were de-identified by the Commons.

Agent use requires the tool and model, date, purpose, prompt, data classes, affected files, output used or rejected, material claim, independent check, correction, human owner, and accountability statement. An agent may suggest a code only after the fixed human benchmark exists. Repeated agent answers are not independent coders.

## 20. Progression and Module 06 handoff

The allowed progression values are `continue`, `continue with conditions`, `revise and resubmit`, and `stop or refer`. Module 06 may begin only when all patient-voice and equity gates pass and the progression record says `permitted for partnered improvement and embedded ML`.

The handoff includes the accepted Module 04 identity, synthetic corpus identity, codebook, human agreement and adjudication evidence, assisted-classification audit, group support table, group estimates and contrasts, channel-exclusion review, 20-point score, responsible-claims record, AI record, and unresolved patient-partner questions.

Module 06 may use the questions to design a partnered improvement proposal and compare transparent response adjustment with bounded machine learning. It may not train on comment text, turn themes into prevalence, use group-specific clinical thresholds, automate patient targeting, or treat the Module 05 memo as proof of inequity.

## 21. Release, review, and known conditions

The construction reference is a runnable release candidate after all automated checks pass. Alpha still requires named APP-2 faculty, patient or caregiver, qualitative-methods, survey-methods, health-services data, equity, accessibility, language-access, privacy, responsible-AI, clinical, and independent-reproduction reviews.

The patient or caregiver reviewer must examine the codebook language, examples, group interpretation, missing-voice questions, channel alternatives, disagreement record, and proposed feedback route. The reviewer may reject a theme, require a different question, or narrow the handoff.

Known conditions remain:

- every comment is generated and no result is observed patient voice;
- the reference double coding is simulated curriculum evidence, not completed human review;
- the MEPS source records categories and service evidence but not discrimination, preference, trust, portal access, or mechanism;
- small or sparse groups remain visible but unsupported estimates stay suppressed;
- public group differences are descriptive and exploratory;
- machine learning remains reserved for Module 06; and
- no module authorizes clinical action, patient targeting, group ranking, causal inference, or implementation.
