# Reference regression interpretation

## Decision

`accept with conditions`

The training-only evidence is reproducible and quantity-correct enough for Module 03 to evaluate the bounded `LOG01` prediction pipeline. The disposition does not endorse the coefficients as causal effects or the model as clinically useful.

## Linear case

`LIN01` uses 69 training rows among the 111 people with a recorded different encounter within 30 days. The 263 people without recorded timing retain structural blanks outside the conditional linear outcome; those blanks are not zero.

The model's R-squared is 0.07951657. The estimated prior-encounter coefficient is -0.10110471 days per one-count increase under the declared additive formula. Its classical 95-percent interval is -0.19973978 to -0.00246963. That interval does not make the result clinically important, causal, stable, or representative of all 374 people.

The Jarque-Bera p-value is 0.04655734. Maximum Cook distance is 0.07408089, above the 4/n review threshold, and maximum leverage is 0.58620136. Classical and HC3 uncertainty are both reported. The correct conclusion is that the small selected conditional model has visible residual and influence limitations.

## Logistic case

`LOG01` uses all 224 training rows and 25 positive acute-return outcomes. Age is centered at the training mean of 46.245535714286 years and expressed per decade. Emergency index class is the reference.

The prior-365-day acute-count coefficient is 0.79038049 on the log-odds scale. Its odds ratio is 2.20423495 with model-based 95-percent interval 1.34053977 to 3.62439954. This is a model-conditional multiplicative change in odds per one-count increase. It is not a risk ratio, a 120-percent increase in probability, or the effect of causing one more acute encounter.

The inpatient-versus-emergency odds ratio is 0.92176105 with a wide model-based 95-percent interval of 0.24698931 to 3.44000081. The evidence does not support a stable group difference under this formula.

`LOG01` converges, but the maximum fitted training probability is 0.99962269 and influence review remains necessary. The model contains a small event count and omits plausible mechanisms. Convergence is not proof that the model is well specified.

## Nonlinear and interaction exercises

`LOG02` adds squared centered age. Its training-only likelihood-ratio p-value against `LOG01` is 0.81417483.

`LOG03` adds the prior-acute-count by inpatient interaction. Its training-only likelihood-ratio p-value is 0.55542782.

These comparisons teach changed interpretation. They do not select a prediction model and do not replace validation evidence. The bounded `LOG01` formula remains the Module 03 handoff.

## Sparse categories

Training race counts include 3 native rows with no positive outcome and no `other` row. Those effects are not estimated in the bounded formulas. Later subgroup evidence must show counts and suppress unsupported rankings. Categories are not merged automatically.

## R reading

The package includes `paired-models.R` and an eight-row numeric reading target for `LIN01` and `LOG01`. The release machine has no R runtime. Named learner or reviewer execution must reconcile estimates, standard errors, and intervals within 0.000001 and record the R version before alpha acceptance.

## Supported statement

Under the declared training-only logistic formula in this synthetic cohort, prior acute-utilization count has a positive model-conditional association with recorded 90-day acute return, with substantial uncertainty and extreme fitted values requiring review.

## Unsupported statements

- Prior acute utilization causes an acute return.
- One additional acute encounter doubles a person's probability.
- The model performs well on new data.
- The model is fair across groups.
- The model should be deployed.
- The result estimates a real clinical population.

## Module 03 handoff

Module 03 receives `LOG01`, exact terms and transforms, Module 01 split and baseline, all coefficient and diagnostic evidence, sparse-cell warnings, and the rule that validation and test remain outside Module 02 development. Module 03 must evaluate prediction rather than reward coefficient significance.
