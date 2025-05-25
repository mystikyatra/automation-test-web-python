import os
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from utils.logger import setup_logging
from locators.common_locators import *

logger = setup_logging(__name__)

class AddRemoveElementsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_remove_elements(self):
        self.driver.find_element(*AddRemove.ADD_REMOVE_LINK).click()
        self.driver.find_element(*AddRemove.ADD_ELEMENT_BUTTON).click()
        self.driver.find_element(*AddRemove.DELETE_BUTTON).click()
        logger.info("Performed add and remove actions on the Add/Remove Elements page.")

class FileUploadPage:
    def __init__(self, driver):
        self.driver = driver

    def upload_file(self, file_path):
        self.driver.find_element(*FileUploadLocators.FILE_UPLOAD_LINK).click()
        abs_path = os.path.abspath(file_path)
        self.driver.find_element(*FileUploadLocators.CHOOSE_FILE).send_keys(abs_path)
        logger.info(f"Uploaded file from path: {abs_path}")
        self.driver.find_element(*FileUploadLocators.UPLOAD_BUTTON).click()

    def is_upload_successful(self):
        success_message = self.driver.find_element(*FileUploadLocators.FILE_UPLOADED_MESSAGE)
        return success_message.is_displayed()

class ReportTablePage:
    def __init__(self, driver):
        self.driver = driver

    def test_extract_challenging_dom_table(self, driver):
        self.driver.find_element(*ReportTableLocators.REPORT_TABLE_LINK).click()
        logger.info("Opened Report Table page.")

        table = self.driver.find_element(*ReportTableLocators.TABLE)
        rows = table.find_elements(*ReportTableLocators.ROWS)
        logger.info(f"Number of rows in the table: {len(rows)}")

        all_rows_data = []

        for row_index, row in enumerate(rows):
            cells = row.find_elements(*ReportTableLocators.CELLS)
            #row_data = [cell.text for cell in cells]
            row_data = [cell.text.replace('\n', '').replace(' ', '') if idx == 6 else cell.text 
            for idx, cell in enumerate(cells)]
            logger.info(f"Row {row_index + 1}: {row_data}")
            all_rows_data.append(row_data)

        # Assertions for first and last row
        assert all_rows_data, "No rows found in the table."

        first_row = all_rows_data[0]
        last_row = all_rows_data[-1]

        expected_first_row = ["Iuvaret0", "Apeirian0", "Adipisci0", "Definiebas0", "Consequuntur0", "Phaedrum0", "editdelete"]
        expected_last_row = ["Iuvaret9", "Apeirian9", "Adipisci9", "Definiebas9", "Consequuntur9", "Phaedrum9", "editdelete"]

        assert first_row == expected_first_row, f"First row does not match. Expected: {expected_first_row}, Found: {first_row}"
        assert last_row == expected_last_row, f"Last row does not match. Expected: {expected_last_row}, Found: {last_row}"

        logger.info("First and last row assertions passed.")

class CheckBoxesPage:
    def __init__(self, driver):
        self.driver = driver

    def check_checkboxes(self):
        self.driver.find_element(*CheckBoxesLocators.CHECKBOX_PAGE).click()
        checkbox1 = self.driver.find_element(*CheckBoxesLocators.CHECKBOX_1)
        checkbox2 = self.driver.find_element(*CheckBoxesLocators.CHECKBOX_2)

        if not checkbox1.is_selected():
            checkbox1.click()
            logger.info("Checkbox 1 was not selected, now it is selected.")
        else:
            logger.info("Checkbox 1 was already selected.")

        if checkbox2.is_selected():
            checkbox2.click()
            logger.info("Checkbox 2 was selected, now it is deselected.")
        else:
            logger.info("Checkbox 2 was already deselected.")

class DisappearingElementsPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_disappearing_elements(self):
        self.driver.find_element(*DisappearingElementsLocators.DISAPPEARING_ELEMENTS_PAGE).click()
        logger.info("Navigated to Disappearing Elements page.")
        self.driver.refresh()

    def find_and_click_gallery_menu(self, max_retries=6, wait_between_retries=2):
        for attempt in range(1, max_retries + 1):
            self.driver.refresh()
            logger.info(f"[Attempt {attempt}] Page refreshed.")

            time.sleep(wait_between_retries)  # allow dynamic elements to re-render

            try:
                gallery = self.driver.find_element(*DisappearingElementsLocators.MENU)
                if gallery.is_displayed():
                    logger.info(f"'Gallery' menu found and is visible on attempt {attempt}. Clicking it.")
                    gallery.click()
                    return True
            except NoSuchElementException:
                logger.info(f"'Gallery' not found on attempt {attempt}. Retrying...")

        logger.warning(f"'Gallery' menu did not appear after {max_retries} attempts.")
        return False

class DragAndDropPage:
    def __init__(self, driver):
        self.driver = driver

    def drag_and_drop(self):
        self.driver.find_element(*DragAndDropLocators.DRAG_AND_DROP_PAGE).click()
        logger.info("Opened Drag and Drop page.")

        drag_element = self.driver.find_element(*DragAndDropLocators.DRAG_ELEMENT)
        drop_element = self.driver.find_element(*DragAndDropLocators.DROP_ELEMENT)

        # Perform drag and drop action
        actions = ActionChains(self.driver)
        actions.drag_and_drop(drag_element, drop_element).perform()
        time.sleep(2)  # Wait for the action to complete
        logger.info("Performed drag and drop action.")

class DropDownPage:
    def __init__(self, driver):
        self.driver = driver

    def select_option(self, visible_text):  # changed method name to match test
        self.driver.find_element(*DropDownLocators.DROPDOWN_PAGE).click()
        dropdown = self.driver.find_element(*DropDownLocators.DROPDOWN_SELECT)
        options = dropdown.find_elements(By.TAG_NAME, "option")
        
        for option in options:
            if option.text.strip() == visible_text:
                option.click()
                logger.info(f"Selected dropdown option: {visible_text}")
                return
        logger.warning(f"Option '{visible_text}' not found in the dropdown.")