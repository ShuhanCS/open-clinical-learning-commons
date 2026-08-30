args <- commandArgs(trailingOnly = TRUE)
default_inputs <- c(file.path("data", "hcahps_ma_recommend_2026.csv"), "hcahps_ma_recommend_2026.csv")
available_default <- default_inputs[file.exists(default_inputs)][1]
input_path <- if (length(args) >= 1) args[[1]] else if (!is.na(available_default)) available_default else default_inputs[[1]]
output_dir <- if (length(args) >= 2) args[[2]] else file.path("outputs", "critique")

if (!requireNamespace("ggplot2", quietly = TRUE)) {
  stop("Package 'ggplot2' is required. Install it with: install.packages('ggplot2')", call. = FALSE)
}
if (!file.exists(input_path)) {
  stop(sprintf("Data file not found: %s", input_path), call. = FALSE)
}

data <- utils::read.csv(input_path, stringsAsFactors = FALSE, na.strings = "")
required_columns <- c("facility_id", "facility_name", "recommend_percent", "completed_surveys", "value_status")
missing_columns <- setdiff(required_columns, names(data))
if (length(missing_columns) > 0) {
  stop(sprintf("Input is missing columns: %s", paste(missing_columns, collapse = ", ")), call. = FALSE)
}

reported <- data[data$value_status == "reported", , drop = FALSE]
peer_set <- head(reported[order(-reported$completed_surveys, reported$facility_id), ], 15)
peer_set$facility_label <- tools::toTitleCase(tolower(peer_set$facility_name))
peer_set <- peer_set[order(peer_set$recommend_percent, peer_set$facility_id), , drop = FALSE]
peer_set$facility_label <- factor(peer_set$facility_label, levels = peer_set$facility_label)
peer_set$percent_label <- factor(peer_set$recommend_percent)

if (!dir.exists(output_dir)) {
  dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
}

unordered_color <- ggplot2::ggplot(peer_set, ggplot2::aes(y = facility_label, x = 1, color = percent_label)) +
  ggplot2::geom_point(size = 7) +
  ggplot2::scale_color_manual(values = grDevices::hcl.colors(length(unique(peer_set$percent_label)), "Dynamic")) +
  ggplot2::scale_x_continuous(limits = c(0.98, 1.02), breaks = NULL) +
  ggplot2::labs(
    title = "Which hospitals have similar recommendation results?",
    subtitle = "The ordered percentage is encoded only with unordered color",
    x = NULL,
    y = NULL,
    color = "Recommend percent"
  ) +
  ggplot2::theme_minimal(base_size = 12) +
  ggplot2::theme(
    panel.grid = ggplot2::element_blank(),
    plot.title.position = "plot",
    axis.text.y = ggplot2::element_text(color = "#0f172a")
  )

area_comparison <- ggplot2::ggplot(peer_set, ggplot2::aes(y = facility_label, x = 1, size = recommend_percent)) +
  ggplot2::geom_point(color = "#1f49b6", alpha = 0.75) +
  ggplot2::scale_size_area(max_size = 17, limits = c(0, 100)) +
  ggplot2::scale_x_continuous(limits = c(0.98, 1.02), breaks = NULL) +
  ggplot2::labs(
    title = "Which hospitals have the highest recommendation results?",
    subtitle = "The percentage is encoded only as circle area",
    x = NULL,
    y = NULL,
    size = "Recommend percent"
  ) +
  ggplot2::theme_minimal(base_size = 12) +
  ggplot2::theme(
    panel.grid = ggplot2::element_blank(),
    plot.title.position = "plot",
    axis.text.y = ggplot2::element_text(color = "#0f172a")
  )

ggplot2::ggsave(file.path(output_dir, "01-unordered-color.png"), unordered_color, width = 10, height = 7.5, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "02-area-for-precision.png"), area_comparison, width = 10, height = 7.5, dpi = 150, bg = "white")

cat("Created two intentionally flawed critique charts in:", normalizePath(output_dir, winslash = "/"), "\n")
cat(paste0(
  "Diagnose each chart before opening the instructor notes:\n",
  "1. What question does the title promise to answer?\n",
  "2. Which variable is mapped to which channel?\n",
  "3. What comparison does that channel make difficult?\n",
  "4. What is the smallest repair that preserves the decision and the data?\n"
))
