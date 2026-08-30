# APP-2 Module 04: Linked patient evidence

## 1. Module identity, status, and durable paths

- Module ID: `oclc-app2-04`.
- Course: APP-2, Data for Patient Experience and Engagement.
- Instructional week: 4.
- Learner work: 16.5 hours.
- Course points: 25.
- Module version: 0.1.0.
- Commons release: 0.59.0.
- Package path: `courses/patient-experience-engagement/modules/04-linked-patient-evidence/`.
- Specification path: `docs/curriculum/courses/APP-2/modules/04-linked-patient-evidence-spec.md`.
- Status: runnable curriculum-construction release candidate.

The 25 points enter the cumulative Week 6 checkpoint exactly once. Module completion does not authorize a local analysis, workflow change, patient contact, or clinical action.

## 2. Role in the course and decision

Module 04 is the first application week after the Week 3 measurement and representation checkpoint. It revisits database linkage, analytic tables, weighted estimation, and uncertainty through a patient-experience problem instead of repeating foundation instruction.

The decision is:

> Can patient-reported, access, communication, digital-service, and service-use evidence be linked with aligned denominators and interpreted without causal, preference, quality, or ranking claims?

The reference case may continue because every official event row links to the person file, the target event totals reconcile, the survey design is retained, and data classes remain distinct. It continues with conditions because the patient-experience response layer is synthetic, portal preference is not measured, one language measure has limited support, and human review remains pending.

## 3. Accepted upstream handoff

Module 04 starts only after Checkpoint 01 grants `permitted for linked analysis`.

| Item | Accepted identity |
|---|---|
| Checkpoint | `oclc-app2-cp01` version 0.1.0 at Commons 0.58.0 |
| Candidate manifest | 135 rows, 23,489 bytes, SHA-256 `5734df858d79721f3efd6766df6299f56d0df49c0aee8b8728b22c284255c903` |
| Module 03 manifest | 31 rows, 4,045 bytes, SHA-256 `3d7787a975335518cf4a4f50b5561a323707e2acea6bd1724b1c92a565f64a30` |
| Accepted target | 1,255 adults with positive `PERWT24F` and at least one 2024 inpatient discharge |
| Base-weighted population | 18,879,474.284615 |
| Accepted synthetic response rows | 1,255, including 782 synthetic respondents |
| Carried Week 3 score | 20.00 of 20.00 from Module 02 exactly once |

The module packages three fingerprinted handoff files totaling 570,340 bytes. A changed checkpoint identity, target order, weight, inpatient count, or response row stops the build.

## 4. Assessable learning outcomes

By the end of Module 04, learners can:

1. state the grain, population, period, key, weight, and claim boundary for one person file and four event files;
2. verify a public person-to-event linkage before interpreting results;
3. construct one person table and one event table without releasing direct source identifiers;
4. reconcile person-reported totals with linked event rows for four service settings;
5. preserve related emergency and inpatient events rather than counting them as unrelated encounters;
6. apply the documented annual-file rule to inpatient stays that begin before the study year;
7. define measure-specific eligible denominators and retain missing or inapplicable values;
8. estimate access and communication measures with `PERWT24F`, `VARSTR`, and `VARPSU`;
9. calculate survey-domain uncertainty while keeping zero-contribution records from all sampled PSUs;
10. distinguish person-grain estimates from event-grain service distributions;
11. interpret telehealth as a service channel without calling it portal access, engagement, or preference;
12. link the accepted synthetic response layer to public MEPS evidence without relabeling the result as observed patient experience;
13. write a noncausal service-use interpretation with complete support and uncertainty; and
14. defend a scored progression decision with exact evidence and accountable agent use.

## 5. Concept ownership and downstream boundaries

### Module 04 owns

- the governed `DUPERSID` linkage between HC-256 and HC-254D through HC-254G;
- person, event, and related-event grain;
- linkage coverage, orphan checks, weight agreement, and reconciliation;
- annual-file period alignment;
- access, communication, shared-decision, language, and affordability measures;
- inpatient, emergency, outpatient, and office-based service-use evidence;
- telehealth event-channel evidence and its limits;
- person-versus-event denominators;
- complex-survey domain estimates and uncertainty;
- linked synthetic-response teaching patterns; and
- the 25-point response and linked-evidence analysis.

