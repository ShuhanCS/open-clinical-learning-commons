# FND-1 Module 04: Cleaning and profiling

## 1. Module identity and place in the course

- Course: FND-1 Healthcare Data Foundations.
- Module: 04 of 07.
- Instructional week: 4.
- Learner workload: 16.5 hours.
- Prerequisite: accepted or conditionally accepted Week 3 checkpoint.
- Module version: 0.1.0.
- Defect-release version: 0.1.0.
- Commons release: 0.32.0.
- Status target: runnable release candidate.
- Decision owner: data-quality lead.
- Core input: exact Module 03 analytic-table release frozen by Checkpoint 1.
- Assessment role: required quality gateway whose evidence enters the cumulative 25-percent Week 6 checkpoint.
- Handoff: resolved analytic table plus visible unresolved quality conditions for Module 05.

Module 04 teaches learners to find, classify, document, and respond to healthcare-data problems without silently rewriting the source. The accepted 374-row analytic table remains immutable. A separately versioned teaching layer adds deterministic defects, exact expected counts, and a transparent manifest. The learner profiles that layer, distinguishes impossible values from extreme but possible values, and makes a bounded stop, fix, proceed, or proceed-with-conditions recommendation.

## 2. Technical decision and named audience

### Decision

> Can this analytic table move into descriptive work now, or must the team stop, fix, proceed, or proceed with conditions?

### Decision owner

A data-quality lead who is accountable for releasing analytic inputs to a clinical analytics reviewer.

### Receiving audience

The Module 05 clinical analytics reviewer who needs:

- a resolved one-row-per-person table;
- a complete issue and resolution trail;
- fields and denominators that retain their meaning;
- unresolved conditions that remain visible; and
- evidence that no accepted source value was silently changed.

### Allowed decisions

- `stop`;
- `fix`;
- `proceed`; or
- `proceed with conditions`.

The reference decision has two stages:

1. `fix` the seeded defect layer because blocking validity, uniqueness, consistency, and completeness defects are present; then
2. `proceed with conditions` using the byte-identical accepted table while retaining natural optionality, extreme-value review, and small-cell cautions.

The module does not authorize a learner to repair the accepted Checkpoint 1 release in place.

## 3. Foundation skill and handoff

### Foundation skill

Create a machine-readable profile, risk log, resolution log, and decision record that distinguish:

- source fact from teaching defect;
- missing from structurally optional;
- invalid from unusual;
- duplicate row from repeated clinical event;
- coding drift from a new legitimate code;
- correction from exclusion;
- row count from affected-person count;
- detected issue from resolved issue; and
- technical readiness from clinical validity.

### Upstream handoff

Checkpoint 1 freezes:

- analytic-table version 0.1.0;
- 374 rows and 29 fields;
- SHA-256 `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a`;
- cohort-definition version 0.1.0;
- one unique patient and index encounter per row; and
- all source, index, history, follow-up, and metadata meanings.

### Downstream handoff

Module 05 receives:

- `resolved-analytic-table.csv`, byte-identical to the accepted input in the reference answer;
- analytic data dictionary;
- quality profile;
- missingness profile;
- quality-rule results;
- quality-risk log;
- resolution log;
- decision record; and
- unresolved conditions that descriptive work must retain.

Module 05 cannot convert missing values to zero, collapse small cells into claims, or infer that an extreme value is erroneous without a new rule and evidence.

## 4. Assessable outcomes

By the end of Module 04, the learner can:

1. verify the accepted input by bytes and SHA-256 before profiling;
2. explain why the defect release is a separate versioned layer;
3. distinguish table grain, row count, distinct patient count, and duplicate count;
4. profile every one of the 29 analytic fields;
5. calculate non-missing, missing, distinct, minimum, maximum, and invalid counts;
6. classify completeness, validity, consistency, uniqueness, timeliness, and conformance issues;
7. detect all 20 seeded defect families at their exact expected counts;
8. preserve all 68 manifest change rows and connect them to 56 issue cases;
9. distinguish malformed timestamps from valid source timestamps;
10. distinguish invalid age values from five source ages at least 100;
11. identify negative counts and numerator-like counts exceeding parent counts;
12. identify coding drift separately from an unknown vocabulary value;
13. reconcile next-state values with required companion fields and elapsed-day boundaries;
14. verify flag vocabularies and endpoint precedence;
15. assess structurally allowed source missingness without calling it error;
16. flag extreme but possible history counts for review without changing them;
17. identify small cells and state a caution without inferring privacy safety or instability automatically;
18. write every issue in the required machine-readable risk-log schema;
19. record correction, retention, exclusion, escalation, owner, and status separately;
20. rebuild the resolved table from the immutable accepted source;
21. prove that the resolved table is byte-identical to the accepted input;
22. make and defend an allowed readiness decision;
23. disclose material AI use and independently verify at least one suggestion; and
24. hand off exact data and conditions to Module 05.

