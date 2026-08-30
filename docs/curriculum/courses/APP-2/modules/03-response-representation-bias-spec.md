# APP-2 Module 03: Response, representation, and survey bias

## 1. Module identity, duration, prerequisites, and place in the course

- Module ID: `oclc-app2-03`.
- Course: APP-2, Data for Patient Experience and Engagement.
- Instructional week: 3.
- Hours: 16.5.
- Module version target: 0.1.0.
- Commons release target: 0.58.0.
- Submission: response and representation audit with the cumulative Week 3 release.
- Decision: whether the accepted patient-reported measure and response evidence may enter linked analysis.
- Prerequisites: accepted APP-2 Modules 01 and 02.

Module 03 turns an exact measurement plan into a defensible survey-response study. Learners define who should be represented, separate the target population from the sampling frame and respondent set, inspect response and item missingness by group, and apply one transparent bounded adjustment. The full public MEPS HC-256 person file supplies the real public analytic population. A deterministic and visibly synthetic layer supplies survey invitation, response, Q21 eligibility, Q22 and Q23 truth, and item missingness so that bias can be measured against known truth.

The cumulative Week 3 checkpoint freezes Modules 01 through 03. It carries the Module 02 measurement score of 20 points exactly once. Module 03 adds noncompensable response and representation gates but no additional course points.

## 2. Decision, audience, and claim boundary

The continuing course decision is:

> Should an adult inpatient patient-experience council continue developing a local, accessible, HCAHPS-derived discharge-information feedback process before any fielding or clinical use?

The narrower Module 03 question is:

> Does the selected Q22 and Q23 measure have a clearly defined population, complete teaching frame, interpretable response evidence, bounded missingness, and a transparent adjustment that is adequate to begin linked analysis?

Primary readers are the patient-experience council, a patient or caregiver partner, the APP-2 faculty owner, and a survey-methods reviewer. They need exact denominators, clear data-class labels, subgroup support counts, weight diagnostics, and a decision that can be audited.

MEPS variables and base weights are public federal survey data. The invitation, response, Q21, Q22, Q23, and item-missingness fields are synthetic. No synthetic rate is a real HCAHPS, hospital, MEPS, access, equity, prevalence, or patient-experience estimate. No output authorizes fielding, patient targeting, hospital ranking, clinical action, or a causal mode claim.

## 3. Accepted upstream package and return triggers

Module 03 accepts only the following measurement contract:

- APP-2 Module 02 ID `oclc-app2-02`;
- Module 02 version `0.1.0`;
- Commons release `0.57.0`;
- accepted score `20 of 20`;
- failed gates `none`;
- progression `continue with conditions`;
- selected instrument `updated HCAHPS Discharge Information pair`;
- selected items `Q22` and `Q23`;
- Q21 another-health-facility response makes Q22 and Q23 not applicable;
- Q22 and Q23 each use their own answered denominator;
- the teaching composite is the mean of the two question-level yes proportions;
- the calculation remains local, unadjusted unless explicitly labeled, and unofficial; and
- public-domain HCAHPS-derived wording and the CAHPS trademark boundary remain in force.

Module 03 may add a response design and analytic weights. It may not change an item, wording, order, response choice, scoring rule, skip rule, translation, construct, naming decision, or intended use. Any such change returns to Module 02 before response analysis continues.

## 4. Target population, sampling frame, coverage, and respondent sets

The public analytic target is adults age 18 or older in MEPS HC-256 who have a positive 2024 person weight and at least one reported 2024 inpatient discharge. The reference extraction contains 1,255 people and represents 18,879,474.284615 people under `PERWT24F` before any synthetic response process.

The teaching sampling frame contains all 1,255 selected public records. Every frame record is invited, so frame coverage is 100 percent by construction. This is a property of the teaching design, not evidence that a hospital contact file, phone list, portal list, language route, or discharge roster would have complete coverage.

The module keeps these sets separate:

