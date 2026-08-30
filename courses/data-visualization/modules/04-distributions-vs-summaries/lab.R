args <- commandArgs(trailingOnly = TRUE)
default_inputs <- c(file.path("data", "ed_los_2026.csv"), "ed_los_2026.csv")
available_default <- default_inputs[file.exists(default_inputs)][1]
input_path <- if (length(args) >= 1) args[[1]] else if (!is.na(available_default)) available_default else default_inputs[[1]]
output_dir <- if (length(args) >= 2) args[[2]] else file.path("outputs", "lab")

if (!requireNamespace("ggplot2", quietly = TRUE)) {
  stop(
    "Package 'ggplot2' is required. Install it with: install.packages('ggplot2')",
    call. = FALSE
  )
}
if (!file.exists(input_path)) {
  stop(sprintf("Data file not found: %s", input_path), call. = FALSE)
}

data <- utils::read.csv(input_path, stringsAsFactors = FALSE)
required_columns <- c(
  "encounter_id",
  "arrival_date",
  "esi",
  "age_group",
  "disposition",
  "boarded",
  "los_min"
)
missing_columns <- setdiff(required_columns, names(data))
if (length(missing_columns) > 0) {
  stop(
    sprintf("Input is missing required columns: %s", paste(missing_columns, collapse = ", ")),
    call. = FALSE
  )
}
if (nrow(data) == 0 || anyNA(data[required_columns]) || any(data$los_min <= 0)) {
  stop("Input must contain complete rows and positive length-of-stay values.", call. = FALSE)
}

data$arrival_date <- as.Date(data$arrival_date)
if (anyNA(data$arrival_date)) {
  stop("arrival_date must use YYYY-MM-DD dates.", call. = FALSE)
}
data$month <- as.Date(format(data$arrival_date, "%Y-%m-01"))

monthly <- do.call(rbind, lapply(split(data$los_min, data$month), function(values) {
  data.frame(
    mean_min = mean(values),
    median_min = stats::median(values),
    p90_min = as.numeric(stats::quantile(values, 0.90, names = FALSE)),
    over_8h_pct = 100 * mean(values > 480)
  )
}))
monthly$month <- as.Date(rownames(monthly))
rownames(monthly) <- NULL
monthly <- monthly[, c("month", "mean_min", "median_min", "p90_min", "over_8h_pct")]

if (!dir.exists(output_dir)) {
  dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
}
utils::write.csv(monthly, file.path(output_dir, "monthly_metrics.csv"), row.names = FALSE)

theme_module <- ggplot2::theme_minimal(base_size = 12) +
  ggplot2::theme(
    panel.grid.minor = ggplot2::element_blank(),
    plot.title.position = "plot"
  )

plot_monthly_mean <- ggplot2::ggplot(monthly, ggplot2::aes(x = month, y = mean_min)) +
  ggplot2::geom_col(fill = "#1f49b6", width = 25) +
  ggplot2::scale_x_date(date_breaks = "2 months", date_labels = "%b") +
  ggplot2::labs(
    title = "Monthly mean emergency department length of stay",
    x = "Arrival month in 2026",
    y = "Mean length of stay (minutes)"
  ) +
  theme_module

plot_histogram <- ggplot2::ggplot(data, ggplot2::aes(x = los_min)) +
  ggplot2::geom_histogram(binwidth = 30, fill = "#0d9488", color = "white") +
  ggplot2::coord_cartesian(xlim = c(0, stats::quantile(data$los_min, 0.995))) +
  ggplot2::labs(
    title = "Distribution of emergency-department length of stay",
    subtitle = "Each row is a synthetic encounter. The view ends at the 99.5th percentile; no rows were removed.",
    x = "Length of stay (minutes)",
    y = "Synthetic encounters"
  ) +
  theme_module

plot_density <- ggplot2::ggplot(
  data,
  ggplot2::aes(x = los_min, color = disposition, linetype = disposition)
) +
  ggplot2::geom_density(linewidth = 1) +
  ggplot2::coord_cartesian(xlim = c(0, stats::quantile(data$los_min, 0.995))) +
  ggplot2::scale_color_manual(values = c(admitted = "#d97706", discharged = "#1f49b6")) +
  ggplot2::labs(
    title = "Admitted and discharged patients follow different length-of-stay patterns",
    subtitle = "Disposition identifies the care pathway. Line type repeats the color distinction.",
    x = "Length of stay (minutes)",
    y = "Density",
    color = "Disposition",
    linetype = "Disposition"
  ) +
  theme_module

metric_data <- rbind(
  data.frame(month = monthly$month, measure = "Mean (minutes)", value = monthly$mean_min),
  data.frame(month = monthly$month, measure = "Median (minutes)", value = monthly$median_min),
  data.frame(month = monthly$month, measure = "90th percentile (minutes)", value = monthly$p90_min),
  data.frame(month = monthly$month, measure = "Over 8 hours (percent)", value = monthly$over_8h_pct)
)
metric_data$measure <- factor(metric_data$measure, levels = c(
  "Mean (minutes)",
  "Median (minutes)",
  "90th percentile (minutes)",
  "Over 8 hours (percent)"
))
plot_metrics <- ggplot2::ggplot(metric_data, ggplot2::aes(x = month, y = value)) +
  ggplot2::geom_line(color = "#1f49b6", linewidth = 0.9) +
  ggplot2::geom_point(color = "#0d9488", size = 2) +
  ggplot2::facet_wrap(~measure, scales = "free_y", ncol = 2) +
  ggplot2::scale_x_date(date_breaks = "3 months", date_labels = "%b") +
  ggplot2::labs(
    title = "Typical emergency-department visits improve while the longest stays worsen",
    x = "Arrival month in 2026",
    y = NULL
  ) +
  theme_module

plots <- list(
  `01-monthly-mean.png` = plot_monthly_mean,
  `02-pooled-histogram.png` = plot_histogram,
  `03-density-by-disposition.png` = plot_density,
  `04-monthly-metrics.png` = plot_metrics
)
for (filename in names(plots)) {
  ggplot2::ggsave(
    file.path(output_dir, filename),
    plots[[filename]],
    width = 9,
    height = 5.5,
    dpi = 150,
    bg = "white"
  )
}

cat("Created the Tier 1 lab outputs in:", normalizePath(output_dir, winslash = "/"), "\n")
print(monthly, row.names = FALSE, digits = 1)
cat(paste0(
  "\nDiscuss:\n",
  "1. If the chief operating officer saw only the monthly mean, what would they conclude about emergency-department flow?\n",
  "2. Which patient experiences become visible in the pooled histogram, and which care processes remain hard to identify?\n",
  "3. How do admitted and discharged encounters differ, and which group creates the second process?\n",
  "4. Which measures describe the typical visit, the longest waits, and the share crossing an eight-hour service threshold?\n",
  "5. Split the trends by disposition and boarding status. What should fast-track, patient-flow, and bed-management leaders do differently?\n"
))