### Earlier modules retain ownership

- Module 01 owns the recovery-at-home decision, construct map, patient-partner authority, and public-versus-local boundary.
- Module 02 owns HCAHPS Q22 and Q23 selection, scoring, instrument rights, meaningful interpretation, access, and burden.
- Module 03 owns the target frame, response mechanism, item missingness, representation audit, and bounded response adjustment.

### Later modules own

- Module 05 owns synthetic patient comments, transparent coding, agreement, group differences, equity, and the 20-point patient-voice memo.
- Module 06 owns patient-partner interpretation, improvement design, and the embedded transparent-versus-ML response-adjustment comparison.
- Module 07 owns clinician and patient leadership, accountable recommendation, patient-facing reporting, monitoring, and defense.

## 6. Explicitly out of scope

Module 04 does not:

- use protected, identifiable, restricted, or local patient data;
- claim that a public-use identifier is a local medical-record identifier;
- infer portal access or portal preference from telehealth use;
- treat service use as patient engagement, satisfaction, or quality;
- treat the synthetic Q21, Q22, or Q23 layer as observed patient testimony;
- establish temporal order or causation between communication and service use;
- rank hospitals, providers, patients, demographic groups, or communities;
- change a clinical workflow, contact patients, or target services;
- fit a machine-learning model; or
- award points outside the 25-point Module 04 component.

## 7. Official public-source suite

The complete source suite contains 25 official AHRQ files totaling 18,206,634 bytes. Ten PDFs total 1,101 pages. Each PUF contributes its ASCII data archive, documentation PDF, codebook PDF, SAS statements, and R statements.

| PUF | Product | Official landing page | Full rows | Teaching role |
|---|---|---|---:|---|
| HC-256 | 2024 Full Year Consolidated Data File | https://meps.ahrq.gov/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256 | 19,140 | person characteristics, access supplement, utilization totals, weight, and design |
| HC-254D | 2024 Hospital Inpatient Stays File | https://meps.ahrq.gov/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254D | 1,912 | inpatient event rows and related emergency event identity |
| HC-254E | 2024 Emergency Room Visits File | https://meps.ahrq.gov/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254E | 4,351 | emergency event rows and related inpatient identity |
| HC-254F | 2024 Outpatient Visits File | https://meps.ahrq.gov/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254F | 22,150 | outpatient service and telehealth event evidence |
| HC-254G | 2024 Office-Based Medical Provider Visits File | https://meps.ahrq.gov/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254G | 145,818 | office-based service and telehealth event evidence |

The four event files contain 174,231 rows. Every row links to HC-256, and every event `PERWT24F` value matches its person record.

## 8. Dataset inventory, provenance, and source use

`data/source-inventory.csv` records the title, repository path, raw URL, media type, bytes, SHA-256, PDF pages, and role of all 25 official files. `data/upstream-inventory.csv` records the three accepted handoff files.

The builder reads each ASCII archive directly. It parses positions and variable names from the official R statements. A source archive must contain exactly one expected `.dat` member, and every record in one PUF must have the same fixed width.

The source suite is public federal survey data. It does not become local evidence when linked. Agency attribution, PUF grain, survey design, and public-use limitations remain attached to every derived table.

## 9. Target, linkage flow, and released identity

The target matches Module 03 exactly: `AGE24X >= 18`, `PERWT24F > 0`, and `IPDIS24 >= 1`.

| Stage | People | Events or pairs | Required result |
|---|---:|---:|---|
| Full HC-256 source | 19,140 | not applicable | parse one fixed width |
| Full HC-254D through HC-254G sources | 15,069 unique event users across files | 174,231 events | every event links to HC-256 |
| Accepted target | 1,255 | not applicable | match Week 3 identity and weight |
| Linked inpatient target | 1,255 | 1,692 | equal `IPDIS24` totals person by person |
| Linked emergency target | 904 | 1,601 | equal `ERTOT24` totals person by person |
| Linked outpatient target | 642 | 4,651 | equal `OPTOTV24` totals person by person |
| Linked office-based target | 1,164 | 20,511 | equal `OBTOTV24` totals person by person |
| Related emergency-inpatient events | 692 people | 855 reciprocal pairs | preserve the relationship in both rows |

