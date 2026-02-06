# 🏦 Bank Customer Churn Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Library](https://img.shields.io/badge/Library-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Complete-green)

## 📌 Project Overview
Customer retention is a critical metric for financial institutions. This project implements a **Machine Learning pipeline** to predict whether a bank customer is likely to "churn" (close their account) based on their demographic and financial activity.

The goal is to provide actionable insights that allow the bank to intervene proactively and retain high-value customers.

## 🚀 Key Features
* **End-to-End Pipeline:** From raw data generation to model evaluation.
* **Synthetic Data Engine:** Includes a custom Python script to generate realistic, legally safe demonstration data (bypassing the need for proprietary datasets).
* **Interpretability:** Uses Feature Importance analysis to explain *why* the model makes specific predictions.
* **Visualizations:** Professional-grade charts using Seaborn for data storytelling.

## 🛠️ Technologies Used
* **Python 3**
* **Pandas & NumPy** (Data Manipulation)
* **Scikit-Learn** (Random Forest Classifier, Preprocessing)
* **Seaborn & Matplotlib** (Visualization)

## 📊 Methodology
1.  **Data Simulation:** A custom function generates a dataset of 2,000 customers, simulating real-world correlations (e.g., older customers with lower credit scores have a higher attrition risk).
2.  **Preprocessing:**
    * One-Hot Encoding for categorical variables (Geography, Gender).
    * Standard Scaling for continuous variables (Balance, Salary).
3.  **Modeling:** A **Random Forest Classifier** (100 estimators) was chosen for its ability to handle non-linear relationships and resistance to overfitting.
4.  **Evaluation:** The model is evaluated using Accuracy, Precision, Recall, and a Confusion Matrix.

## 📈 Key Findings
* **Accuracy:** The model achieved **86% accuracy** on unseen test data.
* **Primary Drivers:** The analysis revealed that **Age**, **Credit Score**, and **Account Balance** significantly influence churn probability.
* **Demographics:** Older customers showed a significantly higher propensity to exit compared to younger demographics.

## 💻 How to Run
This project is designed to be **self-contained**. You do not need to download external CSV files.

1.  Clone the repository:
    ```bash
    git clone [https://github.com/kndukuba17-hub/customer-churn-prediction.git](https://github.com/kndukuba17-hub/customer-churn-prediction.git)
    ```
2.  Install dependencies:
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn
    ```
3.  Open the Jupyter Notebook:
    ```bash
    jupyter notebook customer_predictive_system.ipynb
    ```
4.  Run all cells. The notebook will generate its own data and train the model in real-time.
