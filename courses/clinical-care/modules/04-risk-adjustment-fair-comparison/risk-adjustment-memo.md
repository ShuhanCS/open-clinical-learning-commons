# Risk-adjustment memo

The accepted cohort has 476 synthetic people and 87 first later acute returns by day 335 after the landmark. Every person without an event reaches the same administrative boundary, and no death censors a person before an event. That frozen structure permits the binary fixed-horizon outcome used here. It would not support the same shortcut if follow-up were unequal or a competing outcome occurred first.

The expected-outcome model was fixed before fitting:

`event_indicator ~ age_decade_from_40 + any_prior_acute + prior_365d_condition_count + index_inpatient`

The model excludes scheduled follow-up, site, outcomes, post-exposure fields, synthetic extension fields, and demographic audit fields. Its predicted probabilities sum to 87.00000000 expected events. This is an in-sample fitting identity, not proof that the model is calibrated for another population.

Among 129 people with scheduled follow-up, 25 events were observed and 23.05515435 were expected. The indirectly standardized event rate is 0.19819116. Among 347 people without recorded follow-up, 62 events were observed and 63.94484565 were expected. The standardized rate is 0.17721417. The secondary adjusted odds ratio for scheduled follow-up is 1.16353250, with a 95 percent interval from 0.67665877 to 2.00072462 and p = 0.58392672.

The adjusted odds ratio is not a risk ratio or hazard ratio. The adjusted association does not establish benefit, harm, equivalence, or causation. Scheduled follow-up is an encounter record, and residual confounding remains. Module 03 also found that the proportional-hazards screen failed at p = 0.00636020. This fixed-horizon analysis answers a different question and does not repair that failure.