`DUPERSID` and source event IDs are used inside the build. Released person and event tables use sequential `LINK` and `EVENT` identifiers. This is data minimization for the teaching release, not a claim that a public-use identifier was private or that hashing created de-identification.

## 10. Period alignment and related-event rules

Twelve target inpatient stays begin in 2023 and continue into the 2024 event file. They remain in the annual-file analysis because HC-254D defines the relevant stay records for the 2024 release. Learners must record this carry-in rule before summarizing service use.

HC-254D and HC-254E identify 968 related emergency-inpatient pairs in the full source and 855 in the target. The released event table maps both sides to teaching event IDs. Learners may count setting-specific rows, but they cannot describe each related pair as two unrelated care episodes.

## 11. Measure and denominator registry

The module prespecifies ten person-level access and communication measures:

| Measure | Source field | Valid denominator | Positive definition |
|---|---|---|---|
| Usual source of care | `HAVEUS42` | codes 1 or 2 | yes |
| Regular phone difficulty | `PHNREG42` | codes 1 through 4 | very or somewhat difficult |
| Evening or weekend hours | `OFFHOU42` | codes 1 or 2 | yes |
| After-hours difficulty | `AFTHOU42` | codes 1 through 4 | very or somewhat difficult |
| Asked about other treatments | `TREATM42` | codes 1 or 2 | yes |
| Involved in decisions | `DECIDE42` | codes 1 through 4 | usually or always |
| Options explained | `EXPLOP42` | codes 1 or 2 | yes |
| Provider language match | `PRVSPK42` | codes 1 or 2 | yes |
| Delayed care for cost | `DLAYCA42` | codes 1 or 2 | yes |
| Unable to afford medical care | `AFRDCA42` | codes 1 or 2 | yes |

The immutable denominator registry has 14 rows. It includes the full 1,255-person target, all ten measure-specific domains, the 25,162-event outpatient and office-based digital-service domain, the 538-person complete synthetic-response linkage domain, and a zero-record portal-preference evidence gap.

## 12. Estimation, uncertainty, and support rules

Person estimates use `PERWT24F`, `VARSTR`, and `VARPSU`. The builder calculates a weighted ratio and a Taylor linearized standard error. For domain estimates, all sampled PSUs in the available design remain in the variance calculation; records outside the analytic domain contribute zero.

The reference access results include:

| Measure | Valid n | Weighted percent | Survey SE, percentage points | 95 percent CI |
|---|---:|---:|---:|---|
| Usual source of care | 1,229 | 80.78856833 | 1.35945509 | 78.12403635 to 83.45310031 |
| Regular phone difficulty | 972 | 23.80306525 | 1.74035193 | 20.39197547 to 27.21415504 |
| After-hours difficulty | 708 | 52.44065366 | 2.39646068 | 47.74359073 to 57.13771658 |
| Involved usually or always | 957 | 74.88406042 | 1.77461428 | 71.40581644 to 78.36230440 |
| Delayed for cost | 1,252 | 7.61893012 | 0.84834750 | 5.95616901 to 9.28169123 |
| Provider language match | 45 | 93.59013151 | 3.56420303 | 86.60429356 to 100.00000000 |

Any measure with fewer than 50 valid people is `limited_support`. The provider-language estimate therefore remains visible but cannot support a broad equity conclusion.

## 13. Service-use and digital-service evidence

The 1,255-person target has the following base-weighted service-use estimates:

| Setting | Any-use percent | Mean events per person |
|---|---:|---:|
| Inpatient | 100.00000000 | 1.32034962 |
| Emergency | 70.89748576 | 1.20974128 |
| Outpatient | 50.40502704 | 3.35334442 |
| Office-based | 92.74535872 | 16.71995519 |

