args <- commandArgs(trailingOnly = TRUE)
case_path <- if (length(args) >= 1) args[[1]] else file.path("data", "selection_cases_2026.csv")
default_sources <- c(
  file.path("..", "01-encoding-grammar", "data", "hcahps_ma_recommend_2026.csv"),
  "hcahps_ma_recommend_2026.csv"
)
available_source <- default_sources[file.exists(default_sources)][1]
source_path <- if (length(args) >= 2) args[[2]] else if (!is.na(available_source)) available_source else default_sources[[1]]
output_dir <- if (length(args) >= 3) args[[3]] else file.path("outputs", "lab")

if (!requireNamespace("ggplot2", quietly = TRUE)) {
  stop("Package 'ggplot2' is required. Install it with: install.packages('ggplot2')", call. = FALSE)
}
if (!file.exists(case_path) || !file.exists(source_path)) {
  stop("Selection cases and the Module 01 HCAHPS extract are required.", call. = FALSE)
}

cases <- utils::read.csv(case_path, stringsAsFactors = FALSE)
source <- utils::read.csv(source_path, stringsAsFactors = FALSE, na.strings = "")
required_source_columns <- c(
  "facility_id",
  "facility_name",
  "recommend_percent",
  "completed_surveys",
  "response_rate_percent",
  "value_status",
  "period_start",
  "period_end",
  "cms_release_date"
)
missing_columns <- setdiff(required_source_columns, names(source))
if (length(missing_columns) > 0) {
  stop(sprintf("HCAHPS input is missing columns: %s", paste(missing_columns, collapse = ", ")), call. = FALSE)
}

reported <- source[
  source$value_status == "reported" &
    is.finite(source$recommend_percent) &
    is.finite(source$completed_surveys) &
    is.finite(source$response_rate_percent),
  ,
  drop = FALSE
]
peer_set <- head(reported[order(-reported$completed_surveys, reported$facility_id), ], 15)
peer_set$facility_label <- tools::toTitleCase(tolower(peer_set$facility_name))
peer_set <- peer_set[order(peer_set$recommend_percent, peer_set$facility_id), , drop = FALSE]
peer_set$facility_label <- factor(peer_set$facility_label, levels = peer_set$facility_label)

if (!dir.exists(output_dir)) {
  dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
}

base_theme <- ggplot2::theme_minimal(base_size = 12) +
  ggplot2::theme(
    panel.grid.minor = ggplot2::element_blank(),
    plot.title.position = "plot",
    plot.caption.position = "plot"
  )

comparison <- ggplot2::ggplot(peer_set, ggplot2::aes(x = recommend_percent, y = facility_label)) +
  ggplot2::geom_point(color = "#1f49b6", size = 3.2) +
  ggplot2::geom_text(ggplot2::aes(label = paste0(recommend_percent, "%")), nudge_x = 1.6, size = 3.2) +
  ggplot2::scale_x_continuous(limits = c(45, 92), breaks = seq(50, 90, 10), labels = function(x) paste0(x, "%")) +
  ggplot2::labs(
    title = "Recommendation results across selected Massachusetts hospitals",
    subtitle = "Aligned position supports ordering; the companion table preserves survey context",
    x = "Patients who would definitely recommend the hospital",
    y = NULL,
    caption = paste0("CMS HCAHPS release ", unique(peer_set$cms_release_date), ", period ", unique(peer_set$period_start), " to ", unique(peer_set$period_end), ".")
  ) +
  base_theme +
  ggplot2::theme(panel.grid.major.y = ggplot2::element_blank())

relationship <- ggplot2::ggplot(
  reported,
  ggplot2::aes(x = response_rate_percent, y = recommend_percent, size = completed_surveys)
) +
  ggplot2::geom_point(color = "#1f49b6", alpha = 0.65) +
  ggplot2::scale_size_area(max_size = 10, breaks = c(250, 1000, 2500, 5000)) +
  ggplot2::scale_x_continuous(labels = function(x) paste0(x, "%")) +
  ggplot2::scale_y_continuous(labels = function(x) paste0(x, "%")) +
  ggplot2::labs(
    title = "Recommendation result and survey response rate answer different questions",
    subtitle = "Each point is a Massachusetts hospital; area represents completed surveys",
    x = "Survey response rate",
    y = "Patients who would definitely recommend",
    size = "Completed surveys",
    caption = paste0("CMS HCAHPS release ", unique(reported$cms_release_date), ". Association does not establish a cause.")
  ) +
  base_theme

ggplot2::ggsave(file.path(output_dir, "01-comparison-dot-plot.png"), comparison, width = 10, height = 7.5, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "02-response-relationship.png"), relationship, width = 8.5, height = 6, dpi = 150, bg = "white")

lookup_table <- peer_set[, c("facility_id", "facility_name", "recommend_percent", "response_rate_percent", "completed_surveys")]
utils::write.csv(lookup_table, file.path(output_dir, "03-exact-lookup-table.csv"), row.names = FALSE)
utils::write.csv(cases, file.path(output_dir, "selection-matrix-reference.csv"), row.names = FALSE)

template <- cases[, c("case_id", "case_title", "decision_owner", "decision", "reader_task", "data_shape", "precision_need", "context_required")]
template$candidate_display <- ""
template$required_companion <- ""
template$rejected_alternative <- ""
template$failure_test <- ""
template$final_choice <- ""
template$justification <- ""
utils::write.csv(template, file.path(output_dir, "selection-matrix-template.csv"), row.names = FALSE)

cat(sprintf("Created two charts, one exact-value table, and two selection matrices in %s.\n", normalizePath(output_dir, winslash = "/")))
cat(paste0(
  "For every case:\n",
  "1. Name the decision and reader task before a chart type.\n",
  "2. State the data grain, precision need, and missing context.\n",
  "3. Propose the smallest useful display and a required companion.\n",
  "4. Reject one plausible alternative for a concrete reason.\n",
  "5. Apply the no-display trigger before finalizing the choice.\n"
))