## 5. Concept ownership and out-of-scope boundaries

### Module 04 owns

- deterministic teaching-defect generation;
- source-versus-defect separation;
- field-level profiling;
- missingness description;
- uniqueness and duplicate checks;
- type and timestamp conformance;
- vocabulary and version conformance;
- cross-field consistency;
- extreme-value review flags;
- small-cell caution;
- quality risk and resolution logs;
- stop/fix/proceed decision; and
- resolved-table handoff.

### Module 04 does not own

- changing cohort eligibility or time zero;
- adding or removing analytic fields;
- redefining denominators;
- statistical imputation;
- causal assumptions about missingness;
- statistical outlier removal;
- descriptive inference;
- regression, prediction, or machine learning;
- production master-data management;
- clinical terminology governance;
- privacy re-identification testing; or
- a claim that synthetic records represent real patients.

### Correction rule

The reference defect layer is intentionally corrupted. Its seeded values can be resolved only from the immutable accepted input and manifest. Natural source characteristics remain unless a separately authorized source or cohort change proves an error.

### Exclusion rule

No row is excluded merely because it is inconvenient, missing an optional value, extreme, or in a small category. Exclusion requires a written rule, affected denominator, analytic consequence, owner, and versioned output.

## 6. Lesson sequence and learner time

| Activity | Hours | Required evidence |
|---|---:|---|
| Decision, source freeze, and quality vocabulary | 1.25 | source verification note |
| Grain, uniqueness, duplicates, and row conservation | 1.50 | duplicate and key checks |
| Types, dates, ranges, and vocabulary conformance | 2.00 | validity profile |
| Missingness and structural optionality | 1.75 | missingness profile |
| Cross-field consistency and temporal rules | 2.00 | rule results |
| Extreme values, coding drift, and small cells | 1.50 | review flags and cautions |
| Guided notebook lab | 2.25 | executed notebook |
| Risk and resolution log studio | 1.75 | complete machine-readable logs |
| Stop/fix/proceed decision and peer review | 1.25 | decision draft and peer response |
| Reproduction, AI verification, and handoff | 1.25 | final package and validator output |
| Total | 16.50 |  |

### Teaching rhythm

The instructor reveals the defect categories before the exact rows. Learners must find the issues through profiling and rules. Exact counts become available for reconciliation after an initial independent attempt.

### Feedback checkpoints

- After grain and uniqueness: verify 379 defect-layer rows, 374 distinct patient IDs, and 5 duplicate rows.
- After validity profiling: reconcile the 20 seeded rule families.
- After missingness: separate seeded missing values from structurally allowed blanks.
- Before decision: confirm the risk log and resolution log use the same issue IDs.
- Before handoff: prove the resolved output matches the accepted input byte for byte.

## 7. Readings and authoritative sources

### Required module records

1. Checkpoint 1 specification and release record.
2. Module 03 cohort specification, table specification, data dictionary, and release record.
3. Module 04 data specification and quality-rule registry.
4. SQLite date and time function documentation.
5. pandas missing-data and duplicate-handling documentation for the notebook path.

### Public technical references

- SQLite date and time functions: https://www.sqlite.org/lang_datefunc.html
- pandas missing data: https://pandas.pydata.org/docs/user_guide/missing_data.html
- pandas duplicate detection: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html
- Synthea CSV data dictionary: https://github.com/synthetichealth/synthea/wiki/CSV-File-Data-Dictionary
- Synthea license: https://github.com/synthetichealth/synthea/blob/master/LICENSE

