"""Tests for the Task 2 synthetic research pipeline."""

from pathlib import Path

import pandas as pd

from task_2.analysis import run_primary_analysis
from task_2.preprocessing import preprocess_data
from task_2.validation import validate_data


FIXTURE = (
    Path(__file__).parent
    / "fixtures"
    / "synthetic_data.csv"
)


def load_synthetic_data() -> pd.DataFrame:
    """Load the synthetic fixture."""
    return pd.read_csv(FIXTURE)


def test_synthetic_data_loads():
    """Synthetic dataset should load successfully."""
    data = load_synthetic_data()

    assert len(data) == 20
    assert "participant_id" in data.columns


def test_validation_passes():
    """Synthetic dataset should pass validation."""
    data = load_synthetic_data()

    validate_data(data)


def test_preprocessing():
    """Preprocessing should preserve the expected variables."""
    data = load_synthetic_data()

    processed = preprocess_data(data)

    assert len(processed) == 20
    assert processed["practice_frequency"].dtype.kind in "if"
    assert processed["assessment_score"].dtype.kind in "if"


def test_primary_analysis_output_contract():
    """Primary analysis must produce the expected output columns."""
    data = load_synthetic_data()

    validate_data(data)
    processed = preprocess_data(data)
    result = run_primary_analysis(processed)

    required_columns = [
        "term",
        "coefficient",
        "standard_error",
        "p_value",
        "ci_lower",
        "ci_upper",
    ]

    for column in required_columns:
        assert column in result.columns

    assert len(result) == 2