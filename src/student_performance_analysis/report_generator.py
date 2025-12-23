"""
Report text generation for Student Performance
"""


def overview_text(metrics: dict) -> list[str]:
    return [
        f"Total Students: {metrics['total_students']}",
        f"Pass Percentage: {metrics['pass_percentage']:.2f}%",
        f"Average Score: {metrics['average_score']:.2f}",
    ]


def recommendations() -> list[str]:
    return [
        "Monitor and improve student attendance.",
        "Encourage structured study routines.",
        "Provide academic support for low-performing students.",
        "Introduce early academic intervention programs.",
    ]
