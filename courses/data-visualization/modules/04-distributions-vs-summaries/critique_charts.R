args <- commandArgs(trailingOnly = TRUE)
input_path <- if (length(args) >= 1) args[[1]] else file.path("data", "ed_los_2026.csv")
output_dir <- if (length(args) >= 2) args[[2]] else file.path("outputs", "critique")

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
required_columns <- c("arrival_date", "esi", "disposition", "los_min")
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

if (!dir.exists(output_dir)) {
  dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
}
theme_module <- ggplot2::theme_minimal(base_size = 12) +
  ggplot2::theme(
    panel.grid.minor = ggplot2::element_blank(),
    plot.title.position = "plot"
  )

esi_mean <- stats::aggregate(los_min ~ esi, data, mean)
esi_sd <- stats::aggregate(los_min ~ esi, data, stats::sd)
esi_n <- stats::aggregate(los_min ~ esi, data, length)
names(esi_mean)[2] <- "mean_min"
names(esi_sd)[2] <- "sd_min"
names(esi_n)[2] <- "n"
esi_summary <- Reduce(function(left, right) merge(left, right, by = "esi"), list(
  esi_mean,
  esi_sd,
  esi_n
))
esi_summary$se_min <- esi_summary$sd_min / sqrt(esi_summary$n)
esi_summary$esi <- factor(esi_summary$esi)

plot_se <- ggplot2::ggplot(esi_summary, ggplot2::aes(x = esi, y = mean_min)) +
  ggplot2::geom_col(fill = "#1f49b6", width = 0.65) +
  ggplot2::geom_errorbar(
    ggplot2::aes(ymin = mean_min - se_min, ymax = mean_min + se_min),
    width = 0.2
  ) +
  ggplot2::labs(
    title = "Mean length of stay by ESI",
    subtitle = "Error bars show one standard error.",
    x = "Emergency Severity Index",
    y = "Mean length of stay (minutes)"
  ) +
  theme_module

monthly_mean <- stats::aggregate(los_min ~ month, data, mean)
plot_truncated <- ggplot2::ggplot(monthly_mean, ggplot2::aes(x = month, y = los_min)) +
  ggplot2::geom_line(color = "#b45309", linewidth = 1) +
  ggplot2::geom_point(color = "#b45309", size = 2.5) +
  ggplot2::coord_cartesian(ylim = c(180, 210)) +
  ggplot2::scale_x_date(date_breaks = "2 months", date_labels = "%b") +
  ggplot2::labs(
    title = "Monthly mean emergency department length of stay",
    x = "Arrival month in 2026",
    y = "Mean length of stay (minutes)"
  ) +
  theme_module

group_means <- stats::aggregate(los_min ~ disposition, data, mean)
reported_overall <- mean(group_means$los_min)
comparison <- rbind(
  data.frame(label = paste0(tools::toTitleCase(group_means$disposition), " mean"), value = group_means$los_min),
  data.frame(label = "Overall mean (reported)", value = reported_overall)
)
comparison$label <- factor(comparison$label, levels = rev(comparison$label))
plot_average <- ggplot2::ggplot(comparison, ggplot2::aes(x = label, y = value)) +
  ggplot2::geom_col(fill = "#0d9488", width = 0.65) +
  ggplot2::coord_flip() +
  ggplot2::labs(
    title = "Mean emergency department length of stay",
    x = NULL,
    y = "Mean length of stay (minutes)"
  ) +
  theme_module

plots <- list(
  `C1-mean-with-standard-error.png` = plot_se,
  `C2-truncated-monthly-mean.png` = plot_truncated,
  `C3-average-of-averages.png` = plot_average
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

cat("Created the critique charts in:", normalizePath(output_dir, winslash = "/"), "\n")
cat(sprintf(
  paste0(
    "C3 reported overall mean: %.1f minutes\n",
    "Correct pooled mean: %.1f minutes\n",
    "Difference: %.1f minutes\n\n"
  ),
  reported_overall,
  mean(data$los_min),
  reported_overall - mean(data$los_min)
))
cat(paste0(
  "For each display, ask:\n",
  "1. What does it conceal?\n",
  "2. Who could be affected by a decision based on it?\n",
  "3. What analysis or display should replace it?\n"
))
