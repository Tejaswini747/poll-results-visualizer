# src/data_cleaning.py

import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    # Standardize text
    df["Preferred Tool"] = df["Preferred Tool"].str.strip().str.title()

    # Convert data types
    df["Satisfaction"] = pd.to_numeric(df["Satisfaction"], errors='coerce')

    # Drop rows with invalid values
    df = df.dropna()

    return df