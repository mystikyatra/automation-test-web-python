from selenium.webdriver.common.by import By
from locators.login_locators import LoginLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*LoginLocators.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
