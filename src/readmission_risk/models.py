from sklearn.base import ClassifierMixin
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from .features import build_preprocessor


def build_model(name: str, seed: int) -> Pipeline:
    """Build a preprocessing + classifier pipeline."""
    classifier: ClassifierMixin
    if name == "logreg":
        classifier = LogisticRegression(max_iter=1000, random_state=seed)
    elif name == "random_forest":
        classifier = RandomForestClassifier(n_estimators=300, random_state=seed)
    else:
        raise ValueError(f"Unknown model: {name}")
    return Pipeline([("pre", build_preprocessor()), ("clf", classifier)])
