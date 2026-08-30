# FND-1 Checkpoint 1: Validated cohort and analytic-table release

## 1. Checkpoint identity and place in the course

- Course: FND-1 Healthcare Data Foundations.
- Checkpoint: 01 of 03.
- Due: end of instructional Week 3.
- Course weight: 40 percent.
- Preserved source components: 15-percent Module 01 setup component plus 25-percent Module 03 SQL cohort component.
- Module 02 role: required relational-data gateway with no added course weight.
- Cumulative learner time at submission: 48.0 hours.
- Additional checkpoint hours: none; assembly, review, and defense occur within Modules 01 through 03.
- Checkpoint version: 0.1.0.
- Commons release: 0.31.0.
- Status: runnable release candidate.
- Required tag: `fnd1-checkpoint1-v0.1.0`.
- Repository: https://github.com/ShuhanCS/open-clinical-learning-commons

Checkpoint 1 freezes the technical foundation that Modules 04 through 07 must use. It joins an executable workspace, the accepted relational source, checked retrieval, the adult acute-care cohort, and the one-row-per-person analytic table into one reviewable release. It is not a fourth assignment and does not add weight. It is the cumulative decision point for the work already completed.

Only `accept` or `accept with conditions` permits Module 04 to begin.

## 2. Decision, audience, and review question

### Decision owners

- senior clinical data analyst; and
- course instructor acting as repository maintainer.

Both owners sign the disposition. A technical reviewer may recommend a disposition but does not replace either decision owner.

### Primary audience

A data-quality lead who must decide whether the released analytic table can receive a deterministic defect layer and formal profiling in Module 04.

### Review question

> Are the workspace, source database, cohort definition, denominators, temporal logic, analytic-table grain, and reproduction evidence technically ready for quality and descriptive work?

### Allowed dispositions

- `accept`;
- `accept with conditions`;
- `revise`; or
- `refer`.

`Accept with conditions` must name each condition, owner, evidence needed, and due point. A condition cannot waive a noncompensable gate.

`Refer` is appropriate when privacy, rights, security, governance, academic integrity, or unresolved source integrity exceeds the decision owners' authority.

## 3. Component map and weight preservation

### Course-point map

| Component | Source milestone | Course points | Checkpoint share | Checkpoint treatment |
|---|---|---:|---:|---|
| Reproducible workspace | Module 01 | 15 | 37.5% | Freeze or update the accepted setup evidence. |
| Relational database gateway | Module 02 | 0 additional | required gate | Prove the cohort was built from the accepted source and schema. |
| Cohort and analytic table | Module 03 | 25 | 62.5% | Submit SQL, flow, table, checks, and handoff decision. |
| Total | Modules 01 through 03 | 40 | 100% | Cumulative Week 3 checkpoint. |

Module 02 is not optional merely because it carries no separate source weight. The database is the required evidence bridge between the workspace and the cohort. A missing, changed, or unverified database fails the checkpoint source gate.

### Score preservation rule

The course records Checkpoint 1 on a 40-point scale. The Module 01 component contributes at most 15 points. The Module 03 component contributes at most 25 points. Reviewers may not rescale one component to compensate for failure in the other.

### Feedback milestone rule

Module 01 feedback can be incorporated before Checkpoint 1. The checkpoint copy must record whether the accepted Module 01 tag was used unchanged or superseded by an identified compatible tag. Silent replacement is prohibited.

## 4. Competencies and assessable outcomes

On a passing submission, the learner can:

1. reproduce the declared Python, SQLite, notebook, R-reading, and Git environment;
2. explain why reproducibility is part of healthcare data quality;
3. connect a semantic version and Git tag to an exact released state;
4. identify the pinned public synthetic source, publisher, rights, bytes, and fingerprint;
5. explain the 16-table relational release using grain, keys, cardinality, and optionality;
6. distinguish flat relational records from the included FHIR R4 teaching mappings;
7. retrieve exact table, encounter-class, observation-linkage, timeline, and numeric-observation extracts;
8. define the adult acute-care source population, eligibility, exclusion order, index event, and time zero;
9. distinguish eligible event rows from included patients;
10. select one deterministic index event per included person;
11. calculate pre-index history without join multiplication;
12. define 30-day and 90-day follow-up boundaries from index stop;
13. preserve people with no recorded next encounter through an explicit state;
14. build a 374-row, 29-field one-row-per-person analytic table;
15. reconcile every flow count and numerator-denominator relationship;
16. identify post-index fields that cannot be treated as baseline predictors;
17. reproduce every committed output from read-only SQL;
18. document material AI use and verify at least one material suggestion independently;
19. state the synthetic-data, source-age, and no-real-population claim limits; and
20. issue and defend an allowed technical release disposition.

