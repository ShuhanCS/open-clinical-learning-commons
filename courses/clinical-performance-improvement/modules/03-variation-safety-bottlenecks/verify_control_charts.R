args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
if (length(file_arg) != 1) stop("Run this file with Rscript")
root <- dirname(normalizePath(sub("^--file=", "", file_arg)))

weekly <- read.csv(file.path(root, "upstream", "weekly-metrics.csv"), stringsAsFactors = FALSE)
baseline <- weekly[weekly$week_index >= 1 & weekly$week_index <= 24, ]

p_center <- sum(baseline$left_before_seen) / sum(baseline$arrivals) * 100
x <- baseline$shift_median_arrival_to_clinician_mean
x_center <- mean(x)
mr_bar <- mean(abs(diff(x)))
x_lower <- x_center - 2.66 * mr_bar
x_upper <- x_center + 2.66 * mr_bar

stopifnot(abs(p_center - 8.137669534781974) < 1e-10)
stopifnot(abs(x_center - 97.63695833333333) < 1e-10)
stopifnot(abs(mr_bar - 2.688478260869565) < 1e-10)
stopifnot(abs(x_lower - 90.48560615942029) < 1e-10)
stopifnot(abs(x_upper - 104.78831050724637) < 1e-10)

cat("APP-3 Module 03 base-R control-chart verification passed.\n")
