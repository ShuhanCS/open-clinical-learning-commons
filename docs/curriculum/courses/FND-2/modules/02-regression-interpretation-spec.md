# FND-2 Module 02: Regression models and interpretation

## 1. Module identity and place in the course

- Course: FND-2, Modeling, Inference, and Reproducible Analytics.
- Course role: second straight-through technical foundation after FND-1.
- Module: 02 of 07.
- Source week: 2.
- Learner work: 16.0 hours.
- Course credits: 3.
- Prerequisite: accepted FND-2 Module 01 state.
- Module ID: `oclc-fnd2-02`.
- Module version: 0.1.0.
- Commons release: 0.40.0.
- Status: runnable release candidate; required human reviews pending.
- Week 3 assessment share: 10 of the 25 regression-and-prediction course points.
- Package: `courses/modeling-inference-reproducible-analytics/modules/02-regression-interpretation/`.
- Required learner tag: `fnd2-regression-v0.1.0`.
- Decision owner: biostatistical methods reviewer.
- Primary tools: Python, NumPy, pandas, SciPy, statsmodels, supplied base-R script, Git, CSV, JSON, and Markdown.

Module 02 teaches learners to fit and interpret bounded regression models without letting software output change the question, scale, fitting population, or causal boundary. It uses one continuous conditional outcome and one binary outcome. Each model begins with a declared formula, model matrix, reference level, fitting partition, uncertainty method, and interpretation unit.

The module has one release question:

> Are the fitted regression evidence, diagnostics, uncertainty, and interpretation accurate enough to enter prediction evaluation?

The decision concerns analytic evidence and handoff. It does not decide that a coefficient is important, a relationship is causal, a model predicts well, or a tool should be used clinically.

### Relationship to Module 01

Module 01 owns the analytic aim, unit, prediction time, feature roles, temporal split, and training-prevalence baseline. Module 02 inherits these artifacts exactly. It does not reopen the 374-row cohort, the 224/75/75 split, the 25/7/4 outcome counts, or the nine-field permission boundary.

Module 02 further restricts use. An allowed field does not have to appear in a small teaching formula. A field can be available at prediction time and still be omitted because of sparse categories, high dimensionality, unstable estimates, or the narrow teaching purpose.

### Relationship to Module 03

Module 03 evaluates prediction. It receives the bounded `LOG01` formula, transform definitions, training evidence, assumptions, sparse-cell warnings, and the unchanged Module 01 baseline and split.

Module 03 does not grade a coefficient again. It asks whether a locked pipeline beats the baseline and holds up on validation and test evidence. Statistical significance in Module 02 is neither necessary nor sufficient for predictive value.

### Relationship to Checkpoint 1

Module 02 contributes 10 course points. Module 03 contributes 15 course points. Together they form the 25-point regression-and-prediction component. Module 01's accepted 15-point component is also assembled at Week 3, producing the cumulative 40-point checkpoint.

### Required starting state

The learner begins with:

- Module 01 version 0.1.0;
- accepted or accepted-with-conditions progression;
- exact 374-row and 34-field modeling cohort;
- exact split registry;
- exact training-prevalence baseline;
- exact 34-row field-role contract;
- a working pinned scientific Python environment;
- a supported R environment for paired reading or a scheduled managed R route; and
- no real patient data or restricted clinical material in the public workspace.

### Required ending state

The learner release must:

- preserve every Module 01 input fingerprint;
- declare all formulas before fitting;
- use training data only;
- keep all 263 structural timing blanks as blanks;
- fit the linear case on exactly 69 training rows;
- fit logistic models on exactly 224 training rows and 25 outcomes;
- record reference levels, transformations, and model-matrix columns;
- report classical and HC3 uncertainty;
- report residual, variance, influence, convergence, sparsity, and extreme-probability evidence;
- distinguish log odds, odds ratios, risks, and predicted probabilities;
- fit one nonlinear and one interaction example without using test evidence;
- interpret p-values and intervals without importance or causal substitution;
- run and reconcile the supplied R base models within tolerance;
- reproduce every deterministic output;
- pass submission validation; and
- issue an allowed Module 03 progression disposition.

## 2. Technical decision, owner, and audiences

### Decision owner

The decision owner is a biostatistical methods reviewer. The reviewer must understand linear and generalized linear models, model matrices, reference coding, uncertainty, diagnostics, sparse-data behavior, and the difference between association and causal effect.

The reviewer may use automated checks and specialist input. The human reviewer remains accountable for the final disposition.

### Technical decision

The reviewer decides whether the learner has produced regression evidence whose:

- fitting population matches the question;
- formulas and encodings are explicit;
- estimates are numerically reproducible;
- uncertainty methods are named;
- diagnostics expose rather than hide instability;
- quantities are interpreted on the correct scale;
- selected conditional sample is visible;
- sparse categories and influential rows remain visible;
- Python and R reading agree within tolerance;
- causal and population boundaries are respected; and
- handoff preserves the exact prediction contract.

### What the decision does not approve

Acceptance does not mean:

- `LIN01` estimates time to next encounter for all 374 people;
- a nominal p-value proves clinical importance;
- an odds ratio is a risk ratio;
- a coefficient is an individual probability change;
- adjustment identifies a causal effect;
- model assumptions are proven;
- convergence establishes correct specification;
- training fit establishes predictive performance;
- Python and R agreement establishes scientific validity;
- the synthetic cohort represents real patients; or
- `LOG01` should be deployed.

### Allowed dispositions

| Disposition | Meaning | Next action |
|---|---|---|
| `accept` | All gates pass and no material regression condition remains. | Freeze the evidence and begin Module 03. |
| `accept with conditions` | All gates pass but bounded diagnostic, sparsity, R, source, or interpretation conditions remain. | Name conditions and owners; freeze the evidence and begin Module 03 under those limits. |
| `revise` | A correctable fit, formula, encoding, quantity, uncertainty, diagnostic, reproduction, or interpretation defect blocks handoff. | Correct, rebuild, revalidate, and resubmit. |
| `refer` | Protected data, unauthorized access, integrity concerns, or a causal or clinical decision outside reviewer authority is present. | Stop reuse and refer to the proper process. |

Only `accept` and `accept with conditions` permit Module 03 progression.

### Primary learner audience

The learner is a clinician, researcher, quality professional, analyst, or health-system staff member who has completed FND-1 and FND-2 Module 01. The learner can work with a reproducible data package but may still associate regression with a single software table of coefficients.

This module assumes no prior mastery of:

- matrix-based formula encoding;
- reference levels;
- linear regression assumptions;
- logistic link functions;
- odds and odds ratios;
- robust variance estimates;
- influence measures;
- separation and sparse-data warnings;
- nonlinear terms;
- interactions;
- scenario prediction uncertainty; or
- cross-language reconciliation.

### Review audiences

The release must also be legible to:

