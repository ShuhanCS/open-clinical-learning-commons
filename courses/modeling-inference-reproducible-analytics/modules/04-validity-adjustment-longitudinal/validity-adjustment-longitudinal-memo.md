# Validity, adjustment, and longitudinal memo

## Recommendation

Continue with conditions. Module 05 may use its distinct public time series, but no condition in this memo becomes a clinical-use approval.

## Adjustment evidence

The generated 600-person treatment case has a known average effect of -6.00000000 symptom-score points. Confounding by indication makes the unadjusted estimate only -1.27214587. The full-data IPTW audit is -6.10110832, and every weighted absolute standardized difference is below 0.10. This shows the bounded method recovering a known generated contrast; it does not prove adequate control of confounding in real care.

The observed analysis has 91 missing baseline-severity values. Complete-case IPTW uses 509 people and estimates -6.17942841. Median plus a missingness indicator estimates -5.62153010; low and high delta variants are -5.62177960 and -5.62199963. The narrow delta movement is a feature of this generator, not general reassurance about MNAR bias. The MAR statement remains an assumption outside the known generator.

## Selection evidence

The Synthea timing analysis selects 111 of 374 people because a next encounter is recorded. The 263 structural blanks are not zero-day waits. Selected and nonselected groups differ most visibly for 90-day acute return, medication count, and age. Therefore the recorded-timing regression remains a conditional 111-row description, not a full-cohort time-to-event result.

## Repeated evidence

The repeated case has 2,400 rows but 600 people. The estimated person-level residual variance is 46.82601084, residual variance is 9.18680087, and the intraclass correlation is 0.83598751. The naive, cluster-robust, and random-intercept fits share point estimates under this balanced generator but not standard errors. The treatment-by-week estimate is -0.23518501 per week in all three readings; its uncertainty must respect person clustering.

## Survival evidence

The survival case has 449 events and 151 censored observations. The Kaplan-Meier table keeps censored people in each risk set until censoring. The Cox treatment hazard ratio is 0.67945425 with a 95% interval from 0.55144790 to 0.83717443. It is a conditional synthetic hazard ratio, not a risk ratio, survival probability, clinical effect, or causal effect.

## Boundary

The four cases answer different questions and must not be fused into one result. Specialist review is required for unmeasured confounding, poor real-world overlap, consequential missingness assumptions, complex correlation, informative censoring, competing risks, or clinical interpretation.
