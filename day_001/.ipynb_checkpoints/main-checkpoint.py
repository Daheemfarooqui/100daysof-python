from src.extract import read_students
from src.transform import calculate_grade, process_students
from src.load import save_report
from config.config import DATA_PATH, OUTPUT_PATH

def run_pipeline():
    df = read_students(DATA_PATH)
    if df is None:
        print("Pipeline stopped.")
        return

    df = calculate_grade(df)
    df = process_students(df)
    save_report(df,OUTPUT_PATH)


if __name__ == "__main__":
    run_pipeline()