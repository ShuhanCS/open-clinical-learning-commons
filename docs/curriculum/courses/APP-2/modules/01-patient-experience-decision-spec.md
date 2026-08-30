# APP-2 Module 01: Framing a patient-experience and engagement decision

## 1. Module identity, duration, prerequisites, and place in the course

- Module ID: `oclc-app2-01`.
- Title: Framing a patient-experience and engagement decision.
- Version: 0.1.0.
- Commons release: 0.56.0.
- Course: APP-2, Data for Patient Experience and Engagement.
- Instructional week: 1.
- Learner work: 15.5 hours.
- Prerequisites: accepted FND-1 and FND-2 final packages.
- Package path: `courses/patient-experience-engagement/modules/01-patient-experience-decision/`.
- Primary deliverable: patient-experience decision charter.
- Status: runnable release candidate.

Module 01 fixes the patient-reported question before instrument selection, scoring, response analysis, linkage, or improvement design. It asks what recovery at home means to patients, which care experience is being measured, who shares decision authority, and what the full public source can and cannot answer.

The module awards no separate course points. Accepted evidence enters the cumulative 20-point Week 3 patient-measurement package.

## 2. Healthcare decision and named audience

The module decision is:

> Is the recovery-at-home patient-reported construct defined well enough to enter fit-for-purpose instrument selection for a local multilingual measurement study?

The primary decision owner is an adult inpatient patient-experience council that shares authority with a patient/caregiver advisory group. The next action is instrument selection, not implementation.

Required readers include patient and caregiver partners, the inpatient clinical lead, the survey and measurement team, language and disability-access partners, the data steward, and the future improvement owner.

## 3. Foundation skill being revisited or extended

### FND-1 extension

Learners reuse source identity, data grain, dictionaries, missing-value recognition, exact counts, reproducible scripts, accessible tables, and agent disclosure. APP-2 adds patient-reported constructs, public survey reporting, a target sampling frame, patient-partner decision rights, and evidence gaps that cannot be filled by a hospital-level file.

### FND-2 extension

Learners reuse analytic aims, target populations, claim boundaries, model-use limits, and progression decisions. APP-2 applies them before measurement and separates a patient-experience question from satisfaction, health outcome, causal effect, and future prediction.

### DA-730 use

Learners use an exact table and structured journey map. They do not repeat chart-selection or visual-encoding instruction.

## 4. Learning outcomes that can be assessed

By completing Module 01, the learner can:

1. name one decision owner and one patient-partner authority;
2. define the target population, setting, primary construct, and bounded next action;
3. distinguish patient experience, PREMs, PROMs, satisfaction, engagement, partnership, and clinical outcomes;
4. map seven points in the patient journey where evidence, access, or burden changes;
5. reproduce the complete HCAHPS source profile and fingerprints;
6. interpret all 20 source-profile facts and four discharge-anchor profiles;
7. explain why the public file is hospital level and not patient level;
8. separate public evidence from local evidence still required;
9. state language, disability, proxy, mode, and burden questions;
10. assign decision rights and evidence needs to seven stakeholder roles;
11. allow, condition, or prohibit eight common claims;
12. prohibit hospital ranking, patient-level inference, causal claims, and implementation;
13. disclose agent use and independently verify material source claims; and
14. defend an allowed Module 02 progression decision with owned conditions.

## 5. Concept ownership and explicit out-of-scope boundaries

### Module 01 owns

- the accountable patient-experience decision;
- target population and setting at concept level;
- recovery-at-home construct and supporting concepts;
- patient experience, measure-class, engagement, partnership, and outcome distinctions;
- patient-partner authority;
- patient journey and measurement opportunities;
- full-source feasibility and public reporting limits;
- evidence-needs and stakeholder maps;
- claim, stop, and referral rules; and
- Module 02 progression.

### Later modules own

