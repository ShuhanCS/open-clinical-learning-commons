# FND-1 Final checkpoint: Reproducible healthcare data toolkit

## 1. Checkpoint identity and place in the course

- Checkpoint ID: `oclc-fnd1-cp3`.
- Checkpoint version: 0.1.0.
- Commons release target: 0.37.0.
- Course: FND-1, Healthcare Data Foundations.
- Due: official last day of the assigned MGH Institute half-term.
- Course weight: 35 percent, or 35 course points.
- Cumulative learner work: 112.5 hours.
- Required input: accepted or conditionally accepted Module 07 toolkit candidate version 0.1.0.
- Required final tag: `fnd1-toolkit-v0.1.0`.
- Status: runnable release candidate.

The official calendar controls the submission date: https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

The 7.5-week phrase remains a planning model. This checkpoint is due on the published last day of the assigned half-term, not on a date inferred by adding 7.5 weeks.

The checkpoint freezes the complete 90-file Module 07 candidate, verifies the final defense and review decision, and records the handoff to FND-2. It does not add another 35 points or recompute an analytic result. The Module 07 score is a draft of this same source assessment component; `final-review/final-score.csv` is the course record.

## 2. Decision, audience, and review question

### Decision owner

The final decision owner is a health-system analytics engineering lead. The panel includes:

- FND-1 faculty owner;
- SQL or data engineering reviewer;
- clinical informatics or healthcare-data-meaning reviewer;
- accessibility reviewer;
- privacy and data-governance reviewer;
- responsible-AI reviewer; and
- independent reproducer.

### Receiving audience

The immediate receiver is an FND-2 instructor or analyst who did not build the FND-1 pipeline. They need one accepted technical foundation with clear provenance, exact evidence, runnable source, access routes, conditions, and escalation rules.

### Final review question

May the complete versioned toolkit be accepted as the technical data foundation for downstream modeling or applied analysis without changing source, grain, denominators, quality conditions, access, AI accountability, or claim limits?

### Allowed dispositions

- `accept`;
- `accept with conditions`;
- `revise`; or
- `refer` for rights, privacy, integrity, clinical meaning, accessibility, AI accountability, or governance review.

Only `accept` and `accept with conditions` permit FND-2 handoff. Neither authorizes production deployment, clinical approval, or real-patient use.

## 3. Course-point preservation and final score map

The final checkpoint preserves the source curriculum's 35-percent reproducible-toolkit assessment exactly once.

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

Passing requires at least 28.00 points, all noncompensable gates, an adequate defense, and `accept` or `accept with conditions`.

The five-row defense record allocates the H01 six points without adding weight:

| Defense component | H01 points |
|---|---:|
| source, rights, grain, and cohort explanation | 1.00 |
| quality, denominator, and interpretation explanation | 1.00 |
| reproduction, version, and manifest explanation | 1.00 |
| accessibility and AI-accountability explanation | 1.00 |
| response accuracy, limits, conditions, and final recommendation | 2.00 |
| Total | 6.00 |

## 4. Competencies and assessable outcomes

By completing the checkpoint, the learner can:

1. identify the exact repository, commit, version, and annotated final tag;
2. prove that the reviewed candidate contains exactly 90 files;
3. freeze all 90 candidate files in a final candidate manifest;
4. distinguish the 74 Module 07 immutable rows from the 16 candidate release and manifest records;
5. trace every analytic artifact to its owning source module;
6. explain the source archive, rights, relational system, cohort, grain, and time zero;
7. defend one numerator, denominator, window, and interval;
8. explain D01 through D20 resolution and N01 through N08 retention;
9. explain every equivalent-access route for F01 through F03;
10. reproduce the candidate from a clean checkout and compare exact outputs;
11. identify a hidden dependency or changed byte as a release failure;
12. explain one material AI-assisted step and its independent verification;
13. distinguish validator evidence from human approval;
14. deliver an eight-minute technical handoff;
15. answer ten required questions without relying on prepared text;
16. state permitted use, prohibited claims, conditions, owners, and stop rules; and
17. defend an `accept`, `accept with conditions`, `revise`, or `refer` disposition.

## 5. Ownership and out-of-scope boundaries

### Final checkpoint owns

- whole-candidate freeze and 90-row candidate manifest;
- final 35-point score;
- 20 noncompensable gate results;
- six-point defense breakdown;
- named reviewer record;
- final reproduction confirmation;
- final disposition and conditions;
- accepted handoff statement; and
- FND-2 progression decision.

