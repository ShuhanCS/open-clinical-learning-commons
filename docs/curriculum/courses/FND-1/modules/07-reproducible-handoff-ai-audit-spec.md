# FND-1 Module 07: Reproducible handoff and AI audit

## 1. Module identity and place in the course

- Module ID: `oclc-fnd1-07`.
- Module version: 0.1.0.
- Commons release target: 0.36.0.
- Course: FND-1, Healthcare Data Foundations.
- Week: 7.
- Learner work: 16.0 hours.
- Cumulative course work: 112.5 hours.
- Prerequisite: accepted or conditionally accepted FND-1 Checkpoint 2 version 0.1.0.
- Required tag: `fnd1-handoff-v0.1.0`.
- Source assessment role: creates the 35-point reproducible toolkit candidate for the final checkpoint.
- Downstream receiver: FND-1 final checkpoint, then FND-2.
- Status target: runnable release candidate.

Module 07 turns the accepted technical evidence into a package another analyst can identify, inspect, validate, and reuse. It does not produce a new cohort, statistic, or figure. The final checkpoint reviews this exact candidate, conducts the defense, records the disposition, and preserves the source curriculum's 35-percent final assessment.

## 2. Technical decision and named audience

### Decision owner

The decision owner is a health-system analytics engineering lead. Required supporting reviewers are:

- FND-1 faculty owner;
- SQL or data engineering reviewer;
- clinical informatics or healthcare-data-meaning reviewer;
- accessibility reviewer;
- privacy and data-governance reviewer;
- responsible-AI reviewer; and
- independent reproducer.

### Primary audience

The receiving analyst has not participated in Modules 01 through 06. They need to know what the release contains, how to verify it, how to reproduce it, what it may support, what remains conditional, and when to stop.

### Technical review question

Can the analytics engineering lead accept the complete versioned toolkit for downstream modeling or applied analysis while preserving the accepted grain, fingerprints, denominators, conditions, equivalent access, and synthetic-data limits?

### Allowed dispositions

- `accept`;
- `accept with conditions`;
- `revise`; or
- `refer` for rights, privacy, integrity, clinical meaning, accessibility, AI accountability, or governance review.

Only `accept` and `accept with conditions` create a final-checkpoint candidate. Neither disposition authorizes production deployment or real clinical use.

## 3. Foundation skill and handoff

### Foundation skill

The learner releases a technical data product rather than a folder of plausible files. Release identity, source provenance, code, environment, immutable evidence, human-owned explanation, validation, access routes, and change control must agree.

### Upstream handoff

Checkpoint 2 version 0.1.0 supplies:

- 35 immutable artifacts;
- a 35-row artifact contract;
- a 35-row release manifest;
- three accepted module release records;
- the 374-row, 29-field analytic table;
- D01 through D20 resolution evidence;
- N01 through N08 retained conditions;
- exact descriptive tables and denominator records;
- F01 through F03 exact tables, PNG, SVG, registry rows, and structured alternatives;
- cumulative quality, interpretation, accessibility, reproduction, AI-use, score, and review records; and
- a Module 07 progression disposition.

Module 07 treats the accepted checkpoint as immutable. A needed analytic change returns to the owning upstream module and receives a version decision before the toolkit is rebuilt.

### Pipeline-source handoff

The toolkit also preserves 23 exact source files needed to understand and rerun the released pipeline:

- the pinned Python requirements;
- the Module 02 database builder, query runner, schema, source manifest, and database-workspace template;
- the Module 03 cohort builder and four SQL files;
- the Module 04 deterministic defect builder and profiler;
- the Module 05 descriptive builder; and
- the Module 06 accessible renderer.

These files remain byte-identical to their accepted module releases. Module 07 does not combine them into a new orchestration framework.

### Downstream handoff

The final checkpoint receives one 90-file candidate with a 74-row immutable manifest and learner-owned release records. After final acceptance, FND-2 may use the data toolkit as its technical foundation without absorbing FND-1 content into its own modeling curriculum.

## 4. Assessable outcomes

By completing Module 07, the learner can:

