#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 1) stop("usage: Rscript paired-risk-adjustment.R <analysis-cohort.csv>")
cohort <- read.csv(args[[1]], stringsAsFactors = FALSE)
stopifnot(nrow(cohort) == 476, sum(cohort$event_indicator) == 87)
cohort$age_decade_from_40 <- (cohort$age_at_index - 40) / 10
cohort$any_prior_acute <- as.integer(cohort$prior_365d_acute_count > 0)
cohort$index_inpatient <- as.integer(cohort$index_encounter_class == "inpatient")

expected_model <- glm(
  event_indicator ~ age_decade_from_40 + any_prior_acute + prior_365d_condition_count + index_inpatient,
  data = cohort,
  family = binomial(link = "logit")
)
cohort$expected_probability <- predict(expected_model, type = "response")
adjusted_association <- glm(
  event_indicator ~ age_decade_from_40 + any_prior_acute + prior_365d_condition_count + index_inpatient + landmark_exposure,
  data = cohort,
  family = binomial(link = "logit")
)

print(summary(expected_model))
print(summary(adjusted_association))
print(aggregate(cbind(observed = cohort$event_indicator, expected = cohort$expected_probability) ~ teaching_site_id, cohort, sum))
cat("\nReading boundary: synthetic fixed-horizon descriptive adjustment; no causal effect, fairness certification, or real-site ranking.\n")
