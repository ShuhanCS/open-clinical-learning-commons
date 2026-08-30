# APP-1 Module 07: Clinician leadership, recommendation, and defense

This 16-hour block turns the accepted APP-1 technical case into a clinical leadership recommendation, stakeholder and workflow plan, monitoring contract, and defense. Joe Joseph, MD, SFHM, is the designated clinician of record. The dated public biography and confirmation boundary are in `clinician-profile.md`.

The reference package recommends `revise before testing`. It does not authorize a clinical test, workflow change, patient targeting, or model deployment.

## Build and validate

```powershell
python assemble_candidate.py --target <new-folder> --reference
python validate_candidate.py <new-folder>
python assemble_candidate.py --self-check
python validate_candidate.py --self-check
```

For learner assembly, build and validate accepted Checkpoint 1 and Checkpoint 2 packages, then run:

```powershell
python assemble_candidate.py --checkpoint1 <week3-folder> --checkpoint2 <week6-folder> --target <new-folder>
python validate_candidate.py <new-folder> --starter
```

The assembler refuses an existing target. The candidate freezes both cumulative checkpoints and their release records in a 214-row immutable manifest. Leadership records remain editable until review.

## Durable specification

`docs/curriculum/courses/APP-1/modules/07-clinician-leadership-defense-spec.md`
