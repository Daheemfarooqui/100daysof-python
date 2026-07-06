import requests
import pandas as pd
from config.config import url

def extract_data():
    try:
        response = requests.get(url)
        data = response.json()
        df = pd.json_normalize(data)
        return df 
        print('Data Extracted form API')
    except Exception:
        print('No API Return ')

