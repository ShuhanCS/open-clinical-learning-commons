# FND-2 Checkpoint 1: Modeling-readiness release

This cumulative Week 3 checkpoint freezes accepted FND-2 Modules 01 through 03 and decides whether the modeling question, regression evidence, locked prediction workflow, evaluation, and use boundary may enter validity review.

## Release identity

- Checkpoint ID: `oclc-fnd2-cp1`
- Checkpoint version: 0.1.0
- Commons release: 0.42.0
- Course points: 40
- Cumulative hours: 48.0
- Required tag: `fnd2-checkpoint1-v0.1.0`
- Reference disposition: `accept with conditions`

## What assembly does

The assembler copies 72 accepted module artifacts and 6 checkpoint control files, preserves module-relative paths, and writes a sorted 78-row immutable manifest. It adds 10 cumulative records for scoring, gates, defense, reproduction, review, and progression. The complete assembled checkpoint has 89 files.

It does not recompute any model, prediction, metric, threshold, or subgroup result.

## Reference assembly

From the repository root:

```powershell
python courses/modeling-inference-reproducible-analytics/checkpoints/01-modeling-readiness-release/assemble_checkpoint.py checkpoint-output --reference
python checkpoint-output/validate_checkpoint.py checkpoint-output
```

The target must not exist.

## Learner assembly

```powershell
python courses/modeling-inference-reproducible-analytics/checkpoints/01-modeling-readiness-release/assemble_checkpoint.py checkpoint-output --module01 path/to/module01 --module02 path/to/module02 --module03 path/to/module03
```

Complete every prompted root record, then run:

```powershell
python checkpoint-output/validate_checkpoint.py checkpoint-output
```

## Self-checks

```powershell
python courses/modeling-inference-reproducible-analytics/checkpoints/01-modeling-readiness-release/assemble_checkpoint.py --self-check
python courses/modeling-inference-reproducible-analytics/checkpoints/01-modeling-readiness-release/validate_checkpoint.py --self-check
```

## Progression rule

At least 32 of 40 points, all 23 gates, an adequate 12-question defense, and `accept` or `accept with conditions` are required before Module 04. The reference carries forward the synthetic-data boundary, four test outcomes, 48/23/2/2 confusion counts, sparse subgroup evidence, and no-deployment rule.

Durable specification:

`docs/curriculum/courses/FND-2/checkpoints/01-modeling-readiness-release-spec.md`