1. identify a release by repository, commit, semantic version, and annotated tag;
2. explain the difference between a source module, cumulative checkpoint, toolkit candidate, and final disposition;
3. assemble a protected target without editing accepted evidence;
4. verify a 74-row immutable manifest by byte count and SHA-256;
5. trace every released data, table, and figure artifact to an owning module;
6. locate the exact SQL and source code needed to reproduce each pipeline stage;
7. write release notes that distinguish additions, changes, retained conditions, and prohibited uses;
8. write a data brief with source, grain, cohort, fields, time, quality, denominators, access, and claim limits;
9. document the environment and the exact clean-reproduction sequence;
10. compare reproduced outputs to accepted fingerprints rather than visual plausibility;
11. distinguish pipeline reproduction from source refresh or analytic revision;
12. preserve D01 through D20 and N01 through N08 through handoff;
13. preserve PNG, SVG, exact table, and structured-text access routes;
14. maintain a material prompt and AI-action log without exposing restricted data;
15. audit one material AI-assisted claim against independent evidence;
16. state what AI changed, what a human verified, and what remains human-owned;
17. apply semantic-version rules to compatible and incompatible release changes;
18. recognize stop, revise, and referral triggers;
19. deliver an eight-minute technical handoff; and
20. defend a final disposition and its conditions.

## 5. Concept ownership and out-of-scope boundaries

### Module 07 owns

- final toolkit assembly;
- release identity and version evidence;
- immutable-manifest verification;
- reproducibility runbook and clean-target evidence;
- data brief and limitations record;
- release notes and change log;
- material AI audit and prompt log;
- release checklist;
- final-checkpoint score draft;
- handoff brief and question responses; and
- candidate disposition.

### Upstream ownership retained

| Technical fact | Owning unit | Module 07 action |
|---|---|---|
| source archive, database schema, and first retrieval | Modules 01 and 02 | identify, copy required code, and cite |
| cohort SQL, flow, analytic table, and dictionary | Module 03 | preserve and explain |
| defect layer, quality rules, risks, and resolutions | Module 04 | preserve and hand off |
| descriptive tables, denominators, intervals, and memo | Module 05 | preserve and explain |
| figures, exact tables, alternatives, and access record | Module 06 | preserve and inspect |
| cumulative Week 6 decision | Checkpoint 2 | freeze and carry forward |

### Out of scope

- changing source, cohort, table grain, field definition, or time window;
- adding an imputation, cleaning rule, statistic, chart, model, score, or dashboard;
- choosing or fitting a production model;
- causal inference or risk adjustment;
- real clinical, operational, performance, safety, access, equity, cost, utilization, or population inference;
- production deployment, clinical approval, or automated decision support;
- an unreviewed source refresh;
- committing the source ZIP or generated 141-megabyte database;
- placing patient, workplace, restricted, secret, or credential data in the public package or an external AI tool; and
- treating a passing validator as the final human disposition.

## 6. Lesson sequence and learner time

| Lesson and work | Hours | Required evidence |
|---|---:|---|
| Release architecture, receiver needs, and failure boundaries | 1.25 | annotated toolkit map |
| Protected assembly and immutable manifest | 2.25 | 90-file candidate and 74-row manifest |
| Environment, source, and clean reproduction runbook | 2.75 | exact commands and output comparison |
| Data brief, provenance, and limitations | 2.00 | completed brief and limits record |
| AI-use inventory, prompt log, and one material audit | 2.00 | prompt log and audit conclusion |
| Accessibility and independent inspection | 1.25 | equivalent-access checklist |
| Change log, release notes, semantic version, and tag | 1.25 | versioned release records |
| Validation, response to failures, and checklist | 1.25 | clean validator result |
| Handoff brief, defense rehearsal, and candidate disposition | 2.00 | defense records and review disposition |
| Total | 16.00 | complete toolkit candidate |

The assembly and final-checkpoint preparation occur inside these 16 hours. The final defense is part of the final checkpoint and does not add course weight.

## 7. Readings and authoritative sources

Required local readings:

