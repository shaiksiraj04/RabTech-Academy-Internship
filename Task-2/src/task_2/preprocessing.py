"""Preprocessing functions for Task 2."""

import pandas as pd


def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    """Prepare validated data for analysis."""
    processed = data.copy()

    processed["age"] = pd.to_numeric(processed["age"])
    processed["practice_frequency"] = pd.to_numeric(
        processed["practice_frequency"]
    )
    processed["prior_experience"] = pd.to_numeric(
        processed["prior_experience"]
    )
    processed["assessment_score"] = pd.to_numeric(
        processed["assessment_score"]
    )

    return processed