1. the MEPS HC-256 source population;
2. people with a positive person weight;
3. the adult inpatient-discharge analytic target;
4. the teaching sampling frame;
5. invited frame members;
6. synthetic survey respondents;
7. respondents synthetically eligible for Q22 and Q23 through Q21; and
8. item-specific answered sets for Q22 and Q23.

No denominator may be described only as patients, respondents, or eligible people without naming the set.

## 5. Foundation skill revisited and concept ownership

FND-1 and FND-2 own basic data types, missing values, proportions, weighted means, uncertainty recognition, and reproducible calculation. APP-2 Module 03 revisits those skills for one patient-experience decision.

Module 03 owns:

- target population, sampling frame, coverage, invitation, and response flow;
- overall and subgroup response rates;
- total nonresponse versus item missingness;
- responder and frame comparison;
- mode and language response patterns;
- the distinction between the official public base weight and a teaching response factor;
- one response-cell adjustment with an explicit upper bound;
- effective sample size and weight concentration checks;
- comparison with known synthetic truth;
- privacy, consent, access, and burden conditions; and
- the response-readiness gate in the Week 3 checkpoint.

Module 04 owns linked person-level MEPS analysis, outcome definitions, estimates for the course decision, uncertainty, and the 25-point linked-analysis component. Module 06 owns any machine-learning response model. Module 03 therefore prohibits propensity modeling, variable selection, boosted models, random forests, neural networks, automated tuning, and opaque adjustment.

## 6. Learning outcomes

By the end of the module, a learner can:

- define the target population and show how every analytic set is derived;
- distinguish coverage error, total nonresponse, skip-based non-applicability, and item missingness;
- compute unweighted and base-weighted response rates;
- compare respondents with the full frame using exact support counts;
- inspect response and missingness by age, language, poverty, health, race and ethnicity, sex, proxy status, and assigned mode;
- explain why a high overall response rate can coexist with poor subgroup representation;
- read the public MEPS person weight, stratum, and PSU fields without replacing the survey design;
- build age, language, and poverty response cells that are fixed before outcome comparison;
- calculate a raw inverse response factor and apply a declared upper bound;
- report a bound hit and the resulting weight distribution;
- compare unweighted, base-weighted, and response-adjusted item estimates with known synthetic truth;
- explain why a better estimate is not proof that bias was removed;
- preserve Q21 skip logic and item-specific Q22 and Q23 denominators;
- reject mode, equity, prevalence, hospital, and causal claims that exceed the data; and
- issue an explicit permission or refusal for Module 04.

## 7. Lesson sequence and learner time

| Block | Hours | Work |
|---|---:|---|
| Population and frame contract | 2.0 | Reconcile source, positive-weight, target, frame, and invitation counts |
| Response flow and denominators | 2.5 | Calculate overall response and keep total nonresponse separate from item missingness |
| Representation by group | 2.5 | Compare frame and respondents with counts, weighted totals, and support flags |
| Mode, language, coverage, and access | 2.0 | Inspect programmed mode patterns and state what the complete teaching frame cannot prove |
| Public survey weights and design fields | 2.0 | Read `PERWT24F`, `VARSTR`, `VARPSU`, and the public SAQ response field |
| Bounded response-cell adjustment | 2.5 | Build fixed cells, calculate factors, apply the cap, and inspect weight concentration |
| Known-truth bias recovery | 1.5 | Compare estimators with full-frame synthetic truth and explain residual bias |
| Consent, privacy, and Week 3 release | 1.5 | Complete protections, gates, and cumulative checkpoint records |
| Total | 16.5 |  |

## 8. Official public source suite

The module retains the full official files needed to reproduce the public population and understand its design:

