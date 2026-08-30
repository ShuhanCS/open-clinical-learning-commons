args <- commandArgs(trailingOnly = TRUE)

option_value <- function(flag, default) {
  match <- which(args == flag)
  if (length(match) == 0) return(default)
  if (match[1] == length(args)) stop(flag, " requires a value")
  args[match[1] + 1]
}

if (!requireNamespace("ggplot2", quietly = TRUE)) stop("Install ggplot2 before running this lab.")

script_arg <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
script_dir <- if (length(script_arg)) dirname(normalizePath(sub("^--file=", "", script_arg[1]))) else getwd()
data_path <- option_value("--data", file.path(script_dir, "data", "ma_hospital_capacity_time_2024_2026.csv"))
output_dir <- option_value("--output", file.path(script_dir, "output"))

if (!file.exists(data_path)) stop("Data file not found: ", data_path)
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

data <- read.csv(data_path, stringsAsFactors = FALSE, check.names = FALSE)
required <- c(
  "week_end", "jurisdiction", "inpatient_occupancy_pct", "icu_occupancy_pct",
  "covid_new_admissions", "flu_new_admissions", "rsv_new_admissions",
  "total_respiratory_new_admissions", "hospitals_reporting_occupancy_pct",
  "source_season_status"
)
missing <- setdiff(required, names(data))
if (length(missing)) stop("Missing required columns: ", paste(missing, collapse = ", "))
if (nrow(data) != 94 || any(data$jurisdiction != "MA")) stop("Expected 94 Massachusetts weekly rows.")

data$week_end <- as.Date(data$week_end)
if (any(diff(data$week_end) != 7)) stop("The Massachusetts source must remain a complete weekly sequence.")

rolling_mean <- function(values, width = 4) {
  result <- rep(NA_real_, length(values))
  for (index in seq_along(values)) {
    if (index >= width) result[index] <- mean(values[(index - width + 1):index])
  }
  result
}

data$occupancy_rolling_4_week <- rolling_mean(data$inpatient_occupancy_pct)
data$respiratory_rolling_4_week <- rolling_mean(data$total_respiratory_new_admissions)
data$occupancy_delta_pct_points <- c(NA_real_, diff(data$inpatient_occupancy_pct))

baseline <- data[1:26, ]
baseline_center <- mean(baseline$inpatient_occupancy_pct)
moving_range_bar <- mean(abs(diff(baseline$inpatient_occupancy_pct)))
sigma_estimate <- moving_range_bar / 1.128
lower_limit <- baseline_center - 3 * sigma_estimate
upper_limit <- baseline_center + 3 * sigma_estimate
data$outside_exploratory_limits <- data$inpatient_occupancy_pct < lower_limit | data$inpatient_occupancy_pct > upper_limit

theme_time <- ggplot2::theme_minimal(base_size = 11) +
  ggplot2::theme(
    panel.grid.minor = ggplot2::element_blank(),
    plot.title.position = "plot",
    plot.caption.position = "plot",
    legend.position = "top"
  )

median_occupancy <- median(data$inpatient_occupancy_pct)
occupancy_run <- ggplot2::ggplot(data, ggplot2::aes(x = week_end, y = inpatient_occupancy_pct)) +
  ggplot2::geom_hline(yintercept = median_occupancy, color = "#4D4D4D", linetype = "dashed", linewidth = 0.7) +
  ggplot2::geom_line(color = "#2166AC", linewidth = 0.8) +
  ggplot2::geom_point(color = "#2166AC", size = 1.7) +
  ggplot2::annotate(
    "text",
    x = min(data$week_end) + 21,
    y = median_occupancy + 0.25,
    label = sprintf("Series median %.2f%%", median_occupancy),
    color = "#333333",
    hjust = 0,
    size = 3.5
  ) +
  ggplot2::labs(
    title = "Massachusetts inpatient occupancy changes week by week",
    subtitle = "A run chart keeps the raw weekly values and an honest percent scale",
    x = NULL,
    y = "Inpatient beds occupied (%)",
    caption = paste(
      "CDC NHSN weekly jurisdiction data, 2024-11-09 through 2026-08-22.",
      "The median is descriptive, not a target or control limit."
    )
  ) +
  ggplot2::scale_x_date(date_breaks = "3 months", date_labels = "%Y-%m") +
  ggplot2::coord_cartesian(ylim = c(75, 90)) +
  theme_time

