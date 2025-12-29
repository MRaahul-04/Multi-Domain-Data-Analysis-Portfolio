"""
Report text generation for Weather Trends Analysis
"""


def overview_text(stats: dict) -> list[str]:
    return [
        f"Mean Temperature: {stats['mean_temperature']:.2f} °C",
        f"Median Temperature: {stats['median_temperature']:.2f} °C",
        f"Min Temperature: {stats['min_temperature']:.2f} °C",
        f"Max Temperature: {stats['max_temperature']:.2f} °C",
    ]


def recommendations() -> list[str]:
    return [
        "Monitor long-term temperature trends for climate planning.",
        "Consider humidity and wind patterns in weather forecasting.",
        "Use seasonal insights to support agriculture and energy planning.",
    ]
