from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def wait_for_element_visible(self, locator, timeout=None):
        wait_time = timeout if timeout is not None else self.timeout
        return WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def enter_text(self, locator, text):
        elem = self.wait_for_element_visible(locator)
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator):
        return self.wait_for_element_visible(locator).text

    def is_element_visible(self, locator):
        try:
            return self.wait_for_element_visible(locator).is_displayed()
        except TimeoutException:
            return False

    def is_element_present(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False
