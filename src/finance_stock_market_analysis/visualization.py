"""
Static visualization exports for Finance / Stock Market Analysis
(Logic preserved exactly from notebook)
"""

from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def _ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def save_plot(fig, output_path: Path):
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


# 1️⃣ Preferred Investment Avenues
def plot_preferred_investment_avenues(df, output_dir: Path):
    _ensure_dir(output_dir)

    fig, ax = plt.subplots(figsize=(6, 5))
    sns.countplot(
        data=df,
        x="Investment_Avenues",
        hue="Investment_Avenues",
        palette="Set2",
        legend=False,
        ax=ax
    )
    ax.set_title("Preferred Investment Avenues", fontsize=14)
    ax.set_xlabel("Investment Avenue")
    ax.set_ylabel("Number of Investors")

    save_plot(fig, output_dir / "preferred_investment_avenues.png")


# 2️⃣ Equity Market Participation
def plot_equity_market_participation(df, output_dir: Path):
    _ensure_dir(output_dir)

    fig, ax = plt.subplots()
    df["Equity_Market"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax
    )
    ax.set_title("Equity Market Participation")
    ax.set_ylabel("")

    save_plot(fig, output_dir / "equity_market_participation.png")


# 3️⃣ Investment Objective Distribution
def plot_investment_objective_distribution(df, output_dir: Path):
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.countplot(
        data=df,
        y="Objective",
        hue="Objective",
        palette="Set3",
        legend=False,
        ax=ax
    )
    ax.set_title("Investment Objectives Distribution", fontsize=14)
    ax.set_xlabel("Number of Investors")
    ax.set_ylabel("Objective")

    save_plot(fig, output_dir / "investment_objectives_distribution.png")


# 4️⃣ Risk Factor vs Investment Avenue
def plot_risk_factor_vs_avenue(df, output_dir: Path):
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.countplot(
        data=df,
        x="Factor",
        hue="Investment_Avenues",
        palette="tab10",
        ax=ax
    )
    ax.set_title("Risk Factor vs Investment Avenue", fontsize=14)
    ax.set_xlabel("Risk Factor")
    ax.set_ylabel("Count")

    save_plot(fig, output_dir / "risk_factor_vs_avenue.png")


# 5️⃣ Duration vs Investment Type
def plot_duration_vs_avenue(df, output_dir: Path):
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.countplot(
        data=df,
        x="Duration",
        hue="Investment_Avenues",
        palette="Set1",
        ax=ax
    )
    ax.set_title("Investment Duration vs Avenue", fontsize=14)
    ax.set_xlabel("Investment Duration")
    ax.set_ylabel("Count")

    save_plot(fig, output_dir / "duration_vs_investment_avenue.png")


# 6️⃣ Age vs Investment Avenue
def plot_age_vs_avenue(df, output_dir: Path):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(
        data=df,
        x="AGE_GROUP",
        hue="Investment_Avenues",
        palette="Set2",
        ax=ax
    )
    ax.set_title("Investment Preference by Age Group")
    ax.set_xlabel("Age Group")
    ax.set_ylabel("Number of Investors")

    save_plot(fig, output_dir / "age_vs_investment_avenue.png")


# 7️⃣ Savings Objective vs Investment Avenue
def plot_savings_objective_vs_avenue(df, output_dir: Path):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.countplot(
        data=df,
        x="What are your savings objectives?",
        hue="Investment_Avenues",
        palette="tab10",
        ax=ax
    )
    ax.set_title("Savings Objectives vs Investment Avenue", fontsize=14)
    ax.set_xlabel("Savings Objective")
    ax.set_ylabel("Count")
    plt.setp(ax.get_xticklabels(), rotation=40, ha="right")

    save_plot(fig, output_dir / "savings_objective_vs_avenue.png")


# 8️⃣ Reasons: Equity vs Mutual Funds
def plot_reasons_equity_vs_mutual(df, output_dir: Path):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    sns.countplot(
        data=df,
        y="Reason_Equity",
        hue="Reason_Equity",
        palette="Blues",
        legend=False,
        ax=axes[0]
    )
    axes[0].set_title("Reasons for Investing in Equity", fontsize=13)

    sns.countplot(
        data=df,
        y="Reason_Mutual",
        hue="Reason_Mutual",
        palette="Greens",
        legend=False,
        ax=axes[1]
    )
    axes[1].set_title("Reasons for Investing in Mutual Funds", fontsize=13)

    save_plot(fig, output_dir / "reasons_equity_vs_mutual.png")


# 9️⃣ Investment Monitoring vs Avenue
def plot_investment_monitoring_vs_avenue(df, output_dir: Path):
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.countplot(
        data=df,
        x="Invest_Monitor",
        hue="Investment_Avenues",
        palette="Set3",
        ax=ax
    )
    ax.set_title("Investment Monitoring Frequency vs Avenue")
    ax.set_xlabel("Investment Monitoring Frequency")
    ax.set_ylabel("Count")

    save_plot(fig, output_dir / "investment_monitoring_vs_avenue.png")


# 🔟 Clustered Correlation Heatmap
def plot_clustered_correlation_heatmap(df, output_dir: Path):
    binary_cols = [
        "Mutual_Funds", "Equity_Market", "Debentures",
        "Government_Bonds", "Fixed_Deposits", "PPF", "Gold"
    ]

    corr = df[binary_cols].corr()

    g = sns.clustermap(
        corr,
        cmap="vlag",
        center=0,
        annot=True,
        fmt=".2f",
        linewidths=0.5,
        figsize=(10, 9),
        dendrogram_ratio=(.15, .15),
        cbar_kws={"label": "Correlation Strength"}
    )

    g.fig.suptitle(
        "Clustered Correlation of Investment Instruments",
        fontsize=14,
        y=1.02
    )

    g.fig.savefig(
        output_dir / "clustered_correlation_heatmap.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.close(g.fig)
