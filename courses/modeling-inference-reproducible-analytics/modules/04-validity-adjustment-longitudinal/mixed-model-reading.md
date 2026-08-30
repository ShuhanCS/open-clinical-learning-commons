# Mixed-model reading

The unit of observation is a person-visit; the independent cluster is the generated person. Each of 600 people contributes four visits, producing 2,400 rows.

The random-intercept model estimates 46.82601084 between-person residual variance and 9.18680087 within-person residual variance. Their ratio gives an intraclass correlation of 0.83598751: observations from the same generated person are strongly related.

The treatment-by-week estimate is -0.23518501. In this model it is the additional mean weekly change for treated generated people, conditional on the fixed model and random-intercept structure. It is not the treatment contrast at every week and is not a clinical causal effect.

Naive OLS gives a week standard error of 0.04501928; cluster-robust OLS gives 0.01677907; the random-intercept model gives 0.01824432. There is no rule that a dependence-aware standard error must always be larger. The comparison teaches that the covariance model changes uncertainty and must match the data-generating structure.

Referral is required for irregular visits, informative dropout, time-varying treatment, nonlinear trajectories, competing correlation structures, small cluster counts, or a clinical effect claim.
