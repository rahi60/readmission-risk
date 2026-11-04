import numpy as np
import pandas as pd


def make_synthetic(n: int = 1000, seed: int = 42) -> pd.DataFrame:
    """Create a fictional dataset of discharged patients.

    The outcome `readmitted_30d` depends on the features through a
    logistic formula plus randomness. No real patient data is involved.
    """
    rng = np.random.default_rng(seed)

    age = rng.integers(18, 95, size=n)
    sex = rng.choice(["F", "M"], size=n)
    systolic_bp = rng.normal(135, 20, size=n).clip(60, 260)
    hba1c = rng.normal(7.0, 1.4, size=n).clip(3.0, 20.0)
    prior_admissions = rng.poisson(1.0, size=n).clip(0, 50)
    smoker = rng.binomial(1, 0.25, size=n)

    logit = (
        -2.2
        + 0.03 * (age - 60)
        + 0.015 * (systolic_bp - 135)
        + 0.25 * (hba1c - 7.0)
        + 0.45 * prior_admissions
        + 0.40 * smoker
    )
    probability = 1 / (1 + np.exp(-logit))
    readmitted_30d = rng.binomial(1, probability)

    return pd.DataFrame(
        {
            "age": age,
            "sex": sex,
            "systolic_bp": systolic_bp.round(1),
            "hba1c": hba1c.round(1),
            "prior_admissions": prior_admissions,
            "smoker": smoker,
            "readmitted_30d": readmitted_30d,
        }
    )