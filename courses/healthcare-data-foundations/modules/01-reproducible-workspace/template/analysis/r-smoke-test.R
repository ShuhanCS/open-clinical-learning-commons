root <- normalizePath(".", winslash = "/", mustWork = TRUE)
data_path <- file.path(root, "data", "workspace_smoke_test.csv")

if (!file.exists(data_path)) {
  stop("Run this script from the learner-workspace root.", call. = FALSE)
}

smoke <- read.csv(data_path, stringsAsFactors = FALSE)
stopifnot(
  identical(names(smoke), c("record_id", "source_label", "event_count")),
  nrow(smoke) == 3L,
  length(unique(smoke$record_id)) == 3L,
  sum(smoke$event_count) == 15L
)

dir.create(file.path(root, "outputs"), showWarnings = FALSE)
result <- "WORKSPACE_R_SMOKE_TEST_PASS rows=3 total=15"
writeLines(result, file.path(root, "outputs", "r-smoke-test.txt"))
message(result)
