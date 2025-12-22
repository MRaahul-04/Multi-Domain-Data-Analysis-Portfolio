"""
Textual report generation
"""

from datetime import datetime


def format_overview(overview: dict, currency: str = "₹") -> list[str]:
    return [
        f"Total Period: {overview['period_start'].strftime('%B %Y')} - "
        f"{overview['period_end'].strftime('%B %Y')}",
        f"Total Sales: {currency}{overview['total_sales']:,.0f}",
        f"Total Transactions: {overview['total_transactions']:,}",
        f"Average Transaction Value: {currency}{overview['average_transaction']:,.0f}",
    ]


def default_recommendations() -> list[str]:
    return [
        "Increase inventory for top-performing product categories.",
        "Focus promotional campaigns during peak evening hours.",
        "Strengthen loyalty programs to retain high-value customers.",
    ]
