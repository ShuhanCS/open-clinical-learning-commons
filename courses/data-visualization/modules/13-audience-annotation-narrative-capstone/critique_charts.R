args <- commandArgs(trailingOnly = TRUE)
option_value <- function(flag, default) {
  index <- match(flag, args)
  if (is.na(index) || index == length(args)) default else args[[index + 1]]
}

script_arg <- commandArgs(FALSE)[grep("^--file=", commandArgs(FALSE))][1]
script_path <- normalizePath(sub("^--file=", "", script_arg), mustWork = TRUE)
module_root <- dirname(script_path)
output_dir <- option_value("--output", file.path(module_root, "critique-output"))
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
if (!requireNamespace("ggplot2", quietly = TRUE)) stop("Package ggplot2 is required.")

base_theme <- ggplot2::theme_void() + ggplot2::theme(plot.margin = ggplot2::margin(20, 20, 20, 20))

c1 <- ggplot2::ggplot() +
  ggplot2::annotate("text", x = 1, y = 3.8, label = "STAFFING CAUSED PATIENTS TO LEAVE", size = 7.2, fontface = "bold", color = "#991b1b") +
  ggplot2::annotate("text", x = 1, y = 2.7, label = "23%", size = 14, fontface = "bold", color = "#dc2626") +
  ggplot2::annotate("text", x = 1, y = 1.7, label = "No staffing exposure, local time series,\nor causal design appears in the source", size = 4.8, color = "#475569") +
  ggplot2::annotate("label", x = 1, y = 0.75, label = "Failure: the title invents cause", size = 4.6, fill = "#fee2e2", color = "#7f1d1d", linewidth = 0.3) +
  ggplot2::coord_cartesian(xlim = c(0, 2), ylim = c(0.2, 4.4)) + base_theme
ggplot2::ggsave(file.path(output_dir, "C1-overstated-causality.png"), c1, width = 10, height = 6, dpi = 160, bg = "white")

c2 <- ggplot2::ggplot() +
  ggplot2::annotate("text", x = 1, y = 4.0, label = "CURRENT ED PERFORMANCE", size = 7, fontface = "bold", color = "#0f172a") +
  ggplot2::annotate("text", x = 1, y = 2.75, label = "23%", size = 15, fontface = "bold", color = "#b91c1c") +
  ggplot2::annotate("text", x = 1, y = 1.7, label = "The 2024 period, 2026 release,\nand 590-day lag have been removed", size = 4.9, color = "#475569") +
  ggplot2::annotate("label", x = 1, y = 0.7, label = "Failure: public reporting is mislabeled current", size = 4.4, fill = "#ffedd5", color = "#9a3412", linewidth = 0.3) +
  ggplot2::coord_cartesian(xlim = c(0, 2), ylim = c(0.2, 4.5)) + base_theme
ggplot2::ggsave(file.path(output_dir, "C2-hidden-freshness.png"), c2, width = 10, height = 6, dpi = 160, bg = "white")

c3 <- ggplot2::ggplot() +
  ggplot2::annotate("segment", x = 0.2, xend = 1.25, y = 3.6, yend = 2.5, linewidth = 5, color = "#dc2626", arrow = grid::arrow(length = grid::unit(0.35, "inches"))) +
  ggplot2::annotate("text", x = 0.75, y = 4.15, label = "ALARMING OUTLIER!", size = 8, fontface = "bold", color = "#991b1b") +
  ggplot2::annotate("point", x = 1.35, y = 2.4, size = 9, color = "#1f49b6") +
  ggplot2::annotate("text", x = 1.35, y = 1.75, label = "23%", size = 7, fontface = "bold") +
  ggplot2::annotate("text", x = 1.0, y = 0.42, label = "mock trigger, not CMS | historical period | review before action", size = 2.3, color = "#94a3b8") +
  ggplot2::annotate("label", x = 1, y = 0.95, label = "Failure: dramatic annotation buries the decision boundary", size = 4.0, fill = "#fef2f2", color = "#7f1d1d", linewidth = 0.3) +
  ggplot2::coord_cartesian(xlim = c(0, 2), ylim = c(0.1, 4.6)) + base_theme
ggplot2::ggsave(file.path(output_dir, "C3-annotation-misdirection.png"), c3, width = 10, height = 6, dpi = 160, bg = "white")

message(sprintf("Module 13 critique lab wrote 3 figures to %s", normalizePath(output_dir, winslash = "/", mustWork = TRUE)))