## 5. Concept ownership and out-of-scope boundaries

### Checkpoint-owned integration

This checkpoint owns:

- the cumulative file contract;
- evidence linkage across Modules 01 through 03;
- component scoring on the original 15-plus-25 point scale;
- release-manifest integrity;
- the transition decision into Module 04; and
- the frozen cohort and analytic-table interface.

### Module ownership retained

| Evidence | Owning unit | Checkpoint action |
|---|---|---|
| environment, Git, versioning, reproducibility practice | Module 01 | freeze and verify |
| source database, schema, keys, retrieval, FHIR reading | Module 02 | preserve as required gateway evidence |
| cohort, index, windows, flow, analytic table, query checks | Module 03 | freeze and assess |

The checkpoint does not rewrite accepted module definitions. A necessary change returns to the owning module, receives a semantic-version decision, and then re-enters checkpoint assembly.

### Out of scope

- cleaning, defect correction, imputation, and quality profiling;
- descriptive summaries beyond exact cohort validation facts;
- visualization or dashboard design;
- inference, regression, prediction, machine learning, and causal analysis;
- clinical benchmarking or real-population estimation;
- production database administration;
- production deployment; and
- use of real patient, partner, employer, or restricted data.

Module 04 owns cleaning and profiling after the checkpoint accepts the frozen input.

## 6. Checkpoint sequence and learner work

### Assembly sequence

1. Confirm accepted or conditionally accepted Module 01, 02, and 03 versions.
2. Confirm the working tree is clean and no private file is tracked.
3. Assemble into a new target using the checkpoint assembler.
4. Inspect the release manifest before editing cumulative records.
5. Confirm environment and version evidence from Module 01.
6. Confirm schema, source, first extracts, and FHIR reading from Module 02.
7. Confirm cohort, SQL, flow, analytic table, and dictionary from Module 03.
8. Complete the cumulative README, source-system comparison, transformation record, reproduction check, AI-use record, component score, and review disposition.
9. Rebuild the Module 02 database from the pinned archive.
10. Rerun the Module 02 first extracts.
11. Rerun the four Module 03 SQL files.
12. Compare every released output byte for byte.
13. Run the checkpoint validator.
14. Conduct the technical handoff defense.
15. Record score, gates, disposition, conditions, owners, and date.
16. Tag the accepted or conditionally accepted release.

### Defense prompts

The learner must be ready to explain:

- why 1,048 eligible events become 374 people;
- why completed age is evaluated before event ranking;
- why encounter ID is the ranking tie-breaker;
- why history sources are aggregated separately;
- why follow-up begins after index stop;
- why `No encounter recorded` does not mean no care;
- which fields occur after time zero;
- how source and output fingerprints were checked;
- what AI contributed and how it was verified; and
- why the chosen disposition follows from the evidence.

## 7. Upstream release inventory and immutable facts

### Module 01 release

| Item | Accepted fact |
|---|---|
| module | `oclc-fnd1-01` |
| version | 0.1.0 |
| setup tag | `fnd1-setup-v0.1.0` |
| smoke-test rows | 3 |
| smoke-test total | 15 |
| source SHA-256 | `330da80c517c912fccd9bca3963aded84898dbb51e8b7271aa3bc53b0439c3ab` |
| required stack | Python 3.12.10, SQLite 3.49.1, JupyterLab 4.6.3, nbclient 0.10.2, pandas 3.0.5, R 4.6.1 |

Equivalent later supported versions require a documented compatible release. They cannot enter silently.

### Module 02 release

| Item | Accepted fact |
|---|---|
| module | `oclc-fnd1-02` |
| version | 0.1.0 |
| source | Synthea April 2020 CSV sample |
| source URL | https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip |
| archive bytes | 8,982,431 |
| archive SHA-256 | `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a` |
| source tables | 16 |
| source fields | 168 |
| source rows | 471,836 |
| database dictionary rows | 177 |
| tested database bytes | 141,234,176 |
| tested database SHA-256 | `1116dda22c4297fcfeab6bf2c99bb3dbfaf9f9b5e04041b96be90719c76e704a` |
| foreign-key failures | 0 |
| integrity | `ok` |

