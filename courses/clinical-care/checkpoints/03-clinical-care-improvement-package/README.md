# APP-1 final checkpoint: Clinical care improvement package

This checkpoint freezes the complete 236-file Module 07 leadership candidate and records the final 35-point score, 24 gates, 12-question defense, reviewers, reproduction, conditions, package disposition, and separate clinical recommendation.

The official assigned half-term end date controls the due date:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

The reference package is `accept with conditions`. Its clinical recommendation is `revise before testing`. Clinical implementation, model deployment, and patient targeting remain prohibited.

## Build and validate

```powershell
python assemble_final.py --target <new-folder> --reference
python validate_final.py <new-folder>
python assemble_final.py --self-check
python validate_final.py --self-check
```

For learner review, assemble and validate a complete Module 07 candidate, then run:

```powershell
python assemble_final.py --candidate <module07-folder> --target <new-folder>
python validate_final.py <new-folder> --starter
```

The assembler refuses an existing target and a target inside the candidate. It copies accepted bytes and adds 15 files under `final-review/`.

## Durable specification

`docs/curriculum/courses/APP-1/checkpoints/03-clinical-care-improvement-package-spec.md`
