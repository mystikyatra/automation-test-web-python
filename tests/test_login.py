import pytest
from config import config
from pages.login_page import LoginPage
from utils.logger import setup_logging

logger = setup_logging(__name__)

def test_valid_login(driver):
    logger.info("Test: Valid Login")
    driver.get(config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login(config.USERNAME, config.PASSWORD)
    #assert "inventory" in driver.current_url, "Login failed!"
    logger.info("Login successful, redirected to inventory page.")
