args <- commandArgs(trailingOnly = TRUE)

option_value <- function(flag, default) {
  match <- which(args == flag)
  if (length(match) == 0) return(default)
  if (match[1] == length(args)) stop(flag, " requires a value")
  args[match[1] + 1]
}

if (!requireNamespace("ggplot2", quietly = TRUE)) stop("Install ggplot2 before running this critique set.")

script_arg <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
script_dir <- if (length(script_arg)) dirname(normalizePath(sub("^--file=", "", script_arg[1]))) else getwd()
data_path <- option_value("--data", file.path(script_dir, "data", "ma_hospital_capacity_time_2024_2026.csv"))
output_dir <- option_value("--output", file.path(script_dir, "critique-output"))

data <- read.csv(data_path, stringsAsFactors = FALSE)
if (nrow(data) != 94) stop("Expected 94 Massachusetts weeks.")
data$week_end <- as.Date(data$week_end)
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

scale_factor <- max(data$total_respiratory_new_admissions) / max(data$inpatient_occupancy_pct)
dual_axis <- ggplot2::ggplot(data, ggplot2::aes(x = week_end)) +
  ggplot2::geom_line(ggplot2::aes(y = inpatient_occupancy_pct), color = "#2166AC", linewidth = 1) +
  ggplot2::geom_line(ggplot2::aes(y = total_respiratory_new_admissions / scale_factor), color = "#B2182B", linewidth = 1) +
  ggplot2::scale_y_continuous(
    name = "Occupancy percent",
    sec.axis = ggplot2::sec_axis(~ . * scale_factor, name = "Respiratory admissions")
  ) +
  ggplot2::labs(
    title = "FLAWED: arbitrary dual axes manufacture visual agreement",
    subtitle = "The scale factor was chosen only to overlap the lines",
    x = NULL
  ) +
  ggplot2::theme_minimal(base_size = 11) +
  ggplot2::theme(axis.text.y.right = ggplot2::element_text(color = "#B2182B"), axis.text.y.left = ggplot2::element_text(color = "#2166AC"))

rolling <- rep(NA_real_, nrow(data))
for (index in seq_len(nrow(data))) if (index >= 4) rolling[index] <- mean(data$inpatient_occupancy_pct[(index - 3):index])
smoothed_only <- ggplot2::ggplot(data, ggplot2::aes(x = week_end, y = rolling)) +
  ggplot2::geom_line(color = "#2166AC", linewidth = 1.2, na.rm = TRUE) +
  ggplot2::coord_cartesian(ylim = c(80, 88)) +
  ggplot2::labs(
    title = "FLAWED: smoothing removes the weekly operational question",
    subtitle = "Only a four-week trailing mean is shown",
    x = NULL,
    y = "Smoothed occupancy percent"
  ) +
  ggplot2::theme_minimal(base_size = 11)

invented_limits <- ggplot2::ggplot(data, ggplot2::aes(x = week_end, y = inpatient_occupancy_pct)) +
  ggplot2::geom_hline(yintercept = 82, color = "#333333") +
  ggplot2::geom_hline(yintercept = c(80, 84), color = "#B2182B", linetype = "dashed") +
  ggplot2::geom_line(color = "#2166AC", linewidth = 0.9) +
  ggplot2::geom_point(ggplot2::aes(color = inpatient_occupancy_pct > 84 | inpatient_occupancy_pct < 80), size = 2) +
  ggplot2::scale_color_manual(values = c("FALSE" = "#2166AC", "TRUE" = "#B2182B"), guide = "none") +
  ggplot2::labs(
    title = "FLAWED: invented control limits turn ordinary values into alarms",
    subtitle = "No baseline, method, seasonality check, or reporting-coverage review",
    x = NULL,
    y = "Inpatient occupancy percent"
  ) +
  ggplot2::theme_minimal(base_size = 11)

ggplot2::ggsave(file.path(output_dir, "C1-arbitrary-dual-axis.png"), dual_axis, width = 11, height = 6, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "C2-smoothed-line-hides-weekly-change.png"), smoothed_only, width = 11, height = 6, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "C3-unsupported-control-limits.png"), invented_limits, width = 11, height = 6, dpi = 150, bg = "white")

cat("Created three deliberately flawed time figures in:", normalizePath(output_dir, winslash = "/"), "\n")
