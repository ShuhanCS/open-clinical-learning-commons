# Reference reproducibility check

## Reproducer

Independent machine reproduction is pending. The release author completed a clean temporary-directory reproduction on Windows with Python 3.12.10.

## Procedure

1. Verified the upstream source byte count and SHA-256.
2. Built outputs into a target that did not exist.
3. Rebuilt a complete learner starter into a separate target.
4. Confirmed that the builder refused both existing targets.
5. Validated all output rows, fields, fingerprints, split counts, outcome counts, date ranges, baseline values, and text boundaries.
6. Removed a required file from a copied fixture and confirmed submission validation failed.

## Observed result

- source: 374 rows and 29 fields;
- modeling cohort: 374 rows and 34 fields;
- split: 224 train, 75 validation, and 75 test;
- positives: 25 train, 7 validation, and 4 test;
- baseline: `0.111607142857` from training only;
- release checks: all pass; and
- existing-target refusal: pass.

## Disposition

`accept with conditions`

The build is deterministic and technically reproducible on the tested system. Named Windows, macOS, and Linux reproductions by people other than the release author remain pending before alpha.
