# APP-4 Module 03: Evidence, calibration, and validation

- Module version: `0.1.0`
- Commons release: `0.79.0`
- Status: runnable release candidate
- Learner time: 16.5 hours
- Course points: 20 of the 40-point Week 3 checkpoint

## Decision

Does the historical evidence justify assembling the Week 3 release and continuing toward workflow evaluation under stated limits?

This module uses all 16 pinned NHANES public source files from Module 01 and the accepted logic boundary from Module 02. It creates a transparent historical classification model for the fictional `CGH-GIM-01` teaching case. It does not diagnose diabetes, establish local validity, accept a clinical threshold, score a real patient, display an alert, or authorize clinical use.

## Evidence release

The deterministic release contains:

- 14,892 public age-eligible audit rows;
- 7,544 final model rows and 328 observed HbA1c outcomes;
- 3,652 development rows with 156 outcomes from 2013-2016;
- 1,806 untouched temporal-holdout rows with 97 outcomes from 2017-2018;
- 2,086 separate transport-stress rows with 75 outcomes from 2021-2023;
- a fixed weighted logistic model using age, BMI, and a female indicator;
- weighted performance, calibration, six candidate-threshold audits, decision-curve quantities, subgroup support, transport comparisons, and 500-replicate stratified-PSU sensitivity intervals; and
- 17 immutable evidence files plus `evidence-manifest.csv`.

The temporal-holdout weighted ROC AUC is `0.68783144`; the later transport value is `0.68422573`. These are historical public-survey results, not evidence of local clinical usefulness.

## Threshold boundary

The evidence candidates are `0.02`, `0.03`, `0.04`, `0.05`, `0.075`, and `0.10`. None is selected or accepted. The Module 02 `0.20` value is retained only as a rejected mechanics-fixture comparison. Code and agents have no authority to select a clinical threshold.

## Rebuild and verify

From the repository root:

```powershell
python courses/clinical-decision-support/modules/03-evidence-calibration-validation/build_evidence.py --verify
python courses/clinical-decision-support/modules/03-evidence-calibration-validation/build_evidence.py --self-check
python courses/clinical-decision-support/modules/03-evidence-calibration-validation/build_workspace.py --self-check
python courses/clinical-decision-support/modules/03-evidence-calibration-validation/validate_workspace.py --self-check
```

The evidence builder verifies every inherited XPT byte and hash before parsing, refuses overwrite, produces byte-identical clean builds, and rejects a changed source.

## Official context

- NHANES weighting guidance: https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx
- NHANES 2021-2023 analytic overview: https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/OverviewBrief.aspx?Cycle=2021-2023
- NHANES 2021-2023 glycohemoglobin documentation: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/GHB_L.htm
- USPSTF screening recommendation: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/screening-for-prediabetes-and-type-2-diabetes
- NIDDK diabetes and prediabetes tests: https://www.niddk.nih.gov/health-information/professionals/clinical-tools-patient-management/diabetes/diabetes-prediabetes

The complete learner and reference packages contain 118 files each, including a 102-row immutable manifest and 15 assessed records. A passing reference package permits APP-4 Checkpoint 01 assembly with conditions. It does not yet permit Module 04 construction.
