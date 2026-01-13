import pandas as pd

def clean_clinical_data(path):
    df = pd.read_csv(path)

    df = df.dropna(subset=["patient_id", "diagnosis"])
    df["visit_date"] = pd.to_datetime(df["visit_date"])
    df["ae_reported"] = df["ae_reported"].map({"Yes": 1, "No": 0})

    return df
