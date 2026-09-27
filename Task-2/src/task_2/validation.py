"""Data validation functions for Task 2."""

import pandas as pd


REQUIRED_COLUMNS = [
    "participant_id",
    "age",
    "practice_frequency",
    "prior_experience",
    "assessment_score",
]


def validate_columns(data: pd.DataFrame) -> None:
    """Check that all required columns are present."""
    missing = [column for column in REQUIRED_COLUMNS if column not in data.columns]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def validate_data(data: pd.DataFrame) -> None:
    """Run basic validation checks."""
    validate_columns(data)

    if data["participant_id"].duplicated().any():
        raise ValueError("Duplicate participant IDs detected.")

    if data["age"].isna().any():
        raise ValueError("Missing age values detected.")

    if data["practice_frequency"].isna().any():
        raise ValueError("Missing practice-frequency values detected.")

    if data["assessment_score"].isna().any():
        raise ValueError("Missing assessment-score values detected.")

    if (data["practice_frequency"] < 0).any():
        raise ValueError("Practice frequency cannot be negative.")

    if ((data["assessment_score"] < 0) | (data["assessment_score"] > 100)).any():
        raise ValueError("Assessment scores must be between 0 and 100.")