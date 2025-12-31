"""
Insight generation for COVID Healthcare Analysis
"""

import pandas as pd


def generate_healthcare_insights(df: pd.DataFrame) -> list[str]:
    insights = []

    if df.groupby("AGE_GROUP", observed=True)["DIED"].mean().idxmax() in ["Senior", "Elderly"]:
        insights.append(
            "Older age groups show significantly higher mortality rates."
        )

    if df.groupby("ICU", observed=True)["DIED"].mean().get(1, 0) > 0.3:
        insights.append(
            "ICU admission is associated with higher mortality, indicating severe disease cases."
        )

    if df.groupby("DIABETES", observed=True)["DIED"].mean().get(1, 0) > df.groupby("DIABETES")["DIED"].mean().get(0, 0):
        insights.append(
            "Patients with diabetes have a higher mortality risk compared to non-diabetic patients."
        )

    return insights
