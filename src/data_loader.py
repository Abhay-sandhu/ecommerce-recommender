import pandas as pd

def load_data(path: str):
    """Load dataset from CSV"""
    return pd.read_csv(path)