### Module 07 ownership retained

Module 07 owns the toolkit tree, 74-row immutable release manifest, pipeline contract, release records, data brief, limitations, material AI audit, prompt log, checklist, and defense preparation. The final checkpoint freezes and adjudicates them; it does not silently edit them.

### Upstream ownership retained

Modules 01 through 06 and Checkpoints 1 and 2 continue to own their source, code, analytic, quality, descriptive, figure, accessibility, and cumulative-decision facts.

### Out of scope

- a new or refreshed source;
- changed cohort, grain, field, time window, cleaning rule, denominator, statistic, figure, or access route;
- model fitting, selection, performance assessment, risk adjustment, or causal inference;
- production deployment or clinical approval;
- real clinical, operational, performance, safety, access, equity, utilization, cost, population, trend, forecast, process-control, effect, or causal inference;
- accepting workplace, patient, restricted, secret, or credential data; and
- changing a candidate after defense without a new version and renewed review.

## 6. Final workflow, workload, and defense

The final checkpoint uses work already included in Module 07's 16 hours:

1. validate the complete Module 07 candidate;
2. assemble into a new final-review target;
3. inspect the generated 90-row candidate manifest;
4. compare the candidate manifest to the reviewed commit;
5. complete the final score, gates, defense score, reviewer record, and reproduction record;
6. deliver the eight-minute handoff;
7. answer questions for approximately seven minutes;
8. record conditions, owners, due points, and escalation triggers;
9. set the final disposition and FND-2 progression;
10. validate the complete final package;
11. commit the exact reviewed state; and
12. create `fnd1-toolkit-v0.1.0` only after an allowed disposition.

### Required handoff topics

1. source and permitted use;
2. relational schema and grain;
3. cohort definition and denominator;
4. analytic-table construction;
5. most consequential quality issue;
6. descriptive evidence and limit;
7. accessibility path;
8. reproduction and validation;
9. AI-assisted step and human checks; and
10. recommended disposition and conditions.

### Required questions

1. What does one row in every released table represent?
2. Which query creates the cohort and how do the counts reconcile?
3. What is the numerator and denominator for each released rate?
4. Which defect most threatens downstream use and why?
5. What was fixed, what remains conditional, and how is that visible?
6. Why can the synthetic source support pipeline education but not real clinical inference?
7. How can another analyst reproduce the toolkit?
8. What did AI contribute and how was it checked?
9. What use is permitted now?
10. What evidence would stop or revise the release?

## 7. Accepted input and immutable facts

### Module 07 candidate

| Item | Accepted fact |
|---|---|
| module / version | `oclc-fnd1-07` / 0.1.0 |
| candidate files | 90 |
| Module 07 immutable rows | 74 |
| pipeline-source files | 23 |
| pipeline contract bytes | 4,478 |
| pipeline contract SHA-256 | `d61f208046663b80f8a591be66cc4f22fecbf0c5be7803786f75fd74cdd1d783` |
| Module 07 manifest bytes | 10,856 |
| Module 07 manifest SHA-256 | `804d454dcdf43d0f625c90130b9bd5c698b51451ddcc1fd0910ca52e1bbd9111` |
| reference disposition | `accept with conditions` |

### Analytic and evidence facts

- Source archive: 8,982,431 bytes; SHA-256 `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a`.
- Analytic table: 374 rows, 29 fields, 374 unique patients and index encounters.
- Analytic SHA-256: `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a`.
- Quality: 28 passing rules, D01 through D20 resolved, N01 through N08 retained.
- Descriptive: 17 profiles, 12 cross-tab cells, six rates, two strata, 27 denominator records, 18 passing checks.
- Rate numerators: 111, 92, 4, 15, 36, and 8, each over 374.
- Figures: three exact tables, three PNG, three SVG, three structured alternatives, and a 25-field registry.
- AI audit: 263 `No encounter recorded` rows retain blank companion fields; independent verification passes.

### Rights and claim boundary

The source is public synthetic data and contains no real patient records. The source ZIP and generated SQLite database are not in the package. The toolkit supports technical education and downstream method development only.

## 8. Exact final package and freeze contract

The final checkpoint preserves the entire Module 07 candidate at its existing paths and adds only `final-review/`.

```text
fnd1-toolkit-final/
  [all 90 Module 07 candidate files at unchanged paths]
  final-review/
    CHECKPOINT-VERSION
    candidate-manifest.csv
    submission-record.md
    final-score.csv
    gate-results.csv
    defense-score.csv
    reviewer-record.md
    final-disposition.md
    handoff-acceptance.md
    final-reproduction.md
```

