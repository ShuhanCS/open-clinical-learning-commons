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
reported <- source[source$value_status == "reported" & is.finite(source$response_rate_percent), , drop = FALSE]
data <- head(reported[order(-reported$completed_surveys, reported$facility_id), ], 8)
data$alias <- paste("Hospital", LETTERS[seq_len(nrow(data))])

panels <- rbind(
  data.frame(alias = data$alias, question = "Compare recommendation", value = data$recommend_percent / 100),
  data.frame(alias = data$alias, question = "Look up response rate", value = data$response_rate_percent / 100),
  data.frame(alias = data$alias, question = "Compare survey volume", value = data$completed_surveys / max(data$completed_surveys)),
  data.frame(alias = data$alias, question = "See recommendation-response relationship", value = (data$recommend_percent + data$response_rate_percent) / 200)
)
panels$alias <- factor(panels$alias, levels = rev(unique(data$alias)))

dashboard <- ggplot2::ggplot(panels, ggplot2::aes(x = value, y = alias)) +
  ggplot2::geom_col(fill = "#1f49b6", width = 0.65) +
  ggplot2::facet_wrap(~question, ncol = 2) +
  ggplot2::scale_x_continuous(limits = c(0, 1), labels = function(x) paste0(round(100 * x), "%")) +
  ggplot2::labs(
    title = "One bar template is forced onto four different questions",
    subtitle = "Incompatible metrics are normalized to fit; the relationship is replaced by a meaningless combined value",
    x = "Normalized value",
    y = NULL,
    caption = "Intentionally flawed teaching dashboard."
  ) +
  ggplot2::theme_minimal(base_size = 11) +
  ggplot2::theme(
    panel.grid.major.y = ggplot2::element_blank(),
    panel.grid.minor = ggplot2::element_blank(),
    plot.title.position = "plot"
  )

if (!dir.exists(output_dir)) {
  dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
}
ggplot2::ggsave(file.path(output_dir, "01-one-form-for-every-question.png"), dashboard, width = 11, height = 7.5, dpi = 150, bg = "white")
cat("Created the intentionally flawed one-form dashboard in:", normalizePath(output_dir, winslash = "/"), "\n")
