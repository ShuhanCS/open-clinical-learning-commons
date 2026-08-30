# DAG narrative

Age, baseline severity, comorbidity count, and site precede treatment and the 30-day outcome. They are the measured teaching adjustment set. Clinical preference also affects treatment and outcome but is deliberately unmeasured, so adjustment cannot remove every backdoor path in an ordinary observed study.

Treatment affects early response, and early response affects the outcome. Early response is therefore a mediator for the total-effect question. Adjusting for it would change the estimand and could block part of the effect the exercise is trying to describe.

Complete severity record is caused by age and site. Selecting only complete records can change the study population and can create selection paths. It is not a baseline confounder merely because it predicts inclusion.

The structured equivalent contains nine rows in `dag-nodes.csv` and 18 rows in `dag-edges.csv`. Each row states timing, role, direction, and adjustment implication. The diagram is a teaching assumption record, not evidence that the arrows are true in a real clinical setting.
