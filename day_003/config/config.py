from dotenv import load_dotenv
import os 

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

DATA_PATH = 'data/Student_details.xlsx'
