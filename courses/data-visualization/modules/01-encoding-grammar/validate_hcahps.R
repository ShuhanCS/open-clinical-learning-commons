args <- commandArgs(trailingOnly = TRUE)
input_path <- if (length(args) >= 1) args[[1]] else file.path("data", "hcahps_ma_recommend_2026.csv")

if (!file.exists(input_path)) {
  stop(sprintf("Data file not found: %s", input_path), call. = FALSE)
}

data <- utils::read.csv(input_path, stringsAsFactors = FALSE, na.strings = "")
expected_columns <- c(
  "facility_id",
  "facility_name",
  "city",
  "state",
  "measure_id",
  "measure",
  "recommend_percent",
  "completed_surveys",
  "response_rate_percent",
  "value_status",
  "value_footnote",
  "completed_surveys_footnote",
  "response_rate_footnote",
  "period_start",
  "period_end",
  "cms_release_date"
)

checks <- data.frame(
  check = character(),
  passed = logical(),
  result = character(),
  stringsAsFactors = FALSE
)
record_check <- function(name, passed, result) {
  checks[nrow(checks) + 1, ] <<- list(name, isTRUE(passed), as.character(result))
}

record_check("columns", identical(names(data), expected_columns), paste(names(data), collapse = ", "))
if (!checks$passed[[1]]) {
  print(checks, row.names = FALSE)
  stop("Structural validation failed: unexpected columns.", call. = FALSE)
}

reported <- data$value_status == "reported"
not_available <- data$value_status == "not_available"
record_check("row count", nrow(data) == 65L, nrow(data))
record_check("unique facilities", length(unique(data$facility_id)) == 65L, length(unique(data$facility_id)))
record_check("Massachusetts only", all(data$state == "MA"), paste(unique(data$state), collapse = ", "))
record_check("measure ID", all(data$measure_id == "H_RECMND_DY"), paste(unique(data$measure_id), collapse = ", "))
record_check("reported values", sum(reported) == 56L, sum(reported))
record_check("not-available values", sum(not_available) == 9L, sum(not_available))
record_check(
  "reported percent range",
  all(data$recommend_percent[reported] >= 0 & data$recommend_percent[reported] <= 100),
  sprintf("%.0f to %.0f", min(data$recommend_percent[reported]), max(data$recommend_percent[reported]))
)
record_check(
  "reported survey counts",
  all(is.finite(data$completed_surveys[reported]) & data$completed_surveys[reported] > 0),
  sprintf("%d to %d", min(data$completed_surveys[reported]), max(data$completed_surveys[reported]))
)
record_check(
  "missing values match status",
  all(is.na(data$recommend_percent[not_available])) && all(is.na(data$completed_surveys[not_available])),
  sprintf(
    "missing percent=%d; missing completed surveys=%d",
    sum(is.na(data$recommend_percent)),
    sum(is.na(data$completed_surveys))
  )
)
record_check(
  "footnotes retained",
  all(!is.na(data$value_footnote[not_available]) & nzchar(data$value_footnote[not_available])),
  paste(sort(unique(data$value_footnote[not_available])), collapse = ", ")
)
record_check(
  "measurement period",
  all(data$period_start == "2024-10-01") && all(data$period_end == "2025-09-30"),
  paste(unique(paste(data$period_start, data$period_end, sep = " to ")), collapse = "; ")
)
record_check(
  "CMS release",
  all(data$cms_release_date == "2026-08-13"),
  paste(unique(data$cms_release_date), collapse = ", ")
)

peer_set <- data[reported, , drop = FALSE]
peer_set <- head(peer_set[order(-peer_set$completed_surveys, peer_set$facility_id), ], 15)
record_check("peer set size", nrow(peer_set) == 15L, nrow(peer_set))
record_check(
  "peer set comparison spread",
  diff(range(peer_set$recommend_percent)) >= 20,
  sprintf("%.0f percentage points", diff(range(peer_set$recommend_percent)))
)

cat(sprintf("Validation report: %s\n", input_path))
print(checks, row.names = FALSE)
if (!all(checks$passed)) {
  stop(sprintf("Validation failed: %d check(s).", sum(!checks$passed)), call. = FALSE)
}
cat(sprintf("PASS: %d checks passed.\n", nrow(checks)))