- `docs/curriculum/courses/FND-1/course-spec.md`;
- `docs/curriculum/courses/FND-1/checkpoints/02-quality-descriptive-accessible-release-spec.md`;
- `courses/healthcare-data-foundations/checkpoints/02-quality-descriptive-accessible-release/release.json`;
- all three Module 04 through 06 release records;
- the accepted Checkpoint 2 quality decision, interpretation memo, accessibility synthesis, reproduction record, AI-use record, and review disposition; and
- `docs/source/fnd-1-healthcare-data-foundations-source-record.md`.

External references:

- Semantic Versioning 2.0.0: https://semver.org/spec/v2.0.0.html
- Git tag documentation: https://git-scm.com/docs/git-tag
- Python virtual environments: https://docs.python.org/3/library/venv.html
- Python dependency installation: https://pip.pypa.io/en/stable/cli/pip_install/
- Synthea downloads: https://synthea.mitre.org/downloads
- Synthea CSV data dictionary: https://github.com/synthetichealth/synthea/wiki/CSV-File-Data-Dictionary
- W3C images accessibility tutorial: https://www.w3.org/WAI/tutorials/images/
- W3C tables accessibility tutorial: https://www.w3.org/WAI/tutorials/tables/

Learners cite the version or access date when an external document can change. External guidance does not override the pinned local release contract.

## 8. Dataset inventory, provenance, rights, and teaching purpose

### Source data

| Item | Accepted fact |
|---|---|
| source | Synthea April 2020 CSV sample |
| archive bytes | 8,982,431 |
| archive SHA-256 | `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a` |
| source tables | 16 |
| source fields | 168 |
| source rows | 471,836 |
| synthetic | yes |
| real patients | none |
| source ZIP in Git | no |
| generated SQLite in Git | no |

### Accepted analytic release

| Item | Accepted fact |
|---|---|
| analytic grain | one row per selected synthetic person |
| rows / fields | 374 / 29 |
| unique patient IDs | 374 |
| unique index encounter IDs | 374 |
| analytic SHA-256 | `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a` |
| cohort definition | 0.1.0 |
| index classes | 314 emergency, 60 inpatient |

### Teaching purpose

The toolkit supports instruction in data acquisition, relational structure, cohort construction, quality, descriptive evidence, accessible communication, provenance, versioning, reproduction, AI accountability, and technical handoff. It does not estimate real care or population conditions.

### Rights and privacy rule

Only the documented public synthetic source and its derived teaching artifacts are permitted. The toolkit excludes identity-like source fields not required by the analytic contract. A learner who introduces workplace or patient data receives an automatic referral rather than a score.

## 9. Exact toolkit and integrity contracts

### Assembly input

The builder accepts:

- one complete Checkpoint 2 folder that passes non-starter validation;
- one FND-1 course package root containing the accepted Modules 01 through 06; and
- one new, nonexistent target path.

Reference mode creates the canonical Checkpoint 2 reference in a temporary directory and uses the repository's accepted module roots.

### Immutable manifest

The 74 immutable rows are:

- 35 Checkpoint 2 evidence artifacts;
- 10 accepted Checkpoint 2 cumulative records;
- 4 Checkpoint 2 provenance files;
- 23 pipeline-source files;
- the Module 07 pipeline contract; and
- the Module 07 validator.

Each row records relative path, source unit, source version, bytes, SHA-256, and role. Learner-owned release records are intentionally outside the immutable manifest.

### Protected target

The builder refuses any target that already exists. It does not merge, delete, replace, or repair an existing directory.

### Exact output tree