### Module 03 release

| Item | Accepted fact |
|---|---|
| module | `oclc-fnd1-03` |
| version | 0.1.0 |
| source patients | 1,171 |
| acute period events | 1,243 |
| adult eligible events | 1,048 |
| included people | 374 |
| eligible non-index events | 674 |
| analytic rows | 374 |
| analytic fields | 29 |
| analytic SHA-256 | `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a` |
| query checks | 16 passing |

### Source and rights boundary

Synthea source and generator are Apache-2.0. Commons code is MIT. Commons documentation is CC-BY-4.0. The source is synthetic and contains no real patients. A learner may not substitute local clinical records, MIMIC, partner data, workplace extracts, or any restricted file.

## 8. Exact folder contract

```text
checkpoint-1/
  .gitattributes
  README.md
  VERSION
  requirements.txt
  environment-note.md
  version-policy.md
  schema/
    schema-diagram.svg
    data-model.mmd
    schema-description.md
    data-dictionary.csv
    analytic-data-dictionary.csv
    source-manifest.csv
    schema.sql
    source-system-comparison.md
    fhir-json-reading.md
  sql/
    01-first-extracts.sql
    02-index-cohort.sql
    03-analytic-table.sql
    04-validation.sql
  outputs/
    first-extracts.csv
    first-extracts/
      table-inventory.csv
      encounter-class-counts.csv
      observation-linkage.csv
      selected-patient-timeline.csv
      numeric-observation-sample.csv
    eligible-events.csv
    index-cohort.csv
    cohort-flow.csv
    analytic-table.csv
    query-checks.csv
  cohort-spec.md
  table-spec.md
  source-record.yml
  transformation-record.md
  reproducibility-check.md
  ai-use.md
  component-score.csv
  review-disposition.md
  evidence/
    module-01-ai-use.md
    module-01-reproducibility-check.md
    module-02-ai-use.md
    module-02-validation-notes.md
    module-03-ai-use.md
    module-03-reproducibility-check.md
  release-manifest.csv
```

The generated SQLite database and source ZIP do not enter the checkpoint folder or Git. Their exact fingerprints remain in the source record and reproduction evidence.

Extra screenshots, notebooks, or local exports do not replace any required file. Any permitted addition must appear in the README folder map and cannot contain private data, credentials, or personal absolute paths.

## 9. Assembly and release-manifest rules

### Inputs

The learner-mode assembler requires paths to:

- an accepted Module 01 workspace;
- an accepted Module 02 database workspace;
- an accepted Module 03 submission; and
- a new target that does not exist.

The instructor reference mode uses the canonical released answers and exists for technical validation and teaching preparation. It is not a substitute for the learner's accumulated work.

### Protected target

The assembler refuses any existing target. It never merges into or overwrites a learner folder. A failed assembly leaves its newly created target available for diagnosis.

### Copy and generation rules

- Copy text and data bytes without manual editing.
- Generate `outputs/first-extracts.csv` as a registry of the five Module 02 output files.
- Generate `release-manifest.csv` for immutable imported evidence only.
- Record relative path, source unit, source version, bytes, and SHA-256.
- Do not include cumulative learner-authored records in the immutable manifest because they change during checkpoint completion.
- Sort registry and manifest rows by relative path.
- Write UTF-8 CSV with LF line endings.

### Change control

If a copied immutable file changes, stop. Return to the owning module, determine whether the difference is a defect, compatible update, or incompatible contract change, and version it there. Do not edit the checkpoint copy to make a fingerprint pass.

## 10. Workspace and release evidence contract

### `requirements.txt`

The reference pin set is:

```text
jupyterlab==4.6.3
nbclient==0.10.2
pandas==3.0.5
```

### `environment-note.md`

Record:

- learner identifier;
- operating system and architecture;
- shell;
- Python executable and version;
- pandas, JupyterLab, nbclient, and SQLite versions;
- R and Git versions;
- checkpoint commit and tag;
- installation commands;
- one resolved setup failure; and
- material differences from the tested environment.

Do not record a personal home path, credential, token, or protected host name.

### `version-policy.md`