- landing page: https://meps.ahrq.gov/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256
- HC-256 documentation PDF: https://meps.ahrq.gov/data_stats/download_data/pufs/h256/h256doc.pdf
- HC-256 documentation HTML: https://meps.ahrq.gov/data_stats/download_data/pufs/h256/h256doc.shtml
- HC-256 codebook PDF: https://meps.ahrq.gov/data_stats/download_data/pufs/h256/h256cb.pdf
- HC-256 codebook HTML: https://meps.ahrq.gov/data_stats/download_data_files_codebook.jsp?PUFId=H256
- ASCII data ZIP: https://meps.ahrq.gov/data_files/pufs/h256/h256dat.zip
- SAS programming statements: https://meps.ahrq.gov/data_stats/download_data/pufs/h256/h256su.txt
- R programming statements: https://meps.ahrq.gov/data_stats/download_data/pufs/h256/h256ru.txt

The retained five-file suite is 12,353,779 bytes. The data ZIP is 6,125,956 bytes and contains the full 19,140-row fixed-width `h256.dat` file. The two retained PDFs total 869 pages. Source fingerprints, retrieval dates, media types, and teaching roles are stored in `data/source-inventory.csv`.

## 9. Public source interpretation and field contract

HC-256 is the 2024 Full Year Consolidated MEPS public-use file released in August 2026. The documentation states that it contains 19,140 participating people and that 18,683 have a positive person-level weight. Positive-weight records may be used with `PERWT24F` for estimates of the 2024 United States civilian noninstitutionalized population, subject to the documented in-scope periods and survey design.

The extraction reads only fixed-width fields declared in the official statements. Required fields are:

| Field | Use in this module |
|---|---|
| `DUPERSID` | deterministic generation key; not released in derived teaching rows |
| `PANEL` | public source profile |
| `REGION24` | representation audit |
| `PROXY24` | proxy-response audit |
| `INTVLANG` | interview-language audit |
| `AGE24X` | adult selection and age band |
| `SEX` | representation audit |
| `RACETHX` | race and ethnicity audit |
| `OTHLGSPK` | other-language-at-home audit and response cell |
| `RTHLTH53` | health-status audit and generator input |
| `SAQELIG` | adjacent public survey-response example |
| `POVCAT24` | poverty audit and response cell |
| `INSCOV24` | insurance audit |
| `IPDIS24` | at least one inpatient-discharge selection |
| `PERWT24F` | official public base person weight |
| `VARSTR` | variance stratum retained for later design-aware work |
| `VARPSU` | variance PSU retained for later design-aware work |

Published negative values remain missing or inapplicable categories. They are never silently recoded to no, zero, English, healthy, or uninsured.

## 10. Data classes, row identity, and synthetic generator

The release contains three data classes:

1. official public source files from AHRQ;
2. public-derived frame fields selected from HC-256; and
3. synthetic procedural response fields generated for teaching.

Derived rows receive sequential `FRAME-####` identifiers. The public `DUPERSID` is used only as a stable input to SHA-256 draws and is not released in the derived frame. Each synthetic draw is the first 64 bits of SHA-256 over the fixed generator ID, source person ID, and draw label, divided by 2 to the power of 64. This makes the simulation deterministic without an external random-number package.

The generator ID is `app2-m03-response-v1`. It creates:

- an independently assigned mail, phone, or web mode;
- Q21 home or another-health-facility truth;
- Q22 and Q23 binary truth only for the home route;
- a response probability influenced by age, other language at home, poverty, health, proxy status, assigned mode, and the synthetic item state;
- a survey-response indicator; and
- separate Q22 and Q23 missingness among eligible respondents.

Every formula, coefficient, bound, draw label, and category mapping is frozen in `response-contract.json`. The simulation is intentionally nonignorable because response depends partly on synthetic item truth. A transparent cell adjustment should reduce some bias but is not designed to remove all bias.

## 11. Response flow and denominator discipline

The reference release must report exact counts and base-weighted totals for:

- all 19,140 HC-256 source rows;
- 18,683 positive-person-weight rows;
- 1,255 target adults with at least one inpatient discharge;
- 1,255 frame records;
- 1,255 invitations;
- synthetic respondents and nonrespondents;
- full-frame Q21 home truth;
- respondent Q21 home observations;
- Q22 answered and missing records; and
- Q23 answered and missing records.