```text
fnd1-toolkit/
  .gitattributes
  VERSION
  README.md
  CHANGELOG.md
  requirements.txt
  pipeline-contract.csv
  release-manifest.csv
  release-notes.md
  component-score.csv
  release-checklist.md
  reproducibility-check.md
  review-disposition.md
  data/
    analytic-table.csv
    data-dictionary.csv
  notebooks/
    data-quality.ipynb
    descriptive-results.ipynb
  quality/
    defect-manifest.csv
    quality-profile.csv
    missingness-profile.csv
    quality-rule-results.csv
    quality-risk-log.csv
    resolution-log.csv
  evidence-tables/
    variable-profile.csv
    cross-tabs.csv
    rates.csv
    stratified-table.csv
    denominator-registry.csv
    descriptive-checks.csv
  tables/
    quality-missingness.csv
    descriptive-rates.csv
    quarterly-index-counts.csv
  figures/
    quality-missingness.png
    quality-missingness.svg
    descriptive-rates.png
    descriptive-rates.svg
    quarterly-index-counts.png
    quarterly-index-counts.svg
  alt-text/
    quality-missingness.md
    descriptive-rates.md
    quarterly-index-counts.md
  evidence/
    module-04-stop-fix-proceed.md
    module-05-interpretation-memo.md
    module-06-accessibility-check.md
  module-releases/
    module-04-release.json
    module-05-release.json
    module-06-release.json
  figure-registry.csv
  provenance/
    checkpoint2-VERSION
    checkpoint2-artifact-contract.csv
    checkpoint2-release-manifest.csv
    checkpoint2-summary.csv
  documentation/
    data-brief.md
    limitations.md
    ai-audit.md
    checkpoint2/
      README.md
      component-score.csv
      quality-decision.md
      interpretation-memo.md
      accessibility-synthesis.md
      source-record.yml
      transformation-record.md
      reproducibility-check.md
      ai-use.md
      review-disposition.md
  audit/
    prompt-log.csv
  source-code/
    module02/
      build_database.py
      run_queries.py
      schema.sql
      source-manifest.csv
      template/
    module03/
      build_cohort.py
      sql/
    module04/
      build_defect_release.py
      profile_quality.py
    module05/
      build_descriptive.py
    module06/
      render_figures.py
  validation/
    validate_toolkit.py
  defense/
    handoff-brief.md
    questions-and-responses.md
```

The `template/` subtree under Module 02 contains its nine accepted database-workspace template files. There are 90 files total after assembly.

### Change control

Changing one of the 74 immutable files requires an upstream version decision or a new Module 07 release. Changing a learner-owned release record requires rerunning validation and recording the revision. A path change that breaks a documented receiver is a major-version event.

## 10. Worked example and instructor walkthrough

The instructor begins with the accepted Checkpoint 2 reference and asks whether visual inspection alone proves the final package is correct. The answer is no: two files can look identical while differing in line endings, metadata, hidden dependencies, or unreviewed content.

The walkthrough then:

1. verifies Checkpoint 2 in complete mode;
2. reads the 35-row checkpoint manifest;
3. reads the 23-row pipeline contract;
4. assembles into a new target;
5. confirms 90 files and 74 immutable rows;
6. verifies the analytic-table fingerprint;
7. locates the SQL that establishes the cohort;
8. locates the code that creates the defect, descriptive, and figure releases;
9. reads the data brief before inspecting outputs;
10. traces F02 from figure to registry to exact table to denominator record;
11. recomputes one Wilson interval using independent standard-library arithmetic;
12. checks that a `No encounter recorded` row retains a blank elapsed-time field;
13. audits the AI-assisted claim that such blanks must not become zero;
14. checks release notes, change log, version, and tag instructions;
15. runs complete validation; and
16. records an `accept with conditions` candidate disposition.

The condition is not analytic uncertainty invented by Module 07. It preserves named human review, operating-system reproduction, synthetic scope, and all accepted upstream conditions.

## 11. Guided practice

### Practice 1: Receiver map

For ten named toolkit paths, record the owning source, version, receiver question, and consequence if the file changes.

### Practice 2: Manifest trace

Select one artifact from each upstream module and prove source path, target path, bytes, SHA-256, and role.

### Practice 3: Clean-target test

Assemble twice into two different new directories. Compare all 74 immutable rows. Then attempt an existing target and explain why refusal is safer than merge behavior.

### Practice 4: Release-note repair

Repair release notes that say only "final files added." Name the release, accepted inputs, meaningful contents, retained conditions, compatibility, prohibited uses, and reproduction status.

### Practice 5: Data-brief trace

For one paragraph in the data brief, attach exact evidence for grain, denominator, quality condition, access route, and claim limit.

### Practice 6: AI claim audit

Audit one material AI-assisted statement. Record the claim, decision consequence, independent method, exact evidence, result, human owner, and action taken.

### Practice 7: Accessibility handoff

Review one figure without color, one exact table without the figure, and one structured alternative without either. Record whether the decision-relevant meaning agrees.

### Practice 8: Stop decision

