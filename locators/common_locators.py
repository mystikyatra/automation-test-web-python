from selenium.webdriver.common.by import By

class AddRemove:
    ADD_REMOVE_LINK = (By.LINK_TEXT, "Add/Remove Elements")
    ADD_ELEMENT_BUTTON = (By.XPATH, "//button[text()='Add Element']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button.added-manually")

class FileUploadLocators:
    # File Upload
    FILE_UPLOAD_LINK = (By.LINK_TEXT, "File Upload")
    CHOOSE_FILE = (By.ID, "file-upload")
    UPLOAD_BUTTON = (By.ID, "file-submit")
    FILE_UPLOADED_MESSAGE = (By.XPATH, "//h3[contains(text(), 'File Uploaded')]")

class ReportTableLocators:
    # Report Table
    REPORT_TABLE_LINK = (By.LINK_TEXT, "Challenging DOM")
    TABLE = (By.XPATH, "//div[@class='large-10 columns']//table")
    ROWS = (By.XPATH, "//div[@class='large-10 columns']//table/tbody/tr")
    CELLS = (By.TAG_NAME, "td")

class CheckBoxesLocators:
    # Checkboxes
    CHECKBOX_PAGE = (By.LINK_TEXT, "Checkboxes")
    CHECKBOX_1 = (By.XPATH, '//form[@id="checkboxes"]/input[1]')
    CHECKBOX_2 = (By.XPATH, '//form[@id="checkboxes"]/input[2]')
