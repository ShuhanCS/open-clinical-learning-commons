#!/usr/bin/env Rscript

suppressPackageStartupMessages(library(ggplot2))

args <- commandArgs(trailingOnly = TRUE)
output_dir <- if (length(args) >= 2 && args[1] == "--output") args[2] else file.path(tempdir(), "oclc-da730-m12-lab")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

script_arg <- grep("^--file=", commandArgs(), value = TRUE)
script_path <- if (length(script_arg)) sub("^--file=", "", script_arg[1]) else "lab.R"
module_root <- dirname(normalizePath(script_path, mustWork = TRUE))
data <- read.csv(file.path(module_root, "data", "ma_ed_public_reporting_dashboard_2026.csv"), check.names = FALSE)
selected <- data[data$selected_hospital == "yes", ]

ink <- "#172033"
muted <- "#526071"
blue <- "#1f49b6"
amber <- "#b45309"
amber_light <- "#fff7ed"
blue_light <- "#eff6ff"
line <- "#d9e0ea"

theme_dashboard <- theme_minimal(base_size = 11) +
  theme(
    plot.title = element_text(face = "bold", size = 13, color = ink),
    plot.subtitle = element_text(size = 9.5, color = muted),
    plot.caption = element_text(size = 8.5, color = muted, hjust = 0),
    panel.grid.minor = element_blank(),
    panel.grid.major.y = element_blank(),
    axis.text.y = element_blank(),
    axis.title.y = element_blank(),
    axis.ticks.y = element_blank(),
    plot.margin = margin(8, 12, 8, 8)
  )

peer_plot <- function(measure_id, title, unit_label) {
  d <- data[data$measure_id == measure_id & data$value_status == "reported", ]
  d <- d[order(d$score_numeric, d$facility_id), ]
  d$band <- ((seq_len(nrow(d)) - 1) %% 7 - 3) / 12
  focus <- d[d$selected_hospital == "yes", ]
  median_value <- unique(d$ma_median)[1]
  threshold <- unique(d$scenario_threshold)[1]
  period <- paste(unique(d$period_start), unique(d$period_end), sep = " to ")
  ggplot(d, aes(score_numeric, band)) +
    geom_vline(xintercept = median_value, linetype = "dashed", color = blue, linewidth = 0.8) +
    geom_vline(xintercept = threshold, linetype = "dotted", color = amber, linewidth = 0.9) +
    geom_point(color = "#a7b2c2", size = 2.3, alpha = 0.8) +
    geom_point(data = focus, shape = 23, fill = amber, color = "white", stroke = 1, size = 5) +
    geom_label(
      data = focus,
      aes(label = paste0("Anna Jaques: ", score_numeric, " ", unit_label)),
      color = ink,
      fill = "white",
      linewidth = 0.3,
      label.padding = grid::unit(0.12, "lines"),
      nudge_y = 0.43,
      size = 3.1
    ) +
    annotate("text", x = median_value, y = -0.52, label = paste0("MA median ", median_value), color = blue, size = 3, hjust = 0.5) +
    annotate("text", x = threshold, y = 0.52, label = paste0("Mock trigger ", threshold), color = amber, size = 3, hjust = 0.5) +
    scale_x_continuous(expand = expansion(mult = c(0.05, 0.25))) +
    scale_y_continuous(limits = c(-0.62, 0.66), expand = c(0, 0)) +
    labs(
      title = title,
      subtitle = paste0("Massachusetts reported hospitals, n=", nrow(d), " | period ", period),
      x = unit_label,
      caption = "Each dot is one hospital. Lower values are better. Mock triggers are teaching assumptions, not CMS benchmarks."
    ) +
    theme_dashboard
}

p_op22 <- peer_plot("OP_22", "View 3: Public OP-22 peer position needs validation", "percent")
p_op18 <- peer_plot("OP_18b", "View 4: Public ED time does not cross the mock trigger", "minutes")

make_card <- function(fill, border, title, body, title_color = ink) {
  grid::grobTree(
    grid::roundrectGrob(gp = grid::gpar(fill = fill, col = border, lwd = 1.5), r = grid::unit(0.08, "snpc")),
    grid::textGrob(title, x = 0.035, y = 0.73, just = c("left", "center"), gp = grid::gpar(col = title_color, fontsize = 14, fontface = "bold")),
    grid::textGrob(body, x = 0.035, y = 0.31, just = c("left", "center"), gp = grid::gpar(col = ink, fontsize = 10.5, lineheight = 1.15))
  )
}

alert_card <- make_card(
  amber_light,
  "#fdba74",
  "View 1: Review the public OP-22 signal",
  "23% reported for Anna Jaques Hospital | Massachusetts median 3% | Mock review trigger 10%\nAction now: validate the numerator and denominator, then pull current local abandonment data."
)

freshness_card <- make_card(
  blue_light,
  "#93c5fd",
  "View 2: Public data are historical",
  "OP-22 and volume: 2024 calendar year, ended 590 days before release\nOP-18b: Oct 2024 to Sep 2025, ended 317 days before release | CMS release 2026-08-13"
)

