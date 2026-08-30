# APP-2 final checkpoint: Patient-experience and engagement package

This checkpoint freezes the complete 358-file Module 07 candidate and records the final 35-point score, 26 gates, 14-question defense, reviewers, reproduction, conditions, package disposition, and separate organizational recommendation.

The official assigned half-term end date controls the due date:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

The reference package is `accept with conditions`. Its organizational recommendation is `revise before testing`. Contact, fielding, official HCAHPS reporting, targeting, clinical implementation, and model deployment remain prohibited.

## Build and validate

```powershell
python assemble_final.py --target <new-folder> --reference
python validate_final.py <new-folder>
python assemble_final.py --self-check
python validate_final.py --self-check
```

For learner review, validate and assemble a complete Module 07 candidate, then run:

```powershell
python assemble_final.py --candidate <module07-folder> --target <new-folder>
python validate_final.py <new-folder> --starter
```

The assembler refuses an existing target and a target inside the candidate. It copies accepted bytes and adds 15 files under `final-review/`.

## Durable specification

`docs/curriculum/courses/APP-2/checkpoints/03-patient-experience-engagement-package-spec.md`
