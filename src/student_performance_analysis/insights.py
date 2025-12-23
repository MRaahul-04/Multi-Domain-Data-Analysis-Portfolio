import pandas as pd
from src.student_performance_analysis.analysis import _resolve_result_column


def generate_insights(df: pd.DataFrame) -> list[str]:
    insights = []

    result_series = _resolve_result_column(df)

    if df["attendance_percentage"].corr(df["overall_score"]) > 0.4:
        insights.append(
            "Attendance has a strong positive impact on overall academic performance."
        )

    if df["study_hours"].corr(df["overall_score"]) > 0.3:
        insights.append(
            "Increased study hours are associated with improved student performance."
        )

    top_subject = (
        df[["math_score", "science_score", "english_score"]]
        .mean()
        .idxmax()
        .replace("_score", "")
    )
    insights.append(
        f"{top_subject.capitalize()} is the highest performing subject on average."
    )

    fail_ratio = (result_series == "Fail").mean()
    if fail_ratio > 0.2:
        insights.append(
            "A significant proportion of students are at academic risk and require early intervention."
        )

    return insights
