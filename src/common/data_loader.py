from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_PATHS = {
    "supermarket": BASE_DIR / "datasets" / "supermarket_sales.csv",
    "education": BASE_DIR / "datasets" / "Student_Performance.csv",
    "weather": BASE_DIR / "datasets" / "weatherHistory.csv",
    "healthcare": BASE_DIR / "datasets" / "Covid Data.csv",
    "finance": BASE_DIR / "datasets" / "Finance_data.csv"
}


def load_csv(file_path: Path) -> pd.DataFrame:
    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} not found")
    return pd.read_csv(file_path)
