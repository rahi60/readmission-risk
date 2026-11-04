from pathlib import Path

from sklearn.model_selection import train_test_split

from .data import load_data
from .evaluate import evaluate
from .models import build_model


def run_training(
    data_path: Path,
    target: str = "readmitted_30d",
    model_name: str = "logreg",
    test_size: float = 0.2,
    seed: int = 42,
) -> dict[str, float]:
    """Load data, train a model on the train split, evaluate on the test split."""
    df = load_data(data_path)
    X = df.drop(columns=[target])
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=seed, stratify=y
    )

    model = build_model(model_name, seed)
    model.fit(X_train, y_train)

    proba = model.predict_proba(X_test)[:, 1]
    return evaluate(y_test.to_numpy(), proba)