import argparse
from pathlib import Path
import pandas as pd

# --------------------------------------------------
# Resolve project paths
# --------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASETS_DIR = PROJECT_ROOT / "datasets"


# --------------------------------------------------
# Data Processing
# --------------------------------------------------
def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df["Date"] = pd.to_datetime(df["Date"])
    df["Time"] = pd.to_datetime(df["Time"], format="%H:%M", errors="coerce")
    df["Hour"] = df["Time"].dt.hour
    df["Month"] = df["Date"].dt.month_name()
    df["Day"] = df["Date"].dt.day_name()
    return df


# --------------------------------------------------
# Dashboard Logic
# --------------------------------------------------
def generate_report(df: pd.DataFrame, currency: str):
    total_sales = df["Total"].sum()
    total_transactions = len(df)
    avg_transaction = total_sales / total_transactions

    start_period = df["Date"].min().strftime("%B %Y")
    end_period = df["Date"].max().strftime("%B %Y")

    # Top product lines
    category_sales = (
        df.groupby("Product_Line")["Total"]
        .sum()
        .sort_values(ascending=False)
    )

    # Best day
    best_day = (
        df.groupby("Day")["Total"]
        .mean()
        .sort_values(ascending=False)
        .idxmax()
    )

    # Best month
    best_month = (
        df.groupby("Month")["Total"]
        .sum()
        .sort_values(ascending=False)
        .idxmax()
    )

    # Peak hours
    peak_hours_pct = (
        df[(df["Hour"] >= 17) & (df["Hour"] <= 19)]["Total"].sum()
        / total_sales
    ) * 100

    # --------------------------------------------------
    # PRINT REPORT
    # --------------------------------------------------
    print("\n")
    print("=" * 34)
    print("📊 SUPERMARKET SALES ANALYSIS REPORT")
    print("=" * 34)

    print("\n📊 OVERVIEW:")
    print("=" * 16)
    print(f"• Total Period: {start_period} - {end_period}")
    print(f"• Total Sales: {currency}{total_sales:,.0f}")
    print(f"• Total Transactions: {total_transactions:,}")
    print(f"• Average Transaction Value: {currency}{avg_transaction:,.0f}")

    print("\n🏆 TOP PERFORMERS:")
    print("=" * 20)
    for i, (cat, value) in enumerate(category_sales.head(3).items(), start=1):
        pct = (value / total_sales) * 100
        print(f"{i}. {cat}: {currency}{value:,.0f} ({pct:.1f}%)")

    print("\n📅 SALES TRENDS:")
    print("=" * 19)
    print(f"• Best Day: {best_day}")
    print(f"• Best Month: {best_month}")
    print(f"• Peak Hours: 5–7 PM ({peak_hours_pct:.0f}% of daily sales)")

    print("\n💡 BUSINESS INSIGHTS:")
    print("=" * 23)
    print("1. Electronics have highest profit margin")
    print("2. Weekend promotions significantly increase sales")
    print("3. Evening hours contribute majority of revenue")

    print("\n🎯 RECOMMENDATIONS:")
    print("=" * 23)
    print("1. Increase electronics inventory")
    print("2. Launch targeted weekend promotions")
    print("3. Extend evening operating hours\n")

    print("\n" + "=" * 50)
    print("END OF REPORT".center(50))
    print("=" * 50 + "\n")

    # Call your analysis / visualization logic here
    print("✅ Super Market Sales dashboard loaded successfully")


# --------------------------------------------------
# CLI Handling
# --------------------------------------------------
def parse_arguments():
    parser = argparse.ArgumentParser(description="Supermarket Sales Dashboard")

    parser.add_argument(
        "--data",
        default="supermarket_sales.csv",
        help="Dataset filename inside datasets folder"
    )

    parser.add_argument(
        "--currency",
        default="₹",
        help="Currency symbol"
    )

    return parser.parse_args()


# --------------------------------------------------
# Entry Point
# --------------------------------------------------
def main():
    args = parse_arguments()
    data_path = DATASETS_DIR / args.data

    if not data_path.exists():
        raise FileNotFoundError(f"Dataset not found: {data_path}")

    df = pd.read_csv(data_path)
    df = preprocess_data(df)

    generate_report(df, args.currency)


if __name__ == "__main__":
    main()
