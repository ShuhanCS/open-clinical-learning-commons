args <- commandArgs(trailingOnly = TRUE)
default_sources <- c(
  file.path("..", "01-encoding-grammar", "data", "hcahps_ma_recommend_2026.csv"),
  "hcahps_ma_recommend_2026.csv"
)
available_source <- default_sources[file.exists(default_sources)][1]
source_path <- if (length(args) >= 1) args[[1]] else if (!is.na(available_source)) available_source else default_sources[[1]]
output_dir <- if (length(args) >= 2) args[[2]] else file.path("outputs", "critique")

if (!requireNamespace("ggplot2", quietly = TRUE)) {
  stop("Package 'ggplot2' is required. Install it with: install.packages('ggplot2')", call. = FALSE)
}
if (!file.exists(source_path)) {
  stop(sprintf("Module 01 HCAHPS file not found: %s", source_path), call. = FALSE)
}

source <- utils::read.csv(source_path, stringsAsFactors = FALSE, na.strings = "")
values <- source[source$facility_id %in% c("220012", "220074", "220031", "220002", "220100"), , drop = FALSE]
values <- values[match(c("220012", "220074", "220031", "220002", "220100"), values$facility_id), , drop = FALSE]
if (nrow(values) != 5L || anyNA(values$recommend_percent)) {
  stop("Expected five reported HCAHPS rows for the critique set.", call. = FALSE)
}
values$alias <- paste("Hospital", LETTERS[seq_len(nrow(values))])

pie_values <- values[1:4, ]
pie_data <- data.frame(
  alias = rep(pie_values$alias, each = 2),
  response = rep(c("Would definitely recommend", "Other response"), nrow(pie_values)),
  percent = as.vector(rbind(pie_values$recommend_percent, 100 - pie_values$recommend_percent)),
  stringsAsFactors = FALSE
)
close_pies <- ggplot2::ggplot(pie_data, ggplot2::aes(x = "", y = percent, fill = response)) +
  ggplot2::geom_col(width = 1, color = "white", linewidth = 0.7) +
  ggplot2::coord_polar(theta = "y") +
  ggplot2::facet_wrap(~alias, nrow = 1) +
  ggplot2::scale_fill_manual(values = c("Would definitely recommend" = "#1f49b6", "Other response" = "#cbd5e1")) +
  ggplot2::labs(
    title = "Put these hospitals in exact order",
    subtitle = "Four close recommendation percentages shown as separate angles",
    fill = NULL,
    caption = "Intentionally flawed teaching display."
  ) +
  ggplot2::theme_void(base_size = 12) +
  ggplot2::theme(plot.title.position = "plot", legend.position = "bottom")

bubble_values <- values
bubble_values$radius <- bubble_values$recommend_percent - 60
bubble_values$alias <- factor(bubble_values$alias, levels = rev(bubble_values$alias))
exaggerated_bubbles <- ggplot2::ggplot(bubble_values, ggplot2::aes(x = 1, y = alias)) +
  ggplot2::geom_point(ggplot2::aes(size = radius), color = "#1f49b6", alpha = 0.8) +
  ggplot2::scale_size_identity() +
  ggplot2::scale_x_continuous(limits = c(0.98, 1.02), breaks = NULL) +
  ggplot2::labs(
    title = "Small percentage differences look much larger",
    subtitle = "Circle radius uses percent minus 60, so area exaggerates the gap",
    x = NULL,
    y = NULL,
    caption = "Intentionally flawed teaching display."
  ) +
  ggplot2::theme_minimal(base_size = 12) +
  ggplot2::theme(panel.grid = ggplot2::element_blank(), plot.title.position = "plot")

if (!dir.exists(output_dir)) {
  dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
}
ggplot2::ggsave(file.path(output_dir, "01-close-values-as-pies.png"), close_pies, width = 10, height = 4.8, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "02-exaggerated-bubbles.png"), exaggerated_bubbles, width = 8, height = 5, dpi = 150, bg = "white")

cat("Created two intentionally flawed perception critique charts in:", normalizePath(output_dir, winslash = "/"), "\n")
