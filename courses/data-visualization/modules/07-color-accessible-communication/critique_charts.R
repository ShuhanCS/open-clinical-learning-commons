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
data_path <- option_value("--data", file.path(script_dir, "data", "accessibility_hf_readmission_2026.csv"))
output_dir <- option_value("--output", file.path(script_dir, "critique-output"))

data <- read.csv(data_path, stringsAsFactors = FALSE, check.names = FALSE)
if (nrow(data) != 65) stop("Expected 65 accessibility rows.")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

reported <- data[data$estimate_status == "reported", ]
reported <- reported[order(reported$score), ]
reported$facility_order <- factor(reported$facility_name, levels = reported$facility_name)

red_green_only <- ggplot2::ggplot(reported, ggplot2::aes(x = score, y = facility_order, color = display_status)) +
  ggplot2::geom_point(size = 2.8) +
  ggplot2::scale_color_manual(values = c("no different" = "#00A000", "worse" = "#D00000")) +
  ggplot2::labs(
    title = "FLAWED: red and green are the only status cue",
    subtitle = "Identical point shapes and no direct status labels",
    x = "Readmission estimate",
    y = NULL,
    color = NULL
  ) +
  ggplot2::theme_minimal(base_size = 11) +
  ggplot2::theme(panel.grid.major.y = ggplot2::element_blank(), legend.position = "top")

top <- reported[order(-reported$score), ][1:15, ]
heat <- rbind(
  data.frame(facility_name = top$facility_name, metric = "Score", value = top$score),
  data.frame(facility_name = top$facility_name, metric = "Interval width", value = top$higher_estimate - top$lower_estimate),
  data.frame(facility_name = top$facility_name, metric = "Denominator", value = top$denominator)
)
heat$value_scaled <- ave(heat$value, heat$metric, FUN = function(value) (value - min(value)) / (max(value) - min(value)))
heat$facility_name <- factor(heat$facility_name, levels = rev(top$facility_name))

low_contrast_heatmap <- ggplot2::ggplot(heat, ggplot2::aes(x = metric, y = facility_name, fill = value_scaled)) +
  ggplot2::geom_tile(color = "#F4F4F4", linewidth = 0.3) +
  ggplot2::scale_fill_gradient(low = "#F7FBFF", high = "#C8DDEA", guide = "none") +
  ggplot2::labs(
    title = "FLAWED: a pale heatmap hides values and units",
    subtitle = "Color alone carries three separately normalized measures",
    x = NULL,
    y = NULL
  ) +
  ggplot2::theme_minimal(base_size = 10) +
  ggplot2::theme(panel.grid = ggplot2::element_blank())

ggplot2::ggsave(file.path(output_dir, "C1-red-green-color-only.png"), red_green_only, width = 10, height = 13, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "C2-low-contrast-heatmap.png"), low_contrast_heatmap, width = 9, height = 7, dpi = 150, bg = "white")

cat("Created two deliberately inaccessible critique figures in:", normalizePath(output_dir, winslash = "/"), "\n")
