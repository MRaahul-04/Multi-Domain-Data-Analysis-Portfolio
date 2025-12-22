"""
Data preprocessing and feature engineering
"""

import pandas as pd


def preprocess_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and enriches supermarket sales data.

    Parameters:
        df (pd.DataFrame): Raw sales dataset

    Returns:
        pd.DataFrame: Processed dataset
    """

    df = df.copy()

    # Parse Date column
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Derived time features
    df["Month"] = df["Date"].dt.month_name()
    df["Day_Name"] = df["Date"].dt.day_name()

    # Time → Hour
    df["Hour"] = pd.to_datetime(
        df["Time"],
        format="%H:%M",
        errors="coerce"
    ).dt.hour


    return df