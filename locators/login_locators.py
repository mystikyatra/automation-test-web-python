class LoginLocators:
    USERNAME_INPUT = ("id", "user-name")
    PASSWORD_INPUT = ("id", "password")
    LOGIN_BUTTON = ("id", "login-button")

class InventoryLocators:
    ADD_PRODUCT = ("id", "add-to-cart-test.allthethings()-t-shirt-(red)")
    REMOVE_BUTTON = ("xpath", "//button[text()='Remove']")

class GoToCartLocators:
    GOTOCART= ("xpath", "//a[@data-test='shopping-cart-link']")