# APP-4 Module 03 build plan

## Purpose

Build `oclc-app4-03`, Evidence, calibration, and validation, as a deterministic runnable release candidate at Module version `0.1.0` and Commons release `0.79.0`.

The module asks whether public historical evidence supports continued curriculum work on the fictional `CGH-GIM-01` advisory concept. It does not diagnose diabetes, establish local validity, accept a clinical threshold, score a real patient, display a clinical alert, authorize clinical action, implement, or deploy.

## Fixed analytic contract

- Development evidence: NHANES 2013-2014 and 2015-2016.
- Untuned temporal holdout: NHANES 2017-2018.
- Separate later-cycle transport stress test: NHANES August 2021-August 2023.
- Reference cohort: nonpregnant adults ages 35 through 70 with BMI at least 25, `DIQ010 = 2` for no self-reported diabetes, and observed HbA1c.
- Historical target: `LBXGH >= 6.5%`.
- Target meaning: an observed survey laboratory result at or above the declared cut point, not a diagnosis, confirmed disease, local event, treatment indication, or patient-level recommendation.
- Transparent model: survey-weighted binomial GLM with logit link and the predeclared terms age centered at 50 per 10 years, BMI centered at 30 per 5 kg/m2, and a female indicator.
- Audit-only field: race and Hispanic-origin category is excluded from the model and retained only for descriptive support review.
- Missingness: no imputation; each eligibility and complete-case exclusion remains counted.
- Development weight: `WTMEC2YR / 2` within the two pooled two-year cycles.
- Holdout weight: cycle-specific `WTMEC2YR`.
- Transport weight: cycle-specific `WTPH2YR`, required for the August 2021-August 2023 blood analyte.
- Design fields: `SDMVSTRA` and `SDMVPSU` remain attached to every analytic row.
- Candidate threshold set: `0.02`, `0.03`, `0.04`, `0.05`, `0.075`, and `0.10`.
- Module 02 value `0.20`: retained only as a rejected mechanics-fixture comparison and never promoted to an evidence candidate.
- Threshold decision: no candidate is clinically selected or accepted in Module 03.
- Uncertainty: deterministic stratified-PSU sensitivity bootstrap with 500 replicates and seed `7400303`, labeled as teaching evidence pending formal survey-methods review.

## Required evidence release

Build a complete derived release from all 16 pinned Module 01 XPT files. Preserve source hashes before parsing and release deterministic gzip files, exact tables, a machine-readable report, and an output manifest.

The release must include:

1. the complete joined audit frame for every age-eligible public participant;
2. the final model cohort and partition assignment;
3. cohort flow and missingness by cycle;
4. survey-design and weight treatment;
5. the fixed model coefficients and prediction rows;
6. weighted baseline and transparent-model performance;
7. calibration-in-the-large, calibration slope, and score-range calibration;
8. confusion, burden, and missed-case quantities for every candidate threshold;
9. decision-curve quantities under declared threshold odds;
10. temporal holdout and transport comparisons without unsupported causal explanations;
11. subgroup denominators, outcomes, missingness, support, uncertainty status, and suppression;
12. deterministic bootstrap intervals and invariant checks; and
13. exact accessible CSV alternatives for every analytic display concept.

## Learner and reference workspaces

Freeze the exact 73-file Module 02 immutable handoff. Add the Module 03 controls and evidence release as immutable files. Supply separate incomplete learner and complete reference versions of the assessed records.

Required assessed records:

- `evidence-release.md`;
- `cohort-target-contract.csv`;
- `survey-design-audit.csv`;
- `model-specification.csv`;
- `performance-interpretation.md`;
- `calibration-audit.csv`;
- `threshold-consequence-audit.csv`;
- `decision-curve-interpretation.md`;
- `transport-stress-audit.csv`;
- `subgroup-support-audit.csv`;
- `evidence-limitations.md`;
- `week3-component-release.md`;
- `claim-boundary.csv`;
- `ai-use.md`; and
- `progression-decision.md`.

## Noncompensable gates

1. Every inherited Module 01 and Module 02 source, control, logic, and authority identity remains unchanged.
2. All 16 public XPT sources pass their accepted byte and hash contract before parsing.
3. Eligibility, exclusion, target, predictor, partition, information-cutoff, and missingness rules are explicit and executable.
4. The HbA1c target is never described as a diagnosis or confirmed disease.
5. Development, temporal holdout, and transport partitions remain separate and no holdout or transport row affects fitting or tuning.
6. Weight, stratum, PSU, and the 2021-2023 phlebotomy-weight exception are explicit.
7. Calibration, threshold, burden, missed-case, net-benefit, and subgroup quantities reproduce from the accepted evidence.
8. The Module 02 `0.20` mock value remains a rejected mechanics fixture.
9. No threshold is selected or accepted by an agent or by code.
10. Unsupported subgroup metrics remain suppressed and no group-specific action is authorized.
11. AI use is disclosed and every agent-assisted output receives a deterministic independent check.
12. Progression concerns curriculum construction only and preserves every clinical-use, implementation, and deployment prohibition.

## Verification and release

1. Build the evidence release twice from the immutable XPT sources and require byte-identical output manifests.
2. Verify every committed evidence output against a clean rebuild.
3. Build two reference workspaces and require byte-identical immutable manifests.
4. Validate the complete reference and incomplete learner workspaces.
5. Reject mutated source bytes, changed evidence, copied reference answers, placeholders in complete work, missing records, holdout tuning, threshold acceptance, unsupported subgroup claims, diagnosis language, and live-use or deployment claims.
6. Write the durable 21-section module specification and protected Week 3 component handoff.
7. Advance Commons from `0.78.0` to `0.79.0`.
8. Run the complete curriculum regression.
9. Commit, push, and remote-verify Module 03 before building APP-4 Checkpoint 01.
