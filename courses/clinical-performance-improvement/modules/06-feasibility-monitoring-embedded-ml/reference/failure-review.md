# Failure review

- Difficult folds reviewed: `F03, F09, F15, F16`
- Difficult folds passing the no-worse rule: `4 of 4`
- Error slices retained: `38`
- Largest ML errors retained: `10`
- Largest absolute ML error: `23.120473 arrivals`
- Largest-error direction: `overforecast`
- Feature-importance rows: `30`
- Feature-importance meaning: `model split allocation only; not causal`
- Week 53 ML total: `860.277096 arrivals`
- Week 53 range status: `inside 805.136639 to 970.733035`

The release retains favorable and unfavorable rows. Large underforecasts may leave too little preparation, while large overforecasts may direct scarce attention toward demand that does not occur. Good performance on accepted difficult folds does not override the failed MAE replacement rule.
