# Evidence limitations

1. NHANES is a national cross-sectional public survey, not the fictional `CGH-GIM-01` service or a local prospective cohort.
2. The cohort mirrors one screening recommendation for teaching. It does not encode symptoms, earlier-age risk routes, the lower BMI consideration for Asian American adults, local access, preference, contraindications, or every clinically relevant exception.
3. `DIQ010 = 2` is self-reported history, not a verified local problem list.
4. BMI and HbA1c come from the survey examination context. NHANES does not prove that BMI would be available before a local advisory decision.
5. `LBXGH >= 6.5%` is one observed laboratory result. It is not diagnosis or confirmed disease and may be affected by conditions not represented in the four-file source.
6. Complete-case analysis excludes missing BMI, HbA1c, history, pregnancy, or design information without imputation. Excluded people may differ from analyzed people.
7. Survey weighting supports historical population-oriented point estimates but does not turn this into local model validation.
8. The deterministic stratified-PSU bootstrap is a teaching sensitivity method. A named survey-methods reviewer must confirm any publication-grade variance approach.
9. The simple fixed model may omit nonlinear relations, interactions, clinical context, access factors, or predictors that matter. Complexity is not added in this module because Module 06 owns the fixed ML challenger.
10. Similar AUC values do not prove stable calibration, utility, safety, fairness, or transport.
11. Subgroup rows are descriptive support checks. Many performance cells are suppressed, and none authorizes a group-specific threshold or action.
12. Decision-curve values depend on hypothetical threshold odds and do not establish real benefits, harms, preferences, capacity, or costs.
13. No threshold is selected or accepted. Workflow burden, patient consequences, human factors, safety, governance, and prospective evidence remain unresolved.

These limitations support `continue with conditions` for curriculum construction. They do not authorize clinical use.
