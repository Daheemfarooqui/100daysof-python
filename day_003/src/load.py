from sqlalchemy import create_engine
from config.config import DATABASE_URL

engine = create_engine(DATABASE_URL)


def load_data_postgres(df):
    try:
        df.to_sql(
            name="students",
            con=engine,
            if_exists="replace",
            index = False   
        )

        print("✅ Data loaded successfully.")

    except Exception as e:
        print(f" Error loading data: {e}")