action_grob <- grid::grobTree(
  grid::roundrectGrob(gp = grid::gpar(fill = "#f8fafc", col = line, lwd = 1.2), r = grid::unit(0.05, "snpc")),
  grid::textGrob("View 5: One alert, one owner, one ordered response", x = 0.025, y = 0.78, just = "left", gp = grid::gpar(col = ink, fontsize = 13, fontface = "bold")),
  grid::textGrob("1  Validate definitions\nand extract completeness", x = 0.03, y = 0.44, just = "left", gp = grid::gpar(col = ink, fontsize = 9.7, fontface = "bold", lineheight = 1.1)),
  grid::textGrob("2  Pull current monthly\nOP-22 and ED-time data", x = 0.29, y = 0.44, just = "left", gp = grid::gpar(col = ink, fontsize = 9.7, fontface = "bold", lineheight = 1.1)),
  grid::textGrob("3  If confirmed, review arrival,\ntriage, staffing, and capacity", x = 0.55, y = 0.44, just = "left", gp = grid::gpar(col = ink, fontsize = 9.7, fontface = "bold", lineheight = 1.1)),
  grid::textGrob("4  Record owner, action,\nand next review date", x = 0.81, y = 0.44, just = "left", gp = grid::gpar(col = ink, fontsize = 9.7, fontface = "bold", lineheight = 1.1)),
  grid::segmentsGrob(x0 = c(0.245, 0.505, 0.765), x1 = c(0.265, 0.525, 0.785), y0 = 0.44, y1 = 0.44, arrow = grid::arrow(length = grid::unit(0.08, "inches")), gp = grid::gpar(col = muted, lwd = 1.2)),
  grid::textGrob("Owner: emergency department quality director | Public aggregates trigger review, not a current operational or causal conclusion.", x = 0.03, y = 0.14, just = "left", gp = grid::gpar(col = muted, fontsize = 9.5))
)

dashboard_path <- file.path(output_dir, "01-minimum-ed-public-reporting-dashboard.png")
png(dashboard_path, width = 2520, height = 1620, res = 180, bg = "white")
grid::grid.newpage()
layout <- grid::grid.layout(
  nrow = 5,
  ncol = 2,
  widths = grid::unit(c(1, 1), "null"),
  heights = grid::unit(c(0.85, 1.35, 3.8, 1.15, 0.55), "null")
)
grid::pushViewport(grid::viewport(layout = layout))
place <- function(grob, row, col = 1, colspan = 1) {
  grid::pushViewport(grid::viewport(layout.pos.row = row, layout.pos.col = col:(col + colspan - 1)))
  grid::grid.draw(grob)
  grid::popViewport()
}
title_grob <- grid::grobTree(
  grid::textGrob("Anna Jaques ED public-reporting review", x = 0.01, y = 0.73, just = "left", gp = grid::gpar(col = ink, fontsize = 21, fontface = "bold")),
  grid::textGrob("Purpose: decide whether to open a local definition and current-data review, not whether current care is poor", x = 0.01, y = 0.28, just = "left", gp = grid::gpar(col = muted, fontsize = 11.5))
)
place(title_grob, 1, 1, 2)
place(alert_card, 2, 1)
place(freshness_card, 2, 2)
place(ggplotGrob(p_op22), 3, 1)
place(ggplotGrob(p_op18), 3, 2)
place(action_grob, 4, 1, 2)
footer_grob <- grid::textGrob(
  "Source: CMS Timely and Effective Care - Hospital, release 2026-08-13. Different units and reporting windows remain separate. Exact values, samples, definitions, footnotes, and actions are in the decision table and measure dictionary.",
  x = 0.01, y = 0.6, just = "left", gp = grid::gpar(col = muted, fontsize = 9)
)
place(footer_grob, 5, 1, 2)
grid::popViewport()
dev.off()

decision_table <- selected[c(
  "measure_id", "display_label", "score_raw", "unit", "sample", "value_status",
  "period_start", "period_end", "cms_release_date", "source_lag_days_at_release",
  "ma_reported_n", "ma_median", "ma_rank_unfavorable", "scenario_threshold",
  "threshold_crossed", "threshold_origin", "monitoring_use", "action_if_crossed"
)]
write.csv(decision_table, file.path(output_dir, "dashboard-decision-table.csv"), row.names = FALSE, quote = TRUE)

alt_text <- c(
  "# Module 12 dashboard text alternative",
  "",
  "The dashboard is for the emergency department quality director at Anna Jaques Hospital. Its purpose is to decide whether to open a local definition and current-data review. It does not rate current care.",
  "",
  "View 1 shows one public reporting alert. CMS reports that 23 percent of included emergency department visits left before being seen for calendar year 2024. The Massachusetts median among 53 reported hospitals is 3 percent. The mock teaching trigger is 10 percent, so the value crosses it. The first action is to validate the numerator and denominator and pull current local abandonment data.",
  "",
  "View 2 states that the source is historical. The OP-22 and emergency department volume periods ended on 2024-12-31, 590 days before the 2026-08-13 CMS release. The OP-18b period ended on 2025-09-30, 317 days before release.",
  "",
  "View 3 places the hospital's 23 percent OP-22 value at the highest observed value among 53 reporting Massachusetts hospitals. The state median is 3 percent and the mock trigger is 10 percent. Lower values are better.",
  "",
  "View 4 places the hospital's 188-minute median emergency department time among 54 reporting Massachusetts hospitals. The state median is 211.5 minutes and the mock trigger is 240 minutes, so the hospital value does not cross that teaching trigger. Lower values are better. This measure uses a later reporting window than OP-22.",
  "",
  "View 5 gives the ordered response: validate definitions and extract completeness; pull current monthly local data; if the current signal persists, review arrival, triage, staffing, and capacity; then record an owner, action, and next review date.",
  "",
  "All thresholds are mock quality-improvement assumptions, not CMS benchmarks. Public aggregate values can trigger local review but cannot establish current operations, cause, or intervention effect."
)
writeLines(alt_text, file.path(output_dir, "alt-text-reference.md"), useBytes = TRUE)

cat(sprintf("Module 12 lab wrote 1 dashboard, 1 decision table, and 1 text alternative to %s\n", output_dir))
