import numpy as np


def descriptive_stats(series):
    return {
        "mean": series.mean(),
        "median": series.median(),
        "std": series.std(),
        "min": series.min(),
        "max": series.max()
    }


def correlation(df):
    return df.corr(numeric_only=True)
