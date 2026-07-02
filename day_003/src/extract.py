import pandas as pd

def extarct_data(file_path):
    try:
        df = pd.read_excel(file_path)
        print('Data extracted')
        return df 
    except FileNotFoundError:
        print('file not found')

      
