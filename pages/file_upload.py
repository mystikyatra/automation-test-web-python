import os
import logging
from locators.common_locators import FileUploadLocators
import time

logger = logging.getLogger(__name__)

class FileUploadPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element(*FileUploadLocators.FILE_UPLOAD_LINK).click()

    def upload_file(self, file_path):
        abs_path = os.path.abspath(file_path)
        self.driver.find_element(*FileUploadLocators.CHOOSE_FILE).send_keys(abs_path)
        logger.info(f"Uploaded file from path: {abs_path}")
        self.driver.find_element(*FileUploadLocators.UPLOAD_BUTTON).click()
    
    def is_upload_successful(self):
        success_message = self.driver.find_element(*FileUploadLocators.FILE_UPLOADED_MESSAGE)
        time.sleep(2)
        return success_message.is_displayed()
        
#        return "File Uploaded!" in success_message.text


