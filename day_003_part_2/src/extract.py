import pandas as pd
from sqlalchemy import create_engine
from config.config import DATABASE_URL
from config.sql import query


engine = create_engine(DATABASE_URL)


def extract_data():
    try:
        df = pd.read_sql(query, engine)
        print(f"{len(df)} rows extarcted")
        return df
    except Exception:
        print('data not found')


        



    

