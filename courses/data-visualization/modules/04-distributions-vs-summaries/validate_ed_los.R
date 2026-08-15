args <- commandArgs(trailingOnly = TRUE)
input_path <- if (length(args) >= 1) args[[1]] else file.path("data", "ed_los_2026.csv")
variant <- if (length(args) >= 2) args[[2]] else "real"

allowed_variants <- c("real", "null", "trivial")
if (!variant %in% allowed_variants) {
  stop("Variant must be one of: real, null, trivial", call. = FALSE)
}
if (!file.exists(input_path)) {
  stop(sprintf("Data file not found: %s", input_path), call. = FALSE)
}

data <- utils::read.csv(input_path, stringsAsFactors = FALSE)
expected_columns <- c(
  "encounter_id",
  "arrival_date",
  "esi",
  "age_group",
  "disposition",
  "boarded",
  "los_min"
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

record_check(
  "columns",
  identical(names(data), expected_columns),
  paste(names(data), collapse = ", ")
)
if (!checks$passed[[1]]) {
  print(checks, row.names = FALSE)
  stop("Structural validation failed: unexpected columns.", call. = FALSE)
}
record_check("row count", nrow(data) == 8392L, nrow(data))
record_check(
  "complete rows",
  !anyNA(data) && !any(data == ""),
  sprintf("missing=%d blank=%d", sum(is.na(data)), sum(data == ""))
)
record_check(
  "unique encounter IDs",
  length(unique(data$encounter_id)) == nrow(data),
  length(unique(data$encounter_id))
)

parsed_dates <- as.Date(data$arrival_date)
record_check(
  "2026 arrival dates",
  !anyNA(parsed_dates) && min(parsed_dates) >= as.Date("2026-01-01") &&
    max(parsed_dates) <= as.Date("2026-12-31"),
  sprintf("%s to %s", min(parsed_dates), max(parsed_dates))
)
record_check(
  "ESI values",
  all(data$esi %in% 1:5) && sum(data$esi == 1) == 66L,
  paste(names(table(data$esi)), as.integer(table(data$esi)), collapse = "; ")
)
record_check(
  "age groups",
  all(data$age_group %in% c("18-39", "40-64", "65-79", "80+")),
  paste(names(table(data$age_group)), as.integer(table(data$age_group)), collapse = "; ")
)
disposition_counts <- table(data$disposition)
record_check(
  "disposition counts",
  identical(as.integer(disposition_counts[c("admitted", "discharged")]), c(1930L, 6462L)),
  paste(names(disposition_counts), as.integer(disposition_counts), collapse = "; ")
)
record_check(
  "boarding values",
  all(data$boarded %in% 0:1) && all(data$disposition[data$boarded == 1] == "admitted"),
  sprintf("boarded=%d", sum(data$boarded == 1))
)
record_check(
  "positive whole-minute LOS",
  is.numeric(data$los_min) && all(data$los_min > 0) && all(data$los_min == round(data$los_min)),
  sprintf("range=%d to %d", min(data$los_min), max(data$los_min))
)

if (!all(checks$passed)) {
  print(checks, row.names = FALSE)
  stop("Structural validation failed.", call. = FALSE)
}

month <- as.integer(format(parsed_dates, "%m"))
jan <- data[month == 1, , drop = FALSE]
dec <- data[month == 12, , drop = FALSE]
percent_change <- function(december, january) 100 * (december - january) / january
metric <- function(frame, fn) as.numeric(fn(frame$los_min))

jan_mean <- metric(jan, mean)
dec_mean <- metric(dec, mean)
jan_median <- metric(jan, stats::median)
dec_median <- metric(dec, stats::median)
jan_p90 <- metric(jan, function(x) stats::quantile(x, 0.90, names = FALSE))
dec_p90 <- metric(dec, function(x) stats::quantile(x, 0.90, names = FALSE))
jan_tail <- 100 * mean(jan$los_min > 480)
dec_tail <- 100 * mean(dec$los_min > 480)

mean_change <- percent_change(dec_mean, jan_mean)
median_change <- percent_change(dec_median, jan_median)
p90_change <- percent_change(dec_p90, jan_p90)
tail_change <- dec_tail - jan_tail

record_check(
  "overall right skew",
  mean(data$los_min) / stats::median(data$los_min) >= 1.20,
  sprintf("mean/median=%.3f", mean(data$los_min) / stats::median(data$los_min))
)

if (variant == "real") {
  group_ratio <- max(disposition_counts) / min(disposition_counts)
  admitted <- data[data$disposition == "admitted", , drop = FALSE]
  boarded_median <- stats::median(admitted$los_min[admitted$boarded == 1])
  nonboarded_median <- stats::median(admitted$los_min[admitted$boarded == 0])
  january_admitted <- data[month == 1 & data$disposition == "admitted", , drop = FALSE]
  december_admitted <- data[month == 12 & data$disposition == "admitted", , drop = FALSE]
  boarding_change <- 100 * (
    mean(december_admitted$boarded) - mean(january_admitted$boarded)
  )
  group_means <- tapply(data$los_min, data$disposition, mean)
  average_of_averages_gap <- abs(mean(group_means) - mean(data$los_min))

  record_check("unequal groups", group_ratio >= 2.5, sprintf("ratio=%.3f", group_ratio))
  record_check(
    "hidden-process median gap",
    boarded_median - nonboarded_median >= 300,
    sprintf("gap=%.1f minutes", boarded_median - nonboarded_median)
  )
  record_check(
    "boarding prevalence trend",
    boarding_change >= 25,
    sprintf("change=%.1f percentage points", boarding_change)
  )
  record_check(
    "stable pooled mean",
    abs(mean_change) < 6,
    sprintf("change=%+.1f%%", mean_change)
  )
  record_check(
    "worsening 90th percentile",
    p90_change > 40,
    sprintf("change=%+.1f%%", p90_change)
  )
  record_check(
    "small subgroup",
    min(table(data$esi)) < 100,
    sprintf("smallest n=%d", min(table(data$esi)))
  )
  record_check(
    "average-of-averages gap",
    average_of_averages_gap >= 30,
    sprintf("gap=%.1f minutes", average_of_averages_gap)
  )
} else if (variant == "null") {
  record_check(
    "null mean change",
    abs(mean_change) <= 5,
    sprintf("change=%+.1f%%", mean_change)
  )
  record_check(
    "null median change",
    abs(median_change) <= 5,
    sprintf("change=%+.1f%%", median_change)
  )
  record_check(
    "null p90 change",
    abs(p90_change) <= 5,
    sprintf("change=%+.1f%%", p90_change)
  )
  record_check(
    "null tail-share change",
    abs(tail_change) < 1,
    sprintf("change=%+.1f percentage points", tail_change)
  )
} else {
  wilcoxon_p <- stats::wilcox.test(
    jan$los_min,
    dec$los_min,
    alternative = "two.sided",
    exact = FALSE
  )$p.value
  record_check(
    "trivial statistical detection",
    wilcoxon_p < 0.05,
    sprintf("p=%.4g", wilcoxon_p)
  )
  record_check(
    "trivial median difference",
    abs(dec_median - jan_median) <= 10,
    sprintf("difference=%+.1f minutes", dec_median - jan_median)
  )
  record_check(
    "trivial p90 change",
    abs(p90_change) <= 10,
    sprintf("change=%+.1f%%", p90_change)
  )
  record_check(
    "trivial tail-share change",
    abs(tail_change) <= 2,
    sprintf("change=%+.1f percentage points", tail_change)
  )
}

cat(sprintf("Validation report: %s (%s variant)\n", input_path, variant))
print(checks, row.names = FALSE)
cat(sprintf(
  paste0(
    "January -> December: mean %.1f -> %.1f (%+.1f%%); ",
    "median %.1f -> %.1f (%+.1f%%); p90 %.1f -> %.1f (%+.1f%%); ",
    "over 8h %.1f%% -> %.1f%% (%+.1f points).\n"
  ),
  jan_mean,
  dec_mean,
  mean_change,
  jan_median,
  dec_median,
  median_change,
  jan_p90,
  dec_p90,
  p90_change,
  jan_tail,
  dec_tail,
  tail_change
))

if (!all(checks$passed)) {
  stop(sprintf("Validation failed: %d check(s).", sum(!checks$passed)), call. = FALSE)
}
cat(sprintf("PASS: %d checks passed.\n", nrow(checks)))
