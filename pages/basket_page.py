from .base_page import BasePage
from .locators import BasketPageLocators

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class BasketPage(BasePage):
    def get_items_in_basket(self):
        basket_items = self.browser.find_elements(*BasketPageLocators.BASKET_ITEMS)
        basket_product_names = [item.text for item in basket_items]
        return basket_product_names