The digital-service event domain contains 25,162 outpatient and office-based events. Of those, 1,813 are telehealth. The unweighted event percentage is 7.20530959 and the person-weighted event percentage is 7.37866394. The telehealth rows contain 629 phone, 1,144 video, and 38 other-mode events.

Telehealth is a documented event channel. It is not a measure of portal access, portal preference, digital literacy, engagement, acceptability, or benefit. Portal preference has a registered denominator of zero.

## 14. Linked synthetic-response teaching analysis

The linked teaching analysis uses 538 synthetic respondents with Q21 home and both Q22 and Q23 answered. It compares 309 people with both discharge items answered yes against 229 with one or both answered no. The response-adjusted Module 03 analysis weight is used with the survey design.

| Linked measure | Both yes | One or both no |
|---|---:|---:|
| Usual source, percent | 84.50923314 | 82.02119000 |
| Delayed care for cost, percent | 5.15284197 | 12.69288290 |
| Any emergency visit, percent | 70.53483613 | 70.32076801 |
| Mean office visits | 15.32762989 | 16.96290478 |
| Any telehealth event, percent | 18.28744181 | 19.79853473 |

The Q21, Q22, Q23, response, and response-weight fields are synthetic. The public access and service-use fields are official MEPS data. The resulting differences are procedural teaching associations. They are not observed patient-experience findings, and the overlapping annual periods do not establish temporal order.

## 15. Instructional sequence and learner workflow

The 16.5 hours are allocated as follows:

| Activity | Hours |
|---|---:|
| Source, checkpoint, and decision briefing | 1.0 |
| Person and event grain lesson | 2.0 |
| Fixed-width source and key lab | 2.0 |
| Governed linkage and reconciliation lab | 2.5 |
| Denominator and survey-domain lesson | 2.0 |
| Access and communication estimation lab | 2.0 |
| Service-use and digital-channel lab | 2.0 |
| Interpretation, reproduction, and claim review | 1.5 |
| Submission defense and feedback | 1.5 |
| Total | 16.5 |

Learners first verify the accepted checkpoint and source suite. They then reproduce the linkage, audit event relationships, register denominators, read the immutable estimates, complete the twelve editable records, and defend one randomly selected result by naming its grain, population, data class, weight, uncertainty, and claim limit.

## 16. Required package and submission artifacts

The module builder assembles 65 files:

- 52 immutable rows in `release-manifest.csv`;
- 12 editable learner records; and
- the manifest itself.

The immutable layer includes 25 official source files, three accepted upstream files, two inventories, eleven controls, and eleven generated evidence files. The manifest is 6,529 bytes with SHA-256 `bc0592acd18b8524be907fd42483e85af4180e0b6f6de35d40e82ea3eae46aa8`.

Learners complete:

1. `linkage-plan.md`;
2. `linkage-audit.csv`;
3. `denominator-decisions.csv`;
4. `access-communication-interpretation.md`;
5. `service-use-interpretation.md`;
6. `digital-engagement-interpretation.md`;
7. `linked-evidence-analysis.md`;
8. `responsible-claims.md`;
9. `reproducibility-check.md`;
10. `gate-results.csv`;
11. `ai-use.md`; and
12. `progression-decision.md`.

## 17. Assessment map and noncompensable gates

The response and linked-evidence analysis is worth 25 points:

| Component | Points |
|---|---:|
| Source identity and governed linkage | 5 |
| Reconciliation and denominators | 5 |
| Access, communication, and digital-service evidence | 5 |
| Service use and linked pattern analysis | 5 |
| Reproduction, claims, and defense | 5 |
| Total | 25 |

Twenty gates are noncompensable. They cover the accepted checkpoint, all source and upstream fingerprints, fixed-width parsing, full event linkage, weight agreement, target identity, direct-ID removal, four setting reconciliations, the annual-file rule, related events, denominators, survey design, missingness, limited support, digital-service claims, data-class separation, prohibited uses, reproduction, AI accountability, and progression.

