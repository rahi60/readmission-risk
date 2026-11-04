from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

NUMERIC_COLUMNS = ["age", "systolic_bp", "hba1c", "prior_admissions", "smoker"]
CATEGORICAL_COLUMNS = ["sex"]


def build_preprocessor() -> ColumnTransformer:
    """Scale numeric columns and one-hot encode categorical columns."""
    return ColumnTransformer(
        [
            ("num", StandardScaler(), NUMERIC_COLUMNS),
            ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_COLUMNS),
        ]
    )