Explain patch, minor, and major changes using checkpoint examples. Record the Module 01 accepted tag, checkpoint tag, full tagged commit, clean-tree check, and whether any module version was superseded.

### Git evidence

A passing release has:

- at least three meaningful commits across the technical work;
- at least one branch and merge or documented equivalent collaboration workflow;
- an annotated checkpoint tag at the reviewed commit;
- a clean working tree at validation and tagging; and
- no ignored database, ZIP, credential, or private data accidentally tracked.

Automation may confirm Git structure. The instructor confirms that the history represents meaningful work.

## 11. Database, schema, FHIR, and retrieval evidence contract

### Schema package

`schema/data-model.mmd` is the editable relationship model. `schema/schema-diagram.svg` is an accessible rendered reference with a title and description. `schema/schema-description.md` is the text equivalent and remains required even when the SVG is present.

The schema evidence must state:

- one-row grain for all 16 source tables;
- source or surrogate key;
- parent relationships;
- optional versus required encounter references;
- the 30,363 observations with no encounter reference;
- the zero-row supplies table;
- the nine transparent source-row surrogates;
- minimized-view purpose; and
- identity-like and cost-field minimization.

### Source-system comparison

`schema/source-system-comparison.md` compares EHR, claims, registry, survey, operational, FHIR, public aggregate, and synthetic data across origin, common grain, strengths, limits, and supported decisions. It must not call Synthea an EHR or a real claims source.

### FHIR reading

`schema/fhir-json-reading.md` traces the released Patient, Encounter, and Observation identifiers and references. It states that the examples are transparent CSV-derived teaching mappings, not a full FHIR conformance claim.

### First extracts

The five extract files have these exact row counts:

| Output | Rows |
|---|---:|
| table-inventory.csv | 16 |
| encounter-class-counts.csv | 6 |
| observation-linkage.csv | 3 |
| selected-patient-timeline.csv | 25 |
| numeric-observation-sample.csv | 25 |

`outputs/first-extracts.csv` registers each name, row count, bytes, and SHA-256. The SQL remains read-only and contains all five named query blocks.

## 12. Cohort, analytic-table, and denominator evidence contract

### Eligibility and index

The cohort must retain:

- emergency or inpatient class;
- start on or after 2015-01-01 and before 2020-01-01;
- completed age 18 or older at the event;
- adult filtering before ranking;
- order by start and encounter ID; and
- rank 1 per patient.

### Exact flow

| Step | Starting | Excluded | Remaining |
|---:|---:|---:|---:|
| 1 | 1,171 | 0 | 1,171 |
| 2 | 1,171 | 690 | 481 |
| 3 | 481 | 107 | 374 |
| 4 | 374 | 0 | 374 |

### Analytic table

The released table has:

- 374 rows;
- 29 fields;
- one unique patient per row;
- one unique index encounter per row;
- four nonnegative pre-index count fields;
- an explicit 30-day next state;
- separate 90-day return and death flags;
- death precedence only in the mutually exclusive endpoint;
- source-coverage status;
- source release `synthea-csv-apr2020`; and
- cohort definition version 0.1.0.

### Exact follow-up facts

- 263 no encounter recorded within 30 days;
- 92 scheduled care;
- 4 urgent care;
- 15 acute return;
- 36 any acute return within 90 days;
- 8 deaths within 90 days;
- 330 no acute-return endpoints; and
- 374 complete source-coverage flags.

`No encounter recorded` is a source-observation state. It is not evidence of no care.

## 13. Reproducibility, AI, accessibility, privacy, and claims

### Reproduction record

The cumulative `reproducibility-check.md` records:

- source archive verification;
- Module 02 database build;
- integrity and foreign-key checks;
- five first-extract reruns;
- four Module 03 SQL reruns;
- five Module 03 output comparisons;
- environment versions;
- clean target use;
- checkpoint validation;
- Git clean state and tag; and
- platform-specific differences.

### AI-use record

For every material use, record date, tool and model, purpose, data shared, advice used, human verification, accepted/changed/rejected decision, and affected file or query. The cumulative record may summarize module records but cannot delete them; the six evidence copies preserve the original trail.

At least one material SQL, schema, environment, or cohort suggestion must be verified against source rows, independent SQL, official documentation, or validator evidence.

### Accessibility

