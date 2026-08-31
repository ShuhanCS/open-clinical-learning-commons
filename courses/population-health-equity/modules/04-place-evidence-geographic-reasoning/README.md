# APP-5 Module 04: Place-based evidence and geographic reasoning

## Decision

Can the accepted population evidence be communicated geographically without a wrong join, unstable support, ecological inference, inaccessible output, or language that treats a place or its residents as the problem?

## What learners produce

Learners verify the complete official 2024 TIGER/Line Massachusetts tract archive, freeze the accepted Week 3 checkpoint, reconcile 1,620 geometries with 1,597 accepted CDC PLACES modeled diabetes prevalence rows, preserve 23 unavailable tracts, compare tract and county aggregation, review small-area support, and submit one responsible accessible teaching map with an exact table, text alternative, and context memo.

The 10-point submission contributes once to the separate 25-point Week 6 checkpoint.

## Source and measure

- TIGER/Line release page: https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2024.html
- Massachusetts tract archive: https://www2.census.gov/geo/tiger/TIGER2024/TRACT/tl_2024_25_tract.zip
- Archive SHA-256: `74ca27e8dd9ed393e43b75e237ff7d652ef072e413532821847de58a7aa4bfd4`.
- Measure: CDC PLACES modeled crude adult diabetes prevalence.
- Measure year: 2023.
- Measure release: 2025 census-tract release.
- PLACES methodology: https://www.cdc.gov/places/methodology/index.html

TIGER supplies keys and boundaries. PLACES supplies modeled small-area estimates and intervals. Neither source supplies individual risk, community agreement, priority, eligibility, or authority to act.

## Quick start

From the repository root:

```powershell
python -m pip install -r courses/population-health-equity/modules/04-place-evidence-geographic-reasoning/requirements.txt
python courses/population-health-equity/modules/04-place-evidence-geographic-reasoning/acquire_geometry.py --verify
python courses/population-health-equity/modules/04-place-evidence-geographic-reasoning/freeze_upstream.py
python courses/population-health-equity/modules/04-place-evidence-geographic-reasoning/build_place_evidence.py --verify
python courses/population-health-equity/modules/04-place-evidence-geographic-reasoning/build_workspace.py --self-check
python courses/population-health-equity/modules/04-place-evidence-geographic-reasoning/validate_workspace.py --self-check
```

Build a learner workspace:

```powershell
python courses/population-health-equity/modules/04-place-evidence-geographic-reasoning/build_workspace.py --target app5-module04-learner
python courses/population-health-equity/modules/04-place-evidence-geographic-reasoning/validate_workspace.py app5-module04-learner --learner
```

Build a reference workspace:

```powershell
python courses/population-health-equity/modules/04-place-evidence-geographic-reasoning/build_workspace.py --target app5-module04-reference --reference
python courses/population-health-equity/modules/04-place-evidence-geographic-reasoning/validate_workspace.py app5-module04-reference
```

Builders refuse an existing target. Use a new empty destination for each build.

## Boundary

The reference release contains one responsible teaching map. It does not rank tracts, label a place as high need or vulnerable, choose a target, define eligibility, direct outreach, allocate funding, fit a model, estimate an intervention effect, represent community consent, implement a program, connect to production, or deploy. Module 05 may compare transparent fictional targeting rules only after Module 04 passes and is frozen.
