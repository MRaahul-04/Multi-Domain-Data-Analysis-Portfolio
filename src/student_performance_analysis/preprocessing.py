"""
Preprocessing utilities for Student Performance Analysis
"""

import pandas as pd


def preprocess_student_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Attendance bands
    df["attendance_band"] = pd.cut(
        df["attendance_percentage"],
        bins=[0, 60, 75, 90, 100],
        labels=["Low", "Medium", "High", "Excellent"]
    )

    # Study hours bands
    df["study_hours_band"] = pd.cut(
        df["study_hours"],
        bins=[0, 2, 4, 6, 10],
        labels=["Very Low", "Low", "Moderate", "High"]
    )

    return df

