"""
Core analytical computations for Student Performance
"""

import pandas as pd


def overview_metrics(df: pd.DataFrame) -> dict:
    result_series = _resolve_result_column(df)

    total_students = df.shape[0]
    pass_count = (result_series == "Pass").sum()

    return {
        "total_students": total_students,
        "pass_percentage": (pass_count / total_students) * 100,
        "average_score": df["overall_score"].mean(),
        "median_score": df["overall_score"].median(),
        "attendance_correlation": df["attendance_percentage"].corr(df["overall_score"]),
        "study_hours_correlation": df["study_hours"].corr(df["overall_score"]),
    }


def _resolve_result_column(df: pd.DataFrame) -> pd.Series:
    """
    Safely resolve pass/fail result.
    Priority:
    1. Use 'Result' column if present
    2. Derive from 'final_grade' if available
    3. Derive from 'overall_score'
    """

    if "Result" in df.columns:
        return df["Result"]

    if "final_grade" in df.columns:
        return df["final_grade"].apply(
            lambda x: "Pass" if str(x).lower() not in ["f", "fail"] else "Fail"
        )

    # Fallback: derive from score threshold
    return df["overall_score"].apply(
        lambda x: "Pass" if x >= 40 else "Fail"
    )


def subject_average_scores(df: pd.DataFrame) -> pd.Series:
    return df[["math_score", "science_score", "english_score"]].mean()


def gender_wise_scores(df: pd.DataFrame) -> pd.Series:
    return df.groupby("gender")["overall_score"].mean()


def pass_fail_distribution(df: pd.DataFrame) -> pd.Series:
    return df["Result"].value_counts()
