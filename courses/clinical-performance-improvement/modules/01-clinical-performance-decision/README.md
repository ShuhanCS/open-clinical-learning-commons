# APP-3 Module 01: Framing a clinical performance and improvement decision

- Module ID: `oclc-app3-01`.
- Version: `0.1.0`.
- Commons release: `0.66.0`.
- Duration: 15.5 hours.
- Status: runnable release candidate.
- Course points awarded here: 0.

This module fixes the decision before learners calculate a rate, diagnose a bottleneck, or propose a staffing change. Learners define the fictional `CGH-ED-01` service, one synthetic adult emergency encounter as the unit of flow, the process boundary, the measure families, the evidence roles, the people accountable for action, and the claims the available evidence can support.

## Public sources

The package preserves two complete CMS hospital releases and one reproducible extract from a complete inspected HHS capacity release:

- CMS Timely and Effective Care: https://data.cms.gov/provider-data/dataset/yv7e-xc69
- CMS Complications and Deaths: https://data.cms.gov/provider-data/dataset/ynj2-r877
- HHS historical facility capacity: https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/anag-cw7u

Public aggregate records provide measure definitions and context. They are not local `CGH-ED-01` observations and cannot establish a current bottleneck, cause, staffing need, safety event, or intervention effect.

## Build and validate

From this directory:

```powershell
python build_workspace.py --target "$env:TEMP\app3-module01-reference" --reference
python validate_workspace.py "$env:TEMP\app3-module01-reference"
python profile_sources.py --self-check
python build_workspace.py --self-check
python validate_workspace.py --self-check
```

The builder refuses to overwrite an existing target. Use learner mode by omitting `--reference`; the resulting records contain explicit `REPLACE` markers.

To reproduce the pinned artifacts from all three complete source CSVs:

```powershell
python profile_sources.py --timely-csv "<path-to-complete-timely-csv>" --complications-csv "<path-to-complete-complications-csv>" --capacity-csv "<path-to-complete-capacity-csv>" --write
```

The durable instructional contract is [the Module 01 specification](../../../../docs/curriculum/courses/APP-3/modules/01-clinical-performance-decision-spec.md).
