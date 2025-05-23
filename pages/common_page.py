import os
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
