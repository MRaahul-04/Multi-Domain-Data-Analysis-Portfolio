"""
Core analytical computations
"""

import pandas as pd


def sales_overview(df: pd.DataFrame) -> dict:
    return {
        "total_sales": df["Total"].sum(),
        "total_transactions": len(df),
        "average_transaction": df["Total"].mean(),
        "median_transaction": df["Total"].median(),
        "max_transaction": df["Total"].max(),
        "period_start": df["Date"].min(),
        "period_end": df["Date"].max(),
    }


def product_line_performance(df: pd.DataFrame, top_n: int = 3) -> pd.DataFrame:
    return (
        df.groupby("Product_Line")["Total"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )


def hourly_sales(df: pd.DataFrame) -> pd.Series:
    return df.groupby("Hour")["Total"].sum()


def daily_sales(df: pd.DataFrame) -> pd.Series:
    return df.groupby("Date")["Total"].sum()
