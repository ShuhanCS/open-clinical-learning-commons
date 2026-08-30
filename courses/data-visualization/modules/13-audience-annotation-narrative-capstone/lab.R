args <- commandArgs(trailingOnly = TRUE)
option_value <- function(flag, default) {
  index <- match(flag, args)
  if (is.na(index) || index == length(args)) default else args[[index + 1]]
}

script_arg <- commandArgs(FALSE)[grep("^--file=", commandArgs(FALSE))][1]
script_path <- normalizePath(sub("^--file=", "", script_arg), mustWork = TRUE)
module_root <- dirname(script_path)
repo_root <- normalizePath(file.path(module_root, "..", "..", "..", ".."), mustWork = TRUE)
upstream <- file.path(repo_root, "courses", "data-visualization", "modules", "12-dashboards-multi-view-composition")
data_path <- file.path(upstream, "data", "ma_ed_public_reporting_dashboard_2026.csv")
output_dir <- option_value("--output", file.path(module_root, "output"))
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

if (!requireNamespace("ggplot2", quietly = TRUE)) stop("Package ggplot2 is required.")
data <- read.csv(data_path, check.names = FALSE)
required <- c("facility_id", "facility_name", "measure_id", "display_label", "unit", "score_raw", "score_numeric", "value_status", "sample", "footnote", "period_start", "period_end", "cms_release_date", "ma_reported_n", "ma_median", "ma_rank_unfavorable", "selected_hospital", "scenario_threshold", "threshold_crossed", "threshold_origin", "source_lag_days_at_release", "monitoring_use", "action_if_crossed")
if (!all(required %in% names(data))) stop("The Module 12 teaching table is missing required fields.")

selected <- data[data$selected_hospital == "yes", , drop = FALSE]
if (nrow(selected) != 3) stop("Expected three selected-facility rows.")
op22 <- data[data$measure_id == "OP_22" & data$value_status == "reported", , drop = FALSE]
op22$score_numeric <- as.numeric(op22$score_numeric)
op22 <- op22[order(op22$score_numeric, op22$facility_name), , drop = FALSE]
op22$peer_order <- seq_len(nrow(op22))
op22$is_selected <- op22$facility_id == "220029"
selected_op22 <- selected[selected$measure_id == "OP_22", , drop = FALSE]
selected_op18 <- selected[selected$measure_id == "OP_18b", , drop = FALSE]

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

ggplot2::ggsave(file.path(output_dir, "01-technical-decision-story.png"), technical, width = 12, height = 7.5, dpi = 180, bg = "white")

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

ggplot2::ggsave(file.path(output_dir, "02-executive-decision-story.png"), executive, width = 13, height = 7.5, dpi = 180, bg = "white")

table_fields <- c("measure_id", "display_label", "score_raw", "score_numeric", "unit", "sample", "value_status", "footnote", "period_start", "period_end", "cms_release_date", "source_lag_days_at_release", "ma_reported_n", "ma_median", "ma_rank_unfavorable", "scenario_threshold", "threshold_crossed", "threshold_origin", "monitoring_use", "action_if_crossed")
write.csv(selected[table_fields], file.path(output_dir, "decision-story-table.csv"), row.names = FALSE, quote = TRUE, na = "")

alt_text <- c(
  "# Module 13 reference alternatives",
  "",
  "## Technical decision story",
  "",
  "Audience: emergency department quality director. Decision: whether to open a local definition and current-data review for a public OP-22 signal.",
  "",
  "The figure places 53 reported Massachusetts hospital OP-22 values along a percent axis. Anna Jaques Hospital is directly labeled at 23 percent, the highest observed value. A dashed line marks the descriptive Massachusetts median of 3 percent. A dotted line marks the mock 10-percent course review trigger and is explicitly labeled as not a CMS threshold.",
  "",
  "The source period is January through December 2024. CMS released the file on August 13, 2026, 590 days after the period ended. The figure recommends validating the numerator, denominator, exclusions, source completeness, and current local monthly data before considering an intervention.",
  "",
  "## Executive decision story",
  "",
  "Audience: hospital quality committee. Decision: whether to authorize the emergency department quality director to conduct the review.",
  "",
  "Three cards show the public signal, time boundary, and decision request. The public OP-22 value is 23 percent and is the highest observed among 53 reporting Massachusetts hospitals. The public period ended 590 days before the 2026 CMS release. The requested action is to authorize definition validation and require current local OP-22 and emergency department time evidence at the next review.",
  "",
  "The mock 10-percent trigger is not a CMS threshold. Neither figure supports a current performance judgment, a causal claim, or an intervention decision."
)
writeLines(alt_text, file.path(output_dir, "alt-text-reference.md"), useBytes = TRUE)

adaptation <- c(
  "# Audience adaptation reference",
  "",
  "| Element | Technical quality director | Executive quality committee | Invariant check |",
  "|---|---|---|---|",
  "| Task | Trace the alert and validation evidence. | Authorize a bounded review. | Same decision boundary. |",
  "| Primary evidence | Full OP-22 peer distribution, reported n, median, and mock trigger. | Direct OP-22 value, peer-position sentence, and freshness card. | 23%, n=53, median 3%, trigger 10%. |",
  "| Time | Full period, release date, and lag in caption. | 590-day lag is a primary card. | 2024 period, 2026-08-13 release, 590 days. |",
  "| Action | Validate definition fields and pull current local monthly data. | Authorize the quality director and require return evidence. | No intervention from public data. |",
  "| Detail moved | OP_18b and EDV remain in the exact table. | Peer distribution moves to the technical version. | Three-row table is identical. |",
  "| Material limit | Historical public aggregate reporting. | Historical public aggregate reporting. | Same limit. |"
)
writeLines(adaptation, file.path(output_dir, "audience-adaptation-reference.md"), useBytes = TRUE)

brief <- c(
  "# Reference decision brief",
  "",
  "## Audience and finding",
  "",
  "The emergency department quality director and hospital quality committee are reviewing a historical public CMS signal. Anna Jaques Hospital reports OP-22 at 23 percent for January through December 2024. This is the highest observed value among 53 reporting Massachusetts hospitals and exceeds the mock 10-percent course review trigger.",
  "",
  "## Requested decision",
  "",
  "Authorize the quality director to validate the CMS-to-local numerator, denominator, exclusions, and source completeness, then return with current local monthly OP-22 and emergency department time evidence. If the current signal persists, the team can review system conditions with clinical and operational owners.",
  "",
  "## Material limitation",
  "",
  "The public OP-22 period ended 590 days before CMS released the file. The Massachusetts median is descriptive, and the 10-percent trigger is a course assumption rather than a CMS threshold. The evidence does not support a current performance judgment, causal attribution, or intervention decision."
)
writeLines(brief, file.path(output_dir, "decision-brief-reference.md"), useBytes = TRUE)

message(sprintf("Module 13 lab wrote 2 figures, 1 table, and 3 reference documents to %s", normalizePath(output_dir, winslash = "/", mustWork = TRUE)))
