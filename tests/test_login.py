import pytest
from config import config
from pages.login_page import LoginPage
from utils.logger import setup_logging
from selenium.webdriver.common.by import By
import time

logger = setup_logging(__name__)

def test_valid_login(driver):
    logger.info("Test: Valid Login")
    
    driver.get(config.BASE_URL)
    
    login_page = LoginPage(driver)
    login_page.login(config.USERNAME, config.PASSWORD)
    time.sleep(5)

    logger.info("Login successful, redirected to inventory page.")
    
    # Scroll to product and click "Add to cart"
    login_page.inventory_page()

    logger.info("Clicked 'Add to cart' button.")

    login_page.remove_product()
    logger.info("Assertion passed - Product successfully added to cart.")

    login_page.go_to_cart()
    logger.info("Cart page opened successfully.")  

    login_page.go_to_cart()
    logger.info("Cart page loaded successfully.")


