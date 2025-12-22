"""
Visualization Module for Supermarket Sales Analysis
Exports publication-ready charts as PNG files
"""

from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

COLOR_PALETTE = {
    "primary": "#1f77b4",     # blue
    "secondary": "#ff7f0e",   # orange
    "success": "#2ca02c",     # green
    "warning": "#d62728",     # red
    "neutral": "#7f7f7f"
}


def _ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def _require_columns(df, columns):
    missing = [c for c in columns if c not in df.columns]
    if missing:
        raise KeyError(f"Missing required columns: {missing}")


def save_plot(fig, output_path: Path):
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


# 1️⃣ Daily Sales Trend
def plot_daily_sales(df, output_dir: Path):
    _ensure_dir(output_dir)

    daily = df.groupby("Date")["Total"].sum()

    fig, ax = plt.subplots(figsize=(10, 5))
    daily.plot(ax=ax)
    ax.set_title("Daily Sales Trend")
    ax.set_xlabel("Date")
    ax.set_ylabel("Total Sales")

    save_plot(fig, output_dir / "sales_trend_daily.png")


# 2️⃣ Monthly Sales
def plot_monthly_sales(df, output_dir: Path):
    _ensure_dir(output_dir)

    import calendar

    # 1️⃣ Convert numeric month to names
    df['Month_Name'] = df['Month'].apply(lambda x: calendar.month_name[int(x)])

    # print(df[['Month', 'Month_Name']].head())

    # 2️⃣ Define calendar order
    month_order = list(calendar.month_name[1:])

    # 3️⃣ Group and reindex
    monthly = df.groupby("Month_Name")["Total"].sum().reindex(month_order)

    # 4️⃣ Plot
    fig = monthly.plot(kind='bar', figsize=(10, 6), title='Monthly Sales').get_figure()

    # 5️⃣ Save plot
    save_plot(fig, output_dir / "sales_trend_monthly.png")


# 3️⃣ Hourly Sales
def plot_hourly_sales(df, output_dir: Path):
    hourly = df.groupby("Hour")["Total"].sum()

    fig, ax = plt.subplots(figsize=(8, 5))
    hourly.plot(ax=ax)
    ax.set_title("Hourly Sales Pattern")
    ax.set_xlabel("Hour of Day")
    ax.set_ylabel("Total Sales")

    save_plot(fig, output_dir / "hourly_sales.png")


# 4️⃣ Product Line Revenue
def plot_product_line_revenue(df, output_dir: Path):
    revenue = df.groupby("Product_Line")["Total"].sum().sort_values()

    fig, ax = plt.subplots(figsize=(9, 6))
    revenue.plot(kind="barh", ax=ax)
    ax.set_title("Revenue by Product Line")
    ax.set_xlabel("Total Sales")

    save_plot(fig, output_dir / "product_line_revenue.png")


# 5️⃣ Quantity vs Total (Correlation)
def plot_quantity_vs_total(df, output_dir: Path):
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.scatterplot(
        data=df, x="Quantity", y="Total", alpha=0.6, ax=ax
    )
    ax.set_title("Quantity vs Total Sales")

    save_plot(fig, output_dir / "quantity_vs_total.png")


def plot_product_line_quantity(df, output_dir: Path):
    _ensure_dir(output_dir)
    _require_columns(df, ["Product_Line", "Quantity"])

    quantity_by_product = (
        df.groupby("Product_Line")["Quantity"]
          .sum()
          .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(8, 5))
    quantity_by_product.plot(kind="bar", ax=ax)

    ax.set_title("Quantity Sold by Product Line")
    ax.set_xlabel("Product Line")
    ax.set_ylabel("Total Quantity")

    plt.tight_layout()
    # plt.show()
    plt.savefig(output_dir / "product_line_quantity.png")
    plt.close()


def plot_customer_type_avg_spend(df, output_dir: Path):
    _ensure_dir(output_dir)
    _require_columns(df, ["Customer_Type", "Total"])

    avg_spend = df.groupby("Customer_Type")["Total"].mean()

    fig, ax = plt.subplots(figsize=(7, 5))
    avg_spend.plot(kind="bar", ax=ax, color=["green", "orange"])
    ax.set_title("Average Spend by Customer Type")
    ax.set_ylabel("Average Transaction Value")

    save_plot(fig, output_dir / "customer_type_avg_spend.png")


def plot_gender_wise_sales(df, output_dir: Path):
    _ensure_dir(output_dir)
    _require_columns(df, ["Gender", "Total"])

    gender_sales = df.groupby("Gender")["Total"].sum()

    fig, ax = plt.subplots(figsize=(7, 5))
    gender_sales.plot(kind="bar", ax=ax, color=["purple", "pink"])
    ax.set_title("Total Sales by Gender")
    ax.set_ylabel("Total Sales")

    save_plot(fig, output_dir / "gender_wise_sales.png")


def plot_branch_revenue(df, output_dir: Path):
    _ensure_dir(output_dir)
    _require_columns(df, ["Branch", "Total"])

    branch_sales = df.groupby("Branch")["Total"].sum()

    fig, ax = plt.subplots(figsize=(7, 5))
    branch_sales.plot(kind="bar", ax=ax, color="teal")
    ax.set_title("Revenue by Branch")
    ax.set_ylabel("Total Sales")

    save_plot(fig, output_dir / "branch_revenue_comparison.png")


def plot_payment_method_share(df, output_dir: Path):
    _ensure_dir(output_dir)
    _require_columns(df, ["Payment"])

    payment_counts = df["Payment"].value_counts()

    fig, ax = plt.subplots(figsize=(7, 7))
    payment_counts.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90,
        ax=ax
    )
    ax.set_title("Payment Method Distribution")
    ax.set_ylabel("")

    save_plot(fig, output_dir / "payment_method_share.png")
