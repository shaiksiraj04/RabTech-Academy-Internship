"""Statistical analysis functions for Task 2."""

import pandas as pd
import statsmodels.api as sm


def run_primary_analysis(data: pd.DataFrame) -> pd.DataFrame:
    """Run the preregistered primary regression analysis."""

    x = data[["practice_frequency"]]
    y = data["assessment_score"]

    x = sm.add_constant(x)

    model = sm.OLS(y, x).fit()

    result = pd.DataFrame(
        {
            "term": model.params.index,
            "coefficient": model.params.values,
            "standard_error": model.bse.values,
            "p_value": model.pvalues.values,
            "ci_lower": model.conf_int()[0].values,
            "ci_upper": model.conf_int()[1].values,
        }
    )

    return result