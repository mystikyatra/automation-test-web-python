from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import *
import time
import logging

logger = logging.getLogger(__name__)

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*LoginLocators.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    def scroll_to_element_and_click(self, locator, scroll_by=300, pause=1):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        time.sleep(pause)
        element.click()

    def inventory_page(self):
        self.scroll_to_element_and_click(InventoryLocators.ADD_PRODUCT)
    
    def remove_product(self):
    # Assertion to ensure if the product was not added to cart
        RemoveButton = self.driver.find_element(*InventoryLocators.REMOVE_BUTTON)
        assert RemoveButton.is_displayed(), "Product was added to cart"
    
    def go_to_cart(self):
        self.driver.find_element(*GoToCartLocators.GOTOCART).click()

