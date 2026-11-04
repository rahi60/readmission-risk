import numpy as np
from sklearn.metrics import brier_score_loss, roc_auc_score


def evaluate(y_true: np.ndarray, proba: np.ndarray) -> dict[str, float]:
    """Compute discrimination (AUC) and probability error (Brier score)."""
    return {
        "auc": float(roc_auc_score(y_true, proba)),
        "brier": float(brier_score_loss(y_true, proba)),
    }
