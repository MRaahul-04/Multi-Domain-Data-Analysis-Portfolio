"""
Core analytical computations for Weather Trends
"""

import pandas as pd


def temperature_overview(df: pd.DataFrame) -> dict:
    return {
        "mean_temperature": df["Temperature (C)"].mean(),
        "median_temperature": df["Temperature (C)"].median(),
        "min_temperature": df["Temperature (C)"].min(),
        "max_temperature": df["Temperature (C)"].max(),
    }


def yearly_temperature_trend(df: pd.DataFrame) -> pd.Series:
    return df.groupby("Year")["Temperature (C)"].mean()


def monthly_average_temperature(df: pd.DataFrame) -> pd.Series:
    return df.groupby("Month_Name")["Temperature (C)"].mean()


def weather_variable_correlation(df: pd.DataFrame) -> pd.DataFrame:
    cols = [
        "Temperature (C)",
        "Apparent Temperature (C)",
        "Humidity",
        "Wind Speed (km/h)",
        "Pressure (millibars)",
    ]
    return df[cols].corr()