- the Week 3 scoring instructor;
- a teaching assistant diagnosing a formula or interpretation error;
- a clinical informatics reviewer checking encounter meaning;
- a Python reviewer checking statsmodels execution;
- an R reviewer checking paired output;
- a reproducibility reviewer checking fingerprints and environment;
- a privacy reviewer checking data scope;
- a responsible-AI reviewer checking disclosure and verification;
- an accessibility reviewer checking text and table routes; and
- the Module 03 prediction reviewer inheriting `LOG01`.

### Evidence classes

The decision uses:

1. immutable upstream evidence;
2. formula, reference, and model-matrix evidence;
3. coefficient and uncertainty evidence;
4. residual, influence, convergence, and sparsity evidence;
5. nonlinear and interaction comparison evidence;
6. quantity-correct interpretation;
7. Python and R reconciliation;
8. reproducibility and validator evidence; and
9. progression and accountability records.

### Oral clarification route

When understanding is unclear, ask the learner to:

- interpret one linear coefficient in days;
- interpret one logistic coefficient on the log-odds scale;
- translate that coefficient to an odds ratio without calling it risk;
- compare two scenario probabilities;
- identify the reference category and age center;
- explain why a structural blank is not zero;
- explain one influence finding;
- compute the inpatient interaction slope from two terms;
- explain why test data cannot improve the coefficient story; and
- identify one statement that would require causal design evidence.

## 3. Foundation skill and exact handoff

### Foundation skill

The learner connects a declared statistical model to the quantity actually estimated. This requires more than running `fit()`. The learner must keep the population, sample, model matrix, scale, reference, uncertainty, assumption, and claim boundary aligned.

The foundation skill has ten habits:

1. write the formula before fitting;
2. name the fitting partition;
3. define every encoded column;
4. identify the outcome scale and link;
5. report estimate and uncertainty together;
6. inspect residual, influence, sparsity, and convergence evidence;
7. interpret nonlinear and interaction terms as formula-dependent quantities;
8. distinguish statistical evidence from practical relevance;
9. stop associational language before causation; and
10. reproduce the result across tools without confusing agreement with truth.

### Why this belongs in FND-2

Every later applied course will revisit regression through a different clinical, operational, research, population, or financial problem. This foundation course owns the common discipline: what the coefficient means, what assumptions make it interpretable, what diagnostics can reveal, and what the analysis cannot claim.

### Upstream input contract

| Input | Bytes | SHA-256 |
|---|---:|---|
| modeling cohort | 138503 | `6556ed149e69589253ab58572b2f08535899ae12c3e84dc7bafc7da2ebe6f332` |
| split registry | 51910 | `05ea7ed9f37b20ba9cba4bb2a36d4c95af96cd2f8e5cc82a5bc8eb74c91474c1` |
| baseline | 306 | `613651013e397beeadc84b17482026ca7cb4674abf61bf521699d79af0a3c9af` |
| feature-role contract | 3766 | `599f29ca612cb5f23aed277c56937af78c488ba952c2926faa94166f33449c83` |

Any mismatch stops the model build.

### Exact Module 03 handoff

Module 03 receives:

- Module 01 modeling cohort, split registry, feature roles, and baseline;
- Module 02 version and disposition;
- `LOG01` formula;
- training mean age and transform definition;
- emergency reference level;
- exact model-matrix field list;
- coefficient and uncertainty tables;
- logistic diagnostic table;
- sparse-cell checks;
- assumption register;
- nonlinear and interaction comparison evidence;
- scenario probability examples;
- Python/R reconciliation record;
- reproducibility record;
- AI-use record; and
- every unresolved condition.

### Return conditions

Return to Module 02 when any of the following changes:

- outcome;
- fitting population or partition;
- formula or included term;
- reference level;
- centering or transformation;
- model family or link;
- variance estimator;
- interval method;
- sparse-category handling;
- interpretation quantity;
- R implementation; or
- material diagnostic disposition.

Return to Module 01 when the aim, prediction time, feature permission, source, grain, split, or baseline changes.

## 4. Assessable outcomes and evidence map

By the end of Module 02, the learner can:

1. write a linear or logistic formula before fitting;
2. identify outcome, predictors, reference category, and fitting partition;
3. construct and inspect a model matrix;
4. explain the intercept under the declared references;
5. distinguish a source field from a transformed model term;
6. fit ordinary least squares on the exact conditional training subset;
7. explain why 263 timing blanks are structural rather than zero;
8. interpret a linear coefficient as a conditional mean difference in days;
9. report classical t-based and HC3 uncertainty;
10. distinguish a confidence interval for a mean from a prediction interval for a new outcome;
11. inspect residual distribution, variance, influence, leverage, and conditioning evidence;
12. retain supported extreme rows unless a defensible data error exists;
13. fit a binomial logistic model on exact training rows;
14. interpret a logistic coefficient on the log-odds scale;
15. exponentiate a coefficient to an odds ratio;
16. distinguish odds ratio, risk ratio, probability change, and predicted probability;
17. calculate scenario probabilities under a declared model;
18. report model-based and HC3 uncertainty;
19. inspect convergence, extreme fitted probabilities, influence, leverage, and model conditioning;
20. identify sparse or absent categorical cells before fitting category effects;
21. explain why convergence does not rule out separation or misspecification;
22. add a centered squared term and explain why the age slope changes with age;
23. add one interaction and calculate the reference and combined slopes;
24. interpret a training likelihood-ratio comparison without calling it predictive performance;
25. distinguish statistical evidence from practical or decision relevance;
26. state that regression adjustment alone does not establish a causal effect;
27. run the supplied R script;
28. reconcile R and Python estimates within 0.000001;
29. document environment, reproduction, AI use, and unresolved conditions; and
30. make an allowed Module 03 progression decision.

### Outcome-to-evidence map

| Outcome area | Direct evidence | Supporting evidence |
|---|---|---|
| Formula declaration | `formula-registry.csv` | model-matrix table |
| References and transforms | `reference-levels.csv` | build report age center |
| Linear fit | linear coefficient and prediction tables | linear diagnostics |
| Logistic fit | logistic coefficient and scenario tables | logistic diagnostics |
| Nonlinear and interaction terms | comparison and coefficient tables | interpretation narrative |
| Sparse data | sparse-cell table | assumption register |
| Quantity language | interpretation guide and narrative | oral check |
| R reading | R output and run record | numeric fixture |
| Reproducibility | protected builder and validator | clean-target record |
| Handoff | progression decision | release metadata |

### Minimum explanation standard

Every coefficient interpretation must contain:

- fitted model ID;
- fitting population;
- outcome and scale;
- predictor change and unit;
- reference level when applicable;
- variables conditioned on;
- estimate and uncertainty;
- statistical method boundary; and
- unsupported causal or population claim.

"Significant" or "not significant" alone is never a complete interpretation.

