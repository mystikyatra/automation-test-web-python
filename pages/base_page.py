from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException
from utils.logger import setup_logging

logger = setup_logging(__name__)

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
        
    def accept_alert(self, timeout=None):
        # Wait for and accept a JavaScript alert.
        wait_time = timeout if timeout else self.timeout
        try:
            WebDriverWait(self.driver, wait_time).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            logger.info(f"Accepting alert with text: {alert.text}")
            alert.accept()
        except (TimeoutException, NoAlertPresentException):
            logger.error("No alert was present or timed out waiting.")
            raise
    
    def dismiss_alert(self, timeout=None):
        # Dismiss confirm alert
        wait_time = timeout or self.timeout
        try:
            WebDriverWait(self.driver, wait_time).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            logger.info(f"Dismissing alert with text: {alert.text}")
            alert.dismiss()
        except (TimeoutException, NoAlertPresentException):
            logger.error("No alert was present or timed out waiting.")
            raise
    
    def send_text_to_alert(self, text, accept=True, timeout=None):
        wait_time = timeout or self.timeout
        try:
            WebDriverWait(self.driver, wait_time).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            logger.info(f"Sending text to alert: {text}")
            alert.send_keys(text)
            if accept:
                alert.accept()
                logger.info("Prompt accepted.")
            else:
                alert.dismiss()
                logger.info("Prompt dismissed.")
        except (TimeoutException, NoAlertPresentException):
            logger.error("Prompt alert was not present or timed out.")
            raise

    def scroll_to_element(self, locator):
        # Scrolls the page until the element is in view.
        element = self.wait_for_element_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)
        return element



