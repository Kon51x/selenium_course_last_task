from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage #поможет перемещаться между страницами
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # alert = self.browser.switch_to.alert #поддержка алерта, на всякий случай
        # alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
