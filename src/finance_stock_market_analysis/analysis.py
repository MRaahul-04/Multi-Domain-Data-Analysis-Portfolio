"""
Core analytical computations for Finance / Stock Market Analysis
"""

import pandas as pd


def overview_metrics(df: pd.DataFrame) -> dict:
    return {
        "total_investors": df.shape[0],
        "equity_participation_rate": df["EQUITY_INVESTOR"].mean() * 100,
        "average_age": df["age"].mean(),
    }


def equity_by_gender(df: pd.DataFrame) -> pd.Series:
    return df.groupby("gender")["EQUITY_INVESTOR"].mean() * 100


def equity_by_age_group(df: pd.DataFrame) -> pd.Series:
    return df.groupby("AGE_GROUP")["EQUITY_INVESTOR"].mean() * 100


def risk_vs_avenue(df: pd.DataFrame):
    return pd.crosstab(df["Factor"], df["Investment_Avenues"])
