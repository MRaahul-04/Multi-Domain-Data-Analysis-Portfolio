"""
Business insight generation
"""

import pandas as pd


def generate_business_insights(df: pd.DataFrame) -> list[str]:
    insights = []

    # Peak hours
    peak_hour = df.groupby("Hour")["Total"].sum().idxmax()
    insights.append(
        f"Peak sales occur around {peak_hour}:00 hours, indicating strong evening demand."
    )

    # Customer type behavior
    avg_spend = df.groupby("Customer_Type")["Total"].mean()
    if avg_spend["Member"] > avg_spend["Normal"]:
        insights.append(
            "Members spend more per transaction compared to normal customers."
        )

    # Product dominance
    top_product = (
        df.groupby("Product_Line")["Total"].sum().idxmax()
    )
    insights.append(
        f"{top_product} is the highest revenue-generating product category."
    )

    return insights