Given a changed analytic fingerprint, missing alternative, unlogged AI transformation, or local absolute path, choose accept, condition, revise, or refer and defend the choice.

## 12. Independent exercise

The learner independently:

1. obtains the accepted Checkpoint 2 package;
2. confirms complete validation;
3. assembles the toolkit into a new target;
4. completes every learner-owned record;
5. verifies source, release, commit, version, and tag identity;
6. writes the data brief and limitations record;
7. writes the change log and release notes;
8. records the reproduction sequence and comparison results;
9. records all material AI uses in the prompt log;
10. audits one material AI-assisted step;
11. completes the 35-point score draft;
12. completes the release checklist;
13. writes the handoff brief and responses;
14. runs complete validation;
15. commits the exact candidate;
16. proposes a disposition; and
17. creates the annotated tag only after review permits it.

The learner may use a different operating system or shell, but every command, dependency, path-equivalence decision, and changed byte must be documented.

## 13. Visualization and communication requirements

Module 07 creates no new analytic visualization. It preserves the accepted Module 06 access package and communicates it accurately.

The handoff must:

- name F01, F02, and F03 by decision question rather than file type alone;
- link each figure to its exact CSV and structured alternative;
- preserve PNG and SVG routes;
- state units, denominators, interval meaning, and selected-cohort time meaning;
- preserve redundant non-color cues;
- state that orange is not the only cue;
- record grayscale, 50-percent-width, 200-percent-zoom, reading-order, and equivalence evidence;
- make the data brief and defense understandable without opening a notebook;
- avoid screenshots of code or tables when accessible text is available; and
- avoid describing a connected quarterly line as hospital volume, trend, forecast, process control, or cause.

Any new diagram used in the defense requires a text equivalent, but it does not enter the released analytic evidence without a new upstream contract.

## 14. Exact submission package

### Module package

The teaching module contains:

```text
07-reproducible-handoff-ai-audit/
  .gitattributes
  .gitignore
  VERSION
  README.md
  pipeline-contract.csv
  assemble_toolkit.py
  validate_toolkit.py
  assessment.md
  instructor-notes.md
  release.json
  template/
    .gitattributes
    README.md
    CHANGELOG.md
    release-notes.md
    component-score.csv
    release-checklist.md
    reproducibility-check.md
    review-disposition.md
    documentation/
      data-brief.md
      limitations.md
      ai-audit.md
    audit/
      prompt-log.csv
    defense/
      handoff-brief.md
      questions-and-responses.md
  reference/
    [same completed record paths]
```

### Learner submission

Submit:

- the assembled 90-file toolkit candidate;
- complete validator output;
- full repository commit hash;
- annotated tag `fnd1-handoff-v0.1.0` when authorized;
- reproduction environment identity;
- AI-audit evidence; and
- availability for the final technical defense.

The source ZIP, generated SQLite database, caches, virtual environments, credentials, and local path substitutions do not belong in the submission.

## 15. Rubric and pass conditions

### Thirty-five-point final-component draft

| ID | Criterion | Course points |
|---|---|---:|
| R01 | Repository identity, semantic version, change log, release notes, and tag evidence | 4.00 |
| R02 | Complete package, ownership map, immutable manifest, and fingerprint integrity | 5.00 |
| R03 | Environment, clean reproduction, output comparison, and hidden-dependency removal | 6.00 |
| D01 | Data brief, source, rights, grain, cohort, and denominator clarity | 4.00 |
| D02 | Quality conditions, descriptive limits, permitted use, and stop rules | 3.00 |
| A01 | Accessible schema and figure routes, exact tables, alternatives, and handoff communication | 3.00 |
| AI01 | Complete AI-use inventory, prompt log, material audit, verification, and human ownership | 4.00 |
| H01 | Release checklist, eight-minute handoff, defense, conditions, and disposition | 6.00 |
| Total |  | 35.00 |

Passing requires at least 28.00 of 35.00 points, every noncompensable gate, an adequate defense, and `accept` or `accept with conditions`.

### Noncompensable gates