## 5. Concept ownership and out-of-scope boundaries

### Module 02 owns

- declared regression formulas;
- model matrices and feature-name records;
- intercept and reference interpretation;
- ordinary least squares;
- conditional mean coefficients;
- residual and influence diagnostics;
- classical and HC3 linear uncertainty;
- linear mean confidence intervals;
- linear new-observation prediction intervals;
- binomial logistic regression;
- log odds and odds ratios;
- model-conditional predicted probabilities;
- model-based and HC3 logistic uncertainty;
- convergence and extreme-probability review;
- sparse-cell review;
- one bounded nonlinear term;
- one bounded interaction;
- nested training likelihood-ratio comparison;
- p-value and interval interpretation;
- association versus causation boundary;
- paired R reading and numeric reconciliation; and
- Module 03 formula handoff.

### Module 02 introduces but does not own

- calibration;
- discrimination;
- classification thresholds;
- resampling;
- regularization;
- machine-learning comparison;
- validation-based selection;
- test evaluation;
- subgroup performance; and
- deployment utility.

These belong to Module 03.

### Module 02 does not own

- source cohort revision;
- imputation development;
- causal identification;
- propensity scores;
- time-to-event analysis;
- competing risks;
- repeated-measures modeling;
- forecasting;
- automated model selection;
- a full theory of robust or clustered variance;
- penalized separation correction;
- clinical decision support;
- model cards or monitoring; or
- visual-design competence.

### Separation from causal inference

An adjusted coefficient remains associational unless a defensible causal question, design, identification strategy, time order, and assumptions support a counterfactual contrast. The phrase "controlling for" does not grant causal meaning.

### Separation from survival analysis

`LIN01` conditions on a recorded different encounter within 30 days. It does not include censoring, people without an event, or a hazard. It cannot be relabeled as time to event for the full cohort.

### Separation from prediction evaluation

Training likelihood, AIC, coefficient p-values, and R-squared describe in-sample fitted evidence. They do not establish performance on validation or test rows. Module 03 owns that decision.

## 6. Lesson sequence and learner time

| Sequence | Learning activity | Hours | Required evidence |
|---:|---|---:|---|
| 1 | Module 01 handoff and fingerprint verification | 0.50 | exact upstream check |
| 2 | Formula, outcome, and model-matrix declaration | 0.50 | formula and reference registries |
| 3 | Linear regression concept and fit | 1.50 | `LIN01` coefficient table |
| 4 | Conditional-sample and structural-blank lab | 0.75 | 111/69/263 reconciliation |
| 5 | Linear uncertainty and scenario intervals | 1.25 | classical, HC3, mean, and prediction intervals |
| 6 | Linear residual and influence lab | 1.50 | diagnostic and assumption records |
| 7 | Logistic link, odds, and probability workshop | 1.50 | quantity translation exercises |
| 8 | `LOG01` fit and scenario probabilities | 1.50 | coefficient and probability tables |
| 9 | Logistic convergence, influence, and sparse-data lab | 1.25 | diagnostics and sparse-cell checks |
| 10 | Nonlinear centered-age term | 0.75 | `LOG02` interpretation |
| 11 | Prior-acute by index-class interaction | 0.75 | `LOG03` interpretation |
| 12 | Statistical evidence and practical meaning | 0.75 | supported and unsupported statements |
| 13 | Paired R reading and reconciliation | 1.50 | R run record and comparison |
| 14 | Clean reproduction, validation, and defense | 2.00 | passing package and progression decision |
| Total |  | 16.00 |  |

### Within-week gates

| Gate point | Evidence | Stop condition |
|---|---|---|
| Before fit | formulas, references, and partition declared | silent or data-driven formula |
| After linear subset | 111/69/21/21/263 reconciled | blank-to-zero or nontrain fit row |
| After `LIN01` | coefficient and diagnostic quantities named | causal or full-cohort timing language |
| After `LOG01` | 224 rows, 25 events, log-odds and odds quantities | risk or probability substitution |
| After added terms | changed interpretation documented | training comparison called prediction selection |
| Before release | R, reproduction, and disposition records complete | unresolved difference or missing condition |

## 7. Statistical model contracts

### Shared rules

Every model:

- uses training data only;
- uses Module 01 allowed fields or registered transforms;
- has an explicit outcome;
- has an explicit intercept;
- records reference levels;
- records model-matrix order;
- reports the fitting row and outcome count;
- reports estimate and uncertainty together;
- reports diagnostics appropriate to the family;
- preserves sparse and influential evidence;
- uses associational language; and
- supports synthetic teaching claims only.

### `LIN01` contract

Fitting population: training rows with nonblank `next_30d_days_after_index_stop`.

Rows: 69.

Formula:

```text
next_30d_days_after_index_stop = intercept
  + age_at_index
  + prior_365d_encounter_count
  + index_class_inpatient
```

Reference: emergency index class.

Outcome unit: days.

Primary interpretation: conditional mean difference among training people with a recorded different encounter within 30 days.

### `LOG01` contract

Fitting population: all 224 training rows.

Positive outcomes: 25.

Formula:

```text
logit(P(acute_return_90d = 1)) = intercept
  + age_centered_decade
  + prior_365d_acute_count
  + index_class_inpatient
```

Age center: 46.245535714286 training years.

Reference: emergency index class and outcome zero.

Primary interpretation: conditional change in log odds or odds under the declared formula.

### `LOG02` contract

`LOG02` adds:

```text
age_centered_decade_sq
```

The age log-odds slope at centered age `a` is:

```text
beta_age + 2 * beta_age_squared * a
```

There is no single age odds ratio that applies at all ages.

### `LOG03` contract

`LOG03` adds:

```text
prior_365d_acute_count * index_class_inpatient
```

The prior-acute log-odds slope is:

- emergency: `beta_prior_acute`;
- inpatient: `beta_prior_acute + beta_interaction`.

The index-class coefficient is the inpatient-versus-emergency contrast when prior acute count is zero.

### Handoff selection rule

`LOG01` is the declared bounded handoff formula because it is the predeclared simple model. `LOG02` and `LOG03` teach interpretation changes. Their training AIC and likelihood-ratio p-values do not determine Module 03 selection.

## 8. Linear regression worked case

### Conditional outcome selection

The accepted modeling cohort contains 374 rows. `next_30d_days_after_index_stop` is nonblank for 111 rows and blank for 263 rows.

The 111 available timing rows are distributed as:

| Split | Available timing rows | Fit use in Module 02 |
|---|---:|---|
| Train | 69 | fit and interpretation |
| Validation | 21 | not used |
| Test | 21 | not used |
| Total | 111 | 69 fit |

The linear case conditions on having a recorded different encounter within 30 days. The selection condition must appear in every table and interpretation.

### Why blank is not zero

