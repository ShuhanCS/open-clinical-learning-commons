# APP-3 Module 07: Clinician leadership, recommendation, and defense

This 16-hour clinician-led block turns the accepted APP-3 technical and application evidence into a leadership recommendation, frontline and council communication, stewardship plan, ownership record, conditions, and defense.

The reference package is `accept with conditions`. Its separate clinical recommendation is `revise before testing`. No scenario, staffing change, schedule change, clinical action, automated action, test, implementation, production scoring, or model deployment is authorized.

Joe Joseph, MD, SFHM, is the designated clinician of record. The dated public biography and confirmation boundary are in `clinician-profile.md`.

## Build and validate

```powershell
python assemble_candidate.py --target <new-folder> --reference
python validate_candidate.py <new-folder>
python assemble_candidate.py --self-check
python validate_candidate.py --self-check
```

For learner assembly, first build and validate accepted Checkpoint 01 and Checkpoint 02 packages, then run:

```powershell
python assemble_candidate.py --checkpoint1 <week3-folder> --checkpoint2 <week6-folder> --target <new-folder>
python validate_candidate.py <new-folder> --starter
```

The assembler refuses an existing target. It freezes both complete checkpoints and both release records in a 389-row immutable manifest. The 26 leadership records remain editable until review.

## Durable specification

`docs/curriculum/courses/APP-3/modules/07-clinician-leadership-defense-spec.md`