- accepted Checkpoint 2 version and progression disposition;
- exact 90-file package;
- exact 74-row immutable manifest;
- exact analytic-table fingerprint and grain;
- all D01 through D20 resolutions and N01 through N08 conditions preserved;
- exact descriptive denominators and interval meaning;
- exact F01 through F03 tables, exports, alternatives, and registry;
- all 23 pipeline-source files present and fingerprinted;
- source, rights, and synthetic status explicit;
- environment and exact reproduction commands present;
- no hidden local or network dependency beyond declared source retrieval;
- no source ZIP, generated database, secret, or restricted data committed;
- complete change log, release notes, data brief, limitations, and checklist;
- complete AI-use inventory and one independently verified material audit;
- no AI output treated as evidence by itself;
- no unsupported real-world, trend, forecast, process-control, or causal claim;
- complete equivalent-access handoff;
- complete validation;
- adequate technical defense; and
- allowed disposition.

### Automatic return without scoring

Return the candidate when:

- an immutable file is missing or changed;
- the source, cohort, grain, denominator, or version is ambiguous;
- a required pipeline source is absent or edited without a new version;
- reproduction depends on an undeclared local path, package, credential, or manual edit;
- a structural blank becomes zero;
- an accepted condition is hidden or described as fixed;
- a figure loses an exact table, alternative, or non-color cue;
- source or output identity is based on filename rather than fingerprint;
- release notes omit a material condition or compatibility change;
- AI use is materially incomplete, unverifiable, or exposes restricted data;
- the source is described as real patient evidence;
- the learner cannot explain one pipeline stage or one AI audit; or
- the tag identifies a different commit than the reviewed candidate.

## 16. Common failures and instructor interventions

| Failure | Why it matters | Intervention |
|---|---|---|
| "It runs on my computer" without environment identity | receiver cannot reproduce | require exact Python, packages, SQLite, OS, commands, and result comparison |
| copied output without owning code | package cannot be audited | trace output to pipeline contract and source module |
| new orchestrator that silently changes paths or defaults | creates an unreviewed pipeline | remove it; preserve existing builders and an explicit runbook |
| final manifest covers only data | code or documentation can drift | require all 74 immutable rows |
| changed output accepted because it looks the same | visual plausibility is weak evidence | compare bytes and SHA-256; return to owner if changed |
| all blanks described as missing data | loses structural meaning | trace N01 through N03 and field-state rules |
| interval described as significance | changes the analytic claim | restore descriptive synthetic-cohort wording |
| quarterly line called a decline | invents trend and denominator meaning | restore selected-index chronology and no-trend limit |
| AI log says only "used for help" | material influence is not auditable | require claim, action, evidence, result, and human owner |
| prompt log copies secrets or patient text | creates privacy and security risk | refer, remove exposure, and follow incident policy |
| tag created before review | tag does not mean accepted release | delete only with repository-owner approval; create after disposition |
| validator pass treated as approval | human meaning and defense are skipped | require named reviewers and final disposition |

## 17. Accessibility, equity, privacy, and claim checks

### Accessibility

- All commands and records use selectable text.
- Tables have headers and meaningful reading order.
- Every released figure has PNG, SVG, exact CSV, and structured alternative.
- Color is never the only cue.
- Data brief and handoff brief link equivalent routes.
- Validator output is understandable without color.
- The defense provides accessible materials before the session.
- A learner may request an equivalent written or recorded defense route without changing the technical standard.

### Equity and small results

N07 and N08 remain visible as interpretation and display cautions. The module does not silently suppress exact internal synthetic teaching counts, invent a universal small-cell rule, rank groups, or make fairness claims from the fixed synthetic cohort.

### Privacy and security

- Only public synthetic data are allowed.
- Identity-like source fields remain outside the analytic release.
- The source ZIP and generated database remain outside Git.
- Prompt logs summarize material interaction and never include secrets, credentials, patient data, workplace data, or unnecessary raw records.
- A detected restricted-data exposure triggers referral and local policy, not ordinary revision.

### Claim boundary

The toolkit supports technical education and pipeline testing. It supports no real clinical, operational, performance, safety, access, equity, utilization, cost, population, trend, forecast, process-control, effect, or causal conclusion.

## 18. AI policy, disclosure, and verification

### Permitted uses

