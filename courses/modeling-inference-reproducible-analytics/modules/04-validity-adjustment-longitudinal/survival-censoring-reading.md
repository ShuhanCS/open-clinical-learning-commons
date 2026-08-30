# Survival and censoring reading

The event is the generated event indicator, time zero is synthetic treatment assignment, and `observed_week` is the earlier of generated event and censoring times. There are 449 events and 151 censored observations among 600 people.

At week 26, the Kaplan-Meier event-free estimates are 0.35066787 for untreated and 0.37237475 for treated generated people. These are group-specific survival probabilities under the fixture's censoring structure. They are not the Cox hazard ratio.

The adjusted Cox treatment hazard ratio is 0.67945425. Conditional on age, baseline severity, and comorbidity in this synthetic model, the fitted instantaneous event hazard is lower for treatment. The quantity is not a risk ratio, a probability, a fixed-time risk difference, or a causal effect.

Censoring is not ordinary missing-outcome deletion. A censored person contributes to the risk set until the recorded censoring time. Dropping every censored row would discard valid at-risk time and change the estimand.

Referral is required for doubtful independent censoring, competing events, time-varying hazards or exposures, recurrent events, interval censoring, sparse risk sets, or any clinical survival claim.