A zero-day value would mean a next encounter occurred at the prediction-time origin. A blank means no different encounter timing was recorded under the 30-day source definition. Replacing blank with zero would invent 263 immediate encounters and change the outcome, population, distribution, coefficients, and scientific question.

The learner must reject:

- zero fill;
- mean imputation;
- complete-cohort OLS after artificial fill;
- interpreting excluded rows as censored without a survival model; and
- describing the selected estimate as time to encounter for all people.

### Model matrix

`LIN01` has four columns in this order:

1. `const`;
2. `age_at_index`;
3. `prior_365d_encounter_count`; and
4. `index_class_inpatient`.

Emergency is the reference. The intercept represents expected recorded next-encounter days when age and prior encounter count equal zero for an emergency index. That combination is not the main substantive target, so the intercept is primarily a model anchor.

### Reference coefficient results

| Term | Estimate | Classical SE | Classical 95% interval | Classical p-value |
|---|---:|---:|---|---:|
| Intercept | 18.19672324 | 3.47264894 | 11.26136440 to 25.13208208 | 0.00000186 |
| Age in years | 0.00303591 | 0.06725466 | -0.13128091 to 0.13735274 | 0.96413366 |
| Prior encounter count | -0.10110471 | 0.04938821 | -0.19973978 to -0.00246963 | 0.04469060 |
| Inpatient versus emergency | -3.42865028 | 3.41679847 | -10.25246804 to 3.39516747 | 0.31935586 |

### Quantity-correct interpretation

Under the declared additive model among the 69 selected training rows, one additional prior encounter row is associated with an estimated 0.101-day lower conditional mean time to the recorded next encounter, holding age and index class fixed.

The estimate does not mean:

- an encounter causes the next encounter to happen earlier;
- an individual will return 0.101 days earlier;
- the association applies to people without a recorded next encounter;
- the effect is clinically important because p is below 0.05; or
- the synthetic estimate applies to real patients.

### Model fit and residual evidence

| Metric | Value | Interpretation |
|---|---:|---|
| R-squared | 0.07951657 | in-sample variance summary; not predictive performance |
| Adjusted R-squared | 0.03703272 | penalized in-sample summary |
| RMSE | 10.40449778 days | training residual scale |
| Residual mean | approximately 0 | expected OLS algebra result with intercept |
| Jarque-Bera p-value | 0.04655734 | normal-error approximation requires review |
| Breusch-Pagan p-value | 0.14825876 | no strong test evidence against constant variance; not proof |
| Durbin-Watson | 1.51073136 | ordered residual dependence remains a review item |
| Condition number | 157.99534422 | scale and conditioning require interpretation |

### Influence evidence

Maximum Cook distance is 0.07408089. The 4/n review threshold is 0.05797101. Maximum leverage is 0.58620136, above the 2p/n threshold of 0.11594203.

These thresholds prompt inspection. They do not authorize automatic deletion. Learners must identify whether a row is a source error, a supported extreme, a sparse design point, or a case that exposes model fragility.

### Classical and HC3 uncertainty

Classical OLS uncertainty assumes the declared linear model and constant conditional variance. HC3 adjusts standard errors for heteroskedasticity and leverage sensitivity. Neither corrects sample selection, nonlinearity, omitted variables, or causal identification.

The learner compares intervals and explains whether the substantive conclusion changes. The learner does not select the smaller standard error.

### Mean confidence and new-outcome prediction intervals

The release provides three scenarios. For each, it distinguishes:

- uncertainty about the conditional mean; and
- a wider interval for one new conditional outcome.

The new-outcome interval is not a range that contains every future value, and it remains conditional on the selected outcome population and model assumptions.

## 9. Logistic regression worked case

### Fit population and event count

`LOG01` uses exactly 224 training rows and 25 positive acute-return outcomes. It does not use 7 validation outcomes or 4 test outcomes.

The training outcome prevalence baseline remains `25/224 = 0.111607142857`. Module 02 preserves that baseline but does not compare held-out prediction performance.

### Model matrix

`LOG01` columns are:

1. `const`;
2. `age_centered_decade`;
3. `prior_365d_acute_count`; and
4. `index_class_inpatient`.

Age is centered at the training mean and divided by 10. One age unit is one decade. The intercept is the log odds for an emergency index at mean training age with zero prior acute rows.

### Link and scale

The model is:

```text
log(p / (1 - p)) = X beta
```

The inverse link is:

```text
p = exp(X beta) / (1 + exp(X beta))
```

A coefficient is a conditional change in log odds. `exp(beta)` is a conditional odds ratio. Probability change depends on the entire linear predictor and starting probability.

### Reference `LOG01` results

| Term | Log-odds estimate | Odds ratio | Model-based 95% OR interval | p-value |
|---|---:|---:|---|---:|
| Intercept | -2.61394455 | 0.07324505 | 0.04154410 to 0.12913597 | <0.00000001 |
| Age per centered decade | 0.04355405 | 1.04451645 | 0.83150567 to 1.31209521 | 0.70818990 |
| Prior acute count | 0.79038049 | 2.20423495 | 1.34053977 to 3.62439954 | 0.00183942 |
| Inpatient versus emergency | -0.08146926 | 0.92176105 | 0.24698931 to 3.44000081 | 0.90349439 |

### Odds-ratio interpretation

Under `LOG01` in the 224 training rows, a one-count increase in prior 365-day acute encounters is associated with 2.204 times the conditional odds of a recorded 90-day acute return, holding centered age and index class fixed.

The statement must not become:

- 2.204 times the probability;
- a 120.4 percentage-point increase;
- a 120.4-percent increase in risk;
- the effect of causing an additional acute encounter;
- proof that prior acute count is an important predictor on new data; or
- a real-population estimate.

### Scenario probabilities

The release provides three scenarios at mean training age:

- emergency index and zero prior acute count;
- emergency index and one prior acute count; and
- inpatient index and one prior acute count.

Probability interpretation cites the complete scenario. A probability contrast across scenarios remains model-conditional and associational.

### Convergence and extreme probabilities

All three logistic fits converge. `LOG01` has:

- minimum fitted training probability 0.05633610;
- maximum fitted training probability 0.99962269;
- at least one fitted probability at or above 0.99;
- maximum absolute coefficient below 10;
- maximum standard error below 10;
- maximum Cook distance 0.19351112; and
- maximum leverage 0.17117289.

Convergence means the optimizer returned a solution under the supplied data and model. It does not establish adequate event support, stable extrapolation, correct functional form, transport, or utility.

### Model-based and HC3 uncertainty

Model-based standard errors use the fitted binomial variance and model specification. HC3 provides a leverage-sensitive sandwich comparison. Neither resolves sparse outcomes, absent categories, separation, model misspecification, or causal confounding.

### No test-shaped interpretation

The learner writes the coefficient interpretation before any held-out metric is opened. A surprising validation or test result in Module 03 may change the model-use decision, but cannot retroactively change what a fitted coefficient means.

