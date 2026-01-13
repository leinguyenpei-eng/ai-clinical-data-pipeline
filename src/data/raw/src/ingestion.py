import pandas as pd

def load_raw_data(path):
    """
    Load raw clinical trial data from CSV.
    """
    return pd.read_csv(path)
