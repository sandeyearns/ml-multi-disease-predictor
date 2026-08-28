# this file and folder create because the reason is it will not happen in training but
# also in prediction also. 

import numpy as np

# pasting the exact function from diabetesr_predction.ipynb
# but not pasting other simple imputer converting this function by filling with median
# because that simple imputer will be saved as a pipeline but this function will not be saved so
# so we will confiured and used in training.py and predictor.py

def replace_zeros_with_nan(X):
    """
    Replace 0 -> NaN for selected columns in a pandas DataFrame.
    Returns a NEW DataFrame (safe for sklearn pipelines).
    """
    X = X.copy()
    cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    for col in cols:
        if col in X.columns:
            X[col] = X[col].replace(0, np.nan)
    return X