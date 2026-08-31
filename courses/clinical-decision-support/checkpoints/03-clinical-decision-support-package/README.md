# APP-4 Checkpoint 03: Clinical Decision Support package

- Checkpoint: `oclc-app4-cp03`
- Version: `0.1.0`
- Commons release: `0.86.0`
- Due: official last day of the assigned MGH Institute half-term
- Course points: `35`
- Required input: complete APP-4 Module 07 candidate version `0.1.0`
- Final package files: `1,362`
- Final candidate manifest: `1,347 rows`, `295,377 bytes`
- Final candidate manifest SHA-256: `217a64aad1cbaf5bde9fb2e9a1bd5325140b6a82f20541818b7e1cfd170d17b3`
- Complete validation checks: `6,817`
- Learner validation checks: `6,785`
- Failure routes: `20`, plus complete-mode learner rejection

This final checkpoint freezes the exact Module 07 candidate, records the 35-point component once, and adjudicates the curriculum package separately from the CDS recommendation.

The reference disposition is `accept with conditions`. The CDS recommendation is `revise before seeking local silent-mode approval`. No threshold is accepted. Real-patient scoring, clinical threshold acceptance, clinical alerting or action, silent-mode evaluation, implementation, production connection, and deployment remain prohibited.

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
