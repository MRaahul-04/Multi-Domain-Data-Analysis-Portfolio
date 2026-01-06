"""
CLI Dashboard for Student Performance Analysis
OS-independent | Project 2
Author: Rahul Mahakal
"""

import argparse
from textwrap import fill
import pandas as pd
import sys
from pathlib import Path

# --------------------------------------------------
# Resolve project paths
# --------------------------------------------------
# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT / "src"))

from src.student_performance_analysis.preprocessing import preprocess_student_data
from src.student_performance_analysis.analysis import (
    overview_metrics,
    subject_average_scores,
)
from src.student_performance_analysis.insights import generate_insights
from src.student_performance_analysis.report_generator import (
    overview_text,
    recommendations,
)

# --------------------------------------------------
# Data and Dashboard Logic
# --------------------------------------------------
def print_header(title: str):
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)


def load_data(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"Dataset not found: {csv_path}")
    return pd.read_csv(csv_path)


def run_dashboard(data_path: str):
    df = load_data(Path(data_path))
    df = preprocess_student_data(df)

    # --------------------------------------------------
    # PRINT REPORT
    # --------------------------------------------------

    # ---------------- OVERVIEW ----------------
    metrics = overview_metrics(df)
    overview_lines = overview_text(metrics)

    print_header("**STUDENT PERFORMANCE ANALYSIS REPORT**")

    print("\n📊 OVERVIEW:")
    print("=" * 16)
    for line in overview_lines:
        print(f"• {line}")
    print(f"• Median Score: {metrics['median_score']:.2f}")

    # ---------------- SUBJECT PERFORMANCE ----------------
    print("\n📘 SUBJECT PERFORMANCE:")
    print("=" * 24)
    subject_means = subject_average_scores(df)

    for subject, score in subject_means.items():
        subject_name = subject.replace("_score", "").capitalize()
        print(f"• {subject_name}: {score:.2f}")

    # ---------------- ATTENDANCE & STUDY IMPACT ----------------
    print("\n📉 ATTENDANCE & STUDY IMPACT:")
    print("=" * 30)
    print(
        f"• Attendance vs Score Correlation: "
        f"{metrics['attendance_correlation']:.2f}"
    )
    print(
        f"• Study Hours vs Score Correlation: "
        f"{metrics['study_hours_correlation']:.2f}"
    )

    # ---------------- INSIGHTS ----------------
    print("\n💡 INSIGHTS:")
    print("=" * 13)
    insights = generate_insights(df)
    for idx, insight in enumerate(insights, 1):
        print(f"{idx}. {fill(insight, width=46)}")

    # ---------------- RECOMMENDATIONS ----------------
    print("\n🎯 RECOMMENDATIONS:")
    print("=" * 20)
    for idx, rec in enumerate(recommendations(), 1):
        print(f"{idx}. {fill(rec, width=46)}")

    print("\n" + "=" * 50)
    print("END OF REPORT".center(50))
    print("=" * 50 + "\n")

    # Call your analysis / visualization logic here
    print("✅ Student dashboard loaded successfully")


# --------------------------------------------------
# Entry Point
# --------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Student Performance Analysis Dashboard"
    )

    parser.add_argument(
        "--data",
        type=str,
        default="datasets/Student_Performance.csv",
        help="Path to Student_Performance.csv (default: datasets/Student_Performance.csv)"
    )

    args = parser.parse_args()

    # 🔑 Always resolve from project root
    BASE_DIR = Path(__file__).resolve().parents[1]
    data_path = BASE_DIR / args.data

    if not data_path.exists():
        raise FileNotFoundError(f"Dataset not found: {data_path}")

    # 🔑 Call the actual dashboard
    run_dashboard(str(data_path))


if __name__ == "__main__":
    main()
