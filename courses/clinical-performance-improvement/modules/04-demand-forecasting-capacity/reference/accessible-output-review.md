# Accessible output review

- Table-first evidence: `pass`
- SVG title and description: `pass`
- Color-independent method labels: `pass`
- Visible units: `pass`
- Forecast versus observed status: `pass`
- Synthetic status: `pass`
- Plain-language uncertainty: `pass`
- Claim boundary beside decision: `pass`

The two figures summarize evidence that is also available in CSV and JSON. `forecast-error-comparison.svg` labels each method and reports MAE in arrivals per shift. `week53-demand-forecast.svg` identifies every dated shift as a future synthetic planning estimate and states that actuals are unavailable. Neither figure relies on color alone to identify the evidence.

The preferred verbal summary is: the selected method averaged 5.94 arrivals of absolute error per shift in backtesting. Its Week 53 forecast is about 877 arrivals, while the empirical actual-equivalent range is about 805 to 971. That range supports scenario planning, not a staffing recommendation.
