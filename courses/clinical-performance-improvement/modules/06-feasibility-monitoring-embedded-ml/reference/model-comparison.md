# Model comparison

- Transparent MAE: `5.937283 arrivals per shift`
- ML MAE: `5.205494 arrivals per shift`
- MAE improvement: `0.731788 arrivals per shift`
- Required MAE improvement: `0.750000 arrivals per shift`
- Transparent RMSE: `7.307180 arrivals per shift`
- ML RMSE: `6.554934 arrivals per shift`
- Transparent WAPE: `15.141268 percent`
- ML WAPE: `13.275060 percent`
- ML bias: `-0.513059 arrivals per shift`
- Weighted cost improvement: `9.403087 percent`
- Decision rules passed: `7 of 8`
- Model decision: `retain transparent forecast`

The challenger improves RMSE, WAPE, the declared bias bound, weighted error cost, and all four difficult folds. It misses the MAE improvement rule by 0.018212 arrivals per shift. Because all eight rules are required, the accepted transparent forecast remains the planning input. The threshold is not changed and the model is not tuned again.
