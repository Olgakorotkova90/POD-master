from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner')
    BASKET_TOTAL_PRICE= (By.CSS_SELECTOR, '.alert-info strong')