The package contains exactly 100 files. `candidate-manifest.csv` has exactly 90 rows, one for every candidate file before final-review records are added.

Each manifest row records:

- relative path;
- byte count;
- SHA-256; and
- source role.

The final-review records are reviewer-owned and are not part of the candidate manifest. After final disposition, the entire 100-file Git state is frozen by the reviewed commit and annotated tag.

## 9. Assembly, manifest, and change-control rules

### Protected assembly

The assembler accepts one complete Module 07 candidate and one new target. It runs the Module 07 validator in complete mode before copying. It refuses a target that already exists.

### Candidate freeze

The assembler:

1. enumerates the exact 90 candidate files;
2. rejects an unexpected or missing path;
3. records bytes and SHA-256 for every path;
4. copies the candidate without changing bytes;
5. writes the sorted 90-row candidate manifest;
6. adds the checkpoint version and reviewer templates or reference records; and
7. reports exactly 100 files.

### Change control

Any change to one of the 90 candidate files after assembly invalidates the manifest and returns the work to Module 07 for a version decision. A final-review correction requires renewed validation. A change after defense requires renewed defense when it can affect meaning, evidence, score, gates, or disposition.

### Tag rule

The annotated tag `fnd1-toolkit-v0.1.0` must identify the exact reviewed commit. A tag on another commit, a lightweight tag, or a tag created before an allowed disposition fails the release gate.

## 10. Final technical evidence contract

The final review verifies:

- exact source and rights;
- declared relational grains, keys, and time zero;
- one-row-per-person analytic grain;
- deterministic cohort and flow conservation;
- exact quality-rule and resolution evidence;
- retained natural conditions and structural missingness;
- descriptive denominators, intervals, strata, and limits;
- exact figures, tables, alternatives, and registry links;
- environment, code, source retrieval, and output comparisons;
- semantic version, change log, release notes, and tag evidence;
- data brief and limitations;
- prompt log and one material AI audit;
- release checklist;
- eight-minute handoff and responses; and
- condition ownership and stop rules.

Automation verifies structure, bytes, hashes, rows, arithmetic, required language, and status fields. Human reviewers decide whether explanations, accessibility, clinical meaning, AI accountability, and the final recommendation are credible.

## 11. Defense, accessibility, privacy, and AI gates

### Defense gate

The learner must explain the pipeline without reading a prepared script, answer all ten questions accurately, distinguish evidence from inference, and recognize when a condition requires revision or referral.

### Accessibility gate

- Defense materials are available in accessible digital form before review.
- Tables have headers and logical reading order.
- Figures retain PNG, SVG, exact CSV, structured alternatives, and non-color cues.
- Data brief and handoff brief identify equivalent routes.
- Validator and reviewer status do not depend on color alone.
- An equivalent written or recorded defense route may be used without lowering the technical standard.

### Privacy and rights gate

Only public synthetic data are allowed. No source ZIP, generated database, identity-like source expansion, patient data, workplace data, credential, secret, or restricted file may enter the public release or an external AI tool.

### AI gate

The prompt log must disclose every material use. At least one material step must have claim, consequence, independent method, exact evidence, result, correction or retained action, and named human owner. Repeating the question to the same model is not independent verification. AI output is never evidence by itself.

## 12. Reviewer roles, independence, and decision rules

| Role | Required decision |
|---|---|
| FND-1 faculty owner | objectives, workload, score, defense, and course completion |
| SQL or data engineering | runnable source, schema, cohort SQL, manifest, and reproduction |
| Clinical informatics | grain, time, quality conditions, denominators, and claim meaning |
| Accessibility | equivalent access and defense materials |
| Privacy and data governance | source rights, excluded fields, prompt boundary, and permitted use |
| Responsible AI | disclosure, material audit, independent evidence, and human ownership |
| Independent reproducer | clean checkout, declared environment, ordered commands, and exact comparison |

One person may cover multiple roles when expertise and independence are recorded. The learner cannot serve as the independent reproducer or final decision owner.

### Conditions

Every condition names:

- condition ID;
- owner;
- due point;
- evidence required;
- verifier;
- closure status; and
- escalation trigger.

A condition cannot waive restricted-data exposure, changed immutable evidence, a failed access route, a missing material AI audit, or an inadequate defense.

## 13. Final-review record contracts

### Submission record

Records repository URL, full commit, Module 07 version and candidate status, checkpoint version, final tag, official due date, 90-row manifest fingerprint, validator result, and submitter.

