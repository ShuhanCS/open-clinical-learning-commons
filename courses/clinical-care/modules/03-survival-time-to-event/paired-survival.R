#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 1) stop("usage: Rscript paired-survival.R <analysis-cohort.csv>")
suppressPackageStartupMessages(library(survival))

cohort <- read.csv(args[[1]], stringsAsFactors = FALSE)
stopifnot(nrow(cohort) == 476)
stopifnot(sum(cohort$event_indicator) == 87)
cohort$scheduled_followup <- factor(
  cohort$landmark_exposure,
  levels = c(0, 1),
  labels = c("no_recorded_followup", "scheduled_followup")
)
survival_object <- with(cohort, Surv(observed_time_days, event_indicator))
km <- survfit(survival_object ~ scheduled_followup, data = cohort, conf.type = "log-log")
comparison <- survdiff(survival_object ~ scheduled_followup, data = cohort, rho = 0)
cox <- coxph(survival_object ~ scheduled_followup, data = cohort, ties = "efron", x = TRUE)
ph <- cox.zph(cox)

print(summary(km, times = c(0, 30, 90, 180, 270, 335), extend = TRUE))
print(comparison)
print(summary(cox))
print(ph)

cat("\nReading boundary: synthetic observational association; the hazard ratio is not a probability, risk ratio, or causal effect.\n")
