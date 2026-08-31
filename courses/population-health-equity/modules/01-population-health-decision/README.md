# APP-5 Module 01: Framing a population-health decision

- Module ID: `oclc-app5-01`.
- Module version: `0.1.0`.
- Commons release: `0.87.0`.
- Learner time: 15.5 hours.
- Course points: 0.
- Build status: runnable release candidate.

This module decides whether the fictional `FMA-DP-01` Massachusetts adult diabetes-prevention planning review is defined well enough to begin population-measure construction. It fixes the population, denominator roles, geography, time, public-source roles, community-review rights, accountable owners, and claim limits before anyone calculates a disparity, maps a rate, ranks a tract, chooses a targeting rule, or fits a model.

The public release contains every Massachusetts `DIABETES` row from CDC PLACES 2025, every Massachusetts census-tract row from ACS 2020-2024 Detailed Table B01001 after verification of the complete national table file, and the complete CDC/ATSDR SVI 2022 Massachusetts tract CSV.

| Source | Released rows | Released fields | Teaching role |
|---|---:|---:|---|
| PLACES 2025 Massachusetts diabetes tracts | 1,597 | 24 | Modeled adult diabetes prevalence, interval, and matching PLACES population fields |
| ACS 2020-2024 B01001 Massachusetts tracts | 1,620 | 100 | Population and age-by-sex denominator estimates and margins |
| SVI 2022 Massachusetts tracts | 1,613 | 158 | Area-level contextual estimates, margins, flags, themes, and relative ranks |

All 1,597 PLACES tracts appear in both ACS and SVI. SVI has 16 additional tracts without a PLACES diabetes row. ACS has seven additional tract records beyond SVI. These differences remain explicit.

PLACES is modeled small-area prevalence, not observed cases. ACS and SVI are area-level estimates, not individual traits. None of the sources establishes causation, program effectiveness, automatic eligibility, or allocation authority.

## Build and validate

Verify the committed releases and rebuild the exact profiles:

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

Source acquisition is explicit. It downloads and verifies the complete 200,356,282-byte national ACS B01001 file before replacing the Massachusetts tract extract. A source refresh requires review and a semantic-version decision:

```powershell
python .\profile_sources.py --acquire --temp-root D:\CodexTemp
```

## Reference decision

The reference progression is `continue with conditions`. Module 02 population-measure construction is permitted for curriculum construction only. The final synthetic event design, age bands, standard population, indirect-standardization method, disparity measures, suppression rules, geography review, and human reviewers remain open conditions.

Rate construction, standardization, disparity claims, maps, tract ranking, targeting, allocation, model fitting, intervention evaluation, real community action, implementation, and deployment remain prohibited in Module 01.
