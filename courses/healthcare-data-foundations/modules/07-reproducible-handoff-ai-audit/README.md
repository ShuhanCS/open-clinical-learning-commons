# FND-1 Module 07: Reproducible handoff and AI audit

This module turns an accepted FND-1 Week 6 checkpoint into a versioned toolkit candidate another analyst can inspect, validate, reproduce, and defend. It packages accepted evidence and exact pipeline source without recalculating, retyping, redrawing, or suppressing results.

## Assemble from accepted work

```powershell
python assemble_toolkit.py --checkpoint2 <accepted-checkpoint-2-folder> --course-root <healthcare-data-foundations-folder> --target <new-toolkit-folder>
```

Checkpoint 2 must pass complete validation. The course root must contain the accepted Module 01 through 06 packages. The target must not exist.

## Assemble the instructor reference

```powershell
python assemble_toolkit.py --reference --target <new-reference-toolkit-folder>
```

Reference mode creates a temporary canonical Checkpoint 2 package, verifies the 23 pipeline-source files, and writes the complete instructor records. It is not a learner submission.

## Validate

```powershell
python validate_toolkit.py <toolkit-folder>
```

During drafting, starter mode permits placeholders only in learner-owned release records:

```powershell
python validate_toolkit.py <toolkit-folder> --starter
```

Test the module itself with:

```powershell
python assemble_toolkit.py --self-check
python validate_toolkit.py --self-check
```

## Release result

The candidate contains 90 files and a 74-row immutable manifest: 35 accepted Checkpoint 2 artifacts, ten accepted checkpoint records, four checkpoint provenance files, 23 pipeline-source files, the pipeline contract, and the portable validator.

Passing requires at least 28 of 35 points, every noncompensable gate, an adequate defense, and `accept` or `accept with conditions`. The source is public synthetic data and supports no real clinical, operational, population, trend, forecast, process-control, effect, or causal claim.

Module version: 0.1.0. Commons release: 0.36.0.
