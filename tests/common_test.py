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

@pytest.mark.order(4)
def test_checkboxes(driver):
    logger.info("Opening Checkboxes page")
    driver.get(config.GENERIC_URL)

    checkboxes_page = CheckBoxesPage(driver)
    checkboxes_page.check_checkboxes()
    logger.info("Checkboxes test passed")

@pytest.mark.order(5)
def test_disappearing_elements(driver):
    logger.info("Opening Disappearing Elements page")
    driver.get(config.GENERIC_URL)

    disappearing_elements_page = DisappearingElementsPage(driver)
    disappearing_elements_page.navigate_to_disappearing_elements()

    found = disappearing_elements_page.find_and_click_gallery_menu()
    assert found, "Failed to locate 'Gallery' menu after multiple refreshes."

pytest.mark.order(6)
def test_drag_and_drop(driver):
    logger.info("Opening Drag and Drop page")
    driver.get(config.GENERIC_URL)

    drag_and_drop_page = DragAndDropPage(driver)
    drag_and_drop_page.drag_and_drop()
    logger.info("Drag and Drop test passed")
