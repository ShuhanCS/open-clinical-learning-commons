args <- commandArgs(trailingOnly = TRUE)
case_path <- if (length(args) >= 1) args[[1]] else file.path("data", "selection_cases_2026.csv")
default_sources <- c(
  file.path("..", "01-encoding-grammar", "data", "hcahps_ma_recommend_2026.csv"),
  "hcahps_ma_recommend_2026.csv"
)
available_source <- default_sources[file.exists(default_sources)][1]
source_path <- if (length(args) >= 2) args[[2]] else if (!is.na(available_source)) available_source else default_sources[[1]]

if (!file.exists(case_path)) {
  stop(sprintf("Selection-case file not found: %s", case_path), call. = FALSE)
}
if (!file.exists(source_path)) {
  stop(sprintf("Module 01 HCAHPS file not found: %s", source_path), call. = FALSE)
}

cases <- utils::read.csv(case_path, stringsAsFactors = FALSE, check.names = FALSE)
source <- utils::read.csv(source_path, stringsAsFactors = FALSE, na.strings = "")
expected_columns <- c(
  "case_id",
  "case_title",
  "decision_owner",
  "decision",
  "reader_task",
  "data_shape",
  "precision_need",
  "context_required",
  "source_url",
  "reference_choice",
  "required_companion",
  "no_display_trigger",
  "build_mode"
)

checks <- data.frame(check = character(), passed = logical(), result = character(), stringsAsFactors = FALSE)
record_check <- function(name, passed, result) {
  checks[nrow(checks) + 1, ] <<- list(name, isTRUE(passed), as.character(result))
}

record_check("columns", identical(names(cases), expected_columns), paste(names(cases), collapse = ", "))
if (!checks$passed[[1]]) {
  print(checks, row.names = FALSE)
  stop("Structural validation failed: unexpected selection-case columns.", call. = FALSE)
}

expected_tasks <- c("compare", "lookup", "relationship", "distribution", "time", "composition", "flow", "geography", "monitor", "verify evidence")
record_check("case count", nrow(cases) == 10L, nrow(cases))
record_check("case IDs", identical(cases$case_id, sprintf("C%02d", 1:10)), paste(cases$case_id, collapse = ", "))
record_check("unique titles", length(unique(cases$case_title)) == 10L, length(unique(cases$case_title)))
record_check("reader-task coverage", identical(cases$reader_task, expected_tasks), paste(cases$reader_task, collapse = ", "))
record_check("complete fields", !anyNA(cases) && !any(cases == ""), sprintf("blank=%d missing=%d", sum(cases == ""), sum(is.na(cases))))
record_check("full source URLs", all(grepl("^https://", cases$source_url)), paste(unique(cases$source_url), collapse = "; "))
record_check(
  "build-mode contract",
  sum(cases$build_mode == "build") == 2L && sum(cases$build_mode == "table") == 1L && sum(cases$build_mode == "decision-only") == 7L,
  paste(names(table(cases$build_mode)), as.integer(table(cases$build_mode)), collapse = "; ")
)
record_check("one no-display choice", sum(grepl("^no display", cases$reference_choice)) == 1L, sum(grepl("^no display", cases$reference_choice)))
record_check("failure gate present", all(nchar(cases$no_display_trigger) >= 30), paste(nchar(cases$no_display_trigger), collapse = ", "))

reported <- source[source$value_status == "reported", , drop = FALSE]
record_check("HCAHPS release", all(source$cms_release_date == "2026-08-13"), paste(unique(source$cms_release_date), collapse = ", "))
record_check("HCAHPS reported rows", nrow(reported) == 56L, nrow(reported))
record_check(
  "relationship fields available",
  sum(is.finite(reported$recommend_percent) & is.finite(reported$response_rate_percent) & is.finite(reported$completed_surveys)) >= 50L,
  sum(is.finite(reported$recommend_percent) & is.finite(reported$response_rate_percent) & is.finite(reported$completed_surveys))
)

cat(sprintf("Validation report: %s\n", case_path))
print(checks, row.names = FALSE)
if (!all(checks$passed)) {
  stop(sprintf("Validation failed: %d check(s).", sum(!checks$passed)), call. = FALSE)
}
cat(sprintf("PASS: %d checks passed.\n", nrow(checks)))
