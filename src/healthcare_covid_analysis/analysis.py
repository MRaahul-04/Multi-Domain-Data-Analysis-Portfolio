"""
Core analytical computations for COVID Healthcare Analysis
"""

import pandas as pd


def overview_metrics(df: pd.DataFrame) -> dict:
    total_cases = df.shape[0]
    deaths = df["DIED"].sum()

    return {
        "total_cases": total_cases,
        "mortality_rate": (deaths / total_cases) * 100,
        "average_age": df["AGE"].mean(),
        "icu_mortality_rate": df.groupby("ICU")["DIED"].mean().get(1, 0) * 100,
    }


def mortality_by_age_group(df: pd.DataFrame) -> pd.Series:
    return df.groupby("AGE_GROUP", observed=True)["DIED"].mean()


def comorbidity_mortality(df: pd.DataFrame, condition: str) -> float:
    return df.groupby(condition)["DIED"].mean().get(1, 0) * 100


def icu_vs_mortality(df: pd.DataFrame) -> pd.Series:
    return df.groupby("ICU")["DIED"].mean()
