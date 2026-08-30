args <- commandArgs(trailingOnly = TRUE)
default_sources <- c(
  file.path("..", "01-encoding-grammar", "data", "hcahps_ma_recommend_2026.csv"),
  "hcahps_ma_recommend_2026.csv"
)
available_source <- default_sources[file.exists(default_sources)][1]
source_path <- if (length(args) >= 1) args[[1]] else if (!is.na(available_source)) available_source else default_sources[[1]]
output_path <- if (length(args) >= 2) args[[2]] else file.path("data", "perception_tasks_2026.csv")

if (!file.exists(source_path)) {
  stop(sprintf("Module 01 HCAHPS file not found: %s", source_path), call. = FALSE)
}

source <- utils::read.csv(source_path, stringsAsFactors = FALSE, na.strings = "")
required_columns <- c(
  "facility_id",
  "facility_name",
  "recommend_percent",
  "completed_surveys",
  "value_status",
  "cms_release_date"
)
missing_columns <- setdiff(required_columns, names(source))
if (length(missing_columns) > 0) {
  stop(sprintf("HCAHPS input is missing columns: %s", paste(missing_columns, collapse = ", ")), call. = FALSE)
}

design <- data.frame(
  trial_id = sprintf("T%02d", 1:10),
  display = rep(c("dot", "bar", "table", "pie", "bubble"), each = 2),
  facility_a_id = c(
    "220012", "220163", "220100", "220086", "220086",
    "220100", "220060", "220077", "220033", "220105"
  ),
  facility_b_id = c(
    "220002", "220033", "220031", "220105", "220088",
    "220010", "220074", "220176", "220171", "220031"
  ),
  stringsAsFactors = FALSE
)

lookup <- function(ids, field) {
  positions <- match(ids, source$facility_id)
  if (anyNA(positions)) {
    stop(sprintf("Task design references unknown facility IDs: %s", paste(ids[is.na(positions)], collapse = ", ")), call. = FALSE)
  }
  source[[field]][positions]
}

tasks <- data.frame(
  trial_id = design$trial_id,
  display = design$display,
  facility_a_id = design$facility_a_id,
  facility_a_name = lookup(design$facility_a_id, "facility_name"),
  facility_a_percent = lookup(design$facility_a_id, "recommend_percent"),
  facility_b_id = design$facility_b_id,
  facility_b_name = lookup(design$facility_b_id, "facility_name"),
  facility_b_percent = lookup(design$facility_b_id, "recommend_percent"),
  stringsAsFactors = FALSE
)
if (anyNA(tasks)) {
  stop("Every task facility must have a reported recommendation percentage.", call. = FALSE)
}

tasks$correct_alias <- ifelse(tasks$facility_a_percent > tasks$facility_b_percent, "A", "B")
tasks$correct_hospital_id <- ifelse(
  tasks$correct_alias == "A",
  tasks$facility_a_id,
  tasks$facility_b_id
)
tasks$correct_hospital_name <- ifelse(
  tasks$correct_alias == "A",
  tasks$facility_a_name,
  tasks$facility_b_name
)
tasks$correct_gap_points <- abs(tasks$facility_a_percent - tasks$facility_b_percent)
tasks$cms_release_date <- unique(source$cms_release_date)

output_dir <- dirname(output_path)
if (!dir.exists(output_dir)) {
  dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
}
utils::write.csv(tasks, output_path, row.names = FALSE, eol = "\n", fileEncoding = "UTF-8")

cat(sprintf(
  "Built %s with %d matched perception trials from the Module 01 HCAHPS release.\n",
  normalizePath(output_path, winslash = "/", mustWork = FALSE),
  nrow(tasks)
))
