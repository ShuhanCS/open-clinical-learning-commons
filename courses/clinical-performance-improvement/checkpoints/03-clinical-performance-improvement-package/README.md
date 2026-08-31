# APP-3 Checkpoint 03: Clinical performance improvement package

- Checkpoint: `oclc-app3-cp03`
- Version: `0.1.0`
- Commons release: `0.75.0`
- Due: official last day of the assigned MGH Institute half-term
- Course points: `35`
- Required input: complete APP-3 Module 07 candidate version `0.1.0`
- Final package files: `431`
- Final candidate manifest: `416 rows`, `70,531 bytes`
- Final candidate manifest SHA-256: `b41acddef7397f9e55deee99f815b3d586d246f2353bbd92cf0873654499e8b6`
- Complete validation checks: `2,177`
- Learner validation checks: `2,131`
- Failure routes: `15`, plus complete-mode learner rejection

This final checkpoint freezes the exact Module 07 candidate, records the 35-point component once, and adjudicates the curriculum package separately from the clinical performance recommendation.

The reference disposition is `accept with conditions`. The clinical performance recommendation is `revise before testing`. Clinical action, staffing and schedule changes, automation, testing, implementation, production scoring, and model deployment remain prohibited.

Build a reference package:

```powershell
python assemble_final.py --target <new-target> --reference
python validate_final.py <new-target>
```

Build from a learner Module 07 candidate:

```powershell
python assemble_final.py --candidate <module07-candidate> --target <new-target>
python validate_final.py <new-target> --starter
```

The assembler refuses an existing target and a target inside the candidate. The annotated tag remains proposed and uncreated until named humans authorize the exact reviewed commit.
