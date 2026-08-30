args <- commandArgs(trailingOnly = TRUE)

option_value <- function(flag, default) {
  match <- which(args == flag)
  if (length(match) == 0) return(default)
  if (match[1] == length(args)) stop(flag, " requires a value")
  args[match[1] + 1]
}

if (!requireNamespace("ggplot2", quietly = TRUE)) {
  stop("Install ggplot2 before running this lab.")
}

script_arg <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
script_dir <- if (length(script_arg)) dirname(normalizePath(sub("^--file=", "", script_arg[1]))) else getwd()
data_path <- option_value("--data", file.path(script_dir, "data", "ma_hf_readmission_uncertainty_2026.csv"))
output_dir <- option_value("--output", file.path(script_dir, "output"))

if (!file.exists(data_path)) stop("Data file not found: ", data_path)
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

data <- read.csv(data_path, stringsAsFactors = FALSE, colClasses = c(facility_id = "character"), check.names = FALSE)
required <- c(
  "facility_id", "facility_name", "measure_id", "denominator", "score",
  "lower_estimate", "higher_estimate", "estimate_status", "source_comparison_group",
  "reported_rank_worst_first", "interval_width", "top_ten_point_rank"
)
missing <- setdiff(required, names(data))
if (length(missing)) stop("Missing required columns: ", paste(missing, collapse = ", "))
if (nrow(data) != 65) stop("Expected 65 Massachusetts rows; received ", nrow(data))

reported <- data[data$estimate_status == "reported", ]
if (nrow(reported) != 53) stop("Expected 53 reported rows; received ", nrow(reported))

reported$score <- as.numeric(reported$score)
reported$lower_estimate <- as.numeric(reported$lower_estimate)
reported$higher_estimate <- as.numeric(reported$higher_estimate)
reported$denominator <- as.numeric(reported$denominator)
reported$interval_width <- as.numeric(reported$interval_width)
reported$reported_rank_worst_first <- as.integer(reported$reported_rank_worst_first)
reported$source_comparison_group <- factor(
  reported$source_comparison_group,
  levels = c("better", "no different", "worse")
)

national_rate <- 21.3
palette <- c("better" = "#047857", "no different" = "#1f49b6", "worse" = "#b42318")
shapes <- c("better" = 17, "no different" = 16, "worse" = 18)
base_theme <- ggplot2::theme_minimal(base_size = 12) +
  ggplot2::theme(
    plot.title.position = "plot",
    plot.caption.position = "plot",
    panel.grid.minor = ggplot2::element_blank(),
    legend.position = "bottom",
    axis.text = ggplot2::element_text(color = "#0f172a")
  )

rank_labels <- reported[reported$reported_rank_worst_first %in% c(1, 2, 3, 53), ]
rank_labels$label_y <- c(25.55, 24.48, 24.18, 20.05)[match(
  rank_labels$reported_rank_worst_first,
  c(1, 2, 3, 53)
)]
point_rank <- ggplot2::ggplot(
  reported,
  ggplot2::aes(x = reported_rank_worst_first, y = score, color = source_comparison_group, shape = source_comparison_group)
) +
  ggplot2::geom_hline(yintercept = national_rate, color = "#475569", linewidth = 0.7, linetype = "dashed") +
  ggplot2::geom_line(ggplot2::aes(group = 1), color = "#cbd5e1", linewidth = 0.6) +
  ggplot2::geom_point(size = 2.8) +
  ggplot2::geom_text(
    data = rank_labels,
    ggplot2::aes(y = label_y, label = facility_name),
    hjust = ifelse(rank_labels$reported_rank_worst_first == 53, 1, 0),
    nudge_x = ifelse(rank_labels$reported_rank_worst_first == 53, -0.8, 0.8),
    size = 3,
    color = "#0f172a",
    show.legend = FALSE
  ) +
  ggplot2::annotate("text", x = 52, y = national_rate + 0.15, label = "National rate 21.3", hjust = 1, size = 3.2, color = "#475569") +
  ggplot2::scale_color_manual(values = palette, drop = FALSE) +
  ggplot2::scale_shape_manual(values = shapes, drop = FALSE) +
  ggplot2::scale_x_continuous(breaks = c(1, 10, 20, 30, 40, 53)) +
  ggplot2::labs(
    title = "A league table creates 53 positions from 53 estimates",
    subtitle = "Only one Massachusetts hospital is CMS-classified worse than the national rate",
    x = "Point-estimate rank, higher rate first",
    y = "Risk-standardized readmission rate",
    color = "CMS comparison",
    shape = "CMS comparison",
    caption = "CMS READM_30_HF, 2023-07-01 to 2025-06-30. Rank does not test separation."
  ) +
  base_theme