- schema meaning is available as text and an editable Mermaid model;
- the SVG has title and description metadata;
- all status values use text;
- tables have headers and explicit units;
- no evidence depends on color;
- commands are copyable;
- an accessible SQL, notebook, or terminal alternative is allowed; and
- defense accommodations do not reduce the evidence standard.

### Privacy and security

- only synthetic and public data are permitted;
- the source ZIP and SQLite database remain untracked;
- identity-like synthetic fields not needed for the decision remain excluded from cohort outputs;
- no secret, token, key, internal host, or personal absolute path appears;
- learner identifiers follow course policy; and
- an unexpected private or restricted file triggers automatic return and referral.

### Claims

The package supports technical claims about reproducibility, source preservation, cohort definition, and analytic-table construction. It does not support real utilization, quality, prevalence, mortality, access, effectiveness, prediction, or causal claims.

## 14. Exact submission and review workflow

### Learner submission

Submit the exact folder, validation output, Git commit, and annotated tag. The database and source archive are verified by fingerprint but not uploaded into Git.

### Required cumulative writing

- `README.md`: audience, decision, release summary, folder map, reproduction commands, known limits, and next use.
- `schema/source-system-comparison.md`: eight-source comparison.
- `transformation-record.md`: ordered cross-module transformations and immutable handoffs.
- `reproducibility-check.md`: clean rebuild and comparison evidence.
- `ai-use.md`: cumulative material use and verification.
- `component-score.csv`: 15-point setup and 25-point cohort scoring record.
- `review-disposition.md`: gates, score, disposition, conditions, owners, dates, and signatures.

### Review sequence

1. scan for prohibited data and secrets;
2. check exact versions and source fingerprints;
3. check environment and Git evidence;
4. check schema and first extracts;
5. check cohort definition and SQL;
6. check flow and table uniqueness;
7. rerun outputs;
8. inspect AI verification and accessibility;
9. conduct the defense;
10. score the two preserved components;
11. record gates and disposition; and
12. tag only an accepted or conditionally accepted release.

## 15. Rubric, pass conditions, and automatic return

### Forty-point rubric

| Criterion | Course points |
|---|---:|
| Executable environment and dependency record | 5 |
| Git history, semantic version, clean release, and tag | 5 |
| Reproduction, privacy, and verified AI-use evidence | 5 |
| Source, relational schema, FHIR reading, and first extracts | 5 |
| Eligibility, index event, time zero, and readable SQL | 8 |
| Analytic-table grain, windows, fields, and leakage labels | 7 |
| Flow, denominators, query checks, and technical handoff | 5 |
| Total | 40 |

The first three rows are the preserved 15-point setup component. The final four rows are the preserved 25-point SQL cohort component, including the Module 02 gateway evidence needed to establish its source.

### Numeric threshold

At least 32 of 40 points.

### Noncompensable gates

- permitted data only;
- exact source archive identity;
- runnable environment;
- meaningful version and Git evidence;
- database integrity and zero foreign-key failures;
- declared grain and keys;
- exact first extracts;
- adult eligibility and deterministic index;
- one index and one analytic row per included patient;
- cohort-flow conservation;
- correct temporal boundaries;
- no join multiplication;
- 29-field table and dictionary alignment;
- post-index leakage labeling;
- byte-reproducible outputs;
- accessibility route;
- material AI disclosure and verification;
- learner defense; and
- `accept` or `accept with conditions` disposition.

### Automatic return without scoring

Return when:

- source identity is absent or wrong;
- a private, restricted, or credential-bearing file appears;
- the environment cannot run;
- the database cannot be rebuilt or fails integrity;
- keys or grain are unstated;
- first extracts are absent or manually altered;
- joins multiply rows without explanation;
- cohort counts do not reconcile;
- the analytic table has duplicate people or index encounters;
- a required SQL or output file is missing;
- an immutable source value was manually changed;
- post-index fields are presented as baseline without a new contract;
- AI-generated work is unverified;
- the learner cannot explain the SQL; or
- the release manifest does not match the imported evidence.

## 16. Runnable acceptance checks

The release validator and assembler must check:

