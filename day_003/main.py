from src.extract import extarct_data
from src.transform import transform_data
from src.load import load_data_postgres
from config.config import DATA_PATH

def run_pipeline():
    df = extarct_data(DATA_PATH)
    df = transform_data(df)
    load_data_postgres(df)
    print('data loded successully ')

if __name__ == "__main__":
    run_pipeline()