ordered <- reported[order(reported$score, reported$facility_name), ]
ordered$facility_name <- factor(ordered$facility_name, levels = ordered$facility_name)
interval_plot <- ggplot2::ggplot(
  ordered,
  ggplot2::aes(x = score, y = facility_name, color = source_comparison_group, shape = source_comparison_group)
) +
  ggplot2::geom_vline(xintercept = national_rate, color = "#475569", linewidth = 0.7, linetype = "dashed") +
  ggplot2::geom_errorbar(
    ggplot2::aes(xmin = lower_estimate, xmax = higher_estimate),
    orientation = "y", width = 0, linewidth = 0.55
  ) +
  ggplot2::geom_point(size = 2.2) +
  ggplot2::scale_color_manual(values = palette, drop = FALSE) +
  ggplot2::scale_shape_manual(values = shapes, drop = FALSE) +
  ggplot2::labs(
    title = "Intervals change the committee's question",
    subtitle = "Points are ordered, but the source intervals show how weakly most ranks are separated",
    x = "Risk-standardized readmission rate and CMS source interval",
    y = NULL,
    color = "CMS comparison",
    shape = "CMS comparison",
    caption = paste0(
      "Dashed line: national rate 21.3. CMS READM_30_HF, 2023-07-01 to 2025-06-30.\n",
      "Displayed interval overlap is descriptive and is not a pairwise hypothesis test."
    )
  ) +
  base_theme +
  ggplot2::theme(axis.text.y = ggplot2::element_text(size = 7.2), panel.grid.major.y = ggplot2::element_line(color = "#f1f5f9"))

small_labels <- reported[reported$denominator < 100, ]
small_labels$label_y <- c(7.42, 8.02, 8.68, 8.34)[match(
  small_labels$facility_name,
  c("FAIRVIEW HOSPITAL", "NANTUCKET COTTAGE HOSPITAL", "MARTHA'S VINEYARD HOSPITAL INC", "ATHOL MEMORIAL HOSPITAL")
)]
denominator_plot <- ggplot2::ggplot(reported, ggplot2::aes(x = denominator, y = interval_width)) +
  ggplot2::geom_point(ggplot2::aes(color = source_comparison_group, shape = source_comparison_group), size = 2.8, alpha = 0.9) +
  ggplot2::geom_text(
    data = small_labels,
    ggplot2::aes(y = label_y, label = facility_name),
    hjust = 0,
    size = 3,
    color = "#0f172a",
    show.legend = FALSE
  ) +
  ggplot2::scale_x_log10(breaks = c(30, 50, 100, 250, 500, 1000, 2000)) +
  ggplot2::scale_color_manual(values = palette, drop = FALSE) +
  ggplot2::scale_shape_manual(values = shapes, drop = FALSE) +
  ggplot2::labs(
    title = "Denominator informs precision but does not replace the model",
    subtitle = "Four reported hospitals have denominators under 100",
    x = "CMS denominator, log scale",
    y = "Source interval width",
    color = "CMS comparison",
    shape = "CMS comparison",
    caption = "Descriptive view only. Do not construct binomial or funnel limits from this chart."
  ) +
  base_theme

status <- data.frame(
  status = factor(
    c("Reported: no different", "Reported: worse", "Cases too small", "Not available"),
    levels = rev(c("Reported: no different", "Reported: worse", "Cases too small", "Not available"))
  ),
  count = c(52, 1, 2, 10),
  color = c("#1f49b6", "#b42318", "#b45309", "#64748b")
)
status_plot <- ggplot2::ggplot(status, ggplot2::aes(x = count, y = status, fill = color)) +
  ggplot2::geom_col(width = 0.65) +
  ggplot2::geom_text(ggplot2::aes(label = count), hjust = -0.25, size = 4) +
  ggplot2::scale_fill_identity() +
  ggplot2::scale_x_continuous(limits = c(0, 56), expand = ggplot2::expansion(mult = c(0, 0))) +
  ggplot2::labs(
    title = "All 65 hospital rows remain in the decision record",
    subtitle = "Twelve rows do not have a public estimate in this release",
    x = "Massachusetts hospitals",
    y = NULL,
    caption = "CMS READM_30_HF. A missing public estimate is not a zero rate."
  ) +
  base_theme +
  ggplot2::theme(panel.grid.major.y = ggplot2::element_blank())

ggplot2::ggsave(file.path(output_dir, "01-point-rank.png"), point_rank, width = 11, height = 7, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "02-interval-caterpillar.png"), interval_plot, width = 12, height = 14, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "03-denominator-and-width.png"), denominator_plot, width = 11, height = 7, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "04-reporting-status.png"), status_plot, width = 10, height = 6, dpi = 150, bg = "white")

decision_table <- data[order(is.na(data$reported_rank_worst_first), data$reported_rank_worst_first, data$facility_name), c(
  "facility_id", "facility_name", "reported_rank_worst_first", "score", "lower_estimate",
  "higher_estimate", "denominator", "source_comparison_group", "estimate_status",
  "footnote_code", "footnote_text", "start_date", "end_date"
)]
write.csv(decision_table, file.path(output_dir, "ma_hf_uncertainty_decision_table.csv"), row.names = FALSE, na = "")

cat("Created four figures and one decision table in:", normalizePath(output_dir, winslash = "/"), "\n")
