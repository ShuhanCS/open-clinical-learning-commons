# Assessment: Validated cohort and analytic-table release

## Course value

Checkpoint 1 is worth 40 course points. It preserves the original 15-point Module 01 setup component and 25-point Module 03 SQL cohort component. Module 02 is a required source and schema gateway but does not add another assessment weight.

## Submission

Submit:

- the complete `checkpoint-1/` folder defined in the specification;
- validator output;
- full Git commit hash;
- annotated tag `fnd1-checkpoint1-v0.1.0`; and
- technical handoff defense.

The source ZIP and generated SQLite database are verified by fingerprints and clean reproduction. Do not commit or upload them into the checkpoint folder.

## Required preparation

1. Start from accepted or conditionally accepted Module 01, 02, and 03 work.
2. Assemble into a new target with `assemble_checkpoint.py`.
3. Inspect `release-manifest.csv` before changing cumulative records.
4. Complete every `[REPLACE: ...]` prompt.
5. Rebuild the database and rerun all first-extract and cohort SQL.
6. Validate the complete folder without `--starter`.
7. Commit the exact reviewed state.
8. Complete the defense.
9. Tag only after an `accept` or `accept with conditions` decision.

## Forty-point rubric

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

At least 32 points are required.

## Noncompensable gates

- synthetic and public data only;
- exact source archive identity;
- runnable environment;
- meaningful Git and version evidence;
- database integrity and zero foreign-key failures;
- declared grain and keys;
- exact first extracts;
- adult eligibility and deterministic index;
- one index and analytic row per included person;
- flow conservation;
- correct temporal windows;
- no join multiplication;
- 29 analytic fields and dictionary rows;
- post-index fields labeled;
- byte-reproducible outputs;
- accessible schema route;
- verified material AI-use disclosure;
- adequate learner defense; and
- `accept` or `accept with conditions` disposition.

## Defense questions

Answer without reading prepared text:

1. Why do 1,048 eligible events become 374 people?
2. Why must the adult filter happen before event ranking?
3. What makes index selection deterministic?
4. What is time zero for history and follow-up?
5. Why are encounter, condition, and medication histories aggregated separately?
6. What does `No encounter recorded` mean?
7. Which analytic fields occur after index?
8. How did you prove the source and outputs were unchanged?
9. What material AI advice did you verify and how?
10. Why does your release disposition follow from the evidence?

## Progression rule

Only `accept` and `accept with conditions` permit Module 04 to begin. A condition must name an owner, evidence, due point, and closure status. It cannot waive a failed gate.
