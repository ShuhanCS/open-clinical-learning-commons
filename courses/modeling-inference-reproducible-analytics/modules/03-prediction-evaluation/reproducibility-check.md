# Reference reproducibility check

## Result

A clean temporary-directory build reproduced all 14 CSV evidence tables, two SVG displays, and `build-report.json` on Windows with Python 3.12.10 and the pinned scientific versions. A second build to the same target was refused. A copied learner workspace rebuilt the same outputs from its copied seven upstream inputs.

## Fixed facts

- upstream cohort rows and fields: 374 and 34;
- split rows: 224 training, 75 validation, and 75 test;
- outcomes: 25 training, 7 validation, and 4 test;
- selected model: `ML01`;
- locked threshold: 0.08513264;
- test confusion: 48 TN, 23 FP, 2 FN, and 2 TP;
- transformed features: 15;
- subgroup rows: 10, with unsupported metrics suppressed;
- bootstrap replicates: 2000;
- prediction checks: 22 pass; and
- reference recommendation: `continue to validity review with conditions`.

## Differences

No output difference was observed in the reference self-check. Library, platform, or floating-point changes require review rather than silent replacement of the release evidence.
