# Data

**Dataset:** [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
— 7,043 real customers (26.5% churn), 21 columns.

## One-step download (public IBM mirror)
```bash
curl -L -o data/telco_churn.csv \
  "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
```
Then run the notebook. All cleaning (the text `TotalCharges` column, tenure-0 blanks) and
encoding happen inside the notebook / `src/churn_features.py`.

Raw data (`*.csv`) is kept out of git via `.gitignore`.