1. target overwrite protection;
2. exact required folder and files;
3. checkpoint version 0.1.0;
4. LF line-ending contract for generated CSV;
5. no Unicode dash in learner-facing contracts;
6. no personal absolute path;
7. no unfinished placeholder in complete submission;
8. exact requirement pins;
9. environment record fields;
10. version and tag fields;
11. release-manifest unique relative paths;
12. release-manifest bytes;
13. release-manifest SHA-256 values;
14. Module 01 source fingerprint;
15. Module 02 archive fingerprint;
16. Module 02 database fingerprint record;
17. 16 source-manifest rows;
18. 471,836 source rows;
19. 168 source fields;
20. 177 database dictionary rows;
21. valid schema SQL;
22. complete Mermaid relationship model;
23. accessible SVG title and description;
24. schema-description headings;
25. source-system comparison coverage;
26. FHIR Patient, Encounter, and Observation reading;
27. four read-only checkpoint SQL files;
28. five first-extract files;
29. five exact first-extract row counts;
30. exact first-extract fingerprints;
31. first-extract registry matches files;
32. 1,048 eligible-event rows;
33. 374 index rows;
34. 374 analytic rows;
35. 29 analytic fields;
36. 29 analytic dictionary rows;
37. unique patient IDs;
38. unique index encounter IDs;
39. all ages at least 18;
40. index classes restricted to emergency and inpatient;
41. index dates within bounds;
42. index stop not before start;
43. nonnegative history counts;
44. acute history no greater than encounter history;
45. explicit no-next state and null companions;
46. next encounters after index stop and within 30 days;
47. exact 30-day state counts;
48. exact 90-day return count;
49. exact 90-day death count;
50. endpoint precedence and counts;
51. complete 90-day source coverage;
52. four flow rows;
53. conservation within every flow row;
54. 690 plus 107 plus 374 equals 1,171;
55. 16 passing query checks;
56. source-release labels;
57. cohort-definition versions;
58. immutable Module 03 output fingerprints;
59. cumulative transformation record;
60. cumulative reproduction record;
61. cumulative AI-use record;
62. six preserved module evidence records;
63. component-score rows total 40 available points;
64. earned score at least 32 for a passing decision;
65. every noncompensable gate recorded;
66. allowed disposition;
67. conditions include owner and due point;
68. clean reference assembly;
69. valid complete reference fixture;
70. incomplete submission rejection; and
71. student-mode assembly from three accepted inputs.

Automation proves structure and exact technical facts. Human reviewers decide whether explanations are understandable, Git history is meaningful, accessibility works for the learner, AI verification is substantive, the defense is adequate, and the disposition fits the evidence.

## 17. Release status, reviewers, known issues, and handoff

### Semantic-version decision

Checkpoint 0.1.0 establishes the first cumulative workspace-to-cohort release contract. Commons 0.31.0 adds the compatible checkpoint package without changing Modules 01 through 03.

### Measured runnable release

- Instructor reference assembly creates 45 files and a 35-row immutable release manifest.
- The manifest is 4,107 bytes with SHA-256 `36cf454387db595e9237f461556676db7611b3b60b2762f8554e4d9d580c96a6`.
- The five-row first-extract registry is 527 bytes with SHA-256 `32707acca77a1e6ca06a783912c06bcc765910142646f36eba6af0ee6710f17a`.
- Learner-mode assembly from three accepted inputs passes a 295-check starter validation.
- Complete reference validation passes 341 checks, including the embedded Module 03 submission validator.
- Existing targets and incomplete checkpoint folders are rejected.

### Required human reviewers

| Role | Reviewer | Status |
|---|---|---|
| FND-1 faculty owner | unassigned | pending |
| Senior clinical data analyst | unassigned | pending |
| SQL and data engineering | unassigned | pending |
| Clinical informatics and cohort meaning | unassigned | pending |
| Reproducibility and developer environment | unassigned | pending |
| Accessibility | unassigned | pending |
| Privacy and data governance | unassigned | pending |
| Responsible AI | unassigned | pending |
| Independent reproduction and teachability | unassigned | pending |

### Known issues after technical validation

1. Named human review is pending.
2. macOS and Linux reproduction remain pending.
3. The SQLite byte fingerprint may change after a supported SQLite upgrade even when logical contents remain compatible; any update requires a release decision.
4. The source is synthetic and older.

### Handoff

Checkpoint implementation and technical reproduction are complete. After Commons 0.31.0 integration, commit, and push, an accepted checkpoint freezes the Module 03 analytic-table bytes and cohort definition for Module 04. Module 04 must create a separately versioned deterministic defect layer and cannot mutate the checkpoint release in place.
