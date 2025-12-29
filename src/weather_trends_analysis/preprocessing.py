"""
Preprocessing utilities for Weather Trends Analysis
"""

import pandas as pd


def preprocess_weather_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Parse date column (case-sensitive)
    df["Formatted Date"] = pd.to_datetime(
        df["Formatted Date"], utc=True, errors="coerce"
    )

    # Time-based features
    df["Year"] = df["Formatted Date"].dt.year
    df["Month"] = df["Formatted Date"].dt.month
    df["Month_Name"] = df["Formatted Date"].dt.month_name()

    return df
