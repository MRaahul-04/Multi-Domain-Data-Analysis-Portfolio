"""
Static visualization exports for COVID Healthcare Analysis
"""

import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import numpy as np

sns.set_theme(
    style="whitegrid",
    palette="muted",
    font_scale=1.05
)


def _ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def save_plot(fig, output_path: Path):
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def plot_mortality_distribution(df, output_dir: Path):
    _ensure_dir(output_dir)

    counts = df["DIED"].value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(6, 4))

    bars = ax.bar(
        counts.index.astype(str),
        counts.values,
        color=["#2ca02c", "#d62728"],  # Green = Alive, Red = Died
        edgecolor="black",
        linewidth=0.6
    )

    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{int(height):,}",
            ha="center",
            va="bottom",
            fontsize=10
        )

    ax.set_title("COVID Mortality Distribution", fontsize=14, pad=10)
    ax.set_xlabel("Outcome (0 = Alive, 1 = Died)", fontsize=11)
    ax.set_ylabel("Number of Patients", fontsize=11)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    save_plot(fig, output_dir / "mortality_distribution.png")


def plot_age_group_mortality(df, output_dir: Path):
    _ensure_dir(output_dir)

    data = (df.groupby("AGE_GROUP", observed=True)["DIED"].mean().reset_index())

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(
        data=data,
        x="AGE_GROUP",
        y="DIED",
        color="#d62728",
        ax=ax
    )

    ax.set_title("Mortality Rate by Age Group", fontsize=14)
    ax.set_xlabel("Age Group")
    ax.set_ylabel("Mortality Rate")

    save_plot(fig, output_dir / "age_group_mortality.png")


def plot_comorbidity_impact(df, output_dir: Path, condition: str):
    _ensure_dir(output_dir)

    data = (
        df.groupby(condition, observed=True)["DIED"]
        .mean()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.barplot(
        data=data,
        x=condition,
        y="DIED",
        hue=condition,
        palette="viridis",
        legend=False,
        errorbar=None
    )

    ax.set_title(f"Mortality Rate by {condition}", fontsize=13)
    ax.set_xlabel(condition)
    ax.set_ylabel("Mortality Rate")

    plt.tight_layout()
    plt.savefig(output_dir / f"mortality_by_{condition.lower()}.png", dpi=300)
    plt.close()


def plot_icu_mortality(df, output_dir: Path):
    _ensure_dir(output_dir)

    data = df.groupby("ICU")["DIED"].mean().reset_index()

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(
        data=df,
        x="ICU",
        y="DIED",
        hue="ICU",
        palette="coolwarm",
        legend=False,
        estimator=np.mean,
        errorbar=None
    )

    ax.set_title("Mortality Rate by ICU Admission", fontsize=14)
    ax.set_xlabel("ICU Admission (0 = No, 1 = Yes)")
    ax.set_ylabel("Mortality Rate")

    save_plot(fig, output_dir / "icu_mortality.png")


def plot_clinical_correlation_heatmap(df, output_dir: Path):
    _ensure_dir(output_dir)

    clinical_cols = [
        "AGE", "DIABETES", "COPD", "ASTHMA", "HIPERTENSION",
        "OBESITY", "RENAL_CHRONIC", "ICU", "DIED"
    ]

    fig, ax = plt.subplots(figsize=(12, 7))
    sns.heatmap(
        df[clinical_cols].corr(),
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        linewidths=0.5,
        ax=ax
    )

    ax.set_title("Clinical Variable Correlation Heatmap", fontsize=14)

    save_plot(fig, output_dir / "clinical_correlation_heatmap.png")