### Reading questions

- When is a blank value expected rather than defective?
- Why is a repeated patient ID not always a duplicate in an event table but always violates this table's grain?
- Why is age 107 unusual but not automatically invalid?
- What evidence would authorize a change to an extreme count?
- How can a valid-looking next-state label conflict with its companion fields?
- Why must the risk log preserve denominator and consequence?
- Why is rebuilding from the accepted release safer than editing bad cells manually?

## 8. Dataset inventory, provenance, rights, and teaching purpose

### Accepted input

| Property | Value |
|---|---|
| source path | Module 03 `outputs/analytic-table.csv` |
| version | 0.1.0 |
| rows | 374 |
| fields | 29 |
| bytes | 121,787 |
| SHA-256 | `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a` |
| grain | one included synthetic patient and index event per row |
| real patients | none |

### Defect release

The defect builder creates:

- an exact accepted-input copy;
- a 379-row defective copy with the same 29 fields;
- 5 exact duplicate appended rows;
- 68 manifest change rows;
- 20 seeded defect families affecting 56 issue cases;
- 8 natural source-characteristic review rules;
- a 28-row quality-rule registry; and
- a SQLite teaching database containing all layers and metadata.

### Rights

- Upstream Synthea source and generator: Apache-2.0.
- Commons code: MIT.
- Commons documentation: CC-BY-4.0.
- Defect layer: deterministic teaching transformation of the public synthetic release.

### Teaching purpose

The layer is deliberately imperfect and fully reversible. It trains detection and response. It cannot be presented as naturally observed corruption, production EHR behavior, or a measured real-world data-quality rate.

## 9. Defect-release structure and exact rules

### Layer separation

| Layer | Rows | Fields | Purpose |
|---|---:|---:|---|
| accepted analytic table | 374 | 29 | immutable source of truth for this exercise |
| defective analytic table | 379 | 29 | learner profiling and repair input |
| resolved analytic table | 374 | 29 | reference handoff, byte-identical to accepted input |

### Seeded defect families

| ID | Category | Rule | Expected cases | Severity | Reference response |
|---|---|---|---:|---|---|
| D01 | uniqueness | exact duplicate person rows | 5 | blocking | drop appended duplicates by manifest and verify grain |
| D02 | completeness | missing index encounter ID | 3 | blocking | restore accepted key |
| D03 | validity | age below adult eligibility | 3 | blocking | restore accepted age |
| D04 | validity | age above 120 | 2 | blocking | restore accepted age |
| D05 | conformance | malformed index-start timestamp | 3 | blocking | restore accepted timestamp |
| D06 | temporal consistency | index stop before index start | 3 | blocking | restore accepted stop |
| D07 | vocabulary validity | unknown index class | 2 | blocking | restore accepted class |
| D08 | coding drift | case-changed acute class | 3 | material | restore canonical code and document drift |
| D09 | validity | negative encounter-history count | 3 | blocking | restore accepted count |
| D10 | cross-field consistency | acute history exceeds all encounters | 3 | blocking | restore accepted counts |
| D11 | completeness | missing required gender | 4 | material | restore accepted value |
| D12 | vocabulary validity | invalid gender code | 3 | material | restore accepted value |
| D13 | cross-field consistency | no-record state has next-event companions | 3 | blocking | restore accepted blank companions |
| D14 | cross-field consistency | recorded next state lacks companions | 3 | blocking | restore accepted companions |
| D15 | temporal validity | elapsed next-event days at or below zero | 2 | blocking | restore accepted elapsed days |
| D16 | temporal validity | elapsed next-event days above 30 | 2 | blocking | restore accepted elapsed days |
| D17 | vocabulary validity | acute-return flag outside 0 or 1 | 3 | blocking | restore accepted flag |
| D18 | endpoint consistency | death flag conflicts with endpoint precedence | 2 | blocking | restore accepted endpoint |
| D19 | provenance conformance | source-release label drift | 2 | blocking | restore accepted release label |
| D20 | version conformance | cohort-definition version drift | 2 | blocking | restore accepted version |

Expected affected cases across D01 through D20: 56.

Expected manifest change rows: 68 because D13 and D14 each alter three companion fields per affected case.

