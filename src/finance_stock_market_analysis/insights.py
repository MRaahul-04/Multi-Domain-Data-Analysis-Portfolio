"""
Insight generation for Finance / Stock Market Analysis
"""

import pandas as pd


def generate_finance_insights(df: pd.DataFrame) -> list[str]:
    insights = []

    if df["EQUITY_INVESTOR"].mean() > 0.5:
        insights.append(
            "More than half of the investors participate in the equity market."
        )

    if (df.groupby("AGE_GROUP", observed=True)["EQUITY_INVESTOR"].mean().idxmax()) in ["26–35", "36–45"]:
        insights.append(
            "Middle-aged investors show higher preference towards equity investments."
        )

    if df.groupby("Invest_Monitor")["EQUITY_INVESTOR"].mean().idxmax():
        insights.append(
            "Frequent investment monitoring is associated with higher equity participation."
        )

    return insights
