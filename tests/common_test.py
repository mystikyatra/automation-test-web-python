import pytest
from config import config
from pages.common_page import *
from utils.logger import setup_logging

logger = setup_logging(__name__)

@pytest.mark.order(1)
def test_add_remove_elements(driver):
    logger.info("Opening Add/Remove Elements page")
    driver.get(config.GENERIC_URL)

    add_remove_page = AddRemoveElementsPage(driver)
    add_remove_page.add_remove_elements()
    logger.info("Add/Remove Elements test passed")

@pytest.mark.order(2)
def test_file_upload(driver):
    logger.info("Opening file upload page")
    driver.get(config.GENERIC_URL)

    upload_page = FileUploadPage(driver)
    upload_page.upload_file(config.UPLOAD_FILE_PATH)

    assert upload_page.is_upload_successful(), "File upload failed"
    logger.info("File uploaded successfully")

@pytest.mark.order(3)
def test_extract_challenging_dom_table(driver):
    logger.info("Opening Challenging DOM page")
    driver.get(config.GENERIC_URL)
    report_table_page = ReportTablePage(driver)
    report_table_page.test_extract_challenging_dom_table(driver)
    logger.info("Challenging DOM table extraction test passed")