### Natural source-characteristic rules

| ID | Characteristic | Expected accepted rows | Classification | Reference response |
|---|---|---:|---|---|
| N01 | missing death date | 343 | structurally optional | retain and document |
| N02 | missing index reason code and description | 226 | structurally optional pair | retain and document |
| N03 | no next encounter and blank companion fields | 263 | structurally consistent absence | retain explicit state and blanks |
| N04 | age at least 100 | 5 | extreme but possible synthetic value | review, do not auto-correct |
| N05 | prior encounter count above 100 | 2 | extreme history count | review, do not auto-correct |
| N06 | prior medication count above 100 | 1 | extreme history count | review, do not auto-correct |
| N07 | race categories with fewer than 10 rows | 6 | small-cell caution | retain exact source, limit display |
| N08 | next-state or endpoint small cells | 12 | small-cell caution | retain exact source, limit claims and display |

N08 includes 4 urgent-care next states and 8 death endpoints. It is a communication condition, not proof of privacy risk or invalidity.

## 10. Worked example and instructor walkthrough

### Walkthrough sequence

1. Verify the accepted source bytes and fingerprint.
2. Build the defect layer into a new target.
3. Confirm accepted and defective tables use the same 29-field header.
4. Count 379 defective rows and 374 distinct patients.
5. Locate the 5 duplicate patient IDs.
6. Load the 28 quality rules.
7. Execute each rule and compare observed with expected counts.
8. Produce one 29-row field profile.
9. Produce one 29-row missingness profile.
10. Reconcile 68 manifest change rows to 56 seeded issue cases.
11. Review the eight natural characteristics separately.
12. Build the 28-row risk log.
13. Record a resolution or retained condition for each issue.
14. Rebuild the resolved table from the accepted release.
15. Verify 374 rows, 29 fields, 121,787 bytes, and the accepted SHA-256.
16. Make the staged `fix`, then `proceed with conditions` recommendation.

### Missingness example

Supported:

> Death date is blank for 343 of 374 accepted rows because most synthetic patients have no recorded death date in this release.

Unsupported:

> The dataset is 91.7 percent incomplete and should impute death dates.

### Extreme-value example

Supported:

> Five accepted rows have age at index at least 100. They are review flags, not automatic errors.

Unsupported:

> All ages over 99 are impossible and should be removed.

### Duplicate example

The accepted analytic table has one row per person. The five exact appended rows violate that declared grain. This differs from an encounter table, where repeated patient IDs are expected because one person can have many encounters.

## 11. Guided practice

### Practice 1: Grain before duplicates

Compare repeated patient IDs in an encounter table with repeated patient IDs in the one-row-per-person table.

### Practice 2: Missing versus optional

Classify death date, reason code, index key, and next-event fields using the table contract.

### Practice 3: Timestamp conformance

Parse valid timestamps, malformed timestamps, and stop-before-start pairs. Record which rule each failure triggers.

### Practice 4: Vocabulary and drift

Compare `emergency`, `Emergency`, and `telehealth`. Distinguish case drift from an unknown value.

### Practice 5: Cross-field counts

Explain why prior acute encounters cannot exceed all prior encounters.

### Practice 6: Explicit absence

Check both directions of the next-state contract: absent state with blank companions and recorded state with required companions.

### Practice 7: Flag and endpoint logic

Test values outside 0 or 1 and death-precedence mismatches.

### Practice 8: Extreme but possible

Review age 107, encounter count 187, and medication count 185 without changing them.

### Practice 9: Small cells

Write a display and interpretation caution for counts 1, 4, 5, and 8 without claiming a universal suppression threshold.

### Practice 10: AI verification

Verify one AI-suggested rule or correction against the accepted source, manifest, or independent code.

## 12. Independent exercise

The learner independently:

1. verifies the accepted source;
2. builds the defect release;
3. runs or completes the data-quality notebook;
4. profiles all 29 fields;
5. executes all 28 quality rules;
6. detects every seeded defect family;
7. classifies the eight natural characteristics;
8. completes the quality-risk log;
9. completes the resolution log;
10. rebuilds or approves the resolved table;
11. proves the final handoff fingerprint;
12. writes the decision record;
13. completes transformation, reproduction, and AI-use records; and
14. submits an allowed disposition.

