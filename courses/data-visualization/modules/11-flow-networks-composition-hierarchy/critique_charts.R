#!/usr/bin/env Rscript

suppressPackageStartupMessages(library(ggplot2))

args <- commandArgs(trailingOnly = TRUE)
output_dir <- if (length(args) >= 2 && args[1] == "--output") args[2] else file.path(tempdir(), "oclc-da730-m11-critiques")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
theme_bad <- theme_void(base_size = 12) + theme(plot.title = element_text(face = "bold"), plot.subtitle = element_text(color = "#475569"))

changing <- data.frame(
  stage = factor(c("Eligible", "Reached", "Completed", "Positive"), levels = c("Eligible", "Reached", "Completed", "Positive")),
  n = c(500, 420, 290, 86),
  shown_pct = c(100, 84, 69, 30)
)
p1 <- ggplot(changing, aes(stage, shown_pct, fill = stage)) +
  geom_col(width = 0.9) +
  geom_text(aes(label = paste0(shown_pct, "%")), vjust = -0.3, fontface = "bold") +
  scale_fill_manual(values = c("#1f49b6", "#0d67ff", "#00a6c8", "#e15759"), guide = "none") +
  scale_y_continuous(limits = c(0, 108)) +
  labs(title = "C1: The denominator quietly changes", subtitle = "The final percentages use different bases, but the display looks like one conserved funnel") +
  theme_bad + theme(axis.text.x = element_text(), axis.text.y = element_blank())
ggsave(file.path(output_dir, "C1-changing-denominator-flow.png"), p1, width = 9, height = 5.5, dpi = 180)

set.seed(730)
nodes <- data.frame(x = runif(22), y = runif(22), label = paste0("N", 1:22))
edges <- data.frame(a = sample(1:22, 75, TRUE), b = sample(1:22, 75, TRUE))
edges <- edges[edges$a != edges$b, ]
segments <- data.frame(x = nodes$x[edges$a], y = nodes$y[edges$a], xend = nodes$x[edges$b], yend = nodes$y[edges$b])
p2 <- ggplot() +
  geom_segment(data = segments, aes(x, y, xend = xend, yend = yend), alpha = 0.25, color = "#64748b") +
  geom_point(data = nodes, aes(x, y), size = 6, color = "#1f49b6") +
  geom_text(data = nodes, aes(x, y, label = label), color = "white", size = 2.6) +
  labs(title = "C2: A node-link hairball hides the decision", subtitle = "Neither node meaning, edge definition, direction, weight, nor action is recoverable") +
  theme_bad
ggsave(file.path(output_dir, "C2-hairball-network.png"), p2, width = 9, height = 6, dpi = 180)

tree <- data.frame(
  group = c("Service A", "Service B", "Service C", "Service D"),
  volume = c(640, 240, 90, 30),
  rate = c(4.2, 12.8, 22.1, 31.4),
  xmin = c(0, .64, .88, .97), xmax = c(.64, .88, .97, 1), ymin = 0, ymax = 1
)
p3 <- ggplot(tree) +
  geom_rect(aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax, fill = rate), color = "white", linewidth = 2) +
  geom_text(aes(x = (xmin + xmax) / 2, y = .5, label = paste0(group, "\n", rate, "%")), size = 3.5, fontface = "bold") +
  scale_fill_gradient(low = "#fee2e2", high = "#b91c1c") +
  labs(title = "C3: Treemap area encodes volume while labels emphasize rate", subtitle = "The largest area can look like the highest rate even when it is the lowest") +
  theme_bad + theme(legend.position = "none")
ggsave(file.path(output_dir, "C3-treemap-area-rate-conflict.png"), p3, width = 9, height = 5.5, dpi = 180)

cat(sprintf("Module 11 critique lab wrote 3 figures to %s\n", output_dir))
