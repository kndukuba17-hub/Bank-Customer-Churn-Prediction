# 🏦 Bank Customer Churn Prediction

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-RandomForest-orange)
![Status](https://img.shields.io/badge/Status-Real--data%20upgrade%20in%20progress-yellow)

Predicting which bank customers are likely to close their accounts, so retention teams can intervene before a high-value customer leaves.

> **Behavioural angle:** churn is a behavioural signal — disengagement shows up in activity, balance, and product usage before the customer actually leaves. The model surfaces those at-risk patterns early.

---

## 📊 Results (measured on the current dataset)

| Metric | Value |
|--------|------:|
| Accuracy | 86% |
| Churn-class (1) precision | 0.79 |
| Churn-class (1) recall | 0.68 |
| Churn-class (1) F1 | 0.73 |
| Macro F1 | 0.82 |

Because retaining a customer is cheaper than losing one, **recall on the churn class** is the metric that matters most here — the model currently catches ~68% of churners, which the roadmap aims to improve.

## ⚠️ Data status (honest note)
The committed notebook trains on a **synthetic customer dataset** generated in-notebook. This repo is being upgraded to a **real public churn dataset** (e.g. the [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) dataset) so the pipeline reflects real data-cleaning and class-imbalance challenges. Metrics above will be re-reported on the real data.

## ⚙️ Approach
1. **Preprocessing** — one-hot encoding for categoricals (geography, gender), standard scaling for continuous features.
2. **Modelling** — a **Random Forest Classifier** (100 trees) for non-linear relationships and resistance to overfitting.
3. **Interpretability** — feature-importance analysis to explain *which* factors drive churn (age, credit score, balance).
4. **Evaluation** — accuracy, precision, recall, F1 and a confusion matrix, with emphasis on churn-class recall.

## 🧰 Tech Stack
Python · pandas · NumPy · scikit-learn · Matplotlib · Seaborn

---

## 📁 Repository Structure
```
├── README.md
├── requirements.txt
├── notebooks/
│   └── bank_customer_churn.ipynb
├── src/
├── data/          # real-dataset download instructions — see data/README.md
├── images/
└── docs/
```

## 🚀 How to Run
```bash
git clone https://github.com/kndukuba17-hub/Bank-Customer-Churn-Prediction.git
cd Bank-Customer-Churn-Prediction
pip install -r requirements.txt
jupyter notebook notebooks/bank_customer_churn.ipynb
```
Runs on Jupyter or Google Colab.

## 🗺️ Roadmap
- Swap synthetic data for the real Telco Customer Churn dataset and re-report metrics.
- Add class-imbalance handling (SMOTE / class weights) and threshold tuning to lift churn recall.
- Compare Random Forest against Gradient Boosting and a logistic-regression baseline.