The learner may not copy the reference risk log or resolved table as a substitute for explaining the rules and rerunning the workflow.

## 13. Visualization and communication requirements

### Required communication

- 29-row field profile;
- 29-row missingness profile;
- 28-row rule-result registry;
- 28-row quality-risk log;
- 28-row resolution log;
- stop/fix/proceed decision;
- exact handoff fingerprint; and
- notebook narrative explaining at least four issue categories.

### Optional visualization

No chart is required. Exact tables better preserve issue IDs, counts, denominators, severity, action, owner, and status.

If a learner adds a missingness plot or defect summary:

- the exact CSV remains required;
- bars begin at zero when encoding counts;
- all categories and denominators remain available;
- color is not the only status cue;
- small cells remain exact in the internal teaching record but are handled cautiously in any public-facing display; and
- the plot cannot imply that optional missingness is error.

## 14. Exact submission package

```text
module-04-submission/
  VERSION
  README.md
  data-spec.md
  data-dictionary.csv
  data/
    accepted-analytic-table.csv
    defective-analytic-table.csv
    defect-manifest.csv
    quality-rules.csv
    fnd1-quality-defects.sqlite
  notebooks/
    04-data-quality.ipynb
  outputs/
    quality-profile.csv
    missingness-profile.csv
    quality-rule-results.csv
    quality-risk-log.csv
    resolution-log.csv
    resolved-analytic-table.csv
  stop-fix-proceed.md
  transformation-record.md
  reproducibility-check.md
  ai-use.md
```

Required tag: `fnd1-quality-v0.1.0`.

The submission records but does not duplicate the 141 MB Module 02 database or source archive.

## 15. Rubric and pass conditions

| Criterion | Points |
|---|---:|
| Accepted-source verification and immutable-layer separation | 15 |
| Complete field and missingness profiles | 15 |
| Seeded-rule detection and exact reconciliation | 20 |
| Natural-characteristic classification and claim limits | 15 |
| Risk log, resolution log, and owner/status evidence | 15 |
| Stop/fix/proceed reasoning and Module 05 handoff | 10 |
| Reproduction, accessibility, privacy, and AI accountability | 10 |
| Total | 100 |

### Pass threshold

At least 80 points.

### Noncompensable gates

- exact accepted source;
- accepted source preserved unchanged;
- separately versioned defect layer;
- all 29 fields profiled;
- all 20 seeded defect families detected;
- 68 manifest changes reconciled;
- duplicate-person grain restored;
- blocking invalid and inconsistent values resolved;
- optional missingness not imputed or mislabeled;
- extreme accepted values not silently changed;
- small-cell condition retained;
- risk and resolution logs align by issue ID;
- resolved table fingerprint verified;
- reproducible notebook or approved accessible alternative;
- material AI disclosure and verification; and
- allowed stop/fix/proceed disposition.

## 16. Common failures and instructor interventions

| Failure | Intervention | Required evidence |
|---|---|---|
| Profiles before checking grain | Count rows and distinct patient IDs first. | 379 rows, 374 patients, 5 duplicates. |
| Calls every blank an error | Compare with field nullability and state rules. | Allowed versus seeded missingness table. |
| Drops all incomplete rows | Show denominator loss and source meaning. | Explicit rule and consequence or restoration. |
| Treats age 107 as impossible | Separate validity bound from review threshold. | N04 retained and documented. |
| Treats 187 encounters as a typo | Trace to accepted source before editing. | N05 retained and documented. |
| Lowercases every code silently | Use manifest and canonical vocabulary. | D08 resolution record. |
| Fixes only one side of a consistency rule | Check state, ID, start, and elapsed days together. | D13 and D14 all companions reconcile. |
| Recomputes the cohort | Return to the immutable Checkpoint 1 release. | Unchanged cohort version and source hash. |
| Edits CSV manually | Rebuild the layer and outputs. | Byte-reproducible run. |
| Imputes death | Remove imputation and state optionality. | N01 retained. |
| Uses a small-cell threshold as universal law | State the teaching and audience boundary. | N07/N08 condition wording. |
| Makes a clinical claim | Return to technical readiness. | Synthetic-data claim boundary. |

