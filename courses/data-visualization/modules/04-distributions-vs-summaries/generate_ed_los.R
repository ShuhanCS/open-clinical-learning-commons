args <- commandArgs(trailingOnly = TRUE)
variant <- if (length(args) >= 1) args[[1]] else "real"
seed <- if (length(args) >= 2) suppressWarnings(as.integer(args[[2]])) else 730L
output_path <- if (length(args) >= 3) args[[3]] else file.path("data", "ed_los_2026.csv")
default_calibration <- c(file.path("data", "cms_ed_op18b_2026.csv"), "cms_ed_op18b_2026.csv")
available_calibration <- default_calibration[file.exists(default_calibration)][1]
calibration_path <- if (length(args) >= 4) args[[4]] else if (!is.na(available_calibration)) available_calibration else default_calibration[[1]]

allowed_variants <- c("real", "null", "trivial")
if (!variant %in% allowed_variants) {
  stop("Variant must be one of: real, null, trivial", call. = FALSE)
}
if (is.na(seed)) {
  stop("Seed must be an integer.", call. = FALSE)
}
if (!file.exists(calibration_path)) {
  stop(sprintf("CMS OP_18b calibration file not found: %s", calibration_path), call. = FALSE)
}

calibration <- utils::read.csv(calibration_path, stringsAsFactors = FALSE, na.strings = "")
required_calibration_columns <- c("measure_id", "score_min", "value_status", "cms_release_date")
missing_calibration_columns <- setdiff(required_calibration_columns, names(calibration))
if (length(missing_calibration_columns) > 0) {
  stop(
    sprintf("Calibration file is missing columns: %s", paste(missing_calibration_columns, collapse = ", ")),
    call. = FALSE
  )
}
reported_calibration <- calibration[
  calibration$measure_id == "OP_18b" &
    calibration$value_status == "reported" &
    is.finite(calibration$score_min),
  ,
  drop = FALSE
]
if (nrow(reported_calibration) != 4081L || !all(calibration$cms_release_date == "2026-08-13")) {
  stop("Calibration file does not match the pinned CMS OP_18b release.", call. = FALSE)
}
discharged_anchor_median <- stats::median(reported_calibration$score_min)

# The discharged center is anchored to the national CMS OP_18b hospital median.
# The monthly change, pathway spreads, admission process, and boarding process remain teaching assumptions.
discharged_counts <- c(rep(539L, 6), rep(538L, 6))
admitted_counts <- c(rep(161L, 10), 160L, 160L)
nonboarded_median <- 252
boarded_median <- 782
discharged_sdlog <- 0.35
nonboarded_sdlog <- 0.18
boarded_sdlog <- 0.23

set.seed(seed)

lognormal_values <- function(n, median_minutes, sdlog) {
  probabilities <- (seq_len(n) - 0.5) / n
  values <- round(stats::qlnorm(probabilities, log(median_minutes), sdlog))
  sample(pmax(1L, as.integer(values)), n, replace = FALSE)
}

month_dates <- function(year, month, n) {
  first <- as.Date(sprintf("%04d-%02d-01", year, month))
  next_month <- seq(first, by = "month", length.out = 2)[2]
  sample(seq(first, next_month - 1, by = "day"), n, replace = TRUE)
}

if (variant == "real") {
  discharged_medians <- seq(discharged_anchor_median + 31, discharged_anchor_median - 31, length.out = 12)
  boarding_rates <- seq(0.10, 0.46, length.out = 12)
  monthly_scale <- rep(1, 12)
} else if (variant == "null") {
  discharged_medians <- rep(discharged_anchor_median, 12)
  boarding_rates <- rep(0.24, 12)
  monthly_scale <- rep(1, 12)
} else {
  discharged_medians <- rep(discharged_anchor_median, 12)
  boarding_rates <- rep(0.24, 12)
  monthly_scale <- seq(1, 1.06, length.out = 12)
}

monthly_frames <- vector("list", 12)
for (month in seq_len(12)) {
  n_discharged <- discharged_counts[[month]]
  n_admitted <- admitted_counts[[month]]
  n_boarded <- round(n_admitted * boarding_rates[[month]])
  n_nonboarded <- n_admitted - n_boarded
  scale <- monthly_scale[[month]]

  discharged <- data.frame(
    arrival_date = month_dates(2026, month, n_discharged),
    disposition = "discharged",
    boarded = 0L,
    los_min = lognormal_values(
      n_discharged,
      discharged_medians[[month]] * scale,
      discharged_sdlog
    ),
    stringsAsFactors = FALSE
  )

  admitted_nonboarded <- data.frame(
    arrival_date = month_dates(2026, month, n_nonboarded),
    disposition = "admitted",
    boarded = 0L,
    los_min = lognormal_values(
      n_nonboarded,
      nonboarded_median * scale,
      nonboarded_sdlog
    ),
    stringsAsFactors = FALSE
  )

  admitted_boarded <- data.frame(
    arrival_date = month_dates(2026, month, n_boarded),
    disposition = "admitted",
    boarded = 1L,
    los_min = lognormal_values(
      n_boarded,
      boarded_median * scale,
      boarded_sdlog
    ),
    stringsAsFactors = FALSE
  )

  monthly_frames[[month]] <- rbind(
    discharged,
    admitted_nonboarded,
    admitted_boarded
  )
}

data <- do.call(rbind, monthly_frames)

esi_counts <- c(`1` = 66L, `2` = 1030L, `3` = 3974L, `4` = 2500L, `5` = 822L)
age_counts <- c(`18-39` = 2500L, `40-64` = 3000L, `65-79` = 1900L, `80+` = 992L)
data$esi <- sample(rep(as.integer(names(esi_counts)), esi_counts))
data$age_group <- sample(rep(names(age_counts), age_counts))

data <- data[sample(seq_len(nrow(data))), , drop = FALSE]
data$encounter_id <- sprintf("ED26-%05d", seq_len(nrow(data)))
data <- data[, c(
  "encounter_id",
  "arrival_date",
  "esi",
  "age_group",
  "disposition",
  "boarded",
  "los_min"
)]

output_dir <- dirname(output_path)
if (!dir.exists(output_dir)) {
  dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
}
utils::write.csv(data, output_path, row.names = FALSE, eol = "\n")

cat(sprintf(
  "Generated %s with %s synthetic encounters (variant=%s, seed=%d, CMS OP_18b anchor=%d minutes).\n",
  normalizePath(output_path, winslash = "/", mustWork = FALSE),
  format(nrow(data), big.mark = ","),
  variant,
  seed,
  discharged_anchor_median
))
