# Optional paired reading for FND-2 Module 04.
# Run in a named R environment; Python outputs remain the release reference.

repeated <- read.csv("outputs/repeated-measures-fixture.csv")
survival_data <- read.csv("outputs/survival-fixture.csv")

naive <- lm(symptom_score ~ week * treatment, data = repeated)
print(summary(naive))

if (requireNamespace("nlme", quietly = TRUE)) {
  mixed <- nlme::lme(
    symptom_score ~ week * treatment,
    random = ~ 1 | fixture_id,
    data = repeated,
    method = "ML"
  )
  print(summary(mixed))
} else {
  message("Install nlme in the named teaching environment for the paired mixed-model reading.")
}

if (requireNamespace("survival", quietly = TRUE)) {
  survival_object <- survival::Surv(survival_data$observed_week, survival_data$event)
  print(survival::survfit(survival_object ~ treatment, data = survival_data))
  survival_data$age_decade <- (survival_data$age - mean(survival_data$age)) / 10
  survival_data$severity_10 <- (survival_data$baseline_severity - mean(survival_data$baseline_severity)) / 10
  print(survival::coxph(
    survival_object ~ treatment + age_decade + severity_10 + comorbidity_count,
    data = survival_data
  ))
} else {
  message("Install survival in the named teaching environment for the paired survival reading.")
}
