from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BasketPageLocators
from .login_page import LoginPage #поможет перемещаться между страницами
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    # def __init__(self, *args, **kwargs): #просто заглушка
    #     super(MainPage, self).__init__(*args, **kwargs)
        # alert = self.browser.switch_to.alert #поддержка алерта, на всякий случай
        # alert.accept()

    def basket_should_not_contain_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "basket contains items, but it should not"
    
    def should_be_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "there is no basket is empty message, but should be"