admissions <- rbind(
  data.frame(week_end = data$week_end, pathogen = "COVID-19", admissions = data$covid_new_admissions),
  data.frame(week_end = data$week_end, pathogen = "Influenza", admissions = data$flu_new_admissions),
  data.frame(week_end = data$week_end, pathogen = "RSV", admissions = data$rsv_new_admissions)
)
admissions$pathogen <- factor(admissions$pathogen, levels = c("COVID-19", "Influenza", "RSV"))
pathogen_colors <- c("COVID-19" = "#2166AC", "Influenza" = "#B2182B", "RSV" = "#1B7837")
pathogen_lines <- c("COVID-19" = "solid", "Influenza" = "longdash", "RSV" = "dotdash")

admission_seasonality <- ggplot2::ggplot(admissions, ggplot2::aes(x = week_end, y = admissions, color = pathogen, linetype = pathogen)) +
  ggplot2::geom_line(linewidth = 0.85) +
  ggplot2::scale_color_manual(values = pathogen_colors) +
  ggplot2::scale_linetype_manual(values = pathogen_lines) +
  ggplot2::scale_x_date(date_breaks = "3 months", date_labels = "%Y-%m") +
  ggplot2::labs(
    title = "The winter admission peak is not one respiratory process",
    subtitle = "Color and line type separate weekly COVID-19, influenza, and RSV admissions",
    x = NULL,
    y = "New hospital admissions",
    color = "Source count",
    linetype = "Source count",
    caption = "Counts are aggregated across reporting Massachusetts hospitals. Reporting coverage changes over time."
  ) +
  theme_time

smooth_data <- rbind(
  data.frame(week_end = data$week_end, series = "Raw week", occupancy = data$inpatient_occupancy_pct),
  data.frame(week_end = data$week_end, series = "Four-week trailing mean", occupancy = data$occupancy_rolling_4_week)
)
smooth_data$series <- factor(smooth_data$series, levels = c("Raw week", "Four-week trailing mean"))

smoothing <- ggplot2::ggplot(smooth_data, ggplot2::aes(x = week_end, y = occupancy, color = series, linetype = series)) +
  ggplot2::geom_line(linewidth = 0.9, na.rm = TRUE) +
  ggplot2::geom_point(
    data = smooth_data[smooth_data$series == "Raw week", ],
    size = 1.3,
    na.rm = TRUE
  ) +
  ggplot2::scale_color_manual(values = c("Raw week" = "#2166AC", "Four-week trailing mean" = "#B2182B")) +
  ggplot2::scale_linetype_manual(values = c("Raw week" = "solid", "Four-week trailing mean" = "longdash")) +
  ggplot2::scale_x_date(date_breaks = "3 months", date_labels = "%Y-%m") +
  ggplot2::coord_cartesian(ylim = c(75, 90)) +
  ggplot2::labs(
    title = "Smoothing changes the question",
    subtitle = "The trailing mean shows direction but softens abrupt weekly changes",
    x = NULL,
    y = "Inpatient beds occupied (%)",
    color = NULL,
    linetype = NULL,
    caption = "Keep raw values visible when short operational changes matter. The first three smoothed weeks are unavailable by design."
  ) +
  theme_time

context <- rbind(
  data.frame(week_end = data$week_end, metric = "Inpatient occupancy", value = data$inpatient_occupancy_pct),
  data.frame(week_end = data$week_end, metric = "Hospitals reporting occupancy", value = data$hospitals_reporting_occupancy_pct)
)
context$metric <- factor(context$metric, levels = c("Inpatient occupancy", "Hospitals reporting occupancy"))

coverage_context <- ggplot2::ggplot(context, ggplot2::aes(x = week_end, y = value, group = metric)) +
  ggplot2::geom_line(color = "#244F7A", linewidth = 0.85) +
  ggplot2::geom_point(color = "#244F7A", size = 1.2) +
  ggplot2::facet_grid(metric ~ ., scales = "free_y") +
  ggplot2::scale_x_date(date_breaks = "3 months", date_labels = "%Y-%m") +
  ggplot2::labs(
    title = "Read the process measure beside reporting coverage",
    subtitle = "Aligned panels keep separate percent scales without a dual axis",
    x = NULL,
    y = "Percent",
    caption = "A change in the mix of reporting hospitals can affect a jurisdiction aggregate. Coverage is context, not a correction weight."
  ) +
  theme_time +
  ggplot2::theme(strip.text.y = ggplot2::element_text(angle = 0, hjust = 0))

