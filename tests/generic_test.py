import pytest
from config import config
from pages.file_upload import FileUploadPage
from utils.logger import setup_logging
from config.config import UPLOAD_FILE_PATH

logger = setup_logging(__name__)

def test_file_upload(driver):
    logger.info("Opening file upload page")
    driver.get(config.GENERIC_URL)

    upload_page = FileUploadPage(driver)
    upload_page.upload_file(config.UPLOAD_FILE_PATH)


    assert upload_page.is_upload_successful(), "File upload failed"
    logger.info("File uploaded successfully")
