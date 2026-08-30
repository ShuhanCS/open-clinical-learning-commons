args <- commandArgs(trailingOnly = TRUE)
output_path <- if (length(args) >= 1) args[[1]] else file.path("data", "cms_ed_op18b_2026.csv")
source_location <- if (length(args) >= 2) args[[2]] else paste0(
  "https://data.cms.gov/provider-data/sites/default/files/resources/",
  "0437b5494ac61507ad90f2af6b8085a7_1785189967/",
  "Timely_and_Effective_Care-Hospital.csv"
)

metadata_url <- "https://data.cms.gov/provider-data/api/1/metastore/schemas/dataset/items/yv7e-xc69"
landing_page <- "https://data.cms.gov/provider-data/dataset/yv7e-xc69"
expected_release <- "2026-08-13"
expected_modified <- "2026-07-22"

extract_json_string <- function(text, field) {
  pattern <- paste0('"', field, '"\\s*:\\s*"([^"]+)"')
  hit <- regmatches(text, regexec(pattern, text, perl = TRUE))[[1]]
  if (length(hit) != 2) {
    stop(sprintf("CMS metadata does not contain a readable '%s' field.", field), call. = FALSE)
  }
  hit[[2]]
}

metadata_text <- paste(readLines(metadata_url, warn = FALSE, encoding = "UTF-8"), collapse = "")
release_date <- extract_json_string(metadata_text, "released")
modified_date <- extract_json_string(metadata_text, "modified")
if (release_date != expected_release || modified_date != expected_modified) {
  stop(
    sprintf(
      paste0(
        "CMS now reports release=%s and modified=%s. ",
        "This build is pinned to release=%s and modified=%s. Review the new release before rebuilding."
      ),
      release_date,
      modified_date,
      expected_release,
      expected_modified
    ),
    call. = FALSE
  )
}

downloaded <- grepl("^https://", source_location)
source_path <- source_location
if (downloaded) {
  source_path <- tempfile(fileext = ".csv")
  on.exit(unlink(source_path), add = TRUE)
  utils::download.file(source_location, source_path, mode = "wb", quiet = TRUE)
}
if (!file.exists(source_path)) {
  stop(sprintf("CMS source file not found: %s", source_path), call. = FALSE)
}

source <- utils::read.csv(
  source_path,
  stringsAsFactors = FALSE,
  check.names = FALSE,
  na.strings = NULL,
  encoding = "UTF-8"
)
required_source_columns <- c(
  "Facility ID",
  "Facility Name",
  "City/Town",
  "State",
  "Measure ID",
  "Measure Name",
  "Score",
  "Sample",
  "Footnote",
  "Start Date",
  "End Date"
)
missing_columns <- setdiff(required_source_columns, names(source))
if (length(missing_columns) > 0) {
  stop(sprintf("CMS source is missing columns: %s", paste(missing_columns, collapse = ", ")), call. = FALSE)
}

source <- source[source[["Measure ID"]] == "OP_18b", required_source_columns, drop = FALSE]
if (nrow(source) != 4658L) {
  stop(sprintf("Expected 4,658 OP_18b rows, received %d.", nrow(source)), call. = FALSE)
}

reported <- grepl("^[0-9]+(?:\\.[0-9]+)?$", source[["Score"]])
score_min <- rep(NA_real_, nrow(source))
score_min[reported] <- as.numeric(source[["Score"]][reported])

data <- data.frame(
  facility_id = source[["Facility ID"]],
  facility_name = source[["Facility Name"]],
  city = source[["City/Town"]],
  state = source[["State"]],
  measure_id = source[["Measure ID"]],
  measure_name = source[["Measure Name"]],
  score_min = score_min,
  value_status = ifelse(reported, "reported", "not_available"),
  sample = source[["Sample"]],
  footnote = source[["Footnote"]],
  period_start = format(as.Date(source[["Start Date"]], format = "%m/%d/%Y"), "%Y-%m-%d"),
  period_end = format(as.Date(source[["End Date"]], format = "%m/%d/%Y"), "%Y-%m-%d"),
  cms_release_date = release_date,
  source_url = landing_page,
  stringsAsFactors = FALSE,
  check.names = FALSE
)
data <- data[order(data$state, data$facility_id), , drop = FALSE]
rownames(data) <- NULL

if (sum(data$value_status == "reported") != 4081L || stats::median(data$score_min, na.rm = TRUE) != 148) {
  stop("The pinned OP_18b release no longer matches its reported-row or median contract.", call. = FALSE)
}

output_dir <- dirname(output_path)
if (!dir.exists(output_dir)) {
  dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
}
utils::write.csv(data, output_path, row.names = FALSE, na = "", eol = "\n", fileEncoding = "UTF-8")

cat(sprintf(
  "Built %s with %d national OP_18b rows from CMS release %s; reported median=%d minutes.\n",
  normalizePath(output_path, winslash = "/", mustWork = FALSE),
  nrow(data),
  release_date,
  stats::median(data$score_min, na.rm = TRUE)
))