data$signal_label <- ifelse(data$outside_exploratory_limits, "Outside limits", "Inside limits")
exploratory_control <- ggplot2::ggplot(data, ggplot2::aes(x = week_end, y = inpatient_occupancy_pct)) +
  ggplot2::geom_hline(yintercept = baseline_center, color = "#333333", linewidth = 0.75) +
  ggplot2::geom_hline(yintercept = c(lower_limit, upper_limit), color = "#B2182B", linetype = "dashed", linewidth = 0.7) +
  ggplot2::geom_line(color = "#2166AC", linewidth = 0.75) +
  ggplot2::geom_point(ggplot2::aes(shape = signal_label), color = "#111111", size = 2) +
  ggplot2::scale_shape_manual(values = c("Inside limits" = 16, "Outside limits" = 17)) +
  ggplot2::scale_x_date(date_breaks = "3 months", date_labels = "%Y-%m") +
  ggplot2::labs(
    title = "EXPLORATORY: baseline limits create questions, not a special-cause verdict",
    subtitle = sprintf("First 26 weeks: center %.2f%%, lower %.2f%%, upper %.2f%%", baseline_center, lower_limit, upper_limit),
    x = NULL,
    y = "Inpatient beds occupied (%)",
    shape = NULL,
    caption = paste(
      "Individuals-chart limits use mean moving range / 1.128 for a declared teaching baseline.",
      "Seasonality, changing reporting coverage, and an aggregate jurisdiction mix weaken a formal SPC claim."
    )
  ) +
  theme_time

ggplot2::ggsave(file.path(output_dir, "01-occupancy-run-chart.png"), occupancy_run, width = 11, height = 6.5, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "02-respiratory-admission-seasonality.png"), admission_seasonality, width = 11, height = 6.5, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "03-raw-and-smoothed-occupancy.png"), smoothing, width = 11, height = 6.5, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "04-reporting-coverage-context.png"), coverage_context, width = 11, height = 8, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "05-exploratory-control-chart.png"), exploratory_control, width = 11, height = 6.5, dpi = 150, bg = "white")

table_fields <- c(
  "week_end", "inpatient_occupancy_pct", "occupancy_rolling_4_week",
  "occupancy_delta_pct_points", "icu_occupancy_pct", "covid_new_admissions",
  "flu_new_admissions", "rsv_new_admissions", "total_respiratory_new_admissions",
  "hospitals_reporting_occupancy", "hospitals_reporting_occupancy_pct",
  "respiratory_season", "source_season_status", "outside_exploratory_limits"
)
utils::write.csv(data[table_fields], file.path(output_dir, "weekly_time_decision_table.csv"), row.names = FALSE, na = "")

max_occ <- data[which.max(data$inpatient_occupancy_pct), ]
min_coverage <- data[which.min(data$hospitals_reporting_occupancy_pct), ]
max_admissions <- data[which.max(data$total_respiratory_new_admissions), ]
alt_text <- c(
  "# Reference text alternative",
  "",
  "## Short alternative",
  "",
  paste(
    "Weekly Massachusetts inpatient occupancy from November 2024 through August 2026 ranges from 77.96 to 87.30 percent.",
    "A winter rise in respiratory admissions is visible, but reporting coverage changes and an aggregate hospital mix limit causal and process-control claims."
  ),
  "",
  "## Long description",
  "",
  sprintf(
    "The run chart contains 94 weekly observations from %s through %s with no missing week in the Massachusetts sequence.",
    min(data$week_end), max(data$week_end)
  ),
  "",
  sprintf(
    "Inpatient occupancy reaches %.2f percent for the week ending %s. The series median is %.2f percent.",
    max_occ$inpatient_occupancy_pct, max_occ$week_end, median_occupancy
  ),
  "",
  sprintf(
    "Combined COVID-19, influenza, and RSV admissions reach %d for the week ending %s.",
    max_admissions$total_respiratory_new_admissions, max_admissions$week_end
  ),
  "",
  sprintf(
    "The share of hospitals reporting occupancy reaches a low of %.2f percent for the week ending %s, so coverage must be read beside the process measure.",
    min_coverage$hospitals_reporting_occupancy_pct, min_coverage$week_end
  ),
  "",
  paste(
    "A four-week trailing mean makes the broad direction easier to see but softens abrupt weekly changes.",
    "Exploratory individuals-chart limits are shown only to test assumptions and generate review questions."
  ),
  "",
  "See weekly_time_decision_table.csv for every weekly value, reporting context, smoothing value, and exploratory limit flag."
)
writeLines(alt_text, file.path(output_dir, "alt-text-reference.md"), useBytes = TRUE)

cat("Created five figures, one decision table, and one text alternative in:", normalizePath(output_dir, winslash = "/"), "\n")