AI may help explain code, draft tests, propose documentation, identify ambiguous wording, or suggest verification approaches when only public synthetic or non-sensitive metadata are shared.

### Prohibited uses

- sharing protected, restricted, workplace, patient, secret, or credential data;
- accepting generated code or prose without review;
- inventing a source, test, run, accessibility result, reviewer, or disposition;
- using AI output as the source of a data value or clinical meaning;
- concealing a material transformation or claim; and
- allowing an external tool to change immutable evidence.

### Prompt-log contract

Each material row records:

- entry ID and date;
- tool and model;
- purpose;
- data class shared;
- prompt or request summary;
- response or recommendation summary;
- affected artifact or decision;
- risk if wrong;
- independent verification method;
- evidence path or exact fact;
- result;
- human action and owner; and
- disclosure status.

### Required material audit

The learner selects one AI-assisted step that could change a decision, number, code path, accessibility statement, or release condition. The audit must:

1. quote or precisely summarize the claim;
2. explain the consequence if wrong;
3. use an independent method rather than asking the same model again;
4. identify exact source rows, arithmetic, code, documentation, or fingerprint evidence;
5. record pass, fail, or partial support;
6. state the correction or retained action; and
7. name the human owner.

The reference audits structural missingness: 263 `No encounter recorded` rows retain blank companion fields, so replacing elapsed time with zero would change meaning and is rejected.

## 19. Answer key and instructor materials

The instructor key includes:

- exact toolkit tree and counts;
- Checkpoint 2 and pipeline-contract fingerprints;
- 374-row, 29-field analytic identity;
- source archive identity;
- D01 through D20 and N01 through N08 handoff;
- descriptive result counts and rate numerators;
- F01 through F03 totals and access routes;
- clean assembly and validation results;
- the reference data brief and limitations record;
- a complete release checklist;
- reference prompt-log rows and material AI audit;
- 35-point score key;
- defense answer boundaries; and
- reference disposition.

### Reference handoff answers

- One analytic row represents one selected synthetic person and one unique index encounter.
- The cohort contains 374 people selected from 1,048 eligible acute events.
- The six registered rate numerators are 111, 92, 4, 15, 36, and 8 over 374.
- D01 through D20 were resolved in a separate teaching layer; N01 through N08 remain conditions.
- F03 totals 374 selected indexes, not hospital visits or service demand.
- Reproduction means rebuilding or reassembling from declared source, environment, code, and version, then comparing exact outputs.
- AI output is not evidence; the human owner must verify material influence independently.
- Permitted use is technical teaching and downstream method development on synthetic data, subject to retained conditions.
- A changed immutable artifact, restricted data, broken access route, unsupported claim, or failed defense requires revision or referral.

### Reference disposition

`accept with conditions` for final-checkpoint review. Conditions are named human review, independent operating-system reproduction, preserved synthetic scope, complete equivalent access, and no change to immutable artifacts or upstream claim limits.

## 20. Runnable acceptance checks

The module validator must check:

