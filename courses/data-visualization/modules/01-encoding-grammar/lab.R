args <- commandArgs(trailingOnly = TRUE)
default_inputs <- c(file.path("data", "hcahps_ma_recommend_2026.csv"), "hcahps_ma_recommend_2026.csv")
available_default <- default_inputs[file.exists(default_inputs)][1]
input_path <- if (length(args) >= 1) args[[1]] else if (!is.na(available_default)) available_default else default_inputs[[1]]
output_dir <- if (length(args) >= 2) args[[2]] else file.path("outputs", "lab")

if (!requireNamespace("ggplot2", quietly = TRUE)) {
  stop("Package 'ggplot2' is required. Install it with: install.packages('ggplot2')", call. = FALSE)
}
if (!file.exists(input_path)) {
  stop(sprintf("Data file not found: %s", input_path), call. = FALSE)
}

data <- utils::read.csv(input_path, stringsAsFactors = FALSE, na.strings = "")
required_columns <- c(
  "facility_id",
  "facility_name",
  "state",
  "measure_id",
  "recommend_percent",
  "completed_surveys",
  "value_status",
  "period_start",
  "period_end",
  "cms_release_date"
)
missing_columns <- setdiff(required_columns, names(data))
if (length(missing_columns) > 0) {
  stop(sprintf("Input is missing columns: %s", paste(missing_columns, collapse = ", ")), call. = FALSE)
}

reported <- data[
  data$value_status == "reported" &
    is.finite(data$recommend_percent) &
    is.finite(data$completed_surveys),
  ,
  drop = FALSE
]
if (nrow(reported) < 15) {
  stop("At least 15 reported hospital rows are required for the lab.", call. = FALSE)
}

peer_set <- head(reported[order(-reported$completed_surveys, reported$facility_id), ], 15)
peer_set$facility_label <- tools::toTitleCase(tolower(peer_set$facility_name))
peer_set <- peer_set[order(peer_set$recommend_percent, peer_set$facility_id), , drop = FALSE]
peer_set$facility_label <- factor(peer_set$facility_label, levels = peer_set$facility_label)
state_median <- stats::median(reported$recommend_percent)

if (!dir.exists(output_dir)) {
  dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
}
utils::write.csv(
  peer_set[, c("facility_id", "facility_name", "recommend_percent", "completed_surveys")],
  file.path(output_dir, "peer-set-table.csv"),
  row.names = FALSE
)

encoding_map <- data.frame(
  variable = c("facility_name", "recommend_percent", "recommend_percent", "completed_surveys", "cms_release_date"),
  data_role = c("nominal category", "quantitative measure", "quantitative measure", "quantitative context", "provenance"),
  mark_or_layer = c("point", "point", "text label", "selection rule", "caption"),
  visual_channel = c("y position", "x position", "text", "not encoded", "not encoded"),
  reason = c(
    "An aligned list supports facility lookup.",
    "Position on a common scale supports comparison.",
    "A direct label repeats the exact value.",
    "Survey count defines the teaching peer set and remains in the table.",
    "The release belongs in the source note, not in a data mark."
  ),
  stringsAsFactors = FALSE
)
utils::write.csv(encoding_map, file.path(output_dir, "encoding-map.csv"), row.names = FALSE)

chart <- ggplot2::ggplot(
  peer_set,
  ggplot2::aes(y = facility_label, x = recommend_percent)
) +
  ggplot2::geom_vline(xintercept = state_median, color = "#64748b", linetype = "dashed", linewidth = 0.7) +
  ggplot2::geom_segment(
    ggplot2::aes(x = state_median, xend = recommend_percent, yend = facility_label),
    color = "#cbd5e1",
    linewidth = 0.8
  ) +
  ggplot2::geom_point(color = "#1f49b6", size = 3.2) +
  ggplot2::geom_text(
    ggplot2::aes(label = paste0(recommend_percent, "%")),
    nudge_x = 1.7,
    size = 3.4,
    color = "#0f172a"
  ) +
  ggplot2::scale_x_continuous(
    limits = c(45, 92),
    breaks = seq(50, 90, 10),
    labels = function(values) paste0(values, "%")
  ) +
  ggplot2::labs(
    title = "Patients' willingness to recommend varies across selected Massachusetts hospitals",
    subtitle = paste0(
      "Fifteen hospitals with the most completed surveys. Dashed line: all reported MA hospitals median, ",
      state_median,
      "%"
    ),
    x = "Patients who would definitely recommend the hospital",
    y = NULL,
    caption = paste0(
      "Source: CMS Patient survey (HCAHPS) - Hospital, release ",
      unique(peer_set$cms_release_date),
      ". Measurement period ",
      unique(peer_set$period_start),
      " to ",
      unique(peer_set$period_end),
      "."
    )
  ) +
  ggplot2::theme_minimal(base_size = 12) +
  ggplot2::theme(
    panel.grid.major.y = ggplot2::element_blank(),
    panel.grid.minor = ggplot2::element_blank(),
    plot.title.position = "plot",
    plot.caption.position = "plot",
    axis.text.y = ggplot2::element_text(color = "#0f172a")
  )

ggplot2::ggsave(
  file.path(output_dir, "layered-comparison.png"),
  chart,
  width = 10,
  height = 7.5,
  dpi = 150,
  bg = "white"
)

cat("Created lab outputs in:", normalizePath(output_dir, winslash = "/"), "\n")
cat(sprintf("The comparison uses %d hospitals. The all-reported-hospital median is %.1f%%.\n", nrow(peer_set), state_median))
cat(paste0(
  "\nTier 1, run and observe:\n",
  "1. Match each row of encoding-map.csv to a visible part of layered-comparison.png.\n",
  "2. Explain why recommend_percent is on x position and facility_name is on y position.\n",
  "3. Identify the reference-line layer, point layer, text layer, scale, and labels.\n",
  "\nTier 2, modify:\n",
  "1. Replace geom_point() with geom_col() and explain what length adds or removes.\n",
  "2. Remove the direct labels. Record what becomes harder to read.\n",
  "3. Map completed_surveys to point size. Decide whether that second encoding helps this decision.\n",
  "\nTier 3, author:\n",
  "Build a comparison for a clearly named patient-experience decision. Submit the six files listed in assessment.md.\n"
))
