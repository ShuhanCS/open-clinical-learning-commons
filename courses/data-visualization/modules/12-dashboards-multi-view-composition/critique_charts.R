#!/usr/bin/env Rscript

suppressPackageStartupMessages(library(ggplot2))

args <- commandArgs(trailingOnly = TRUE)
output_dir <- if (length(args) >= 2 && args[1] == "--output") args[2] else file.path(tempdir(), "oclc-da730-m12-critiques")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

set.seed(12)
kpis <- data.frame(
  id = factor(1:18),
  value = sample(40:99, 18),
  row = rep(3:1, each = 6),
  col = rep(1:6, 3)
)
p1 <- ggplot(kpis, aes(col, row)) +
  geom_tile(aes(fill = value), width = 0.9, height = 0.82, color = "white") +
  geom_text(aes(label = paste0("KPI ", id, "\n", value)), color = "white", fontface = "bold", size = 4) +
  scale_fill_gradient(low = "#64748b", high = "#1f49b6", guide = "none") +
  labs(title = "C1: A wall of KPIs has no decision hierarchy", subtitle = "Eighteen equally prominent values, no owner, no exception, no action") +
  theme_void(base_size = 13) + theme(plot.title = element_text(face = "bold"), plot.subtitle = element_text(color = "#526071"))
ggsave(file.path(output_dir, "C1-wall-of-kpis.png"), p1, width = 11, height = 6.5, dpi = 180)

windows <- data.frame(
  metric = c("Left before seen", "ED time", "Patient experience"),
  value = c(23, 188, 71),
  scaled = c(92, 75, 71),
  window = c("2024", "Oct 2024-Sep 2025", "Oct 2024-Sep 2025")
)
p2 <- ggplot(windows, aes(metric, scaled, fill = metric)) +
  geom_col(width = 0.7) +
  geom_text(aes(label = value), vjust = -0.4, fontface = "bold", size = 5) +
  scale_fill_manual(values = c("#1f49b6", "#00a6c8", "#d97706"), guide = "none") +
  scale_y_continuous(limits = c(0, 105)) +
  labs(title = "C2: Different units and windows are disguised as one scorecard", subtitle = "Percent, minutes, and another percent share an invented scale labeled Current", x = NULL, y = "Current performance") +
  theme_minimal(base_size = 13) + theme(plot.title = element_text(face = "bold"), axis.text.x = element_text(angle = 12, hjust = 1), panel.grid.minor = element_blank())
ggsave(file.path(output_dir, "C2-hidden-windows-and-units.png"), p2, width = 10, height = 6.2, dpi = 180)

gauges <- data.frame(metric = c("Flow", "Care", "Experience"), value = c(0.82, 0.61, 0.74), y = 1)
p3 <- ggplot(gauges, aes(metric, y, fill = value)) +
  geom_col(width = 0.72, color = "white") +
  geom_text(aes(label = paste0(round(value * 100), "%")), color = "white", fontface = "bold", size = 6) +
  scale_fill_gradient(low = "#a78bfa", high = "#4c1d95", guide = "none") +
  coord_polar(theta = "x") +
  labs(title = "C3: Decorative widgets do not create an action", subtitle = "Undefined composite scores, no denominator, no threshold owner, no next step") +
  theme_void(base_size = 13) + theme(plot.title = element_text(face = "bold"), plot.subtitle = element_text(color = "#526071"))
ggsave(file.path(output_dir, "C3-decorative-widgets.png"), p3, width = 9, height = 6.2, dpi = 180)

cat(sprintf("Module 12 critique lab wrote 3 figures to %s\n", output_dir))
