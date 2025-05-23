import os
from utils.logger import setup_logging
from locators.common_locators import FileUploadLocators, AddRemove

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