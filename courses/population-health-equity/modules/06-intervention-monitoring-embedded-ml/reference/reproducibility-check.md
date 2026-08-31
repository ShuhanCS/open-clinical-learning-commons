# Reproducibility check

The frozen Module 05 handoff verifies at 340 files with SHA-256 `0ab8cc15d252ef91436aa1b281f316e4eb21115aefc668a0930d04c90397a828`.

Two independent source generations produce the same six-file manifest and 280-record gzip. The committed source manifest SHA-256 is `d6e09f0e57d4890300d44bf48fcf1be34f52698af05a0934c62e25926f6622cd`, and the dry-run SHA-256 is `067ac19e07eb8db3a48373d063e77a5b898d63a65b83f7e27504fba8beacdcda`.

Two independent analysis builds produce the same 14 files. The committed build-report SHA-256 is `f53dc9a5b3274ee33917a3f78d1b0152f1dcaca232bc07de3b39045e5246f6f7`.

The release uses pandas 3.0.3 and scikit-learn 1.9.0. KMeans uses four clusters, seed 73056, 20 initializations, and the Lloyd algorithm. The learner does not alter the fixed model or its observed failure.
