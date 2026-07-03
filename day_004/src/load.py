from sqlalchemy import create_engine
from config.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

def load_data(df):
    try:
        df.to_sql(
            name="api_data",
            con=engine,
            if_exists="replace",
            index=False
        )
        print("Data loaded successfully")
    except Exception as e:
        print(f"Error while data loading: {e}")