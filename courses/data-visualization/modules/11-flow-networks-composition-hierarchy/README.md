# Module 11: Flow, networks, composition, and hierarchy

Module 11 asks when the decision depends on movement, connection, nesting, or part-to-whole structure rather than an ordinary comparison.

## Decision

A simulated transitions-of-care director must choose one index-to-follow-up pathway for a definition audit before a real quality measure is proposed.

The reference screen identifies `Inpatient -> No encounter recorded` because the path has at least 20 synthetic patients and its 90-day acute-return percentage is above the full synthetic cohort percentage. This is a teaching screen, not a quality threshold or evidence about real care.

## Learning outcomes

By the end of the module, learners can:

1. define a cohort before drawing a flow;
2. state the unit that travels through every stage;
3. distinguish a node, edge, state, path, hierarchy, and composition;
4. keep one person from being counted twice in a conserved flow;
5. declare index, follow-up, and observation windows;
6. show the denominator at each node and in each rate;
7. choose among an alluvial view, matrix, stacked bar, hierarchy, or ordinary table;
8. explain why a node-link diagram can become a hairball;
9. distinguish area encoding of volume from color or labels encoding a rate;
10. preserve an exact path table and equivalent text alternative;
11. describe an absence in an extract without claiming that care did not occur; and
12. keep synthetic teaching results separate from real clinical evidence.

## Public source

- Synthea downloads: https://synthea.mitre.org/downloads
- Sample archive: https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip
- Synthea project: https://synthetichealth.github.io/synthea/
- CSV data dictionary: https://github.com/synthetichealth/synthea/wiki/CSV-File-Data-Dictionary
- Synthea repository: https://github.com/synthetichealth/synthea

The records are simulated. They are not de-identified records from real patients.

## Released data

| File | Grain | Rows | Purpose |
|---|---|---:|---|
| `data/synthea_patients_transition_source_2020.csv` | One synthetic patient | 1,171 | Complete patient source selection with only fields needed for cohort logic and context. |
| `data/synthea_encounters_transition_source_2020.csv` | One synthetic encounter | 53,346 | Complete encounter source selection for the sample archive. |
| `data/synthea_acute_transition_cohort_2020.csv` | One adult synthetic patient and one index event | 374 | Exact index, next-state, endpoint, denominator, and screen values. |
| `data/synthea_transition_edges_2020.csv` | One directed aggregate edge | 15 | Conservation audit for the two stage-to-stage transitions. |

Synthetic names, addresses, SSNs, driver identifiers, passports, costs, provider IDs, organization IDs, and payer IDs were omitted because the module does not use them.

## Cohort contract

- Observation start: 2015-01-01.
- Index end: 2019-12-31.
- Eligible person: age 18 or older at index.
- Index: first emergency or inpatient encounter in the window.
- Unit: one synthetic patient.
- Thirty-day state: first encounter that starts after index stop and no more than 30 days later.
- Ninety-day endpoint: death; otherwise acute return; otherwise no acute return.
- One patient contributes once.

`No encounter recorded` means no qualifying row appears in the sample during the defined 30-day interval. It does not prove that follow-up failed.

## Files

| File | Purpose |
|---|---|
| `build_transition_case.py` | Standard-library source selection, cohort, path, rate, screen, and edge build. |
| `validate_transition_case.py` | Sixty-four source, cohort, denominator, path, screen, and conservation checks. |
| `lab.R` | Defined cohort flow, transition matrix, endpoint composition, exact table, and text alternative. |
| `critique_charts.R` | Three deliberately flawed figures for repair. |
| `assessment.md` | Exact learner task, files, rubric, and pass conditions. |
| `instructor-notes.md` | Measured answers, facilitation plan, and critique key. |
| `data-spec.md` | Grain, fields, transformations, rights, and limits. |
| `source-record.yml` | URLs, retrieval date, checksums, rights, and cohort contract. |
| `release.json` | Machine-readable release and review status. |

## Rebuild

From the repository root:

```powershell
python courses/data-visualization/modules/11-flow-networks-composition-hierarchy/build_transition_case.py
```

The default build uses the committed source selections and deterministically rewrites the cohort and edge tables.

To refresh from the pinned archive:

```powershell
Invoke-WebRequest -Uri "https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip" -OutFile "$env:TEMP\synthea_sample_data_csv_apr2020.zip" -UseBasicParsing
python courses/data-visualization/modules/11-flow-networks-composition-hierarchy/build_transition_case.py --source-zip "$env:TEMP\synthea_sample_data_csv_apr2020.zip"
```

The archive checksum is pinned. A changed source must fail instead of silently changing the lesson.

## Validate

```powershell
python courses/data-visualization/modules/11-flow-networks-composition-hierarchy/validate_transition_case.py
```

Expected result:

```text
Module 11 synthetic transition data passed 64 checks.
```

## Run the reference lab

R and ggplot2 are required.

```powershell
Rscript courses/data-visualization/modules/11-flow-networks-composition-hierarchy/lab.R --output "$env:TEMP\oclc-da730-m11-lab"
```

The lab writes three figures, a seven-row exact path table, and a text alternative.

## Run the critique lab

```powershell
Rscript courses/data-visualization/modules/11-flow-networks-composition-hierarchy/critique_charts.R --output "$env:TEMP\oclc-da730-m11-critiques"
```

## Learner package

```text
module-11/
  structure-definition.md
  analysis.R
  cohort-flow.png
  transition-matrix.png
  composition.png
  path-table.csv
  source-record.yml
  alt-text.md
  decision-note.md
  ai-use.md
```

## Interpretation boundary

This module supports a definition audit in a simulated system. It does not support a real quality rating, a claim of failed follow-up, a causal claim, a patient-level intervention, or a production dashboard threshold.

## Handoff

Module 12 inherits the exact cohort, definitions, denominators, accessible outputs, and action language. It asks which minimum set of coordinated views a decision owner needs to monitor a process.
