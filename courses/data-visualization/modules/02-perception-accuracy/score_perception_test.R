args <- commandArgs(trailingOnly = TRUE)
response_path <- if (length(args) >= 1) args[[1]] else file.path("outputs", "lab", "response-template-a.csv")
task_path <- if (length(args) >= 2) args[[2]] else file.path("data", "perception_tasks_2026.csv")
output_dir <- if (length(args) >= 3) args[[3]] else file.path("outputs", "scored")

if (!file.exists(response_path)) {
  stop(sprintf("Response file not found: %s", response_path), call. = FALSE)
}
if (!file.exists(task_path)) {
  stop(sprintf("Task file not found: %s", task_path), call. = FALSE)
}

responses <- utils::read.csv(response_path, stringsAsFactors = FALSE, na.strings = "")
tasks <- utils::read.csv(task_path, stringsAsFactors = FALSE)
required_response_columns <- c(
  "order",
  "trial_id",
  "display",
  "higher_response",
  "estimated_gap_points",
  "seconds",
  "confusion_note"
)
missing_columns <- setdiff(required_response_columns, names(responses))
if (length(missing_columns) > 0) {
  stop(sprintf("Response file is missing columns: %s", paste(missing_columns, collapse = ", ")), call. = FALSE)
}
if (nrow(responses) != nrow(tasks) || anyDuplicated(responses$trial_id)) {
  stop(sprintf("Response file must contain each of the %d trials exactly once.", nrow(tasks)), call. = FALSE)
}

positions <- match(responses$trial_id, tasks$trial_id)
if (anyNA(positions)) {
  stop(sprintf("Unknown trial IDs: %s", paste(responses$trial_id[is.na(positions)], collapse = ", ")), call. = FALSE)
}
responses$higher_response <- toupper(trimws(responses$higher_response))
responses$estimated_gap_points <- suppressWarnings(as.numeric(responses$estimated_gap_points))
responses$seconds <- suppressWarnings(as.numeric(responses$seconds))
if (!all(responses$higher_response %in% c("A", "B"))) {
  stop("Every higher_response must be A or B.", call. = FALSE)
}
if (anyNA(responses$estimated_gap_points) || any(responses$estimated_gap_points < 0)) {
  stop("Every estimated_gap_points value must be a non-negative number.", call. = FALSE)
}
if (anyNA(responses$seconds) || any(responses$seconds <= 0)) {
  stop("Every seconds value must be a positive number.", call. = FALSE)
}

key <- tasks[positions, , drop = FALSE]
scored <- data.frame(
  order = responses$order,
  trial_id = responses$trial_id,
  display = key$display,
  higher_response = responses$higher_response,
  correct_alias = key$correct_alias,
  is_correct = responses$higher_response == key$correct_alias,
  estimated_gap_points = responses$estimated_gap_points,
  correct_gap_points = key$correct_gap_points,
  absolute_gap_error = abs(responses$estimated_gap_points - key$correct_gap_points),
  seconds = responses$seconds,
  confusion_note = ifelse(is.na(responses$confusion_note), "", responses$confusion_note),
  stringsAsFactors = FALSE
)

summary_rows <- lapply(split(scored, scored$display), function(frame) {
  data.frame(
    display = frame$display[[1]],
    trials = nrow(frame),
    higher_accuracy_percent = 100 * mean(frame$is_correct),
    mean_absolute_gap_error = mean(frame$absolute_gap_error),
    median_seconds = stats::median(frame$seconds),
    stringsAsFactors = FALSE
  )
})
summary <- do.call(rbind, summary_rows)
summary <- summary[match(c("dot", "bar", "table", "pie", "bubble"), summary$display), , drop = FALSE]
rownames(summary) <- NULL

if (!dir.exists(output_dir)) {
  dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
}
utils::write.csv(scored, file.path(output_dir, "scored-trials.csv"), row.names = FALSE)
utils::write.csv(summary, file.path(output_dir, "perception-summary.csv"), row.names = FALSE)

cat("Perception test summary\n")
print(summary, row.names = FALSE, digits = 3)
cat(paste0(
  "\nThese 10 classroom trials are practice evidence, not a population study. ",
  "Use them to inspect your own errors and effort, not to claim a universal ranking from one learner.\n"
))