1. Module 07 version 0.1.0;
2. exact required module-package files;
3. complete Checkpoint 2 validation before assembly;
4. accepted Checkpoint 2 version;
5. allowed Checkpoint 2 progression disposition;
6. 23-row pipeline contract;
7. unique pipeline source and target paths;
8. safe relative paths;
9. pipeline source byte counts;
10. pipeline source SHA-256 values;
11. protected target refusal;
12. exact 90-file assembled tree;
13. 74-row release manifest;
14. unique manifest target paths;
15. sorted manifest paths;
16. source unit and version fields;
17. manifest byte counts;
18. manifest SHA-256 values;
19. exact Checkpoint 2 artifact contract copy;
20. exact Checkpoint 2 manifest copy;
21. exact Checkpoint 2 summary copy;
22. exact Checkpoint 2 version copy;
23. ten accepted Checkpoint 2 cumulative records;
24. all 35 Checkpoint 2 immutable artifacts;
25. 11 Module 04 artifacts;
26. 9 Module 05 artifacts;
27. 15 Module 06 artifacts;
28. 374 analytic rows;
29. 29 analytic fields;
30. 374 unique patient IDs;
31. 374 unique index encounter IDs;
32. exact analytic SHA-256;
33. 29 dictionary rows and positions;
34. 68 defect-manifest rows;
35. D01 through D20 manifest coverage;
36. 28 passing quality rules;
37. D01 through D20 resolved;
38. N01 through N08 retained;
39. 17 variable profiles;
40. 12 cross-tab cells;
41. six rates;
42. exact six numerators and denominators;
43. Wilson interval arithmetic;
44. two strata summing to 374;
45. 27 denominator records;
46. 18 passing descriptive checks;
47. three exact visual tables;
48. three PNG files;
49. three SVG files;
50. three structured alternatives;
51. 3-row, 25-field figure registry;
52. all registry links and fingerprints;
53. F03 totals 374, 314, and 60;
54. Python requirement pins;
55. Module 02 database-source files;
56. Module 03 four SQL files and builder;
57. Module 04 builder and profiler;
58. Module 05 builder;
59. Module 06 renderer;
60. no source ZIP or SQLite file;
61. no virtual environment, cache, secret, or credential file;
62. no local absolute path in learner records;
63. no Unicode dash in contracts;
64. no unresolved placeholder in complete mode;
65. release identity and tag format;
66. change log completeness;
67. release-note compatibility and conditions;
68. data-brief source, grain, rights, and use boundaries;
69. limitations include synthetic, selected-cohort, denominator, time, and human-review limits;
70. reproduction record includes environment, commands, and exact comparisons;
71. release checklist statuses;
72. prompt-log schema;
73. at least one material prompt-log row;
74. no prohibited data class in prompt log;
75. AI audit claim, consequence, independent method, evidence, result, action, and owner;
76. no AI-as-evidence claim;
77. 8-row component score;
78. score points total 35;
79. complete-mode score at least 28;
80. criterion statuses pass;
81. defense brief covers ten required topics;
82. ten question responses;
83. allowed disposition;
84. independent reproduction status;
85. starter validation;
86. complete validation;
87. reference assembly;
88. learner-mode assembly;
89. incomplete-record rejection;
90. missing-artifact rejection; and
91. assembler and validator self-checks.

Starter mode permits placeholders only in learner-owned release records. It never relaxes immutable evidence, pipeline-source, manifest, data, figure, or access checks.

## 21. Release status, reviewers, version, and known issues

### Semantic-version decision

Module 0.1.0 establishes the first runnable FND-1 toolkit-assembly, immutable-manifest, data-brief, material-AI-audit, and final-handoff contract. Commons 0.36.0 adds the compatible module without changing Modules 01 through 06 or Checkpoints 1 and 2.

### Required human reviewers

| Role | Reviewer | Status | Review focus |
|---|---|---|---|
| FND-1 faculty owner | unassigned | pending | objectives, workload, assessment, and defense |
| SQL and data engineering | unassigned | pending | runnable source, environment, manifest, and handoff |
| Clinical informatics | unassigned | pending | grain, cohort, conditions, and claim meaning |
| Accessibility | unassigned | pending | equivalent access and defense materials |
| Privacy and data governance | unassigned | pending | source, fields, prompts, and permitted use |
| Responsible AI | unassigned | pending | prompt log, material audit, verification, and ownership |
| Independent reproducer | unassigned | pending | clean checkout and exact output comparison |

### Measured release facts and known issues

1. The 23-row pipeline contract is 4,478 bytes with SHA-256 `d61f208046663b80f8a591be66cc4f22fecbf0c5be7803786f75fd74cdd1d783`.
2. Reference and learner assembly each create 90 files. The 10,856-byte, 74-row manifest SHA-256 is `804d454dcdf43d0f625c90130b9bd5c698b51451ddcc1fd0910ca52e1bbd9111`.
3. Starter validation passes 585 checks; complete reference validation passes 657 checks.
4. Named macOS and Linux reproduction remains pending.
5. Named human review remains pending.
6. The source is synthetic and older.

### Context-safe handoff

Module 07 version 0.1.0 is the frozen candidate contract for the final checkpoint. Continue by preserving the 90-file tree, 74-row immutable manifest, exact 35-point rubric, release records, material AI audit, defense evidence, and all upstream conditions. Commit and push Module 07 before building the final checkpoint.
