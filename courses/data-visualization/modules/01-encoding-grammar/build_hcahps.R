args <- commandArgs(trailingOnly = TRUE)
output_path <- if (length(args) >= 1) args[[1]] else file.path("data", "hcahps_ma_recommend_2026.csv")

metadata_url <- "https://data.cms.gov/provider-data/api/1/metastore/schemas/dataset/items/dgck-syfz"
api_url <- paste0(
  "https://data.cms.gov/provider-data/api/1/datastore/query/dgck-syfz/0?",
  "limit=1500&format=csv",
  "&conditions%5B0%5D%5Bproperty%5D=hcahps_measure_id",
  "&conditions%5B0%5D%5Bvalue%5D=H_RECMND_DY",
  "&conditions%5B0%5D%5Boperator%5D=%3D",
  "&conditions%5B1%5D%5Bproperty%5D=state",
  "&conditions%5B1%5D%5Bvalue%5D=MA",
  "&conditions%5B1%5D%5Boperator%5D=%3D"
)
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

source <- utils::read.csv(
  api_url,
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
  "HCAHPS Measure ID",
  "HCAHPS Question",
  "HCAHPS Answer Percent",
  "HCAHPS Answer Percent Footnote",
  "Number of Completed Surveys",
  "Number of Completed Surveys Footnote",
  "Survey Response Rate Percent",
  "Survey Response Rate Percent Footnote",
  "Start Date",
  "End Date"
)
missing_columns <- setdiff(required_source_columns, names(source))
if (length(missing_columns) > 0) {
  stop(
    sprintf("CMS response is missing columns: %s", paste(missing_columns, collapse = ", ")),
    call. = FALSE
  )
}
if (nrow(source) != 65L) {
  stop(sprintf("Expected 65 filtered CMS rows, received %d.", nrow(source)), call. = FALSE)
}
if (!all(source$State == "MA") || !all(source[["HCAHPS Measure ID"]] == "H_RECMND_DY")) {
  stop("CMS response does not match the requested state and measure filters.", call. = FALSE)
}

numeric_or_na <- function(values) {
  reported <- grepl("^[0-9]+(?:\\.[0-9]+)?$", values)
  result <- rep(NA_real_, length(values))
  result[reported] <- as.numeric(values[reported])
  result
}

data <- data.frame(
  facility_id = source[["Facility ID"]],
  facility_name = source[["Facility Name"]],
  city = source[["City/Town"]],
  state = source[["State"]],
  measure_id = source[["HCAHPS Measure ID"]],
  measure = source[["HCAHPS Question"]],
  recommend_percent = numeric_or_na(source[["HCAHPS Answer Percent"]]),
  completed_surveys = numeric_or_na(source[["Number of Completed Surveys"]]),
  response_rate_percent = numeric_or_na(source[["Survey Response Rate Percent"]]),
  value_status = ifelse(
    grepl("^[0-9]+(?:\\.[0-9]+)?$", source[["HCAHPS Answer Percent"]]),
    "reported",
    "not_available"
  ),
  value_footnote = source[["HCAHPS Answer Percent Footnote"]],
  completed_surveys_footnote = source[["Number of Completed Surveys Footnote"]],
  response_rate_footnote = source[["Survey Response Rate Percent Footnote"]],
  period_start = format(as.Date(source[["Start Date"]], format = "%m/%d/%Y"), "%Y-%m-%d"),
  period_end = format(as.Date(source[["End Date"]], format = "%m/%d/%Y"), "%Y-%m-%d"),
  cms_release_date = release_date,
  stringsAsFactors = FALSE,
  check.names = FALSE
)
data <- data[order(data$facility_id), , drop = FALSE]
rownames(data) <- NULL

output_dir <- dirname(output_path)
if (!dir.exists(output_dir)) {
  dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
}
utils::write.csv(data, output_path, row.names = FALSE, na = "", eol = "\n", fileEncoding = "UTF-8")

cat(sprintf(
  "Built %s with %d Massachusetts HCAHPS rows from CMS release %s.\n",
  normalizePath(output_path, winslash = "/", mustWork = FALSE),
  nrow(data),
  release_date
))
