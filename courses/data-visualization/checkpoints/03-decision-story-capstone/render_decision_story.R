args <- commandArgs(trailingOnly = TRUE)
option_value <- function(flag, default) {
  index <- match(flag, args)
  if (is.na(index) || index == length(args)) default else args[[index + 1]]
}

script_arg <- commandArgs(FALSE)[grep("^--file=", commandArgs(FALSE))][1]
script_path <- normalizePath(sub("^--file=", "", script_arg), mustWork = TRUE)
submission_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
data_path <- option_value("--data", file.path(submission_root, "data", "ma_ed_public_reporting_dashboard_2026.csv"))
output_dir <- option_value("--output", submission_root)
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

if (!requireNamespace("ggplot2", quietly = TRUE)) stop("Package ggplot2 is required.")
data <- read.csv(data_path, check.names = FALSE)
required <- c("facility_id", "facility_name", "measure_id", "display_label", "unit", "score_raw", "score_numeric", "value_status", "sample", "footnote", "period_start", "period_end", "cms_release_date", "ma_reported_n", "ma_median", "ma_rank_unfavorable", "selected_hospital", "scenario_threshold", "threshold_crossed", "threshold_origin", "source_lag_days_at_release", "monitoring_use", "action_if_crossed")
if (!all(required %in% names(data))) stop("The final checkpoint teaching table is missing required fields.")
if (nrow(data) != 186) stop("Expected 186 released teaching rows.")

selected <- data[data$selected_hospital == "yes", , drop = FALSE]
if (nrow(selected) != 3) stop("Expected three selected-facility rows.")
op22 <- data[data$measure_id == "OP_22" & data$value_status == "reported", , drop = FALSE]
op22$score_numeric <- as.numeric(op22$score_numeric)
op22 <- op22[order(op22$score_numeric, op22$facility_name), , drop = FALSE]
op22$peer_order <- seq_len(nrow(op22))
op22$is_selected <- op22$facility_id == "220029"
if (nrow(op22) != 53 || sum(op22$is_selected) != 1) stop("Expected 53 reported OP-22 peers and one selected hospital.")

technical <- ggplot2::ggplot(op22, ggplot2::aes(x = score_numeric, y = peer_order)) +
  ggplot2::geom_vline(xintercept = 3, color = "#64748b", linetype = "dashed", linewidth = 0.8) +
  ggplot2::geom_vline(xintercept = 10, color = "#b45309", linetype = "dotted", linewidth = 1.0) +
  ggplot2::geom_point(color = "#94a3b8", size = 2.5) +
  ggplot2::geom_point(data = op22[op22$is_selected, , drop = FALSE], color = "#1f49b6", shape = 18, size = 5) +
  ggplot2::annotate("label", x = 23, y = 48, label = "Anna Jaques Hospital\n23% public OP-22", hjust = 1, color = "#1f49b6", fill = "white", linewidth = 0.2, size = 4.1) +
  ggplot2::annotate("text", x = 3, y = 4, label = "MA median: 3%\nDescriptive, not a benchmark", hjust = -0.05, vjust = 0, color = "#475569", size = 3.5) +
  ggplot2::annotate("text", x = 10, y = 16, label = "Mock review trigger: 10%\nNot a CMS threshold", hjust = -0.05, vjust = 0, color = "#92400e", size = 3.5) +
  ggplot2::scale_x_continuous(limits = c(0, 25), breaks = seq(0, 25, 5), labels = function(x) paste0(x, "%"), expand = c(0, 0)) +
  ggplot2::scale_y_continuous(breaks = NULL) +
  ggplot2::labs(
    title = "The 23% public OP-22 signal needs definition and current-data review",
    subtitle = "Technical view for the emergency department quality director | 53 reporting Massachusetts hospitals",
    x = "Patients leaving before being seen, public CMS value",
    y = "Reporting hospitals ordered by value",
    caption = "Reporting period: 2024-01-01 through 2024-12-31 | CMS release: 2026-08-13 | Lag at release: 590 days\nAction: validate numerator, denominator, exclusions, source completeness, and current local monthly data before considering intervention."
  ) +
  ggplot2::theme_minimal(base_size = 12) +
  ggplot2::theme(
    plot.title = ggplot2::element_text(face = "bold", size = 17, color = "#0f172a"),
    plot.subtitle = ggplot2::element_text(size = 11.5, color = "#334155"),
    plot.caption = ggplot2::element_text(hjust = 0, color = "#475569", size = 9.5, margin = ggplot2::margin(t = 12)),
    panel.grid.major.y = ggplot2::element_blank(),
    panel.grid.minor = ggplot2::element_blank(),
    axis.title.y = ggplot2::element_text(color = "#475569"),
    plot.margin = ggplot2::margin(18, 24, 18, 18)
  )