## 17. Accessibility, equity, privacy, and claim checks

### Accessibility

- all machine-readable outputs have explicit headers;
- issue status, severity, and decision use text;
- no evidence relies on color;
- commands are copyable;
- notebook Markdown explains the purpose of each code section;
- an accessible Python script and exact CSV path is available if notebook interaction is a barrier;
- optional charts require text and exact-table alternatives; and
- filenames communicate content.

### Equity

All learners receive the same accepted input, deterministic defect rules, and validation standard. Technical support may address environment access without changing the evidence requirement. The small-cell discussion avoids equating rare categories with errors or erasing them from internal analysis.

### Privacy

The records are synthetic. Identity-like fields excluded upstream remain excluded. Learners cannot substitute real patient or workplace data. Small-cell caution is taught as a disclosure and interpretation concern, not proof that synthetic people can be re-identified.

### Claims

- Defect rates describe a deliberately seeded teaching layer.
- Natural-characteristic counts describe only the accepted synthetic release.
- Missing does not mean negative or absent clinically.
- Extreme does not mean erroneous.
- Resolved does not mean clinically validated.
- No real quality, safety, access, utilization, or outcome inference is supported.

## 18. AI policy, disclosure, and verification

### Permitted uses

- explain a profiling method;
- suggest a validation rule;
- diagnose a timestamp or type failure;
- compare duplicate-detection approaches;
- propose risk-log wording; and
- edit documentation.

### Prohibited uses

- invent issue counts;
- change expected values to make a check pass;
- fabricate notebook output;
- infer a correction without the accepted source or manifest;
- hide a failed rule;
- share protected data or credentials;
- recommend imputation without a later approved modeling contract; or
- turn synthetic quality facts into clinical conclusions.

### Required record

For each material use, record:

- date;
- tool and model;
- purpose;
- data shared;
- advice used;
- human verification;
- accepted, changed, or rejected decision; and
- affected file, field, rule, or query.

At least one material rule, count, correction, or decision suggestion is verified against the immutable source, defect manifest, independent code, or authoritative documentation.

## 19. Answer key and instructor materials

### Source and defect facts

- accepted rows: 374;
- accepted fields: 29;
- accepted bytes: 121,787;
- defective rows: 379;
- distinct defective patient IDs: 374;
- exact duplicate rows: 5;
- seeded defect families: 20;
- seeded issue cases: 56;
- manifest change rows: 68;
- natural-characteristic rules: 8;
- total quality rules: 28.

### Accepted missingness

- death date: 343;
- index reason code: 226;
- index reason description: 226;
- next encounter ID: 263;
- next start: 263;
- next elapsed days: 263.

### Accepted extremes and small cells

- age at least 100: 5;
- prior encounter count above 100: 2;
- prior medication count above 100: 1;
- race rows in categories smaller than 10: 6;
- urgent-care next states: 4;
- death endpoints: 8.

### Reference decision

Initial defect layer: `fix`.

After deterministic restoration and duplicate removal: `proceed with conditions`.

Conditions:

- retain optional missingness as missing;
- carry extreme-value review flags;
- preserve small-cell cautions;
- do not infer real population results; and
- use the exact resolved table and quality records in Module 05.

### Review order

1. verify source fingerprint;
2. verify separate layer;
3. inspect manifest and rules;
4. run field and missingness profiles;
5. run seeded rules;
6. inspect natural rules;
7. reconcile risk and resolution logs;
8. rerun notebook or script;
9. verify resolved bytes;
10. review AI and accessibility records; and
11. score and record disposition.

## 20. Runnable acceptance checks

The release validator must check:

