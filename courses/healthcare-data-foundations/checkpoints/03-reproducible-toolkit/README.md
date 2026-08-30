# FND-1 Final checkpoint: Reproducible healthcare data toolkit

This package freezes and reviews the complete FND-1 Module 07 toolkit. It copies the accepted 90-file candidate without changing a byte, writes a 90-row candidate manifest, and adds ten final-review files. The result is an exact 100-file submission.

The checkpoint decides whether the technical synthetic-data foundation may pass to FND-2 under its recorded conditions. It does not recalculate the cohort, quality evidence, descriptive results, or figures.

## Assemble from learner work

```powershell
python assemble_checkpoint.py --toolkit <accepted-module-07-toolkit> --target <new-final-folder>
```

The target must not exist. The assembler runs Module 07 complete validation before it copies anything. Complete every `REPLACE` prompt in `final-review/` and leave the 90 candidate files unchanged.

## Assemble the instructor reference

```powershell
python assemble_checkpoint.py --reference --target <new-reference-folder>
```

Reference mode builds the released Module 07 fixture first. Its accepting disposition is a technical teaching example with open conditions. It does not claim named human approval or create the learner's final tag.

## Validate

```powershell
python validate_checkpoint.py <final-folder>
```

During review drafting, starter mode permits placeholders only in the eight final-review records:

```powershell
python validate_checkpoint.py <final-folder> --starter
```

Test the package itself with:

```powershell
python assemble_checkpoint.py --self-check
python validate_checkpoint.py --self-check
```

## Final review

The final-review folder contains the candidate manifest, eight learner and reviewer records, and the checkpoint version. Passing requires at least 28.00 of 35.00 points, at least 4.80 of 6.00 defense points, all 20 gates, and `accept` or `accept with conditions` with explicit FND-2 progression.

Create the annotated tag `fnd1-toolkit-v0.1.0` only after the decision owner authorizes it. The tag must point to the exact reviewed 100-file commit.

The source is public synthetic data. This release supports technical education and method development. It does not authorize real-patient use, production deployment, clinical approval, or real-world clinical or causal claims.

Checkpoint version: 0.1.0. Commons release: 0.37.0.
