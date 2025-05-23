from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

LOG_FILE_PATH = 'logs/test_log.log'

GENERIC_URL = os.getenv("GENERIC_URL")

# File upload location
UPLOAD_FILE_PATH = os.path.join('data', 'upload_excel_file.xlsx')
