# FND-1 Checkpoint 2: Quality, descriptive, and accessible evidence release

This package assembles and validates the cumulative Week 6 release from accepted FND-1 Modules 04 through 06. It freezes 35 immutable artifacts and assesses them once as the course's 25-point quality, descriptive, and accessible-evidence checkpoint.

The decision is whether the restored 374-person analytic table, exact descriptive evidence, and accessible figures may enter Module 07 without changing grain, denominators, uncertainty, retained conditions, or claim limits.

## Assemble from learner work

```powershell
python assemble_checkpoint.py --module04 <accepted-module-04-package> --module05 <accepted-module-05-package> --module06 <accepted-module-06-package> --target <new-checkpoint-folder>
```

The target must not exist. The assembler verifies every source fingerprint, copies only registered evidence, writes the manifest and module summary, and adds cumulative writing templates. Replace every `REPLACE` prompt.

## Assemble the instructor reference

```powershell
python assemble_checkpoint.py --reference --target <new-reference-folder>
```

Reference mode uses the released Module 04, 05, and 06 packages for instructor preparation and technical reproduction. It is not a learner submission.

## Validate

```powershell
python validate_checkpoint.py <checkpoint-folder>
```

During drafting, `--starter` checks all immutable data, manifests, figures, notebooks, and access routes while allowing unfinished cumulative records:

```powershell
python validate_checkpoint.py <checkpoint-folder> --starter
```

Test the package itself with:

```powershell
python assemble_checkpoint.py --self-check
python validate_checkpoint.py --self-check
```

## Passing rule

A passing checkpoint earns at least 20 of 25 points, passes every noncompensable gate and the defense, and receives `accept` or `accept with conditions`. Only those dispositions permit Module 07 to begin.

The source is synthetic and older. This release supports reproducibility, quality, descriptive, and accessibility teaching claims only, not real clinical, operational, population, trend, forecast, or causal conclusions.

Checkpoint version: 0.1.0. Commons release: 0.35.0.