- Module 02: exact instrument version, rights, scoring, direction, validity, reliability, meaningful interpretation, accessibility, and burden;
- Module 03: target frame, coverage, response, item missingness, nonresponse, mode effects, weighting, privacy, and consent;
- Module 04: MEPS sources, person-event linkage, access, communication, engagement, service use, and denominator alignment;
- Module 05: synthetic comment corpus, codebook, agreement, bounded assisted classification, groups, uncertainty, and equity;
- Module 06: patient-partner interpretation, improvement design, measures, feedback, and transparent-versus-ML response adjustment; and
- Module 07: clinician and patient leadership, accountability, patient-facing report, monitoring, and defense.

### Out of scope

- selecting or reproducing a complete survey instrument;
- scoring an instrument or interpreting change;
- estimating local response bias or subgroup experience;
- fitting a weighting, response, or ML model;
- linking person or service-use records;
- analyzing comments;
- ranking public hospitals;
- changing a clinical workflow; and
- using protected, identifiable, workplace, or restricted patient data.

## 6. Lesson sequence with estimated learner time

| Sequence | Activity | Hours | Evidence produced |
|---:|---|---:|---|
| 1 | Course decision, patient-partner authority, source, and claim boundary | 1.0 | annotated case notes |
| 2 | Experience, PREM, PROM, satisfaction, engagement, partnership, and outcome distinctions | 2.0 | construct map |
| 3 | Define the target population, setting, construct, and accountable next action | 2.0 | charter draft |
| 4 | Map the patient journey, measurement points, access, and burden | 2.0 | patient journey map |
| 5 | Reproduce and challenge the full CMS source profile | 2.0 | source-feasibility interpretation |
| 6 | Separate public evidence from local evidence still needed | 1.5 | evidence-needs record |
| 7 | Assign partnership, clinical, measurement, access, governance, and improvement roles | 1.0 | stakeholder map |
| 8 | Audit claims, AI use, stop rules, and progression | 1.0 | claim boundary and AI record |
| 9 | Independent completion, peer critique, revision, and defense | 3.0 | complete package and progression decision |
| Total |  | 15.5 |  |

## 7. Authoritative readings and public clinical sources

1. CMS Patient survey (HCAHPS) - Hospital dataset:
   https://data.cms.gov/provider-data/dataset/dgck-syfz
2. CMS HCAHPS topic page and reporting description:
   https://data.cms.gov/provider-data/topics/hospitals/hcahps
3. CMS Hospital data dictionary:
   https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/hospital/HOSPITAL_Data_Dictionary.pdf
4. AHRQ CAHPS program overview:
   https://www.ahrq.gov/data/cahps.html
5. PCORI Methodology Standards for patient-centered questions and engagement:
   https://www.pcori.org/research-related-projects/about-our-research/research-methodology/pcori-methodology-standards

CMS establishes the public reporting context and exact fields. AHRQ establishes the role of CAHPS patient-experience measurement. PCORI supports patient-centered question and stakeholder discipline. The module does not imply endorsement of its teaching decision by any source organization.

## 8. Dataset inventory, provenance, terms, and teaching purpose

### Source course document

| Item | Value |
|---|---|
| file | `06-APP-2-Patient-Experience-and-Engagement.docx` |
| bytes | 25,906 |
| SHA-256 | `3feff30f5128587a482a3f4ca42979a46059bbe98e3febc98f4556c4cfafc009` |
| verified copies | both supplied curriculum archives |

### Full CMS source

| Item | Value |
|---|---|
| dataset ID | `dgck-syfz` |
| raw bytes | 105,461,119 |
| raw SHA-256 | `b70e598f29552df302e30ed649d178abd1b3d3c868ae97cf8e55453dd33898fc` |
| deterministic gzip bytes | 2,195,547 |
| gzip SHA-256 | `56c6c11f1d61820f367417a00b1e2abaaf02d0b7104d7a5429031e750332503c` |
| rows | 325,720 |
| fields | 22 |
| facilities | 4,790 |
| measure IDs | 68 |
| state or territory codes | 56 |
| reporting period | 2024-10-01 through 2025-09-30 |
| patient-level response rows | 0 |

The source is publicly downloadable from CMS. Source terms and notices control. The Commons records provenance and does not claim ownership of imported data.