The overall unweighted response rate is respondents divided by invited frame records. The base-weighted response rate is the sum of `PERWT24F` among respondents divided by the sum among all invited records. An item response rate is answered records divided by respondents for whom that item is applicable. These quantities are not interchangeable.

The module also profiles the real public `SAQELIG` field as an adjacent example. In the target population, 1,251 records are publicly marked SAQ eligible, 993 have SAQ data, and the unweighted public SAQ data rate is 79.37649880 percent. This is not an HCAHPS response rate and is not used as the synthetic generator truth.

## 12. Subgroup representation, mode, and support

The immutable subgroup table reports frame and response support for:

- age band;
- sex;
- race and ethnicity;
- other language at home;
- poverty category;
- health status;
- proxy status;
- interview language;
- insurance coverage;
- region; and
- assigned teaching mode.

Every row contains an unweighted frame count, respondent count, response rate, base-weighted frame total, base-weighted respondent total, base-weighted response rate, difference from the total response rate, and a support flag. Counts below 30 are labeled limited support. The row remains visible because the table is an audit, but it may not support a stable comparative claim.

Assigned mode is independent within the deterministic simulation, and the response formula includes a programmed mode term. Learners may say that the observed synthetic mode pattern is consistent with the programmed simulation. They may not claim that mail, phone, or web causes a response difference in real patients.

## 13. Item missingness and preserved measurement rules

Total nonresponse occurs when an invited frame member does not return the synthetic survey. Item missingness occurs only after response and only when Q21 makes Q22 and Q23 applicable. Q21 another-health-facility truth makes both items not applicable, not no.

The item audit reports Q22 and Q23 separately by total, age band, other-language-at-home group, and assigned mode. Each row contains applicable respondents, answered records, missing records, missing percent, and support status.

The released estimates preserve the Module 02 score contract:

- Q22 yes divided by Q22 yes plus no;
- Q23 yes divided by Q23 yes plus no; and
- teaching composite equal to the mean of those two item proportions.

Nonrespondents, missing item responses, and not-applicable states never enter a denominator as no. The adjusted calculation changes weights, not response states or the score definition.

## 14. Official base weights, variance fields, and teaching response factors

`PERWT24F` is the official 2024 MEPS final person weight. The HC-256 documentation explains that annual weights already include statistical adjustment for full-year and part-year MEPS nonresponse. Module 03 preserves that weight and never labels it a raw sampling weight.

`VARSTR` and `VARPSU` identify the variance strata and primary sampling units used for design-aware variance estimation. They remain in the public-derived frame for later analysis. The Module 03 reference estimate comparison is descriptive and does not publish a design-based confidence interval. Module 04 must use the documented design fields or record a specialist referral before making inferential population claims.

The synthetic response factor is a second, teaching-only quantity. It adjusts the deterministic local response layer placed on top of the public analytic population. It does not alter, reproduce, improve, or replace AHRQ's official nonresponse adjustment.

## 15. Bounded response-cell adjustment

Response cells are fixed before item estimates are compared. The cell is the cross of:

- age band: 18 to 44, 45 to 64, or 65 and older;
- other language at home: yes, no, or an explicit missing or inapplicable state; and
- poverty group: poor, near poor, or low income versus middle or high income.

For each of the 13 observed cells:

1. sum `PERWT24F` across all frame records;
2. sum `PERWT24F` across synthetic respondents;
3. divide the frame total by the respondent total to obtain the raw response factor;
4. cap the factor at 3.0; and
5. multiply each respondent's `PERWT24F` by the bounded factor.

The lower bound is 1.0 because every invited respondent represents at least their own base-weighted mass in this response adjustment. The cap is a declared stability choice, not an optimized value. A cap hit must be visible. Learners report the minimum, maximum, mean, and coefficient of variation of the final weights, the largest weight share, and Kish effective sample size before and after the response factor.

