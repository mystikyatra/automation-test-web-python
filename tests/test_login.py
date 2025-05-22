import pytest
import time
from config import config
from pages.login_page import LoginPage
from utils.logger import setup_logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = setup_logging(__name__)

def test_valid_login(driver):
    logger.info("Test: Valid Login")
    
    driver.get(config.BASE_URL)
    
    login_page = LoginPage(driver)
    login_page.login(config.USERNAME, config.PASSWORD)

    # Wait for inventory page to load using explicit wait
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn_primary.btn_inventory"))
    )

    logger.info("Login successful, redirected to inventory page.")
    
    # Scroll to product and click "Add to cart"
    login_page.inventory_page()
    logger.info("Clicked 'Add to cart' button.")

    login_page.remove_product()
    logger.info("Assertion passed - Product successfully added to cart.")

    login_page.go_to_cart()
    logger.info("Cart page opened successfully.")

    login_page.checkout()
    logger.info("Payment made successfully and Back to Home page.")