# Failure-period review

- Highest-MAE fold: `F09`
- Test week: `33`
- Issue date: `2024-08-11`
- Actual arrivals: `746`
- Forecast arrivals: `891.433773`
- Weekly signed forecast error: `145.433773 arrivals over forecast`
- Fold MAE: `8.174933 arrivals per shift`
- Special-event shifts: `0`

The largest fold MAE occurs immediately after the bounded special-event window, not inside it. This pattern is consistent with slow adaptation after a level change, but it does not establish a cause. F03 also under-forecasts by 151.431012 arrivals at the start of the special-event window. F15 and F16 then show consecutive large errors in opposite directions.

- Special-event MAE: `5.956421 arrivals per shift across 126 rows`
- Routine MAE: `5.932063 arrivals per shift across 462 rows`
- Unsupported slice: `holiday, 9 rows`

The special-event slice is not materially worse in average absolute error, and holiday support is too small for a stable claim. Module 05 must keep abrupt shifts, post-event adaptation, and the full empirical error range visible.
