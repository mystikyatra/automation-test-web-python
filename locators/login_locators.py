from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

class InventoryLocators:
    ADD_ITEM = (By.XPATH, "//div[text()='Test.allTheThings() T-Shirt (Red)']")
    ADD_PRODUCT = (By.CSS_SELECTOR, "button.btn_primary.btn_inventory")
    REMOVE_BUTTON = (By.CSS_SELECTOR, ".btn_secondary.btn_inventory")

class GoToCartLocators:
    GOTOCART = (By.ID, "shopping_cart_container")

class CheckOut:
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".btn_action.checkout_button")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".btn_primary.cart_button")
    FINISH_BUTTON = (By.CSS_SELECTOR, ".btn_action.cart_button")



