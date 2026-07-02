from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
from config.config import OUTPUT_PATH , DATABASE_URL
from config.sql import query
def run_pipeline():
    df = extract_data()
    df = transform_data(df)
    load_data(df,OUTPUT_PATH)
    print("load successfull")

if __name__ == "__main__":
    run_pipeline()