The reference earns 25.00 of 25.00 with 20 of 20 gates passing. A failed gate blocks the score from authorizing progression.

## 18. Common errors and instructor response

- Joining on the wrong key: stop and restore `DUPERSID` from the official layouts.
- Treating an event row as a person: return to grain and denominator registration.
- Summing repeated event-row weights to estimate people: rebuild the person table and use one person weight once.
- Dropping the 12 carry-in stays because their start year is 2023: return to the HC-254D annual-file definition.
- Calling 855 related emergency-inpatient pairs 1,710 unrelated encounters: restore reciprocal event links.
- Using the full 1,255 as every access denominator: retain measure-specific valid domains.
- Dropping missing or inapplicable values before counting them: restore the denominator registry.
- Reporting the 45-record language measure as settled: mark limited support and narrow the claim.
- Calling telehealth portal preference or engagement: record that portal evidence is unavailable.
- Treating synthetic Q22 and Q23 associations as patient testimony: separate data classes and rewrite the result.
- Claiming communication changed service use: remove causal wording and state overlapping time periods.
- Using an agent result as verification: require a source, calculation, test, or qualified human review.

## 19. Accessibility, equity, privacy, and responsible claims

Every estimate must have an exact table and a plain-language interpretation. Structured text carries the same denominators, units, uncertainty, and conditions as any visual used later. General visualization theory remains in DA-730.

Equity work begins with coverage, missingness, language, channel, and support. The provider-language domain is limited support. No missing group is described as uninterested, noncompliant, or disengaged.

The repository contains public-use data only. Released teaching tables omit direct public-use person and event identifiers. No local patient row, protected data, contact route, or restricted comment enters the package or an external agent.

Supported claims describe the pinned public sources, exact linkage, denominators, survey estimates, uncertainty, and teaching limits. Local experience, portal preference, channel acceptability, clinical quality, causation, ranking, targeting, and implementation remain unsupported or prohibited.

## 20. Reproduction, validation, and agent accountability

`build_linked_evidence.py` uses the Python standard library. It verifies all 28 fingerprints, parses five fixed-width PUFs, checks the checkpoint identity, builds both teaching tables, reconciles counts, estimates measures, and evaluates 25 invariants.

Two independent evidence builds match byte for byte. The committed evidence matches a clean rebuild. `build_workspace.py` creates two identical reference workspaces and refuses to overwrite an existing target. `validate_workspace.py` runs from the source package and from an assembled copy, then rejects a changed event, failed gate, and invalid progression.

Validation results:

- complete reference: 249 checks;
- learner starter: 234 checks;
- evidence invariants: 25 of 25 pass;
- assembled files: 65;
- generated evidence: 11 files and 5,298,996 bytes; and
- external Python dependencies: zero.

The AI-use record names the tool, date, task, shared data classes, files, output disposition, material claim, independent checks, correction, human owner, and accountability statement. Agent output does not approve an interpretation or downstream use.

## 21. Release status, reviewers, conditions, and handoff

Module 04 is version 0.1.0 at Commons 0.59.0. The reference progression is `continue with conditions`; Module 05 is `permitted for patient-voice and equity analysis`.

Required named reviews before alpha include APP-2 faculty, a patient or caregiver partner, survey methods, health-services data, qualitative methods, accessibility, equity, privacy and governance, responsible AI, clinical decision ownership, and independent reproduction.

Known conditions remain:

- telehealth does not answer portal-access or portal-preference questions;
- the provider-language estimate has limited support;
- the response layer is synthetic and cannot support a real patient-experience association;
- public MEPS evidence cannot replace a local roster, workflow, survey, or patient partnership;
- causal, ranking, targeting, clinical, and machine-learning uses remain prohibited; and
- an actual course section must map the Week 6 checkpoint to the official half-term calendar.

The durable next path is `docs/curriculum/courses/APP-2/modules/05-patient-voice-equity-spec.md`. Module 05 must accept this module's 25-point identity, linkage manifest, denominator registry, data-class boundaries, limited-support condition, portal evidence gap, and progression decision before building the synthetic comment and equity case.
