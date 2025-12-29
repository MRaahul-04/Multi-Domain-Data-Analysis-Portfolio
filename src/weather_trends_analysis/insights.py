"""
Insight generation for Weather Trends Analysis
"""

import pandas as pd


def generate_weather_insights(df: pd.DataFrame) -> list[str]:
    insights = []

    yearly_trend = df.groupby("Year")["Temperature (C)"].mean()

    if yearly_trend.iloc[-1] > yearly_trend.iloc[0]:
        insights.append(
            "Average temperature shows an increasing trend over the observed years."
        )

    humidity_corr = df["Humidity"].corr(df["Temperature (C)"])
    if humidity_corr < 0:
        insights.append(
            "Humidity is negatively correlated with temperature, indicating drier conditions during warmer periods."
        )

    wind_corr = df["Wind Speed (km/h)"].corr(df["Temperature (C)"])
    if abs(wind_corr) > 0.3:
        insights.append(
            "Wind speed demonstrates a noticeable relationship with temperature variations."
        )

    return insights
