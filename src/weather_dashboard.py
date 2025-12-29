"""
CLI Dashboard for Weather Trends Analysis
Project 3 – Weather Analytics
Author: Rahul Mahakal
"""

import argparse
from pathlib import Path
from textwrap import fill
import pandas as pd

from weather_trends_analysis.preprocessing import preprocess_weather_data
from weather_trends_analysis.analysis import (
    temperature_overview,
    yearly_temperature_trend,
)
from weather_trends_analysis.insights import generate_weather_insights
from weather_trends_analysis.report_generator import (
    overview_text,
    recommendations,
)


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
    df = preprocess_weather_data(df)

    stats = temperature_overview(df)
    insights = generate_weather_insights(df)
    yearly_trend = yearly_temperature_trend(df)

    print_header("WEATHER TRENDS ANALYSIS REPORT")

    # ---------------- OVERVIEW ----------------
    print("\n📊 OVERVIEW:")
    print("=" * 16)
    for line in overview_text(stats):
        print(f"• {line}")

    # ---------------- TEMPORAL ANALYSIS ----------------
    print("\n📅 TEMPORAL ANALYSIS:")
    print("=" * 20)
    print(f"• Years Covered: {yearly_trend.index.min()} – {yearly_trend.index.max()}")
    print(f"• Warmest Year (Avg): {yearly_trend.idxmax()}")
    print(f"• Coldest Year (Avg): {yearly_trend.idxmin()}")

    # ---------------- CORRELATION INSIGHTS ----------------
    print("\n🔗 CORRELATION INSIGHTS:")
    print("=" * 26)
    print(
        f"• Temperature vs Humidity: "
        f"{df['Temperature (C)'].corr(df['Humidity']):.2f}"
    )
    print(
        f"• Temperature vs Wind Speed: "
        f"{df['Temperature (C)'].corr(df['Wind Speed (km/h)']):.2f}"
    )

    # ---------------- CLIMATE INSIGHTS ----------------
    print("\n💡 CLIMATE INSIGHTS:")
    print("=" * 26)
    for idx, insight in enumerate(insights, 1):
        print(f"{idx}. {fill(insight, width=46)}")

    # ---------------- RECOMMENDATIONS ----------------
    print("\n🎯 RECOMMENDATIONS:")
    print("=" * 23)
    for idx, rec in enumerate(recommendations(), 1):
        print(f"{idx}. {fill(rec, width=46)}")

    print("\n" + "=" * 50)
    print("END OF REPORT".center(50))
    print("=" * 50 + "\n")

    # Call your analysis / visualization logic here
    print("✅ Weather dashboard loaded successfully")


def main():
    parser = argparse.ArgumentParser(
        description="Weather Trends Analysis CLI Dashboard"
    )
    parser.add_argument(
        "--data",
        type=str,
        default="datasets/weatherHistory.csv",
        help="Path to weatherHistory.csv (relative to project root)"
    )

    args = parser.parse_args()

    BASE_DIR = Path(__file__).resolve().parents[1]
    data_path = BASE_DIR / args.data

    if not data_path.exists():
        raise FileNotFoundError(f"Dataset not found: {data_path}")

    run_dashboard(str(data_path))


if __name__ == "__main__":
    main()
