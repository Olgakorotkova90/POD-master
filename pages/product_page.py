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
        assert total_price==price, "Total price is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should not be "

    def should_not_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message disappeared, but should be presented "
















