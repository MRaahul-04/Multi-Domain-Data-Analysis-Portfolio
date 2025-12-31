"""
Preprocessing utilities for Healthcare COVID Analysis
"""

import pandas as pd


def preprocess_covid_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Mortality outcome
    df["DIED"] = df["DATE_DIED"].apply(
        lambda x: 0 if x == "9999-99-99" else 1
    )

    # Age groups
    df["AGE_GROUP"] = pd.cut(
        df["AGE"],
        bins=[0, 18, 40, 60, 80, 120],
        labels=["Child", "Young Adult", "Adult", "Senior", "Elderly"]
    )

    # COVID-positive classification (1–3)
    df["COVID_POSITIVE"] = df["CLASIFFICATION_FINAL"].apply(
        lambda x: 1 if x in [1, 2, 3] else 0
    )

    return df
