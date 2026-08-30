# Transparent versus ML response adjustment

- Population: `1,255 accepted frame records with 878 training and 377 evaluation rows`
- Held-out response: `235 respondents and 142 nonrespondents`
- Eligible fields: `age_band, other_language_at_home, and income_group for both methods`
- Transparent method: `training-only base-weighted response cells with factors from 1.0 through 3.0`
- ML method: `one bounded random forest with prespecified settings and training base weights`
- Transparent Brier score: `0.22962545`
- ML Brier score: `0.23135127`
- ML minus transparent Brier: `0.00172582`
- Transparent AUC: `0.54335192`
- ML AUC: `0.53869891`
- Transparent weighted teaching error cost: `227`
- ML weighted teaching error cost: `225`
- Transparent adjusted composite absolute bias: `2.48289986 percentage points`
- ML adjusted composite absolute bias: `2.39922466 percentage points`
- Composite improvement: `0.08367520 percentage points`
- Weight stability: `both pass`
- Decision: `ML does not change the response-adjustment decision because the composite improvement is below 0.50 percentage points`

The small error-cost advantage does not override the prespecified rule or the worse Brier and AUC values. The transparent benchmark remains the teaching adjustment. Neither method repairs item nonresponse or omitted selection fields, and neither may be used for patient targeting.
