# Decision-curve interpretation

`net-benefit.csv` compares the fixed model with test-all and test-none strategies at every declared threshold. The false-positive weight is the threshold odds `p / (1 - p)`.

The output is useful because it forces the learner to connect a probability threshold to an explicit consequence ratio instead of treating sensitivity, specificity, or AUC as a decision rule. It can show where the model has greater mathematical net benefit than test-all or test-none under those exact assumptions.

It cannot establish patient benefit, patient harm, preference, access, cost, confirmatory capacity, workflow burden, fairness, safety, or clinical utility. The threshold odds are not elicited clinical values. A positive number does not authorize an alert or choose a threshold.

Reference decision: retain the table for Checkpoint 01 comparison. Keep all six evidence candidates open. Reject `0.20` as a Module 02 mechanics fixture. Require clinical, patient, workflow, survey-methods, calibration, and governance review before any later threshold acceptance.
