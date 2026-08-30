args <- commandArgs(trailingOnly = TRUE)
output_path <- if (length(args) >= 1) args[[1]] else file.path("data", "selection_cases_2026.csv")

cases <- data.frame(
  case_id = sprintf("C%02d", 1:10),
  case_title = c(
    "Compare hospital recommendation results",
    "Look up exact patient-experience values",
    "Examine recommendation and response rate",
    "Find patients hidden by an average length of stay",
    "Monitor an emergency-care measure over reporting periods",
    "Show how causes contribute to a mortality total",
    "Find where patients leave a care pathway",
    "Locate counties with need and limited workforce access",
    "Monitor three hospital measures and preserve exact values",
    "Answer a question the available data do not support"
  ),
  decision_owner = c(
    "Hospital executive team",
    "Patient-experience director",
    "Survey program lead",
    "Emergency department director",
    "Clinical operations committee",
    "Population-health director",
    "Care-pathway improvement team",
    "Community health planning coalition",
    "Hospital quality committee",
    "Hospital executive team"
  ),
  decision = c(
    "Choose results for deeper review without declaring a quality ranking.",
    "Retrieve the exact recommendation, response-rate, and completed-survey values for named hospitals.",
    "Identify hospitals whose recommendation result and response rate warrant follow-up.",
    "Decide whether the typical stay conceals a long-stay group that changes the improvement plan.",
    "Decide whether a process measure shows a sustained change that warrants action.",
    "Choose which cause group needs a prevention or investigation priority.",
    "Choose the transition where pathway redesign should begin.",
    "Choose counties for deeper access planning, not allocate resources from a map alone.",
    "Monitor current status while preserving the detail needed for follow-up.",
    "Decide whether to pause and request better evidence before communicating a result."
  ),
  reader_task = c(
    "compare",
    "lookup",
    "relationship",
    "distribution",
    "time",
    "composition",
    "flow",
    "geography",
    "monitor",
    "verify evidence"
  ),
  data_shape = c(
    "one quantitative result across named hospitals",
    "three exact values for a small named hospital set",
    "two quantitative measures plus survey-count context",
    "encounter-level continuous values with possible skew and subgroups",
    "one consistently defined measure across ordered periods",
    "counts within a defensible total and hierarchy",
    "counts moving among ordered pathway states",
    "county estimate, geography, population context, and workforce measure",
    "three current measures across hospitals plus exact values",
    "suppressed or mismatched values with no defensible denominator"
  ),
  precision_need = c(
    "ordered pattern and close gaps",
    "exact values",
    "broad relationship and unusual combinations",
    "shape, tails, and subgroup structure",
    "direction, timing, and process variation",
    "part-to-whole contribution and exact counts",
    "pathway magnitude and drop-off location",
    "spatial pattern plus exact comparison",
    "overview and exact lookup",
    "no quantitative claim until evidence is adequate"
  ),
  context_required = c(
    "completed surveys, response rate, release, period, and comparison limits",
    "measure definitions, unavailable values, release, and period",
    "completed surveys, missingness, release, and noncausal claim",
    "sample size, subgroup, censoring, and unit definition",
    "reporting period, measure-definition stability, target, and ordinary variation",
    "denominator, cause hierarchy, suppression, and reliability flags",
    "cohort entry, state definitions, repeated encounters, and missing transitions",
    "population denominator, estimate uncertainty, geography, and workforce year",
    "measure definitions, target or reference, unavailable values, release, and period",
    "missingness reason, denominator, population, time alignment, and decision need"
  ),
  source_url = c(
    "https://data.cms.gov/provider-data/dataset/dgck-syfz",
    "https://data.cms.gov/provider-data/dataset/dgck-syfz",
    "https://data.cms.gov/provider-data/dataset/dgck-syfz",
    "https://synthetichealth.github.io/synthea/",
    "https://data.cms.gov/provider-data/dataset/yv7e-xc69",
    "https://wonder.cdc.gov/datasets.html",
    "https://synthetichealth.github.io/synthea/",
    "https://data.cdc.gov/d/fu4u-a9bh",
    "https://data.cms.gov/provider-data/topics/hospitals",
    "https://data.cms.gov/provider-data/dataset/dgck-syfz"
  ),
  reference_choice = c(
    "aligned dot plot",
    "table",
    "scatterplot",
    "distribution view with subgroup comparison",
    "line or run chart with process context",
    "ordered composition view with companion counts",
    "flow view with a companion transition table",
    "map plus aligned comparison",
    "coordinated comparison and table",
    "no display; request adequate evidence"
  ),
  required_companion = c(
    "table with response rate and completed surveys",
    "plain-language measure and missing-value notes",
    "table of the plotted values and survey counts",
    "summary table with n, median, upper quantile, and subgroup counts",
    "measure-definition and reporting-period note",
    "accessible table with counts, denominator, and suppressed values",
    "transition table and cohort definition",
    "ranked table with estimate, denominator, uncertainty, and workforce measure",
    "accessible exact-value table and source status",
    "written evidence-gap note"
  ),
  no_display_trigger = c(
    "The hospital set or measure is not consistently defined.",
    "The requested measures use incompatible definitions or periods.",
    "Either quantitative measure is mostly missing or not comparable.",
    "Only an aggregate mean is available for a distribution question.",
    "Measure definitions or reporting periods change across the series.",
    "The parts do not share one defensible total or suppression hides the total.",
    "The cohort and transition states cannot be reconstructed.",
    "Geographies, years, or denominators cannot be aligned.",
    "The measures cannot be refreshed consistently enough for monitoring.",
    "The available evidence does not support the question."
  ),
  build_mode = c(
    "build",
    "table",
    "build",
    "decision-only",
    "decision-only",
    "decision-only",
    "decision-only",
    "decision-only",
    "decision-only",
    "decision-only"
  ),
  stringsAsFactors = FALSE
)

output_dir <- dirname(output_path)
if (!dir.exists(output_dir)) {
  dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
}
utils::write.csv(cases, output_path, row.names = FALSE, eol = "\n", fileEncoding = "UTF-8")
cat(sprintf("Built %s with %d question-to-display cases.\n", normalizePath(output_path, winslash = "/", mustWork = FALSE), nrow(cases)))
