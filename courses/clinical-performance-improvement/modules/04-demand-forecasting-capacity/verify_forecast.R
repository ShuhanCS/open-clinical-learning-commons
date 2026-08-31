args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
if (length(file_arg) != 1) stop("Run this file with Rscript")
root <- dirname(normalizePath(sub("^--file=", "", file_arg)))

shift <- read.csv(file.path(root, "upstream", "shift-metrics.csv"), stringsAsFactors = FALSE)
stopifnot(nrow(shift) == 1092)

period <- 21
alpha <- 0.30
gamma <- 0.20

seasonal_smoothing <- function(train) {
  level <- mean(train[1:period])
  seasonal <- train[1:period] - level
  for (index in (period + 1):length(train)) {
    old_seasonal <- seasonal[index - period]
    level <- alpha * (train[index] - old_seasonal) + (1 - alpha) * level
    seasonal[index] <- gamma * (train[index] - level) + (1 - gamma) * old_seasonal
  }
  pmax(0, level + tail(seasonal, period))
}

actual <- numeric()
last_value <- numeric()
seasonal_naive <- numeric()
smoothing <- numeric()
for (test_week in 25:52) {
  start <- (test_week - 1) * period + 1
  train <- shift$arrivals[1:(start - 1)]
  actual <- c(actual, shift$arrivals[start:(start + period - 1)])
  last_value <- c(last_value, rep(tail(train, 1), period))
  seasonal_naive <- c(seasonal_naive, tail(train, period))
  smoothing <- c(smoothing, seasonal_smoothing(train))
}

score <- function(forecast) {
  error <- forecast - actual
  c(
    mae = mean(abs(error)),
    rmse = sqrt(mean(error ^ 2)),
    bias = mean(error),
    wape = 100 * sum(abs(error)) / sum(actual),
    under = sum(-error[error < 0]),
    over = sum(error[error > 0])
  )
}

last_score <- score(last_value)
naive_score <- score(seasonal_naive)
smooth_score <- score(smoothing)
week53 <- sum(seasonal_smoothing(shift$arrivals))

stopifnot(abs(last_score["mae"] - 10.775510204081632) < 1e-10)
stopifnot(abs(naive_score["mae"] - 7.095238095238095) < 1e-10)
stopifnot(abs(smooth_score["mae"] - 5.937282542565626) < 1e-10)
stopifnot(abs(smooth_score["rmse"] - 7.30718022275896) < 1e-10)
stopifnot(abs(smooth_score["bias"] - 0.008214576104419) < 1e-10)
stopifnot(abs(smooth_score["wape"] - 15.141268161592793) < 1e-10)
stopifnot(abs(week53 - 876.9240843532087) < 1e-10)

cat("APP-3 Module 04 base-R forecast verification passed.\n")