## 10. Reference levels, transformations, and model matrices

### Reference registry

| Element | Reference or transform | Interpretation effect |
|---|---|---|
| Index class | emergency | inpatient indicator compares with emergency |
| Logistic outcome | 0 is no recorded acute return | model predicts outcome 1 |
| Age | center 46.245535714286 and divide by 10 | coefficient is per decade at training center |
| Prior acute count | zero is intercept value | coefficient is per one-count increase |
| Linear timing outcome | nonblank recorded timing only | model is conditional on selection |

### Why references are release artifacts

Software can silently choose alphabetical levels, drop a category, or reorder a matrix after a data change. The same model formula text can therefore yield a differently interpreted coefficient. The release records both the human-readable formula and exact matrix columns.

### Centering rule

The age center is calculated from training rows only. It is not recalculated in validation or test. A future row uses the fixed training center.

Centering changes the intercept and lower-order terms in nonlinear or interaction models. It does not change fitted values when done consistently.

### Model matrix evidence

`model-matrix-fields.csv` records 18 rows across four models. Every row names:

- model ID;
- column position;
- term;
- source or derived origin;
- exact expression; and
- interpretation unit.

### Silent-change gate

Any unregistered change in:

- factor reference;
- indicator coding;
- centering constant;
- unit scaling;
- squared-term construction;
- interaction construction;
- intercept inclusion; or
- column order

fails the formula gate and requires a rebuild.

## 11. Assumptions, diagnostics, and failure interpretation

### Diagnostics are evidence, not approval

A diagnostic can identify a pattern that conflicts with a model assumption. Failure to reject a diagnostic null does not prove the assumption. A passing convergence flag does not prove stability. A low p-value does not prove importance.

### Linear assumptions

The assumption register covers:

- selected conditional outcome;
- independent modeling rows;
- linear conditional mean;
- constant conditional variance;
- normal-error approximation for model-based inference;
- influential observations; and
- correct scale and specification.

### Logistic assumptions

The register covers:

- independent binary rows;
- event support;
- linearity in log odds for continuous terms;
- no complete or quasi-separation;
- categorical support;
- correct link and specification;
- influence and extrapolation; and
- stable numerical estimation.

### Shared boundaries

Both model families carry:

- no causal identification;
- no real-population transport;
- synthetic teaching use only;
- training-only evidence; and
- omitted-variable and specification limits.

### Status vocabulary

| Status | Meaning | Required action |
|---|---|---|
| `pass` | exact technical invariant or no material diagnostic concern under the check | retain evidence; do not overclaim proof |
| `review` | evidence needs interpretation or sensitivity review | describe consequence and preserve condition |
| `limit` | design or sample boundary permanently narrows claim | state boundary in every interpretation |
| `not supported` | current data and design cannot support the claim | prohibit that claim |
| `fail` | technical model or release condition is broken | stop progression and revise |

### Influence rule

Cook distance and leverage thresholds are screening rules, not deletion rules. A row is removed only if an upstream data error or predeclared eligibility rule justifies removal. Supported extremes remain in the analysis and may motivate robust methods, sensitivity analysis, or narrower interpretation.

### Separation rule

The build records convergence, coefficient magnitude, standard errors, extreme fitted probabilities, category cells, influence, and leverage. An extreme probability or zero cell triggers review. Complete separation requires revision or an approved penalized method; it cannot be ignored because software returned a coefficient.

## 12. Sparse categories and subgroup boundaries

### Training category counts

| Field | Category | Rows | Positives | Key condition |
|---|---|---:|---:|---|
| Gender | F | 155 | 14 | descriptive support only |
| Gender | M | 69 | 11 | descriptive support only |
| Race | asian | 15 | 3 | small event count |
| Race | black | 16 | 2 | small event count |
| Race | native | 3 | 0 | zero positive cell |
| Race | other | 0 | 0 | absent from training |
| Race | white | 190 | 20 | dominant category |
| Ethnicity | hispanic | 14 | 2 | small event count |
| Ethnicity | nonhispanic | 210 | 23 | dominant category |
| Index class | emergency | 180 | 15 | reference |
| Index class | inpatient | 44 | 10 | modeled indicator |

### Why allowed does not mean required

Race, ethnicity, and gender were allowed by Module 01 as information available at prediction time. The bounded `LOG01` formula omits them because the module is teaching core regression quantities with only 25 training outcomes and sparse categories. Inclusion would add parameters and unstable comparisons.

### Prohibited shortcuts

Learners may not:

- drop absent categories from the source record;
- infer that a zero positive cell proves no risk;
- merge categories solely to obtain a coefficient;
- rank category odds ratios with unsupported cells;
- declare fairness from an omitted group variable;
- treat source categories as universal identity definitions; or
- use test rows to supply missing training category support.

### Later handling

Module 03 reports subgroup counts before any performance metric and suppresses unsupported rankings. Module 04 examines validity and adjustment. Any future inclusion of sparse categories requires a new formula, preprocessing, reporting, and version decision.

## 13. Nonlinear-term and interaction teaching cases

### Nonlinear centered-age term

`LOG02` adds squared centered age. The training-only comparison with `LOG01` has:

- likelihood-ratio statistic 0.05524553;
- 1 degree of freedom; and
- p-value 0.81417483.

The purpose is not to conclude that age is linear or that curvature is absent. The purpose is to show that adding a squared term changes every age interpretation and that weak training evidence does not prove a functional form.

### Interaction term

`LOG03` adds prior acute count by inpatient indicator. The training-only comparison has:

- likelihood-ratio statistic 0.34768274;
- 1 degree of freedom; and
- p-value 0.55542782.

The learner calculates reference and combined slopes. A single interaction p-value does not prove equality or difference across groups.

### Hierarchy rule

When a squared term is included, retain the lower-order linear age term. When an interaction is included, retain both main terms. The model matrix makes this hierarchy explicit.

### Center-dependent main effects

In `LOG03`, the index-class main coefficient is evaluated at prior acute count zero. In `LOG02`, the linear age coefficient is the slope at mean training age because centered age equals zero there.

### Comparison boundary

The output table includes training log likelihood, AIC, and nested likelihood-ratio results for interpretation. It explicitly labels `LOG02` and `LOG03` as interpretation exercises only. Module 03 still needs validation evidence to compare prediction pipelines.

## 14. Uncertainty and interpretation quantities

### Linear quantities

| Quantity | Unit | Correct phrase |
|---|---|---|
| Coefficient | days per predictor unit | conditional mean difference |
| Mean confidence interval | days | uncertainty about conditional mean |
| Prediction interval | days | interval for one new conditional outcome |
| R-squared | proportion of training outcome variance | in-sample summary under model |

### Logistic quantities

