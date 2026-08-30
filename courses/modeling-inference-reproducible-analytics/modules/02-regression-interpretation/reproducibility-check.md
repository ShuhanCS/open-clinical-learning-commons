# Reference reproducibility check

## Python reproduction

A clean temporary-directory build reproduced all 13 CSV tables and `build-report.json` byte for byte on Windows with Python 3.12.10 and the declared scientific versions. A second build to the same target was refused. A copied learner workspace rebuilt identical outputs from its copied Module 01 inputs.

## R reproduction

The release machine has no R runtime. `paired-models.R` and an eight-row numeric target are included. Named R execution, version capture, and tolerance reconciliation remain pending before alpha.

## Fixed facts

- upstream modeling rows and fields: 374 and 34;
- linear available rows: 111;
- linear training fit rows: 69;
- structural timing blanks: 263;
- logistic training rows and positives: 224 and 25;
- validation used in fitting: no;
- test used in fitting: no;
- regression checks: 24 pass; and
- reference disposition: `accept with conditions`.

## Differences

No Python output difference was observed. The absent local R runtime is recorded as a material release condition rather than represented as a completed R run.
