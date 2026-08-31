# APP-4 Module 01: Framing a decision support use case

- Module ID: `oclc-app4-01`.
- Module version: `0.1.0`.
- Commons release: `0.77.0`.
- Learner time: 15.5 hours.
- Course points: 0.
- Build status: runnable release candidate.

This module decides whether the fictional `CGH-GIM-01` advisory concept is defined well enough to begin logic and input specification. It fixes the user, workflow moment, intended action, nonaction, harm boundary, public and synthetic data roles, accountable owners, and open conditions before anyone fits a model or chooses a threshold.

The source release contains all 16 complete official NHANES XPT files for DEMO, BMX, DIQ, and GHB across 2013-2014, 2015-2016, 2017-2018, and 2021-2023. The raw XPT files total 34,221,200 bytes and 145,563 component rows. They are committed as 16 deterministic gzip files totaling 3,149,043 bytes. The field inventory has 442 rows, and all 16 files have unique `SEQN` values.

NHANES supplies historical survey evidence only. It does not describe the fictional service, establish local validity, represent workflow, or justify clinical use.

## Build and validate

Verify all committed source bytes and rebuild the exact profiles:

```powershell
python .\profile_sources.py
```

Build an incomplete learner workspace:

```powershell
python .\build_workspace.py --target .\learner-workspace
python .\validate_workspace.py .\learner-workspace --starter
```

Build and validate the reference workspace:

```powershell
python .\build_workspace.py --target .\reference-workspace --reference
python .\validate_workspace.py .\reference-workspace
```

Run the protected failure checks:

```powershell
python .\profile_sources.py --self-check
python .\build_workspace.py --self-check
python .\validate_workspace.py --self-check
```

Source acquisition is explicit and replaces the committed raw layer only when a new release has been reviewed and assigned a semantic version:

```powershell
python .\profile_sources.py --acquire
```

## Reference decision

The reference progression is `continue with conditions`. Module 02 logic and input construction is permitted for curriculum construction only. The clinical target, eligibility, exclusions, predictor list, units, terminology, threshold candidates, survey-weight treatment, synthetic generator details, and clinical wording still require named human review.

Model fitting, final target selection, threshold selection, alert firing, real-patient scoring, clinical action, implementation, and deployment remain prohibited.
