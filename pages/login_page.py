from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login URL was not found"

    def should_be_login_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_form"), "Login for was not found"

    def should_be_register_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#register_form"), "Registration form was not found"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_ADRESS)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password2_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password2_field.send_keys(password)

    def press_log_in(self):
        log_in_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        log_in_button.click()

    def press_registration(self):
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        registration_button.click()