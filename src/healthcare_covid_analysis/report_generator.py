"""
Report text generation for COVID Healthcare Analysis
"""


def overview_text(metrics: dict) -> list[str]:
    return [
        f"Total COVID Cases: {metrics['total_cases']}",
        f"Mortality Rate: {metrics['mortality_rate']:.2f}%",
        f"Average Patient Age: {metrics['average_age']:.1f}",
        f"ICU Mortality Rate: {metrics['icu_mortality_rate']:.2f}%",
    ]


def recommendations() -> list[str]:
    return [
        "Prioritize vaccination and monitoring for elderly populations.",
        "Ensure early detection and management of comorbid conditions.",
        "Optimize ICU resource allocation for severe cases.",
        "Use data-driven risk stratification for patient care.",
    ]