| Quantity | Scale | Correct phrase |
|---|---|---|
| Coefficient | log odds | conditional log-odds change |
| Exponentiated coefficient | odds ratio | conditional odds multiplier |
| Scenario prediction | probability | model-conditional estimated probability |
| Likelihood-ratio statistic | likelihood | nested training fit comparison |

### P-value boundary

A p-value is a model-based compatibility calculation under a null and assumptions. It is not:

- probability that the null is true;
- probability the result occurred by chance;
- effect size;
- clinical importance;
- predictive performance;
- causal evidence;
- replication probability; or
- a universal decision threshold.

### Confidence interval boundary

A 95-percent confidence interval is produced by a method that would cover the target parameter in 95 percent of repeated compatible samples under its assumptions. It is not a 95-percent probability statement about the fixed parameter after observing this one dataset unless a compatible Bayesian analysis is used.

### Practical meaning

Learners report:

1. estimate;
2. interval;
3. fitting sample;
4. unit;
5. baseline or reference;
6. diagnostic conditions;
7. decision-relevant scale; and
8. unsupported claim.

A narrow interval around a trivial quantity and a wide interval around a potentially important quantity lead to different decisions. Neither is summarized adequately by a p-value.

### Prediction probability boundary

A scenario probability is a fitted mean on the probability scale for a declared covariate pattern. It is not an individual outcome, a guarantee, a treatment recommendation, or held-out calibration evidence.

## 15. Python and paired R interpretation contract

### Teaching objective

R is read, run, and interpreted in this curriculum. Learners are not graded on writing the R models from scratch. The supplied script demonstrates that the same declared model should produce reconcilable estimates across established statistical tools.

### Supplied R models

`paired-models.R`:

- reads the exact Module 01 modeling cohort;
- filters train rows;
- calculates the training age center;
- creates the inpatient indicator;
- filters nonblank timing rows for `LIN01`;
- fits base R `lm()` for `LIN01`;
- fits base R `glm(..., family=binomial(link="logit"))` for `LOG01`;
- uses default model-based standard errors;
- uses t-based `confint()` for the linear model and normal-approximation `confint.default()` for the logistic model;
- normalizes term names; and
- writes eight coefficient rows.

### Run command

Inside the learner workspace:

```text
Rscript paired-models.R data/modeling-cohort.csv outputs/r-coefficients.csv
```

### Required run record

The learner records:

- R version;
- operating system;
- exact command;
- output path and SHA-256;
- row count;
- maximum absolute coefficient difference;
- maximum absolute standard-error difference;
- maximum absolute interval difference;
- tolerance; and
- disposition.

### Numeric tolerance

The absolute tolerance is 0.000001 after aligning model IDs and normalized term names. Display rounding is not used as an input. A difference beyond tolerance is investigated for:

- different rows;
- missing-value handling;
- reference coding;
- centering;
- model family or link;
- interval method;
- package or language version;
- convergence; or
- term alignment.

### Reference release condition

The release machine has no R runtime. The reference package therefore includes:

- exact R source code;
- an eight-row Python-generated numeric reading target;
- a transparent pending R record; and
- an explicit human-review condition.

The reference does not claim that R executed locally. A named R reviewer must complete the run before alpha approval.

### Meaning of agreement

Python and R agreement supports implementation reproducibility for the same formula and rows. It does not validate the analytic question, sample selection, assumptions, clinical meaning, or causal claim.

## 16. Exact learner deliverables and package contract

### Required teaching and decision files

| File | Required content |
|---|---|
| `README.md` | disposition, both model cases, added terms, R reconciliation, handoff |
| `VERSION` | `0.1.0` |
| `requirements.txt` | exact scientific pins |
| `data-spec.md` | immutable inputs, fit partitions, formulas, uncertainty, output contract |
| `source-record.yml` | Module 01 fingerprints and synthetic claim boundary |
| `formula-registry.csv` | four declared models |
| `reference-levels.csv` | five reference and transform rows |
| `interpretation-quantity-guide.csv` | nine quantity boundaries |
| `regression-interpretation.md` | supported and unsupported interpretations |
| `environment-note.md` | actual Python and R environments |
| `reproducibility-check.md` | clean Python build and R evidence |
| `r-run-record.md` | exact paired R reconciliation |
| `ai-use.md` | material assistance and independent checks |
| `progression-decision.md` | Module 03 disposition, conditions, and return triggers |
| `assessment.md` | unchanged ten-point contract and gates |
| `paired-models.R` | supplied paired execution route |
| builder and validator | executable release and failure checks |

### Required copied inputs

- `data/modeling-cohort.csv`;
- `data/split-registry.csv`;
- `data/baseline-metrics.csv`; and
- `data/feature-role-contract.csv`.

These must match Module 01 exactly.

### Required output tables

| Output | Rows | Purpose |
|---|---:|---|
| `linear-subset-registry.csv` | 111 | selection, split, timing, and fit-use evidence |
| `linear-coefficients.csv` | 4 | estimate and classical/HC3 uncertainty |
| `linear-diagnostics.csv` | 13 | fit, residual, variance, influence, and conditioning evidence |
| `linear-prediction-examples.csv` | 3 | mean and new-outcome interval distinctions |
| `logistic-coefficients.csv` | 14 | three model coefficient sets and two uncertainty methods |
| `logistic-diagnostics.csv` | 45 | 15 diagnostics for each logistic model |
| `logistic-prediction-examples.csv` | 3 | probability-scale scenarios |
| `model-matrix-fields.csv` | 18 | exact encoded columns across four models |
| `model-comparison.csv` | 3 | training-only nested comparisons and handoff status |
| `sparse-cell-checks.csv` | 11 | category rows and outcomes |
| `assumption-register.csv` | 14 | pass, review, limit, and unsupported conditions |
| `r-reading-fixture.csv` | 8 | paired base-model numeric target |
| `regression-checks.csv` | 24 | release invariants |
| `build-report.json` | one object | inputs, partitions, output fingerprints, and decision |

### Reference output fingerprints

| Output | SHA-256 |
|---|---|
| Linear subset | `547e21378c40241ae33982da67eebc58ef5a67bb89bfdda1638b9cb3ab85696b` |
| Linear coefficients | `74a1b688949921468149c2d90bbbbfb5c0279331681de7a019fd4a913fc0d1da` |
| Linear diagnostics | `10c620213cda7cb089b208cc2918225c2f59c74b9d3aa07f8097a5f594a63f1b` |
| Linear scenarios | `fd034d7b207161c1df084d7552f3744c8cfae3a9c5279ae3adad7a63cebdb007` |
| Logistic coefficients | `4af1eee015652d064bdc583f931b1191b494910e15c70166dbde5af76375b6f4` |
| Logistic diagnostics | `6e3a610a5d7e1b474e655d6d75cf5ca70eae0ae1c94b0926a67f1739cb95d07e` |
| Logistic scenarios | `0fa6420cde11bb0f20bb57c8527c9ededc6f53c565729d36fd7709d17c1ffbc1` |
| Model matrix | `7a91e166796ae1030518da95e49f6a19ecc687d7cf5784f76718509c0abc9c38` |
| Model comparison | `d1dcdc7b89adb8d10b0614ced7ab9e81dab52e5c47a76ddbf9826d918d070d0c` |
| Sparse cells | `affb962905af94b0f7ba6b205c00c414441ec509d51f8cf93df13cb92ee6261e` |
| Assumptions | `7c6322667a383458a34aea49b687d1a6716aaaf0f780ccf060f1c99d671956e3` |
| R reading target | `89fe104cd40f81718d4f4d46842ec3aba1ef62bda85fd41f5576f86307c3d322` |
| Regression checks | `fd2472e946a84923aca7c07d42ec592615c67d6d86e8ee48053d7079f2242da6` |

