# FND-1 Checkpoint 1: Validated cohort and analytic-table release

This package assembles and validates the cumulative Week 3 release from accepted FND-1 Modules 01 through 03. The checkpoint preserves the original 15-point workspace component and 25-point SQL cohort component for 40 course points total.

The decision is whether the workspace, database, cohort, and 374-row analytic table are technically ready for cleaning and profiling in Module 04.

## Assemble from learner work

```powershell
python assemble_checkpoint.py --module01 <accepted-module-01-workspace> --module02 <accepted-module-02-workspace> --module03 <accepted-module-03-submission> --target <new-checkpoint-folder>
```

The target must not exist. The assembler copies accepted evidence, creates the first-extract registry and immutable release manifest, and adds cumulative writing templates. Replace every `[REPLACE: ...]` prompt.

## Assemble the instructor reference

```powershell
python assemble_checkpoint.py --reference --target <new-reference-folder>
```

Reference mode uses released answer assets for technical reproduction and instructor preparation. It is not a learner submission.

## Validate

```powershell
python validate_checkpoint.py <checkpoint-folder>
```

During drafting, `--starter` checks structure and immutable evidence while allowing unfinished cumulative records:

```powershell
python validate_checkpoint.py <checkpoint-folder> --starter
```

Test the package itself with:

```powershell
python assemble_checkpoint.py --self-check
python validate_checkpoint.py --self-check
```

## Passing rule

A passing checkpoint earns at least 32 of 40 points, passes every noncompensable gate, and receives `accept` or `accept with conditions`. Only those two dispositions permit Module 04 to begin.

The source is synthetic and older. The release supports technical reproducibility and cohort-definition claims only, not real clinical or population conclusions.

Checkpoint version: 0.1.0. Commons release: 0.31.0.