The full gzip is included because the raw CSV exceeds GitHub's single-file limit. `gzip 1.14` with level 9 and no stored name produces the accepted deterministic artifact.

## 9. Data dictionary and expected analytic structure

`data/source-profile.csv` contains 20 ordered facts covering source size, dimensions, reporting period, hashes, response support, completed-survey scale, patient-level status, and the no-ranking boundary.

`data/measure-inventory.csv` contains all 68 measure IDs. Each row records the CMS question and answer description, the source field that carries the reported value, facility rows, supported and unavailable values, and teaching role.

`data/discharge-measure-profile.csv` contains four decision anchors:

- `H_COMP_6_Y_P`: primary recovery-at-home anchor, 3,949 reported and 841 unavailable facilities, median 87 percent;
- `H_COMP_6_N_P`: complementary response, 3,949 reported and 841 unavailable facilities, median 13 percent;
- `H_DISCH_HELP_Y_P`: support-after-discharge item, 3,610 reported and 1,180 unavailable facilities, median 86 percent; and
- `H_SYMPTOMS_Y_P`: warning-sign item, 3,610 reported and 1,180 unavailable facilities, median 88 percent.

These are descriptive public reporting facts. The module does not compare named facilities or infer patient-level experience.

## 10. Worked example and instructor walkthrough

The instructor starts with a flawed recommendation:

> Some hospitals report lower recovery-at-home percentages, so the service should begin discharge follow-up calls.

Learners find the defects:

1. the file is hospital level, not a local patient sample;
2. public values do not define the local target population;
3. the statement turns a reporting distribution into a hospital ranking;
4. a PREM is treated as a clinical outcome;
5. response, missingness, language, mode, proxy, and burden are ignored;
6. no fit-for-purpose instrument or scoring decision exists;
7. patients have no stated role in defining or interpreting the question; and
8. the source contains no intervention or causal evidence.

The corrected decision is whether to proceed to instrument selection for a local multilingual measurement study.

## 11. Guided practice

Learners run `profile_source.py --verify-committed`, trace each decision anchor through the 68-row measure inventory, and explain why 841 unavailable response-rate facilities and 1,180 unavailable supporting-item values cannot be discarded without comment.

They then map one discharge journey from admission through feedback, marking what the public source covers, what must be collected locally, where patient partners decide, and where burden or exclusion can occur.

## 12. Independent exercise

Each learner completes all nine editable records for the same recovery-at-home decision. The charter must stay inside the fixed source and scope. Learners may narrow or refer the decision, but they may not substitute a different dataset, implement a workflow, or rank hospitals.

The defense asks the learner to explain why a large public source can still be inadequate for a local patient-experience action.

## 13. Visualization and communication requirements

No chart is required in Module 01. The complete measure inventory, four-row discharge profile, and seven-stage journey are the primary evidence displays.

If a learner adds a display, it must include the exact table, a structured text alternative, clear reporting support, and no named hospital ranking. Color cannot carry meaning alone. Patient-facing language must distinguish public hospital reporting from local patient evidence.

## 14. Exact submission package and filenames

The assembled workspace contains 25 files:

- 15 immutable controls and source evidence files;
- nine editable learner records; and
- `release-manifest.csv`.

Editable records are:

1. `patient-experience-decision-charter.md`;
2. `construct-map.csv`;
3. `patient-journey-map.csv`;
4. `evidence-needs.csv`;
5. `stakeholder-partnership-map.csv`;
6. `claim-boundary.csv`;
7. `source-feasibility-interpretation.md`;
8. `ai-use.md`; and
9. `progression-decision.md`.

The 15-row immutable manifest is 1,787 bytes with SHA-256 `c693e04592994f6f7bef14459b83669a5c824d0bf0b027a0624bab12a3cb4862`.

## 15. Rubric and pass conditions

Module 01 uses 12 noncompensable readiness gates and awards zero course points. The Week 3 checkpoint later scores the 20-point measurement component.

