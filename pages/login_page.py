from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from selenium import webdriver
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):

        assert self.browser.current_url=='http://selenium1py.pythonanywhere.com/en-gb/accounts/login/', 'Wrong link'

    def should_be_login_form(self):

        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):

        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'

    def register_new_user(self, email, password):
        email_input=self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password_input=self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        password_confirm=self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM)
        password_confirm.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()