ggplot2::ggsave(file.path(output_dir, "figure-supporting.png"), technical, width = 12, height = 7.5, dpi = 180, bg = "white")

cards <- data.frame(
  xmin = c(0.2, 1.15, 2.1),
  xmax = c(1.0, 1.95, 2.9),
  ymin = c(2.5, 2.5, 2.5),
  ymax = c(5.6, 5.6, 5.6),
  heading = c("PUBLIC SIGNAL", "TIME BOUNDARY", "DECISION REQUEST"),
  value = c("23% OP-22", "590 days", "Authorize review"),
  detail = c(
    "Highest observed value among\n53 reporting MA hospitals",
    "2024 period ended before\nthe 2026 CMS release",
    "Validate definitions and return\nwith current local monthly data"
  ),
  stringsAsFactors = FALSE
)

executive <- ggplot2::ggplot() +
  ggplot2::geom_rect(data = cards, ggplot2::aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = "#f8fafc", color = "#cbd5e1", linewidth = 0.6) +
  ggplot2::geom_text(data = cards, ggplot2::aes(x = (xmin + xmax) / 2, y = 5.15, label = heading), size = 3.6, color = "#475569", fontface = "bold") +
  ggplot2::geom_text(data = cards, ggplot2::aes(x = (xmin + xmax) / 2, y = 4.25, label = value), size = 6.4, color = c("#1f49b6", "#b45309", "#047857"), fontface = "bold") +
  ggplot2::geom_text(data = cards, ggplot2::aes(x = (xmin + xmax) / 2, y = 3.2, label = detail), size = 3.7, color = "#334155", lineheight = 1.05) +
  ggplot2::annotate("text", x = 1.55, y = 7.15, label = "A historical public signal warrants a current local review", size = 7.2, fontface = "bold", color = "#0f172a") +
  ggplot2::annotate("text", x = 1.55, y = 6.45, label = "Decision story for the hospital quality committee", size = 4.4, color = "#475569") +
  ggplot2::annotate("label", x = 1.55, y = 1.65, label = "Owner: emergency department quality director  |  Return evidence: current local OP-22 and ED-time series", size = 4.0, color = "#064e3b", fill = "#ecfdf5", linewidth = 0.25) +
  ggplot2::annotate("text", x = 1.55, y = 0.75, label = "The 10% review trigger is a course assumption, not a CMS threshold. Do not infer current performance, cause, or intervention need.", size = 3.7, color = "#7c2d12") +
  ggplot2::coord_cartesian(xlim = c(0, 3.1), ylim = c(0.2, 7.6), clip = "off") +
  ggplot2::theme_void() +
  ggplot2::theme(plot.margin = ggplot2::margin(20, 24, 20, 24))

ggplot2::ggsave(file.path(output_dir, "figure-primary.png"), executive, width = 13, height = 7.5, dpi = 180, bg = "white")

table_fields <- c("measure_id", "display_label", "score_raw", "score_numeric", "unit", "sample", "value_status", "footnote", "period_start", "period_end", "cms_release_date", "source_lag_days_at_release", "ma_reported_n", "ma_median", "ma_rank_unfavorable", "scenario_threshold", "threshold_crossed", "threshold_origin", "monitoring_use", "action_if_crossed")
write.csv(selected[table_fields], file.path(output_dir, "accessible-table.csv"), row.names = FALSE, quote = TRUE, na = "")

message(sprintf("Final checkpoint analysis wrote 2 figures and 1 exact table to %s", normalizePath(output_dir, winslash = "/", mustWork = TRUE)))
