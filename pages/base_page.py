from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def wait_for_element_visible(self, locator, timeout=None):
        # Wait for an element to be visible on the page.
        wait_time = timeout if timeout is not None else self.timeout
        return WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        self.wait_for_element_visible(locator).click()

    def enter_text(self, locator, text):
        elem = self.wait_for_element_visible(locator)
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator):
        return self.wait_for_element_visible(locator).text
    
    def is_element_visible(self, locator):
        # Check if an element is visible on the page.
        try:
            return self.wait_for_element_visible(locator).is_displayed()
        except:
            return False
    
    def is_element_present(self, locator):
        # Check if an element is present in the DOM.
        try:
            return self.driver.find_element(*locator).is_displayed()
        except:
            return False
