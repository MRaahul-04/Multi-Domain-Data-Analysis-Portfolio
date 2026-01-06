"""
CLI Dashboard for Finance / Stock Market Analysis
Project 5 – Finance Analytics
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

from src.finance_stock_market_analysis.preprocessing import preprocess_finance_data
from src.finance_stock_market_analysis.analysis import (
    overview_metrics,
    equity_by_gender,
    equity_by_age_group,
)
from src.finance_stock_market_analysis.insights import generate_finance_insights
from src.finance_stock_market_analysis.report_generator import (
    overview_text,
    recommendations,
)


def print_header(title: str):
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)

# --------------------------------------------------
# Data loading
# --------------------------------------------------
def load_data(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"Dataset not found: {csv_path}")
    return pd.read_csv(csv_path)

# --------------------------------------------------
# Dashboard Logic
# --------------------------------------------------
def run_dashboard(data_path: str):
    df = load_data(Path(data_path))
    df = preprocess_finance_data(df)

    metrics = overview_metrics(df)
    insights = generate_finance_insights(df)

    most_common_avenue = df["Investment_Avenues"].mode()[0]
    top_age_group = df["AGE_GROUP"].value_counts().idxmax()
    top_objective = df["Objective"].mode()[0]
    top_duration = df["Duration"].mode()[0]
    top_monitoring = df["Invest_Monitor"].mode()[0]
    dominant_risk = df["Factor"].mode()[0]

    gender_equity = equity_by_gender(df)
    top_gender = gender_equity.idxmax()


    # --------------------------------------------------
    # PRINT REPORT
    # --------------------------------------------------
    print_header("FINANCE & STOCK MARKET ANALYSIS REPORT")

    # ---------------- OVERVIEW ----------------
    print("\n📊 INVESTOR OVERVIEW:")
    print("=" * 22)
    for line in overview_text(metrics):
        print(f"• {line}")
    print(f"• Most Common Investment Avenue: {most_common_avenue}")

    # ---------------- DEMOGRAPHICS ----------------
    print("\n👥 DEMOGRAPHIC INSIGHTS:")
    print("=" * 25)
    print(f"• Highest Investor Group: {top_age_group}")
    print(f"• Gender with Higher Equity Participation: {top_gender}")

    # ---------------- BEHAVIOR ----------------
    print("\n📈 INVESTMENT BEHAVIOR:")
    print("=" * 24)
    print(f"• Most Preferred Objective: {top_objective}")
    print(f"• Most Preferred Duration: {top_duration}")
    print(f"• Most Active Monitoring Frequency: {top_monitoring}")

    # ---------------- RISK ----------------
    print("\n⚖️ RISK & DECISION PATTERNS:")
    print("=" * 29)
    print(f"• Dominant Risk Factor: {dominant_risk}")
    print("• Risk-aware investors prefer equity and mutual funds")

    # ---------------- INSIGHTS ----------------
    print("\n🧠 BEHAVIORAL INSIGHTS:")
    print("=" * 24)
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
    print("✅ Finance Stock-Market dashboard loaded successfully")

# --------------------------------------------------
# Entry Point
# --------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Finance / Stock Market Analysis CLI Dashboard"
    )
    parser.add_argument(
        "--data",
        type=str,
        default="datasets/Finance_data.csv",
        help="Path to Finance_data.csv (relative to project root)"
    )

    args = parser.parse_args()

    BASE_DIR = Path(__file__).resolve().parents[1]
    data_path = BASE_DIR / args.data

    if not data_path.exists():
        raise FileNotFoundError(f"Dataset not found: {data_path}")

    run_dashboard(str(data_path))


if __name__ == "__main__":
    main()