### Final score

Eight rows preserve the exact 35-point rubric. Scores use decimals, stay within each criterion, total at least 28, cite evidence, and record status.

### Gate results

Twenty rows record gate ID, gate, result, evidence, reviewer, and condition ID. Results are `pass`, `pass with condition`, or `fail`. A failed gate cannot receive an accepting disposition.

### Defense score

Five rows allocate the H01 six points. The total must equal the H01 score in the final score.

### Reviewer record

Records every required role, reviewer identity or explicit pending condition, independence, date, evidence reviewed, decision, and signature or equivalent acknowledgment.

### Final disposition

Records total score, gates, defense result, allowed disposition, conditions and owners, tag authorization, and FND-2 progression.

### Handoff acceptance

States what FND-2 receives, permitted use, conditions, prohibited claims, support owner, change-notification rule, and stop or referral triggers.

### Final reproduction

Records clean-checkout identity, OS, Python, SQLite, packages, source archive fingerprint, commands, exact output comparisons, validator output, independent reproducer, date, and unresolved platform conditions.

## 14. Submission and review workflow

### Learner workflow

1. Freeze the complete Module 07 candidate at a commit.
2. Assemble the final checkpoint into a new target.
3. Verify the 90-row candidate manifest.
4. Complete the submission and reproduction records.
5. Propose scores and gate evidence without changing rubric weights.
6. Deliver the handoff and answer the ten questions.
7. Respond to reviewer findings in the owning record or upstream unit.
8. Rerun complete validation after every correction.
9. Obtain the final disposition.
10. Commit the exact reviewed 100-file state.
11. Create the annotated tag only when authorized.
12. Hand the accepted commit, tag, conditions, and toolkit path to FND-2.

### Reviewer workflow

1. Confirm the official due date and candidate identity.
2. Scan for prohibited files and data.
3. Validate the Module 07 candidate and 90-row freeze.
4. Trace source, cohort, quality, descriptive, figure, access, and AI evidence.
5. Review the clean reproduction and independent comparison.
6. Review release identity and proposed tag.
7. Conduct and score the defense.
8. Complete all 20 gate rows.
9. Finalize the eight score rows.
10. Record conditions and owners.
11. Set disposition, tag authorization, and FND-2 progression.
12. Validate the final package and verify the tagged commit.

## 15. Pass conditions, gates, and automatic return

### Numeric and decision rule

Passing requires:

- at least 28.00 of 35.00 points;
- all 20 gates passed or explicitly passed with an allowed condition;
- at least 4.80 of 6.00 H01 defense points;
- no failed gate;
- `accept` or `accept with conditions`; and
- explicit FND-2 progression.

### Twenty noncompensable gates

1. exact accepted Module 07 version and candidate;
2. exact 90-row candidate manifest;
3. exact 100-file final tree;
4. repository, commit, semantic version, and tag identity;
5. exact source archive and rights;
6. exact analytic grain and fingerprint;
7. deterministic cohort and conserved counts;
8. D01 through D20 resolution preserved;
9. N01 through N08 conditions preserved;
10. exact descriptive denominators and interval meaning;
11. exact F01 through F03 evidence and equivalent access;
12. complete pipeline source and declared environment;
13. clean reproduction and exact output comparison;
14. no hidden dependency or manual output edit;
15. no prohibited data, archive, database, secret, or credential;
16. complete data brief, limitations, change log, release notes, and checklist;
17. complete material AI disclosure and independent audit;
18. adequate accessible technical defense;
19. complete reviewer, condition, and final-disposition records; and
20. no unsupported real-world or causal claim.

### Automatic return without scoring

Return when:

- the candidate does not pass Module 07 complete validation;
- one candidate file is missing, changed, or unexpected;
- the source, commit, version, tag, grain, denominator, or condition is ambiguous;
- the source ZIP, SQLite database, cache, secret, restricted data, or local absolute path appears;
- reproduction requires an undeclared dependency or manual output edit;
- a structural blank becomes zero;
- a quality condition or small result is hidden;
- a figure loses equivalent access or changes an exact value;
- the AI log or material audit is incomplete or unverifiable;
- the learner makes a real clinical, volume, trend, forecast, process-control, effect, or causal claim;
- the defense is incomplete or materially inaccurate;
- a gate fails; or
- the tag identifies a different commit.

## 16. Runnable acceptance checks

The final validator must check:

