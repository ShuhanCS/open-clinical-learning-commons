# Independent verification record

The reference suite recalculates three material facts from lower-level rows with separate standard-library code:

1. The 75 test prediction rows produce confusion counts 48/23/2/2.
2. The 20 damped-Holt forecast rows produce MAE 14.99587157.
3. The same 20 rows produce RMSE 21.07855007.

All three match the accepted outputs. This verifies arithmetic and row use, not clinical or operational utility.
