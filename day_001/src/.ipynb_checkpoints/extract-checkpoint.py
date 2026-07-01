import pandas as pd

def read_students(file_path):
    try:
        df = pd.read_csv(file_path)
        return df 
    except Exception:
        'file not found'
        return None





    

    
    