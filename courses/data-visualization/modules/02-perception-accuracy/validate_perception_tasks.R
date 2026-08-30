args <- commandArgs(trailingOnly = TRUE)
task_path <- if (length(args) >= 1) args[[1]] else file.path("data", "perception_tasks_2026.csv")
default_sources <- c(
  file.path("..", "01-encoding-grammar", "data", "hcahps_ma_recommend_2026.csv"),
  "hcahps_ma_recommend_2026.csv"
)
available_source <- default_sources[file.exists(default_sources)][1]
source_path <- if (length(args) >= 2) args[[2]] else if (!is.na(available_source)) available_source else default_sources[[1]]

if (!file.exists(task_path)) {
  stop(sprintf("Task file not found: %s", task_path), call. = FALSE)
}
if (!file.exists(source_path)) {
  stop(sprintf("Module 01 HCAHPS file not found: %s", source_path), call. = FALSE)
}

tasks <- utils::read.csv(task_path, stringsAsFactors = FALSE)
source <- utils::read.csv(source_path, stringsAsFactors = FALSE, na.strings = "")
expected_columns <- c(
  "trial_id",
  "display",
  "facility_a_id",
  "facility_a_name",
  "facility_a_percent",
  "facility_b_id",
  "facility_b_name",
  "facility_b_percent",
  "correct_alias",
  "correct_hospital_id",
  "correct_hospital_name",
  "correct_gap_points",
  "cms_release_date"
)

checks <- data.frame(check = character(), passed = logical(), result = character(), stringsAsFactors = FALSE)
record_check <- function(name, passed, result) {
  checks[nrow(checks) + 1, ] <<- list(name, isTRUE(passed), as.character(result))
}

record_check("columns", identical(names(tasks), expected_columns), paste(names(tasks), collapse = ", "))
if (!checks$passed[[1]]) {
  print(checks, row.names = FALSE)
  stop("Structural validation failed: unexpected task columns.", call. = FALSE)
}

display_counts <- table(tasks$display)
expected_displays <- c("bar", "bubble", "dot", "pie", "table")
record_check("trial count", nrow(tasks) == 10L, nrow(tasks))
record_check("unique trial IDs", identical(tasks$trial_id, sprintf("T%02d", 1:10)), paste(tasks$trial_id, collapse = ", "))
record_check(
  "two trials per display",
  identical(names(display_counts), expected_displays) && all(display_counts == 2L),
  paste(names(display_counts), as.integer(display_counts), collapse = "; ")
)
record_check(
  "balanced correct aliases",
  identical(as.integer(table(tasks$correct_alias)[c("A", "B")]), c(5L, 5L)),
  paste(names(table(tasks$correct_alias)), as.integer(table(tasks$correct_alias)), collapse = "; ")
)
record_check(
  "comparison gaps",
  all(tasks$correct_gap_points >= 2 & tasks$correct_gap_points <= 10),
  paste(sort(unique(tasks$correct_gap_points)), collapse = ", ")
)
record_check(
  "release",
  all(tasks$cms_release_date == "2026-08-13"),
  paste(unique(tasks$cms_release_date), collapse = ", ")
)

match_source <- function(ids, field) {
  positions <- match(ids, source$facility_id)
  if (anyNA(positions)) rep(NA, length(ids)) else source[[field]][positions]
}
record_check(
  "facility A values match source",
  identical(as.numeric(tasks$facility_a_percent), as.numeric(match_source(tasks$facility_a_id, "recommend_percent"))),
  "checked 10 values"
)
record_check(
  "facility B values match source",
  identical(as.numeric(tasks$facility_b_percent), as.numeric(match_source(tasks$facility_b_id, "recommend_percent"))),
  "checked 10 values"
)

calculated_alias <- ifelse(tasks$facility_a_percent > tasks$facility_b_percent, "A", "B")
calculated_gap <- abs(tasks$facility_a_percent - tasks$facility_b_percent)
record_check("answer aliases", identical(tasks$correct_alias, calculated_alias), paste(tasks$correct_alias, collapse = ", "))
record_check("answer gaps", identical(as.numeric(tasks$correct_gap_points), as.numeric(calculated_gap)), paste(tasks$correct_gap_points, collapse = ", "))
record_check(
  "answer hospital IDs",
  identical(
    tasks$correct_hospital_id,
    ifelse(tasks$correct_alias == "A", tasks$facility_a_id, tasks$facility_b_id)
  ),
  "checked 10 IDs"
)

cat(sprintf("Validation report: %s\n", task_path))
print(checks, row.names = FALSE)
if (!all(checks$passed)) {
  stop(sprintf("Validation failed: %d check(s).", sum(!checks$passed)), call. = FALSE)
}
cat(sprintf("PASS: %d checks passed.\n", nrow(checks)))
