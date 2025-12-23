"""
Static visualization exports for Student Performance Analysis
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


def plot_pass_fail(df, output_dir: Path):
    _ensure_dir(output_dir)

    fig, ax = plt.subplots()
    df["Result"].value_counts().plot(kind="bar", ax=ax)
    ax.set_title("Pass vs Fail Distribution")

    save_plot(fig, output_dir / "pass_fail_distribution.png")


def plot_avg_score_by_subject(df, output_dir: Path):
    _ensure_dir(output_dir)

    subject_columns = ["math_score", "science_score", "english_score"]

    subject_means = (
        df[subject_columns]
        .dropna()
        .mean()
        .sort_values()
    )

    plt.figure(figsize=(9, 5))
    sns.barplot(
        x=subject_means.values,
        y=subject_means.index,
        hue=subject_means.index,
        palette="Set2",
        legend=False
    )

    plt.title("Average Score by Subject", fontsize=14)
    plt.xlabel("Average Score")
    plt.ylabel("Subject")
    plt.grid(axis="x", linestyle="--", alpha=0.4)
    plt.tight_layout()

    plt.savefig(output_dir / "avg_score_by_subject.png", dpi=300)
    plt.close()


def plot_attendance_vs_score(df, output_dir: Path):
    _ensure_dir(output_dir)

    plt.figure(figsize=(9, 5))
    sns.scatterplot(
        data=df,
        x="attendance_percentage",
        y="overall_score",
        hue="Result",
        palette="Set2",
        alpha=0.7
    )

    plt.title("Attendance vs Overall Score", fontsize=14)
    plt.xlabel("Attendance Percentage")
    plt.ylabel("Overall Score")
    plt.legend(title="Result")
    plt.tight_layout()

    plt.savefig(output_dir / "attendance_vs_score.png", dpi=300)
    plt.close()


def plot_correlation_heatmap(df, output_dir: Path):
    _ensure_dir(output_dir)

    corr_cols = [
        "math_score",
        "science_score",
        "english_score",
        "attendance_percentage",
        "overall_score"
    ]

    corr_matrix = df[corr_cols].corr()

    plt.figure(figsize=(10, 7))
    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5,
        cbar_kws={"shrink": 0.8}
    )

    plt.title("Correlation Heatmap of Academic Metrics", fontsize=15)
    plt.tight_layout()

    plt.savefig(output_dir / "correlation_heatmap.png", dpi=300)
    plt.close()


def plot_overall_score_distribution(df, output_dir: Path):
    _ensure_dir(output_dir)

    plt.figure(figsize=(9, 5))
    sns.histplot(
        df["overall_score"],
        bins=20,
        kde=True,
        color="teal"
    )

    plt.title("Distribution of Overall Scores", fontsize=14)
    plt.xlabel("Overall Score")
    plt.ylabel("Student Count")
    plt.tight_layout()

    plt.savefig(output_dir / "overall_score_distribution.png", dpi=300)
    plt.close()


def plot_gender_score_distribution(df, output_dir: Path):
    _ensure_dir(output_dir)

    plt.figure(figsize=(9, 5))
    sns.boxplot(
        data=df,
        x="gender",
        y="overall_score",
        hue="Result",
        palette="pastel"
    )

    plt.title("Score Distribution by Gender", fontsize=14)
    plt.xlabel("Gender")
    plt.ylabel("Overall Score")
    plt.legend(title="Result")
    plt.tight_layout()

    plt.savefig(output_dir / "gender_score_distribution.png", dpi=300)
    plt.close()


