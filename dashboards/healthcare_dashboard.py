"""
CLI Dashboard for Healthcare COVID Analysis
Project 4 – Healthcare Analytics
Author: Rahul Mahakal
"""

import argparse
from textwrap import fill
import pandas as pd
import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT / "src"))

from src.healthcare_covid_analysis.preprocessing import preprocess_covid_data
from src.healthcare_covid_analysis.analysis import (
    overview_metrics,
    mortality_by_age_group,
    comorbidity_mortality,
)
from src.healthcare_covid_analysis.insights import generate_healthcare_insights
from src.healthcare_covid_analysis.report_generator import (
    overview_text,
    recommendations,
)
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


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
    df = preprocess_covid_data(df)

    metrics = overview_metrics(df)
    insights = generate_healthcare_insights(df)
    age_risk = mortality_by_age_group(df)

    print_header("COVID HEALTHCARE ANALYSIS REPORT")

    # ---------------- OVERVIEW ----------------
    print("\n📊 OVERVIEW:")
    print("=" * 13)
    for line in overview_text(metrics):
        print(f"• {line}")

    # ---------------- AGE RISK ----------------
    print("\n👥 AGE-BASED RISK:")
    print("=" * 19)
    print(f"• Highest Mortality Group: {age_risk.idxmax()}")
    print("• Senior & Elderly patients show elevated risk")

    # ---------------- COMORBIDITY INSIGHTS ----------------
    print("\n🧬 COMORBIDITY INSIGHTS:")
    print("=" * 25)
    for condition in ["DIABETES", "HIPERTENSION", "OBESITY"]:
        rate = comorbidity_mortality(df, condition)
        print(f"• {condition.capitalize()} Mortality Rate: {rate:.2f}%")

    # ---------------- ICU INSIGHTS ----------------
    print("\n🏥 ICU INSIGHTS:")
    print("=" * 17)
    print("• ICU admission is strongly associated with severe outcomes")

    # ---------------- HEALTHCARE INSIGHTS ----------------
    print("\n💡 HEALTHCARE INSIGHTS:")
    print("=" * 24)
    for idx, insight in enumerate(insights, 1):
        print(f"{idx}. {fill(insight, width=46)}")

    # ---------------- RECOMMENDATIONS ----------------
    print("\n🎯 RECOMMENDATIONS:")
    print("=" * 21)
    for idx, rec in enumerate(recommendations(), 1):
        print(f"{idx}. {fill(rec, width=46)}")

    print("\n" + "=" * 50)
    print("END OF REPORT".center(50))
    print("=" * 50 + "\n")

    # Call your analysis / visualization logic here
    print("✅ Healthcare-Covid-19 dashboard loaded successfully")


def main():
    parser = argparse.ArgumentParser(
        description="Healthcare COVID Analysis CLI Dashboard"
    )
    parser.add_argument(
        "--data",
        type=str,
        default="datasets/Covid Data.csv",
        help="Path to Covid Data.csv (relative to project root)"
    )

    args = parser.parse_args()

    BASE_DIR = Path(__file__).resolve().parents[1]
    data_path = BASE_DIR / args.data

    if not data_path.exists():
        raise FileNotFoundError(f"Dataset not found: {data_path}")

    run_dashboard(str(data_path))


if __name__ == "__main__":
    main()
