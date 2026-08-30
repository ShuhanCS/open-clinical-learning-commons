render_portfolio_artifact <- function(checkpoint_root, module_slug, selected_figure, selected_table, output_base) {
  repo <- normalizePath(".", mustWork = TRUE)
  module_root <- file.path(repo, "courses", "data-visualization", "modules", module_slug)
  lab <- file.path(module_root, "lab.R")
  checkpoint_root <- normalizePath(checkpoint_root, mustWork = TRUE)

  if (!file.exists(file.path(repo, "VERSION")) || !file.exists(lab)) {
    stop("Run this analysis from the Open Clinical Learning Commons repository root.")
  }

  work <- tempfile(paste0("oclc-da730-cp2-", output_base, "-"))
  dir.create(work, recursive = TRUE)
  on.exit(unlink(work, recursive = TRUE, force = TRUE), add = TRUE)

  rscript <- file.path(R.home("bin"), if (.Platform$OS.type == "windows") "Rscript.exe" else "Rscript")
  status <- system2(rscript, c(shQuote(lab), "--output", shQuote(work)))
  if (!identical(status, 0L)) {
    stop(sprintf("Released %s lab failed with exit code %s.", module_slug, status))
  }

  copies <- c(
    file.copy(file.path(work, selected_figure), file.path(checkpoint_root, "figures", paste0(output_base, ".png")), overwrite = TRUE),
    file.copy(file.path(work, selected_table), file.path(checkpoint_root, "evidence-tables", paste0(output_base, ".csv")), overwrite = TRUE),
    file.copy(file.path(work, "alt-text-reference.md"), file.path(checkpoint_root, "alt-text", paste0(output_base, ".md")), overwrite = TRUE)
  )
  if (!all(copies)) {
    stop(sprintf("Could not copy all %s checkpoint artifacts.", output_base))
  }

  message(sprintf("Rendered %s from %s.", output_base, module_slug))
}