### No screenshot-only evidence

Software summary screenshots do not replace coefficient tables, formula records, diagnostics, R output, or interpretation. Every assessed quantity must be machine-readable and accessible in text.

## 17. Assessment, rubric, gates, and checkpoint assembly

### Ten-point rubric

| Criterion | Full-credit evidence | Points |
|---|---|---:|
| Formulas, encodings, and references | four predeclared models, exact matrix, age center, reference levels | 2.00 |
| Linear and logistic fitting | exact training rows, outcomes, estimates, uncertainty, scenario quantities | 2.50 |
| Assumptions and failure checks | residual, variance, influence, convergence, sparsity, extreme-value evidence | 2.50 |
| Quantity-correct interpretation | days, log odds, odds ratios, probabilities, intervals, causal boundary | 2.00 |
| Reproduction and accountability | protected build, R reconciliation, environment, AI use, handoff | 1.00 |
| Total |  | 10.00 |

### Performance levels

| Level | Score | Meaning |
|---|---:|---|
| Ready | 9.00-10.00 | accurate and independently defensible with all gates passing |
| Ready with bounded revision | 8.00-8.99 | minimum met with all gates passing and documented nonblocking conditions |
| Revise | 0.00-7.99 | incomplete or inaccurate evidence |
| Gate failure | any | progression prohibited until correction or referral |

### Noncompensable gates

1. Module 01 fingerprints and conditions are unchanged.
2. All model fits use training only.
3. `LIN01` uses 69 selected training rows.
4. The 263 structural blanks remain blank.
5. `LOG01` through `LOG03` use 224 training rows and 25 outcomes.
6. Validation and test do not shape formulas or interpretations.
7. Formulas and model matrices are declared.
8. Reference levels and age center are fixed.
9. Classical and HC3 uncertainty are identified.
10. Linear quantities are interpreted in days.
11. Logistic quantities are named as log odds, odds ratios, or scenario probabilities.
12. No odds ratio is called a risk ratio or probability multiplier.
13. No coefficient is called a causal effect.
14. Residual, influence, sparsity, and extreme-probability evidence stays visible.
15. Added-term exercises do not become selected prediction models.
16. Python and R reconcile within tolerance or progression stops.
17. The builder refuses existing targets and validation passes.
18. Material AI assistance is disclosed and checked.
19. No real patient data, secret, private URL, or local path is present.
20. Module 03 disposition and conditions are explicit.

### Scoring notes

- A numerically correct coefficient with the wrong quantity name receives no interpretation credit.
- A correct odds ratio called a probability multiplier fails a gate.
- A correct model fit on validation or test fails the partition gate.
- A complete Python package without a completed R condition cannot receive unconditional acceptance.
- Automatic removal of an influential row without upstream evidence fails the integrity gate.
- A p-value-only narrative earns no more than half interpretation credit.

### Checkpoint assembly

The checkpoint freezes:

- accepted Module 02 tag and commit;
- ten-point score;
- gate result;
- formula and reference records;
- exact coefficient and diagnostic tables;
- R reconciliation;
- progression decision; and
- unresolved conditions.

Module 03 later adds its 15-point prediction evidence to the same 25-point component.

## 18. Feedback, revision, recovery, and support

### Feedback order

Review in this order:

1. privacy, access, or integrity stop;
2. upstream fingerprint or partition error;
3. blank-to-zero or selected-population error;
4. formula, encoding, or reference error;
5. model family or link error;
6. quantity or causal-language error;
7. uncertainty or diagnostic omission;
8. Python/R discrepancy;
9. reproducibility or documentation defect; and
10. clarity or formatting issue.

### Revision cycle

The learner preserves the failed state, identifies the affected quantities, decides version impact, rebuilds into a new target, reruns both language routes, updates interpretation and conditions, and resubmits.

### High-impact revision examples

| Defect | Required correction | Downstream effect |
|---|---|---|
| timing blanks changed to zero | restore exact source and invalidate linear outputs | restart Module 02 |
| validation rows fit | rebuild from train only | invalidate formula-development evidence |
| wrong index reference | correct encoding and every interpretation | new outputs and handoff |
| odds ratio called risk ratio | rewrite quantity logic and defense | progression blocked until understood |
| influential row deleted | restore unless upstream error is proven | rerun all models |
| R interval differs | align interval method or explain approved difference | R gate remains open |
| `LOG02` selected from training AIC | restore `LOG01` handoff | Module 03 starts from declared formula |
| causal language used | remove claim or refer to causal-design review | progression blocked |

### Supported environment route

Learners without local R or scientific-package installation use an institution-managed environment. The same input, output, version, and reconciliation contract applies.

### Accessibility route

All outputs are CSV, JSON, Markdown, Python, or R text. No assessed task requires interpreting a chart. A learner may use command-line, accessible table, or screen-reader routes.

### Extension principle

Accommodations may change schedule and response format. They do not change the training-only boundary, quantity meanings, source contract, or noncompensable gates.

## 19. Responsible AI, privacy, accessibility, and integrity

### AI may assist with

- explaining model vocabulary;
- drafting formula alternatives for human review;
- suggesting diagnostic checks;
- debugging code;
- translating software term names;
- checking whether prose uses odds or risk correctly; and
- drafting accessible table descriptions.

### AI may not own

- input permission;
- fitting partition;
- formula selection;
- reference coding;
- variance method;
- diagnostic disposition;
- causal interpretation;
- R discrepancy resolution;
- Module 03 handoff; or
- clinical use.

### Required AI-use evidence

Record tool, purpose, data shared, output used, independent check, rejected advice, and human decision owner. A material suggestion that changed a formula, field, uncertainty method, or interpretation requires direct evidence of verification.

### Prompt boundary

Do not share real patient data, credentials, private URLs, restricted source text, or institution-only model output with an unapproved system. This release uses synthetic data, but learners practice the stricter real-world boundary.

### Integrity traps

