args <- commandArgs(trailingOnly = TRUE)
task_path <- if (length(args) >= 1) args[[1]] else file.path("data", "perception_tasks_2026.csv")
output_dir <- if (length(args) >= 2) args[[2]] else file.path("outputs", "lab")

if (!requireNamespace("ggplot2", quietly = TRUE)) {
  stop("Package 'ggplot2' is required. Install it with: install.packages('ggplot2')", call. = FALSE)
}
if (!file.exists(task_path)) {
  stop(sprintf("Task file not found: %s", task_path), call. = FALSE)
}

tasks <- utils::read.csv(task_path, stringsAsFactors = FALSE)
required_columns <- c(
  "trial_id",
  "display",
  "facility_a_percent",
  "facility_b_percent",
  "correct_alias",
  "correct_hospital_name",
  "correct_gap_points",
  "cms_release_date"
)
missing_columns <- setdiff(required_columns, names(tasks))
if (length(missing_columns) > 0 || nrow(tasks) != 10L) {
  stop(
    sprintf("Task input must have 10 rows and these columns: %s", paste(required_columns, collapse = ", ")),
    call. = FALSE
  )
}

stimulus_dir <- file.path(output_dir, "stimuli")
if (!dir.exists(stimulus_dir)) {
  dir.create(stimulus_dir, recursive = TRUE, showWarnings = FALSE)
}

base_theme <- ggplot2::theme_minimal(base_size = 13) +
  ggplot2::theme(
    panel.grid.minor = ggplot2::element_blank(),
    plot.title.position = "plot",
    plot.caption.position = "plot"
  )

trial_frame <- function(task) {
  data.frame(
    alias = factor(c("Hospital A", "Hospital B"), levels = c("Hospital B", "Hospital A")),
    value = c(task$facility_a_percent, task$facility_b_percent),
    stringsAsFactors = FALSE
  )
}

common_labels <- function(task) {
  ggplot2::labs(
    title = "Which hospital has the higher recommendation result?",
    subtitle = "Estimate the difference in percentage points. Do not open the source table while timing.",
    caption = paste0("CMS HCAHPS teaching stimulus. Source release ", task$cms_release_date, ".")
  )
}

make_dot <- function(task) {
  frame <- trial_frame(task)
  ggplot2::ggplot(frame, ggplot2::aes(x = value, y = alias)) +
    ggplot2::geom_point(color = "#1f49b6", size = 5) +
    ggplot2::scale_x_continuous(limits = c(40, 90), breaks = seq(40, 90, 10), labels = function(x) paste0(x, "%")) +
    ggplot2::labs(x = "Patients who would definitely recommend", y = NULL) +
    common_labels(task) +
    base_theme +
    ggplot2::theme(panel.grid.major.y = ggplot2::element_blank())
}

make_bar <- function(task) {
  frame <- trial_frame(task)
  ggplot2::ggplot(frame, ggplot2::aes(x = value, y = alias)) +
    ggplot2::geom_col(fill = "#1f49b6", width = 0.6) +
    ggplot2::scale_x_continuous(limits = c(0, 100), breaks = seq(0, 100, 20), labels = function(x) paste0(x, "%")) +
    ggplot2::labs(x = "Patients who would definitely recommend", y = NULL) +
    common_labels(task) +
    base_theme +
    ggplot2::theme(panel.grid.major.y = ggplot2::element_blank())
}

make_table <- function(task) {
  frame <- trial_frame(task)
  frame$label <- paste0(frame$value, "%")
  ggplot2::ggplot(frame, ggplot2::aes(y = alias)) +
    ggplot2::geom_text(ggplot2::aes(x = 0, label = alias), hjust = 0, size = 5) +
    ggplot2::geom_text(ggplot2::aes(x = 1, label = label), hjust = 1, size = 5, fontface = "bold") +
    ggplot2::annotate("segment", x = 0, xend = 1, y = 1.5, yend = 1.5, color = "#cbd5e1") +
    ggplot2::scale_x_continuous(limits = c(0, 1), breaks = NULL) +
    ggplot2::scale_y_discrete(labels = NULL) +
    ggplot2::labs(x = NULL, y = NULL) +
    common_labels(task) +
    ggplot2::theme_void(base_size = 13) +
    ggplot2::theme(plot.title = ggplot2::element_text(size = 15), plot.subtitle = ggplot2::element_text(size = 11), plot.caption = ggplot2::element_text(size = 9), plot.title.position = "plot")
}

