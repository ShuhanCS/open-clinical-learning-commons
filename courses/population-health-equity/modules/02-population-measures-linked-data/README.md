# APP-5 Module 02: Population measures from linked data

- Module ID: `oclc-app5-02`.
- Module version: `0.1.0`.
- Commons release: `0.88.0`.
- Learner time: 16.0 hours.
- Course points: 20.
- Build status: runnable release candidate.

This module builds population measures for the fictional `FMA-DP-01` planning case. It freezes the complete accepted Module 01 reference package, keeps all public-source mismatches visible, derives five adult age-band denominators from ACS B01001, and links one clearly synthetic planning-need numerator.

The accepted release contains 7,985 tract-age denominator rows and 7,985 generated event rows across 1,597 matched Massachusetts tracts. The denominator total is 5,679,768, and the generated numerator totals 283,614 events. SQL builds crude, age-specific, directly standardized, and indirectly standardized measures. Python independently reproduces every result.

PLACES remains a separate modeled small-area prevalence source. It is never treated as observed cases or combined with the generated numerator.

## Build and validate

Verify the frozen handoff and synthetic source:

```powershell
python .\freeze_upstream.py --self-check
python .\generate_synthetic_events.py --self-check
```

Rebuild the accepted measure outputs:

```powershell
python .\build_measures.py --self-check
```

Build the learner workspace:

```powershell
python .\build_workspace.py --target .\learner-workspace
python .\validate_workspace.py .\learner-workspace --starter
```

Build the reference workspace:

```powershell
python .\build_workspace.py --target .\reference-workspace --reference
python .\validate_workspace.py .\reference-workspace
```

Run the protected failure checks:

```powershell
python .\validate_workspace.py --self-check
```

## Reference decision

The reference scores 20 of 20, passes all 15 gates, and records `continue with conditions`. Module 03 disparity and data-limit construction may begin for curriculum work only.

The module does not authorize a disparity claim, map, tract rank, targeting or allocation rule, model, intervention-effect estimate, real community action, implementation, or deployment.
