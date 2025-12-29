"""
Static visualization exports for Weather Trends Analysis
"""

from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


def _ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def save_plot(fig, output_path: Path):
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


# 1️⃣ Temperature Trend Over Time
def plot_temperature_trend(df, output_dir: Path):
    _ensure_dir(output_dir)

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df["Formatted Date"], df["Temperature (C)"], alpha=0.6)
    ax.set_title("Temperature Trend Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")

    save_plot(fig, output_dir / "temperature_trend.png")


# 2️⃣ Monthly Average Temperature
def plot_monthly_average_temperature(df, output_dir: Path):
    monthly = df.groupby("Month_Name")["Temperature (C)"].mean()

    fig, ax = plt.subplots(figsize=(10, 5))
    monthly.plot(kind="bar", ax=ax, color="tomato")
    ax.set_title("Average Monthly Temperature")
    ax.set_ylabel("Temperature (°C)")

    save_plot(fig, output_dir / "monthly_average_temperature.png")


# 3️⃣ Humidity Distribution
def plot_humidity_distribution(df, output_dir: Path):
    fig, ax = plt.subplots()
    ax.hist(df["Humidity"], bins=30)
    ax.set_title("Humidity Distribution")
    ax.set_xlabel("Humidity")

    save_plot(fig, output_dir / "humidity_distribution.png")


# 4️⃣ Actual vs Apparent Temperature
def plot_actual_vs_apparent_temperature(df, output_dir: Path):
    fig, ax = plt.subplots()
    ax.scatter(
        df["Temperature (C)"],
        df["Apparent Temperature (C)"],
        alpha=0.5
    )
    ax.set_title("Actual vs Apparent Temperature")
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Apparent Temperature (°C)")

    save_plot(fig, output_dir / "actual_vs_apparent_temperature.png")


# 5️⃣ Weather Summary Frequency
def plot_weather_summary_frequency(df, output_dir: Path):
    summary_counts = df["Summary"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 5))
    summary_counts.plot(kind="bar", ax=ax)
    ax.set_title("Most Frequent Weather Conditions")

    save_plot(fig, output_dir / "weather_summary_frequency.png")


# 6️⃣ Correlation Heatmap
def plot_weather_correlation_heatmap(df, output_dir: Path):
    corr_cols = [
        "Temperature (C)",
        "Apparent Temperature (C)",
        "Humidity",
        "Wind Speed (km/h)",
        "Pressure (millibars)",
    ]

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(
        df[corr_cols].corr(),
        annot=True,
        cmap="coolwarm",
        ax=ax
    )
    ax.set_title("Weather Variable Correlation Heatmap")

    save_plot(fig, output_dir / "correlation_heatmap.png")


# 7️⃣ Yearly Average Temperature Trend
def plot_yearly_avg_temperature(df, output_dir: Path):
    _ensure_dir(output_dir)

    yearly_avg = df.groupby("Year")["Temperature (C)"].mean()

    plt.figure(figsize=(12, 5))

    plt.plot(
        yearly_avg.index,
        yearly_avg.values,
        marker="o",
        linewidth=2.5,
        color="#D62728",  # warm red → temperature semantics
        alpha=0.9
    )

    plt.title("Yearly Average Temperature Trend", fontsize=15)
    plt.xlabel("Year")
    plt.ylabel("Average Temperature (°C)")
    plt.grid(True, linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.savefig(output_dir / "yearly_avg_temperature_trend.png", dpi=300)
    plt.close()


# 8️⃣ Pressure vs Temperature
def plot_pressure_vs_temperature(df, output_dir: Path):
    _ensure_dir(output_dir)

    plt.figure(figsize=(11, 5))

    sns.scatterplot(
        data=df,
        x="Pressure (millibars)",
        y="Temperature (C)",
        hue="Temperature (C)",
        palette="coolwarm",
        alpha=0.6,
        legend=True
    )

    plt.title("Pressure vs Temperature Relationship", fontsize=14)
    plt.xlabel("Pressure (millibars)")
    plt.ylabel("Temperature (°C)")
    plt.grid(True, linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.savefig(output_dir / "pressure_vs_temperature.png", dpi=300)
    plt.close()


# 9️⃣ Wind Speed Distribution
def plot_wind_speed_distribution(df, output_dir: Path):
    _ensure_dir(output_dir)

    plt.figure(figsize=(11, 5))

    sns.histplot(
        data=df,
        x="Wind Speed (km/h)",
        bins=30,
        kde=True,
        color="#4C72B0",
        edgecolor="white",
        alpha=0.8
    )

    plt.title("Distribution of Wind Speed", fontsize=14)
    plt.xlabel("Wind Speed (km/h)")
    plt.ylabel("Frequency")
    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.savefig(output_dir / "wind_speed_distribution.png", dpi=300)
    plt.close()


# 🔟 Temperature Heatmap by Month & Year
def plot_temperature_heatmap(df, output_dir: Path):
    _ensure_dir(output_dir)

    month_order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    pivot = (
        df.pivot_table(
            index="Year",
            columns="Month_Name",
            values="Temperature (C)",
            aggfunc="mean"
        )
        .reindex(columns=month_order)
    )

    plt.figure(figsize=(14, 6))

    sns.heatmap(
        pivot,
        cmap="RdYlBu_r",   # blue=cold → red=hot
        annot=True,
        fmt=".1f",
        linewidths=0.4,
        linecolor="white",
        cbar_kws={"label": "Avg Temperature (°C)"}
    )

    plt.title("Average Monthly Temperature by Year", fontsize=15)
    plt.xlabel("Month")
    plt.ylabel("Year")
    plt.yticks(rotation=0)

    plt.tight_layout()
    plt.savefig(output_dir / "temperature_heatmap_month_year.png", dpi=300)
    plt.close()


