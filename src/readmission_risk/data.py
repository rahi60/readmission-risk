from pathlib import Path

import pandas as pd

from .schemas import PatientRecord


def save_data(df: pd.DataFrame, path: Path) -> None:
    """Save a dataframe to CSV, creating parent folders if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def validate_records(df: pd.DataFrame) -> None:
    """Raise a ValidationError if any row violates the PatientRecord schema."""
    for row in df.to_dict(orient="records"):
        PatientRecord(**row)


def load_data(path: Path) -> pd.DataFrame:
    """Read a CSV and validate every row."""
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")
    df = pd.read_csv(path)
    validate_records(df)
    return df