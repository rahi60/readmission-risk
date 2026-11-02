from .schemas import PatientRecord


def mean_age(records: list[PatientRecord]) -> float:
    """Return the mean age of the given patients."""
    if not records:
        raise ValueError("records must not be empty")
    return sum(r.age for r in records) / len(records)