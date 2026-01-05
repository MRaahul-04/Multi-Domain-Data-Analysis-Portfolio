"""
Report text generation for Finance / Stock Market Analysis
"""


def overview_text(metrics: dict) -> list[str]:
    return [
        f"Total Investors: {metrics['total_investors']}",
        f"Equity Participation Rate: {metrics['equity_participation_rate']:.2f}%",
        f"Average Investor Age: {metrics['average_age']:.1f}",
    ]


def recommendations() -> list[str]:
    return [
        "Promote diversified portfolios across age groups.",
        "Encourage long-term investment horizons.",
        "Educate investors on risk-adjusted returns.",
        "Support active monitoring for equity investments.",
    ]