make_pie <- function(task) {
  values <- c(task$facility_a_percent, task$facility_b_percent)
  frame <- data.frame(
    alias = rep(c("Hospital A", "Hospital B"), each = 2),
    response = rep(c("Would definitely recommend", "Other response"), 2),
    value = c(values[[1]], 100 - values[[1]], values[[2]], 100 - values[[2]]),
    stringsAsFactors = FALSE
  )
  ggplot2::ggplot(frame, ggplot2::aes(x = "", y = value, fill = response)) +
    ggplot2::geom_col(width = 1, color = "white", linewidth = 0.7) +
    ggplot2::coord_polar(theta = "y") +
    ggplot2::facet_wrap(~alias) +
    ggplot2::scale_fill_manual(values = c("Would definitely recommend" = "#1f49b6", "Other response" = "#cbd5e1")) +
    ggplot2::labs(fill = NULL) +
    common_labels(task) +
    ggplot2::theme_void(base_size = 13) +
    ggplot2::theme(plot.title = ggplot2::element_text(size = 15), plot.subtitle = ggplot2::element_text(size = 11), plot.caption = ggplot2::element_text(size = 9), plot.title.position = "plot", legend.position = "bottom")
}

make_bubble <- function(task) {
  frame <- trial_frame(task)
  ggplot2::ggplot(frame, ggplot2::aes(x = 1, y = alias, size = value)) +
    ggplot2::geom_point(color = "#1f49b6", alpha = 0.8) +
    ggplot2::scale_size_area(max_size = 28, limits = c(0, 100), breaks = c(25, 50, 75, 100)) +
    ggplot2::scale_x_continuous(limits = c(0.98, 1.02), breaks = NULL) +
    ggplot2::labs(x = NULL, y = NULL, size = "Percent") +
    common_labels(task) +
    base_theme +
    ggplot2::theme(panel.grid = ggplot2::element_blank())
}

plotters <- list(dot = make_dot, bar = make_bar, table = make_table, pie = make_pie, bubble = make_bubble)
for (index in seq_len(nrow(tasks))) {
  task <- tasks[index, , drop = FALSE]
  plotter <- plotters[[task$display]]
  if (is.null(plotter)) {
    stop(sprintf("Unknown display type: %s", task$display), call. = FALSE)
  }
  plot <- plotter(task)
  ggplot2::ggsave(
    file.path(stimulus_dir, paste0(task$trial_id, "-", task$display, ".png")),
    plot,
    width = 8,
    height = 4.8,
    dpi = 150,
    bg = "white"
  )
}

set.seed(73002)
order_a <- tasks[sample(seq_len(nrow(tasks))), c("trial_id", "display")]
order_a$order <- seq_len(nrow(order_a))
order_a <- order_a[, c("order", "trial_id", "display")]
order_b <- order_a[nrow(order_a):1, , drop = FALSE]
order_b$order <- seq_len(nrow(order_b))

make_template <- function(order_frame) {
  data.frame(
    order = order_frame$order,
    trial_id = order_frame$trial_id,
    display = order_frame$display,
    higher_response = "",
    estimated_gap_points = "",
    seconds = "",
    confusion_note = "",
    stringsAsFactors = FALSE
  )
}

utils::write.csv(make_template(order_a), file.path(output_dir, "response-template-a.csv"), row.names = FALSE)
utils::write.csv(make_template(order_b), file.path(output_dir, "response-template-b.csv"), row.names = FALSE)
utils::write.csv(tasks, file.path(output_dir, "instructor-key.csv"), row.names = FALSE)

cat(sprintf("Created %d perception stimuli and two counterbalanced response templates in %s.\n", nrow(tasks), normalizePath(output_dir, winslash = "/")))
cat(paste0(
  "Test rule:\n",
  "1. Use template A or B. A partner opens one named stimulus at a time.\n",
  "2. Start timing when the full image is visible.\n",
  "3. Record A or B, the estimated percentage-point gap, elapsed seconds, and any confusion.\n",
  "4. Stop after all 10 trials, then run score_perception_test.R.\n"
))
