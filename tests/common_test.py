import pytest
from config import config
from pages.common_page import *
from utils.logger import setup_logging

logger = setup_logging(__name__)

@pytest.mark.order(1)
def test_add_remove_elements(driver):
    logger.info("1. Opening ADD/REMOVE ElEMENTS page !!!")
    driver.get(config.GENERIC_URL)

    add_remove_page = AddRemoveElementsPage(driver)
    add_remove_page.add_remove_elements()
    logger.info("Add/Remove Elements test passed")

@pytest.mark.order(2)
def test_file_upload(driver):
    logger.info("2. Opening FILE UPLOAD page !!!")
    driver.get(config.GENERIC_URL)

    upload_page = FileUploadPage(driver)
    upload_page.upload_file(config.UPLOAD_FILE_PATH)

    assert upload_page.is_upload_successful(), "File upload failed"
    logger.info("File uploaded successfully")

@pytest.mark.order(3)
def test_extract_challenging_dom_table(driver):
    logger.info("3. Opening CHALLENGING DOM TABLE page !!!")
    driver.get(config.GENERIC_URL)
    report_table_page = ReportTablePage(driver)
    report_table_page.test_extract_challenging_dom_table(driver)
    logger.info("Challenging DOM table extraction test passed")

@pytest.mark.order(4)
def test_checkboxes(driver):
    logger.info("4. Opening CHECKBOXES page !!!")
    driver.get(config.GENERIC_URL)

    checkboxes_page = CheckBoxesPage(driver)
    checkboxes_page.check_checkboxes()
    logger.info("Checkboxes test passed")

@pytest.mark.order(5)
def test_disappearing_elements(driver):
    logger.info("5. Opening DISAPPEARING ELEMENTS page !!!")
    driver.get(config.GENERIC_URL)

    disappearing_elements_page = DisappearingElementsPage(driver)
    disappearing_elements_page.navigate_to_disappearing_elements()

    found = disappearing_elements_page.find_and_click_gallery_menu()
    assert found, "Failed to locate 'Gallery' menu after multiple refreshes."

@pytest.mark.order(6)
def test_drag_and_drop(driver):
    logger.info("6. Opening DRAG AND DROP page !!!")
    driver.get(config.GENERIC_URL)

    drag_and_drop_page = DragAndDropPage(driver)
    drag_and_drop_page.drag_and_drop()
    logger.info("Drag and Drop test passed")

@pytest.mark.order(7)
def test_dropdown(driver):
    logger.info("7. Opening DROPDOWN page !!!")
    driver.get(config.GENERIC_URL)

    dropdown_page = DropDownPage(driver)
    dropdown_page.select_option("Option 1")
    logger.info("Dropdown option selected successfully")

@pytest.mark.order(8)
def test_dynamic_content_refresh(driver):
    logger.info("8. Opening DYNAMIC CONTENT REFRESH page !!!")
    driver.get(config.GENERIC_URL)

    dynamic_content_page = DynamicContentPage(driver)

    logger.info("Navigating to Dynamic Controls page")
    dynamic_content_page.navigate_to_dynamic_controls()

    contents = []

    for i in range(3):
        logger.info(f"Clicking refresh link - Attempt {i+1}")
        dynamic_content_page.click_refresh()

        # You might want a slight wait here if content updates asynchronously
        content = dynamic_content_page.get_content_text()
        logger.info(f"Content after click {i+1}: {content}")
        contents.append(content)

    unique_contents = len(set(contents))
    logger.info(f"Unique contents found after 3 refreshes: {unique_contents}")

    assert unique_contents == 3, "Content did not change on each refresh"

    third_content = contents[2]
    assert dynamic_content_page.is_content_displayed(), "Content element is not displayed"
    assert third_content != "", "Third content is empty"

    logger.info("Dynamic content refresh test passed")

@pytest.mark.order(9)
def test_multiple_windows(driver):
    logger.info("9. Opening MULTIPLE WINDOWS page !!!")
    driver.get(config.GENERIC_URL)

    multiple_windows_page = MultipleWindowsPage(driver)
    multiple_windows_page.navigate_to_multiple_windows()

    multiple_windows_page.open_new_window_and_validate_header()
    logger.info("Multiple Windows test passed")