## 16. Known-truth comparison and residual bias

The simulation retains full-frame Q22 and Q23 truth for applicable records. The immutable comparison table reports four estimators for each item and the teaching composite:

1. full-frame base-weighted synthetic truth;
2. respondent unweighted estimate;
3. respondent estimate using `PERWT24F` only; and
4. respondent estimate using `PERWT24F` times the bounded response factor.

Each estimate is paired with signed and absolute bias in percentage points. The reference release must show whether the bounded adjustment improves both items and the composite relative to base weighting alone. It must also show any remaining difference from truth.

A smaller known-truth error demonstrates only that this prespecified adjustment helped in this prespecified simulation. It does not prove missing at random, eliminate item nonresponse bias, validate the response cells, establish a real patient-experience rate, or show that the same method will work after fielding.

## 17. Privacy, consent, access, and public-data use

The raw source is an AHRQ public-use file. The derived release does not retain `DUPERSID`, exact age, or an exact public record linkage key. This is data minimization for the teaching package, not a claim that all privacy risk has been eliminated.

Before any real fielding, the council must approve:

- who is contacted and why;
- plain-language notice and any consent or authorization requirement;
- a refusal and stop-contact route;
- mail, phone, web, language, disability, literacy, and non-digital access;
- proxy rules and patient preference;
- minimum necessary data collection;
- role-based access, retention, deletion, and incident response;
- a process for distress, complaint, or urgent safety content; and
- a patient or caregiver partner's review of burden and acceptable use.

The public-use source does not grant permission to contact people, identify respondents, link to local records, or reuse answers for clinical outreach. No teaching artifact may contain real patient data.

## 18. Learner deliverables and cumulative Week 3 package

The Module 03 workspace contains immutable source, generator, frame, response, weight, estimate, and validation evidence plus these editable records:

- `target-frame.md`;
- `response-flow.csv`;
- `subgroup-representation.csv`;
- `item-missingness.csv`;
- `mode-coverage-interpretation.md`;
- `weighting-decision.md`;
- `bias-recovery.csv`;
- `privacy-consent.md`;
- `reproducibility-check.md`;
- `gate-results.csv`;
- `ai-use.md`; and
- `progression-decision.md`.

The cumulative checkpoint path is `courses/patient-experience-engagement/checkpoints/01-measurement-representation-readiness/`. It must freeze:

- the Module 01 decision charter, audience, evidence needs, partnership terms, source feasibility, and claim boundary;
- the Module 02 instrument, item, scoring, validity, reliability, interpretation, access, rights, score, gate, and progression records;
- the Module 03 target, frame, response, missingness, subgroup, mode, weight, known-truth, privacy, and progression records;
- source, environment, repository, commit, and semantic-version evidence;
- the Module 02 score of 20 points exactly once;
- all response and checkpoint integrity gates; and
- permission or refusal to begin Module 04.

## 19. Assessment and noncompensable gates

Module 03 adds no course points. The cumulative checkpoint carries the accepted Module 02 score of 20.00 out of 20.00. The following response gates are noncompensable:

1. exact Module 02 measurement contract preserved;
2. full official HC-256 source suite fingerprinted;
3. source, positive-weight, target, frame, and invitation counts reconciled;
4. target population and frame stated separately;
5. complete teaching coverage labeled as constructed;
6. total nonresponse separated from Q21 non-applicability and item missingness;
7. overall and subgroup response rates use named denominators;
8. small subgroup support remains visible and bounded;
9. `PERWT24F` remains the official public base weight;
10. synthetic response factors are labeled teaching-only;
11. all 13 observed response cells, the one-record missing-language cell, and any cap hit are reported;
12. weight concentration and effective sample size are reported;
13. Q21, Q22, Q23, and composite rules remain exact;
14. adjusted estimates are compared with known synthetic truth;
15. improvement is not called removal of bias;
16. privacy, consent, access, burden, and stop rules are complete;
17. AI use is disclosed and independently checked;
18. no synthetic-as-real, causal-mode, hospital, clinical, or population overclaim appears; and
19. progression to Module 04 is explicit.

