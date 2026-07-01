import pandas as pd

def extract(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print('file is not found')