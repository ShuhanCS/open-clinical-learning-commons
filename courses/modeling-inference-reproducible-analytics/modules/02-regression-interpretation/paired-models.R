args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 2) {
  stop("Usage: Rscript paired-models.R INPUT_CSV OUTPUT_CSV")
}

input_path <- args[[1]]
output_path <- args[[2]]
d <- read.csv(input_path, stringsAsFactors = FALSE, check.names = FALSE)
train <- d[d$split == "train", ]
age_mean <- mean(train$age_at_index)
train$age_centered_decade <- (train$age_at_index - age_mean) / 10
train$index_class_inpatient <- ifelse(train$index_class == "inpatient", 1, 0)

linear <- train[!is.na(train$next_30d_days_after_index_stop), ]
lin_fit <- lm(
  next_30d_days_after_index_stop ~ age_at_index + prior_365d_encounter_count + index_class_inpatient,
  data = linear
)
log_fit <- glm(
  acute_return_90d ~ age_centered_decade + prior_365d_acute_count + index_class_inpatient,
  data = train,
  family = binomial(link = "logit")
)

extract_rows <- function(model_id, fit, names_out) {
  table <- summary(fit)$coefficients
  ci <- if (inherits(fit, "glm")) {
    confint.default(fit, level = 0.95)
  } else {
    confint(fit, level = 0.95)
  }
  data.frame(
    model_id = model_id,
    term = names_out,
    estimate = unname(table[, 1]),
    std_error = unname(table[, 2]),
    statistic = unname(table[, 3]),
    p_value = unname(table[, 4]),
    lower95 = unname(ci[, 1]),
    upper95 = unname(ci[, 2]),
    stringsAsFactors = FALSE
  )
}

lin_names <- c("const", "age_at_index", "prior_365d_encounter_count", "index_class_inpatient")
log_names <- c("const", "age_centered_decade", "prior_365d_acute_count", "index_class_inpatient")
result <- rbind(
  extract_rows("LIN01", lin_fit, lin_names),
  extract_rows("LOG01", log_fit, log_names)
)
write.csv(result, output_path, row.names = FALSE, quote = TRUE, na = "")
cat(sprintf("R regression evidence written: %d rows\n", nrow(result)))