Passing Module 01 requires exact source identity, one accountable decision, a patient-partner authority, complete construct and journey maps, reproduced full-source evidence, public-versus-local evidence separation, access and burden questions, a responsible claim boundary, complete AI verification, and an allowed progression with owned conditions.

The reference passes all 12 gates and records `continue with conditions`.

## 16. Common errors, failure modes, and instructor interventions

- Calling HCAHPS a satisfaction survey without distinguishing patient experience: return to the construct map.
- Treating a reported percentage as an individual response: return to source grain.
- Dropping unavailable values without explaining support: rerun the source profile.
- Ranking named hospitals: fail the claim boundary and remove the ranking.
- Assuming portal response means patient preference: mark the evidence gap for later engagement work.
- Choosing an intervention before an instrument and local frame: narrow the next action to Module 02.
- Naming a patient partner without decision rights: revise the stakeholder map.
- Ignoring language, proxy, disability access, or burden: fail progression until the questions are owned.
- Presenting agent output as verification: require a source, calculation, test, or qualified review.

## 17. Accessibility, equity, privacy, and responsible-claim checks

The charter must require multilingual, disability-accessible, low-literacy, proxy, and non-digital options to be resolved during instrument selection. It must name who could be excluded and who can stop an inaccessible plan.

The source contains public facility identity but no patient rows. Learners may inspect measurement support and structure. They may not infer local subgroup fairness, individual experience, or patient preference.

Every claim is marked allowed, conditional, or prohibited. Hospital ranking, patient-level inference, local representation claims, causal effects, and implementation are prohibited.

## 18. AI and agent policy, required disclosure, and verification

Agents may explain source fields, draft code, propose tests, and help edit records. Only public hospital-level data may be shared. The learner records the tool, date, purpose, prompt, data classes, files, output disposition, material claim, independent check, correction, human owner, and accountability statement.

Full-source hashes, counts, measure support, and profile values require deterministic verification. Repeating the same agent prompt is not an independent check.

## 19. Answer key and instructor notes

The reference decision is `continue with conditions`. The construct is measurable and public reporting supplies useful anchors. The source cannot answer the local patient-experience decision by itself.

The expected next action is Module 02 instrument selection. Seven conditions remain open: faculty approval, patient-partner terms, instrument version and rights, target frame and response plan, accessibility and proxy routes, governance, and independent reproduction.

Clinical action and hospital ranking remain prohibited.

## 20. Runnable acceptance checks for data, code, links, and expected findings

Release requires:

- exact raw and gzip fingerprints;
- 325,720 rows, 22 fields, 4,790 facilities, 68 measures, and 56 state or territory codes;
- one row per facility for every measure;
- exact reporting period;
- 20 source facts, 68 measure rows, and four discharge profiles;
- deterministic profile generation;
- changed-source rejection;
- two identical workspace manifests;
- existing-target refusal;
- complete and starter validation;
- incomplete-record rejection;
- changed-profile, missing-journey, invalid-progression, and hospital-ranking-overclaim rejection; and
- no Unicode dashes, personal paths, hidden dependencies, or unverified external packages.

The source profiler, builder, and validator use only the Python standard library.

## 21. Release status, reviewers, version, and known issues

The module is version 0.1.0 at Commons 0.56.0. It is a runnable curriculum-construction release candidate.

- Complete reference validation: 173 checks.
- Learner starter validation: 134 checks.
- Immutable manifest: 15 rows, 1,787 bytes, SHA-256 `c693e04592994f6f7bef14459b83669a5c824d0bf0b027a0624bab12a3cb4862`.
- Reference progression: `continue with conditions`.
- Module 02 permission: `permitted for curriculum construction`.
- Course points awarded here: 0.
- Clinical action: prohibited.

Required named reviews before alpha include APP-2 faculty, patient/caregiver partner, patient-experience measurement, survey methods, accessibility, equity, privacy and governance, responsible AI, clinical decision owner, and independent reproduction.

Known issues are the lack of patient-level rows, unconfirmed patient-partner participation, pending instrument rights and version decisions, missing local frame and response evidence, and the need to assign an official half-term section. No reference may be described as a local patient-experience finding or authorization to change care.
