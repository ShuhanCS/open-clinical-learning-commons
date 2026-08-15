args <- commandArgs(trailingOnly = TRUE)
variant <- if (length(args) >= 1) args[[1]] else "real"
seed <- if (length(args) >= 2) suppressWarnings(as.integer(args[[2]])) else 730L
output_path <- if (length(args) >= 3) args[[3]] else file.path("data", "ed_los_2026.csv")

allowed_variants <- c("real", "null", "trivial")
if (!variant %in% allowed_variants) {
  stop("Variant must be one of: real, null, trivial", call. = FALSE)
}
if (is.na(seed)) {
  stop("Seed must be an integer.", call. = FALSE)
}

# These are teaching parameters, not estimates from a hospital or patient dataset.
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
  discharged_medians <- seq(164, 102, length.out = 12)
  boarding_rates <- seq(0.10, 0.46, length.out = 12)
  monthly_scale <- rep(1, 12)
} else if (variant == "null") {
  discharged_medians <- rep(132, 12)
  boarding_rates <- rep(0.24, 12)
  monthly_scale <- rep(1, 12)
} else {
  discharged_medians <- rep(132, 12)
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
  "Generated %s with %s synthetic encounters (variant=%s, seed=%d).\n",
  normalizePath(output_path, winslash = "/", mustWork = FALSE),
  format(nrow(data), big.mark = ","),
  variant,
  seed
))
