# APP-5 Module 02 build plan

## Purpose

Build `oclc-app5-02`, Population measures from linked data, as a deterministic 16-hour, 20-point release at Module version `0.1.0` and Commons release `0.88.0`.

The module turns the accepted Module 01 population, source, denominator, geography, time, community, and claim boundaries into executable population measures. It links the complete accepted Massachusetts tract releases, adds one clearly synthetic event layer for rate exercises, and produces crude, age-specific, directly standardized, and indirectly standardized measures. It does not make a disparity, place, targeting, allocation, intervention, or real-community claim.

## Frozen Module 01 handoff

`freeze_upstream.py` must build and validate the accepted Module 01 reference workspace, then copy it without editing into `upstream/module01-reference/`. The Module 02 handoff adds the accepted Module 01 `release.json` and a deterministic manifest for every frozen file.

The handoff must preserve:

- all 1,597 CDC PLACES diabetes tract rows;
- all 1,620 ACS B01001 Massachusetts tract rows;
- all 1,613 SVI Massachusetts tract rows;
- the 1,597-tract three-source intersection and 1,620-tract union;
- all ten accepted Module 01 decision records;
- the 16-row Module 01 immutable manifest;
- the Module 01 progression decision and conditions; and
- every prohibition on early analysis and real-world authority.

Any changed, missing, added, or renamed upstream file must fail validation.

## Synthetic event release

The synthetic source identity is fixed before results are inspected:

- Release: `fma-dp-01-measures-v1`.
- Generator: `generate_synthetic_events.py` version `0.1.0`.
- Seed: `73052`.
- Geography: all 1,597 tracts in the accepted PLACES, ACS, and SVI intersection.
- Period: fictional calendar year 2024.
- Age bands: 18-34, 35-49, 50-64, 65-74, and 75 years and older.
- Grain: one tract, age band, and period.
- Expected rows: 7,985.
- Numerator: a generated adult planning-need event used only to teach measure construction.

The generator derives age-band denominator structure from ACS B01001 and generates event counts from fixed age-specific probabilities plus a seeded fictional tract effect. It does not use PLACES prevalence, SVI values, real diagnoses, intervention outcomes, or community preference to generate the numerator. Every row carries the synthetic flag, seed, generator version, period, geography, denominator source, and claim limit.

The generated event is not a diabetes diagnosis, PLACES case, clinical eligibility result, patient record, local program observation, intervention outcome, or funding signal.

## Denominator and uncertainty contract

ACS 2020-2024 B01001 supplies five adult age-band denominator estimates for the 1,597 matched tracts. The age-band crosswalk names every male and female source cell used in each sum.

For a sum of ACS cells, the module approximates the 90 percent margin of error by taking the square root of the sum of squared margins for nonzero estimates and, when zero-estimate cells are present, adding only the largest zero-estimate margin. This follows the Census Bureau teaching guidance and records that the approximation omits covariance.

PLACES `totalpop18plus` remains attached to the modeled PLACES estimate. It is not substituted for the ACS denominator. Differences between the PLACES population field and the derived ACS adult denominator remain visible in reconciliation output.

## Measure contract

SQL owns source loading, tract-key joins, age-band denominator construction, event-to-denominator linkage, crude and age-specific rates, direct standardization, indirect expected counts, standardized event ratios, unmatched states, and reconciliation checks.

Python independently reproduces and verifies every accepted table. The rate multiplier is 100,000 throughout.

The release contains:

- a 1,620-row tract linkage audit that preserves all union tracts and source-presence states;
- five standard-population rows derived from the complete matched ACS adult population;
- 7,985 age-band denominator rows with ACS estimates and approximate 90 percent margins;
- 7,985 synthetic event rows;
- 7,985 age-specific rate rows with Wilson 95 percent intervals where denominators are positive;
- 1,597 crude and direct-standardization summaries;
- 1,597 indirect-standardization summaries; and
- separate public PLACES modeled-prevalence evidence that is never relabeled or combined with the synthetic numerator.

Direct standardization uses one declared standard age distribution across all matched tracts. A direct rate is unavailable when any age-band denominator is zero. A tract is marked for support review when any age-band denominator is below 50. The guided indirect exercise applies the complete synthetic statewide age-specific rates to each tract's age distribution. Its standardized event ratio is not comparable across tracts as though it were a directly standardized rate.

## Learner and reference records

The package will provide four SQL files and these assessed records:

- `population-measure-specifications.csv`;
- `age-band-and-moe-method.md`;
- `linkage-and-denominator-audit.md`;
- `standardization-interpretation.md`;
- `public-synthetic-separation.md`;
- `measure-score.csv`;
- `gate-results.csv`;
- `progression-decision.md`;
- `reproducibility-check.md`; and
- `ai-use.md`.

The learner workspace contains immutable controls, sources, and the frozen handoff, but no accepted answer outputs. The reference workspace adds accepted SQL, completed records, and deterministic outputs.

## Assessment and gates

The 20-point component has five four-point criteria:

1. population, age-band, numerator, denominator, and linkage logic;
2. crude and age-specific rate construction;
3. direct and indirect standardization;
4. uncertainty, support, unavailable states, and public-synthetic separation; and
5. reproducibility, interpretation, AI disclosure, and handoff quality.

Noncompensable gates require exact upstream and synthetic identities, complete joins, conserved denominators and events, explicit multipliers, declared standard weights, reproducible SQL and Python, no unavailable-to-zero conversion, no public-synthetic blending, no unsupported observed-case wording, and no authority beyond Module 03 curriculum construction.

## Verification and release

1. Freeze and verify the complete accepted Module 01 handoff twice.
2. Generate the synthetic source twice and require byte-identical files.
3. Execute the accepted SQL and independently verify every output with Python.
4. Build two reference workspaces and require identical manifests.
5. Build and validate the incomplete learner workspace.
6. Reject upstream mutation, source mutation, missing files, placeholder answers, changed SQL, bad scores, bad progression, public-synthetic blending, observed-case claims, tract ranking, targeting language, and personal paths.
7. Add the Module 02 specification, course and catalog status, build ledger handoff, and central curriculum checks.
8. Advance Commons from `0.87.0` to `0.88.0`.
9. Commit, push, and remote-verify the isolated Module 02 release before starting Module 03.
