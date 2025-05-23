from selenium.webdriver.common.by import By

class FileUploadLocators:
    # File Upload
    FILE_UPLOAD_LINK = (By.LINK_TEXT, "File Upload")
    CHOOSE_FILE = (By.ID, "file-upload")
    UPLOAD_BUTTON = (By.ID, "file-submit")
    FILE_UPLOADED_MESSAGE = (By.XPATH, "//h3[contains(text(), 'File Uploaded')]")