1. exact source path contract;
2. accepted input bytes;
3. accepted input SHA-256;
4. 374 accepted rows;
5. 29 accepted fields;
6. accepted patient uniqueness;
7. accepted index uniqueness;
8. protected nonempty target;
9. defect-release version 0.1.0;
10. 379 defective rows;
11. 29 defective fields;
12. 374 distinct defective patients;
13. 5 duplicate rows;
14. 20 seeded defect families;
15. 56 seeded issue cases;
16. 68 manifest change rows;
17. manifest original values match accepted source;
18. manifest defect values match defective source;
19. 28 quality rules;
20. exact D01 count;
21. exact D02 count;
22. exact D03 count;
23. exact D04 count;
24. exact D05 count;
25. exact D06 count;
26. exact D07 count;
27. exact D08 count;
28. exact D09 count;
29. exact D10 count;
30. exact D11 count;
31. exact D12 count;
32. exact D13 count;
33. exact D14 count;
34. exact D15 count;
35. exact D16 count;
36. exact D17 count;
37. exact D18 count;
38. exact D19 count;
39. exact D20 count;
40. N01 count 343;
41. N02 count 226;
42. N03 count 263;
43. N04 count 5;
44. N05 count 2;
45. N06 count 1;
46. N07 count 6;
47. N08 count 12;
48. SQLite user version 1;
49. SQLite integrity `ok`;
50. four database tables;
51. database row counts match CSV;
52. 29-row quality profile;
53. 29-row missingness profile;
54. 28-row rule results;
55. all observed rule counts match expected;
56. 28-row risk log;
57. exact required risk-log fields;
58. 28-row resolution log;
59. risk and resolution issue IDs align;
60. blocking seeded issues resolved;
61. natural issues retained or documented;
62. 374 resolved rows;
63. 29 resolved fields;
64. resolved patient uniqueness;
65. resolved bytes equal accepted bytes;
66. resolved SHA-256 equals accepted SHA-256;
67. notebook is valid JSON;
68. notebook has stable cell IDs;
69. notebook contains required narrative and code sections;
70. notebook executes in a clean output target;
71. learner records exist;
72. no unfinished placeholder in a complete submission;
73. no personal absolute path;
74. no Unicode dash in contract files;
75. AI verification recorded;
76. allowed decision recorded;
77. builder self-check;
78. profiler self-check;
79. validator self-check;
80. complete reference reproduction;
81. incomplete submission rejection; and
82. clean Module 05 handoff.

### Automated and human boundary

Automation proves exact structure, seeded counts, manifests, profiles, rule results, and fingerprints. Human review decides whether classifications are understandable, an extreme value received proportionate review, the risk consequence is meaningful, the accessibility route works, AI verification is substantive, and the final readiness decision fits the evidence.

## 21. Release status, reviewers, version, and known issues

### Release identity

- Module ID: `oclc-fnd1-04`.
- Module version: 0.1.0.
- Defect-release version: 0.1.0.
- Commons release: 0.32.0.
- Status target: runnable release candidate.
- Repository: https://github.com/ShuhanCS/open-clinical-learning-commons

### Semantic-version decision

Module 0.1.0 establishes the first deterministic quality-defect, profiling, resolution, and readiness-decision contract. Commons 0.32.0 adds a compatible FND-1 module without changing Checkpoint 1 or Modules 01 through 03.

### Required human reviewers

| Role | Reviewer | Status |
|---|---|---|
| FND-1 faculty owner | unassigned | pending |
| Data-quality lead | unassigned | pending |
| SQL and data engineering | unassigned | pending |
| Clinical informatics and field meaning | unassigned | pending |
| Python and notebook teachability | unassigned | pending |
| Accessibility | unassigned | pending |
| Privacy and data governance | unassigned | pending |
| Responsible AI | unassigned | pending |
| Independent reproduction and teachability | unassigned | pending |

### Known issues after technical implementation

1. Named human review is pending.
2. macOS and Linux reproduction remain pending.
3. The source is synthetic and older.
4. The small-cell threshold is a teaching caution, not a universal disclosure policy.

The first clean build locked the defective CSV at 123,211 bytes and SHA-256 `7800c1d24093b93ce40634afe652e574a1ed2775eba8a742c0bd00bf3596a02d`, the SQLite release at 385,024 bytes and SHA-256 `3b9cbf4ba7920f85a8af524902f2e7d35b3e837e5dd6b94deb4f20a156644275`, and every profile and log fingerprint in `release.json`. A clean notebook run executed four code cells with four outputs. The validator passes 344 release checks and 340 complete-submission checks.

### Context-safe handoff

Implementation and clean reproduction are complete. Module 05 must use the resolved table with SHA-256 `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a` and carry N01 through N08 into its denominator and interpretation records.
