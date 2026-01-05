"""
Preprocessing utilities for Finance / Stock Market Analysis
"""

import pandas as pd


def preprocess_finance_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Age grouping (derived, non-destructive)
    df["AGE_GROUP"] = pd.cut(
        df["age"],
        bins=[18, 25, 35, 45, 60, 100],
        labels=["18–25", "26–35", "36–45", "46–60", "60+"]
    )

    # Binary equity participation (derived)
    df["EQUITY_INVESTOR"] = df["Equity_Market"].apply(
        lambda x: 1 if str(x).lower() == "yes" else 0
    )

    return df
