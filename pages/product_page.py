from pages.base_page import BasePage
from pages.base_page import solve_quiz_and_get_code
from pages.locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):

        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button_add_to_basket.click()
        solve_quiz_and_get_code(self)



    def should_be_success_message(self):
        product_name=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message=self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert f'{product_name} has been added to your basket.'== message, 'product name is not presented'

    def should_be_total_price(self):
        total_price=self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        price=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert total_price==price, "Ttal price is not presented"










