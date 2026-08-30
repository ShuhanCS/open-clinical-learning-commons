# Reference R run record

## Status

`pending named R execution`

## Supplied command

```text
Rscript paired-models.R data/modeling-cohort.csv outputs/r-coefficients.csv
```

## Required reconciliation

Compare model ID, normalized term, estimate, standard error, and 95-percent interval with `outputs/r-reading-fixture.csv`. Absolute differences must be no more than 0.000001 after accounting for display precision.

## Release condition

The current release machine does not have R. A named reviewer must record R version, operating system, command, output fingerprint, row-by-row maximum absolute difference, and disposition before alpha approval.
