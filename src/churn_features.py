"""Reusable cleaning + feature prep for the Telco Customer Churn dataset.

Extracted from the notebook so the logic is importable and testable.

Example
-------
>>> import pandas as pd
>>> from churn_features import clean, prepare_features
>>> df = clean(pd.read_csv("data/telco_churn.csv"))
>>> X, y = prepare_features(df)
"""
from __future__ import annotations
import pandas as pd

NUMERIC = ["tenure", "MonthlyCharges", "TotalCharges", "SeniorCitizen"]


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Drop the ID, fix the text `TotalCharges` column, encode the target as 0/1.

    The 11 blank `TotalCharges` values are tenure-0 new customers who have not been
    billed yet; they are set to 0 rather than dropped.
    """
    df = df.drop(columns=["customerID"], errors="ignore").copy()
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce").fillna(0.0)
    if not pd.api.types.is_numeric_dtype(df["Churn"]):
        df["Churn"] = (df["Churn"] == "Yes").astype(int)
    return df


def prepare_features(df: pd.DataFrame):
    """One-hot encode categoricals and return (X, y). Numeric columns are left raw
    (scale them inside the train/test split to avoid leakage)."""
    y = df["Churn"]
    X = df.drop(columns=["Churn"])
    cat = [c for c in X.columns if c not in NUMERIC]
    X = pd.get_dummies(X, columns=cat, drop_first=True)
    return X, y
