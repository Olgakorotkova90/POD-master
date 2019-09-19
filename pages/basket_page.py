from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import ProductPageLocators

class BasketPage(BasePage):
    def should_be_empty_message(self):
        message=self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert 'Your basket is empty.' in message, "Empty basket message is not presented "

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME), \
            'Product name presented in basket, but should not be '