1. checkpoint version 0.1.0;
2. exact required checkpoint-package files;
3. complete Module 07 candidate validation;
4. exact 90 candidate files;
5. 90-row candidate manifest;
6. unique sorted candidate paths;
7. portable candidate paths;
8. candidate byte counts;
9. candidate SHA-256 values;
10. exact 100-file final tree;
11. exact Module 07 pipeline contract fingerprint;
12. exact Module 07 release manifest fingerprint;
13. exact analytic-table fingerprint;
14. 374 analytic rows and 29 fields;
15. 374 unique patients and index encounters;
16. D01 through D20 and N01 through N08;
17. 28 passing quality rules;
18. 17 profiles, 12 cross-tab cells, six rates, two strata, and 27 denominator records;
19. six exact rate numerators and denominators;
20. Wilson interval arithmetic;
21. 18 passing descriptive checks;
22. F01 through F03 exact routes and fingerprints;
23. F03 totals 374, 314, and 60;
24. 23 pipeline-source files;
25. Python requirement pins;
26. no prohibited file suffix or folder;
27. no learner-record local absolute path;
28. no Unicode dash in contracts;
29. no unresolved placeholder in complete mode;
30. submission-record release identity;
31. full commit format;
32. final tag format;
33. official calendar URL and last-day rule;
34. eight-row final score;
35. exact criterion IDs and 35 available points;
36. earned-score ranges and total;
37. 20-row gate record;
38. exact gate IDs;
39. allowed gate statuses;
40. no failed gate for acceptance;
41. condition IDs for conditional gates;
42. five-row defense score;
43. six available defense points;
44. defense earned score at least 4.8;
45. defense total equals H01 final score;
46. ten handoff topics represented;
47. ten questions answered;
48. all required reviewer roles represented;
49. learner is not independent reproducer or decision owner;
50. condition ownership and verification fields;
51. allowed final disposition;
52. explicit tag authorization;
53. explicit FND-2 progression;
54. handoff permitted-use boundary;
55. handoff prohibited-claim boundary;
56. final reproduction environment;
57. source archive fingerprint in reproduction record;
58. exact output comparison record;
59. independent reproducer status;
60. AI audit and prompt-log evidence;
61. accessibility evidence;
62. no AI-as-evidence statement;
63. no unsupported real-world claim;
64. protected target refusal;
65. reference assembly;
66. learner-mode assembly;
67. starter validation;
68. complete validation;
69. incomplete-record rejection;
70. missing-candidate-file rejection; and
71. assembler and validator self-checks.

Starter mode permits placeholders only in final-review learner and reviewer records. It never relaxes the complete Module 07 candidate, candidate manifest, source, data, figure, access, pipeline, or AI evidence.

## 17. Release status, reviewers, known issues, and handoff

### Semantic-version decision

Checkpoint 0.1.0 establishes the first final 90-file candidate-freeze, 35-point adjudication, gate, defense, reviewer, final-disposition, and FND-2 handoff contract. Commons 0.37.0 adds the compatible checkpoint without changing Modules 01 through 07 or Checkpoints 1 and 2.

### Required human reviewers

| Role | Reviewer | Status |
|---|---|---|
| FND-1 faculty owner | unassigned | pending |
| Health-system analytics engineering lead | unassigned | pending |
| SQL and data engineering | unassigned | pending |
| Clinical informatics | unassigned | pending |
| Accessibility | unassigned | pending |
| Privacy and data governance | unassigned | pending |
| Responsible AI | unassigned | pending |
| Independent reproducer | unassigned | pending |

### Measured release evidence

- Reference and learner assembly each produce exactly 100 files: 90 frozen candidate files and ten final-review files.
- The sorted 90-row candidate manifest is 11,804 bytes with SHA-256 `200df43e17926e29cc09aa89427a04205fd39ac289aebdf1217f952b188b89a0`.
- Complete reference validation passes 493 checks.
- Learner starter validation passes 404 checks.
- Existing targets, unfinished final-review records, and a missing candidate artifact are rejected.
- The assembler and validator use the Python standard library and have no new external dependency.

### Open maturity conditions

1. Named human review and a real learner defense remain pending before alpha.
2. Named macOS and Linux reproduction remains pending before stable.
3. A learner release must record and tag its final reviewed 100-file commit.
4. The source is synthetic and older.

### Context-safe handoff

The FND-1 technical package is complete at Commons 0.37.0. Resume with the FND-2 course specification. Keep FND-2 separate, preserve its source ownership and assessment weights, and do not repeat FND-1's data-pipeline work as generic review.
