from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def wait_for_element_visible(self, locator, timeout=None):
        wait_time = timeout if timeout else self.timeout
        return WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(locator)
        )