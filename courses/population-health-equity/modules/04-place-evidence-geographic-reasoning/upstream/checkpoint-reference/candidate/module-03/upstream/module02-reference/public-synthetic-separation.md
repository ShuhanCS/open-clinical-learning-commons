# Public and synthetic evidence separation

PLACES provides modeled small-area prevalence; the synthetic release provides generated planning-need events. They are never combined into one observed measure.

The PLACES table keeps its publisher, release, measure year, estimate type, adult population field, modeled point estimate, and published confidence interval. It supports source interpretation and later bounded comparison questions. It does not contain observed diagnoses or intervention outcomes.

The synthetic table keeps case ID `FMA-DP-01`, generator version `0.1.0`, seed `73052`, fictional period `2024`, and `synthetic_flag=1`. Its age-specific probabilities use fixed teaching baselines and a seeded fictional tract effect. PLACES and SVI values do not generate the numerator.

The synthetic numerator is not a diabetes diagnosis, PLACES case, patient record, individual eligibility result, local observation, intervention outcome, community preference, targeting score, or allocation signal.

Module 02 may explain how crude and standardized synthetic measures differ. It may not use either public or synthetic results to make a disparity claim, rank a tract, draw a map, select a target, allocate resources, estimate an intervention effect, or authorize action.
