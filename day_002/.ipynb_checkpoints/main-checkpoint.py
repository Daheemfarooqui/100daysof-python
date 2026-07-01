from src.extract import extract
from src.transform import incress_salary , filter_sales
from src.load import save_report
from config.config import  DATA_PATH, OUTPUT_PATH

def run_pipeline():
    df = extract(DATA_PATH)
    df = incress_salary(df)
    df = filter_sales(df)
    save_report(df,OUTPUT_PATH)

if __name__ == "__main__":
    run_pipeline()