Any failed gate returns the Week 3 package for revision even when the 20-point measurement score is passing.

## 20. Common failure modes and instructor response

| Failure | Required response |
|---|---|
| Target population and frame are treated as synonyms | rebuild the response flow with both sets named |
| Constructed 100 percent coverage is treated as real-world coverage | correct the claim and add a local-frame audit condition |
| Nonrespondents are coded no on Q22 or Q23 | restore missing state and rebuild every score |
| Q21 not applicable is coded no | restore skip logic and return to the Module 02 contract |
| One denominator is shared across Q22 and Q23 | compute item-specific answered denominators |
| `PERWT24F` is called an unadjusted raw weight | use the official final-person-weight description |
| Teaching factor is called an AHRQ or HCAHPS weight | relabel and stop release |
| Cells are chosen after seeing favorable item results | restore the fixed cell contract and rebuild |
| Factor cap is hidden | expose the raw factor, cap, and bound hit |
| Weighting improvement is called unbiasedness | report the remaining known-truth error |
| Small subgroup difference is called inequity | retain support flag and narrow the interpretation |
| Mode pattern is called a real causal effect | limit the statement to the programmed simulation |
| Public data are treated as contact permission | complete privacy and consent review before fielding |
| Synthetic result is called a real patient rate | stop use and correct every data-class label |
| Module 04 begins with a failed gate | return the cumulative checkpoint for revision |

Instructors intervene at the first changed population, hidden denominator, changed response state, mislabeled weight, unsupported subgroup claim, or synthetic-as-real statement.

## 21. Reproducibility, release checks, review, and exit criteria

The package must:

- verify all five official source fingerprints before extraction;
- read the full fixed-width data file from the retained ZIP with Python standard-library code;
- generate stable public-derived frame IDs without releasing `DUPERSID`;
- rebuild the public frame and synthetic response study byte for byte;
- reject an existing output target rather than overwrite it;
- validate source counts, target counts, category mappings, response flow, item states, cell totals, bounds, weights, estimates, and known-truth bias;
- prove that every frame record is invited exactly once;
- prove that Q22 and Q23 are not applicable after the synthetic another-health-facility state;
- prove that nonrespondents have no observed item response;
- prove that adjusted estimate improvement and remaining bias are both reported;
- assemble separate learner and reference workspaces;
- validate a copied workspace with no dependency beyond Python;
- reject a source mutation, changed response state, weight above the cap, invalid score rule, failed gate, or unauthorized progression;
- scan learner-facing text for personal paths, unsupported placeholders, and non-ASCII dash characters;
- assemble and validate the cumulative Week 3 checkpoint;
- pass the whole-curriculum checker; and
- record exact file counts, bytes, SHA-256 values, and validation counts in `release.json`.

Module version 0.1.0 exits as a runnable release candidate at Commons 0.58.0 only when the reference package passes every response gate and the cumulative checkpoint carries the 20-point Module 02 score exactly once. Named APP-2 faculty, patient or caregiver, survey-methods, accessibility, language-access, privacy, responsible-AI, clinical, and independent reproduction reviews remain required before alpha use. An actual course section must map the module to the official half-term calendar before assigning a due date.

The reference release retains five official files totaling 12,353,779 bytes and 869 PDF pages. It produces 12 generated evidence files totaling 583,571 bytes, including 1,255 public-derived frame rows, 1,255 synthetic response rows, 40 subgroup rows, 20 item-missingness rows, 13 response cells, 12 estimate rows, and 23 passing invariants. The assembled workspace contains 31 immutable manifest rows and 44 files. Its manifest is 4,045 bytes with SHA-256 `3d7787a975335518cf4a4f50b5561a323707e2acea6bd1724b1c92a565f64a30`. The reference validator passes 190 checks and the learner validator passes 175 checks.