- asking an agent to write the interpretation without reading the coefficients;
- accepting a risk-ratio substitution;
- hiding a failed convergence or influential row;
- using test output to rewrite the model story;
- claiming R ran when it did not;
- copying reference prose without being able to defend the quantity; and
- reporting a fabricated package or version.

### Accessibility requirements

- heading hierarchy is logical;
- tables have headers and units;
- status is not encoded by color;
- equations have plain-text explanations;
- software output is exported to readable tables;
- URLs needed for use are visible in full;
- no image-only evidence is required;
- command paths are repository-relative; and
- the defense may be oral, written, or in an approved accessible recorded format.

### Privacy and security gate

No release file may contain a real patient record, direct real identifier, credential, token, private signed URL, or absolute personal filesystem path. Discovery triggers `refer`.

## 20. Validation, acceptance tests, risks, and human review

### Builder self-check

The builder must:

- verify all four Module 01 inputs;
- fit exact training-only models;
- build all 13 CSV evidence tables and the report;
- confirm the 69-row linear and 25-event logistic facts;
- refuse an existing output target;
- build a learner workspace;
- reproduce identical outputs from copied inputs; and
- print a pass marker.

### Validator self-check

The validator must:

- rebuild expected outputs;
- compare every CSV field and value;
- compare the full build report;
- validate formula, reference, interpretation, and R source contracts;
- validate release metadata and output fingerprints;
- validate a prompted starter;
- reject the starter as a completed submission; and
- reject a fixture missing a required coefficient table.

Reference version 0.1.0 passes 2025 release checks and 1972 starter checks.

### Acceptance commands

```text
python courses/modeling-inference-reproducible-analytics/modules/02-regression-interpretation/build_regression_evidence.py --self-check
python courses/modeling-inference-reproducible-analytics/modules/02-regression-interpretation/validate_regression_evidence.py --self-check
powershell -ExecutionPolicy Bypass -File scripts/check-curriculum-specs.ps1
```

R execution in a learner or managed environment:

```text
Rscript paired-models.R data/modeling-cohort.csv outputs/r-coefficients.csv
```

### Technical acceptance criteria

- 21 numbered specification sections;
- all required files present;
- no Unicode em or en dash in release text;
- no local personal paths;
- all Python self-checks pass;
- R condition is truthfully recorded;
- exact Module 01 and output fingerprints match;
- root Commons version is 0.40.0;
- curriculum checker passes; and
- worktree is clean after commit.

### Known material limitations

1. The source is synthetic and older.
2. The linear case conditions on recorded timing and has 69 fit rows.
3. Linear residual normality and influence evidence require caution.
4. Logistic fitting has 25 positive training outcomes.
5. Maximum fitted probability is near one for extreme prior use.
6. Some categories are sparse or absent in training.
7. Models omit plausible mechanisms.
8. Training evidence does not establish held-out prediction.
9. The release machine lacks R.
10. No causal or real-population transport is supported.

### Required human reviews before alpha

| Review | Required decision |
|---|---|
| Course faculty | workload, outcomes, and checkpoint fit |
| Biostatistics | formulas, uncertainty, diagnostics, and interpretation |
| Clinical informatics | encounter outcome meaning and selection boundary |
| Python | statsmodels implementation and portable environment |
| R | paired execution and numeric reconciliation |
| Reproducibility | clean build, versions, and fingerprints |
| Accessibility | table, equation, command, and defense routes |
| Privacy/security | synthetic scope and prompt boundary |
| Responsible AI | disclosure, verification, and ownership |
| Independent instructor | teachability without author context |

### Reference disposition

The technical reference disposition is `accept with conditions`. It supports Module 03 package development, not human curriculum approval. Conditions include selected linear outcome, diagnostic review, sparse and extreme logistic evidence, pending named R execution, synthetic scope, and no causal or deployment claim.

## 21. References, release record, and continuation contract

### Authoritative references

- statsmodels regression: https://www.statsmodels.org/stable/regression.html
- statsmodels generalized linear models: https://www.statsmodels.org/stable/glm.html
- statsmodels regression diagnostics: https://www.statsmodels.org/stable/diagnostic.html
- NumPy linear algebra: https://numpy.org/doc/stable/reference/routines.linalg.html
- SciPy statistical functions: https://docs.scipy.org/doc/scipy/reference/stats.html
- R linear models: https://stat.ethz.ch/R-manual/R-devel/library/stats/html/lm.html
- R generalized linear models: https://stat.ethz.ch/R-manual/R-devel/library/stats/html/glm.html
- R default confidence intervals: https://stat.ethz.ch/R-manual/R-devel/library/stats/html/confint.html
- scikit-learn common pitfalls: https://scikit-learn.org/stable/common_pitfalls.html
- Synthea downloads: https://synthea.mitre.org/downloads
- Semantic Versioning 2.0.0: https://semver.org/spec/v2.0.0.html

### Release record

- Module version: 0.1.0.
- Commons release: 0.40.0.
- Release date: 2026-08-30.
- Status: runnable release candidate.
- Reference disposition: accept with conditions.
- Builder self-check: pass.
- Validator self-check: pass.
- Release checks: 2025.
- Starter checks: 1972.
- Regression checks: 24.
- Linear available, fit, and blank rows: 111, 69, and 263.
- Logistic training rows and outcomes: 224 and 25.
- Validation used in fitting: no.
- Test used in fitting: no.
- R execution: pending named reviewer.
- Real patients: none.

### Contributors

- Shuhan He: Commons sponsor and curriculum direction.
- OpenAI Codex: module specification, regression build, validation, and teaching package.

AI assistance is disclosed. Named faculty and specialist reviewers remain responsible for human approval.

### Module 03 continuation contract

Begin Module 03 only from an accepted or accepted-with-conditions Module 02 state. Module 03 is `Prediction workflows and evaluation` with 16.5 learner hours.

Module 03 must:

1. verify Module 01 and Module 02 fingerprints;
2. preserve the 224/75/75 temporal split;
3. preserve the training-prevalence baseline;
4. convert `LOG01` terms into one leakage-safe preprocessing and fit pipeline;
5. fit preprocessing only on training data;
6. use training resampling only for training-stage development;
7. compare the baseline, `LOG01`, and one bounded machine-learning baseline on validation evidence;
8. reject a deliberately leaked critique model;
9. declare a selection rule and threshold before test;
10. freeze the chosen pipeline;
11. run the test set once;
12. report discrimination, calibration, thresholds, exact confusion counts, prevalence, and uncertainty;
13. show subgroup counts and suppress unsupported rankings;
14. preserve the four-positive test limitation; and
15. make a Week 3 checkpoint and Module 04 progression decision without deployment claims.

### Resume record

FND-2 Module 02 is complete as a runnable reference candidate at Commons 0.40.0 when all acceptance commands pass and the unit is committed and pushed. Resume with Module 03 only. Do not reopen formulas, references, fit partitions, or interpretation quantities without a documented return and version decision.
