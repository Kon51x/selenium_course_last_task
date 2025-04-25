from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductPage(BasePage):
    def add_product_to_basket(self):
        count = self.get_product_stock_count()
        assert count > 0, "product is out of stock"
        add_product = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_product.click()
    
    def guest_should_see_add_product_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "add_to_basket is not presented"

    def get_product_stock_count(self):
        stock_element = self.browser.find_element(*ProductPageLocators.PRODUCT_STOCK)
        stock_text = stock_element.text
        count = stock_text.split('(')[1].split()[0]  # ['9999999946', 'available)'] разделим строку по скобкам и достанем число "в наличии"
        return int(count)

    def product_has_info(self):
        self.product_has_title()
        self.product_has_stock()
        self.product_has_price()

    def product_has_title(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE)

    def product_has_stock(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_STOCK)
    
    def product_has_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE)

    def product_has_image(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IMAGE), "image is not presented"
        image_element = self.browser.find_element(*ProductPageLocators.PRODUCT_IMAGE)
        src = image_element.get_attribute("src")
        assert src and src.strip() != "", "image's src is empty "

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_success_message_product_name(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text

    def get_basket_total_price(self):
        product_price_text = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        price_digits = ''.join(c for c in product_price_text if c.isdigit() or c == '.')
        return float(price_digits)
    
    def get_product_price_as_float(self):
        price_text = self.get_product_price()
        price_digits = ''.join(c for c in price_text if c.isdigit() or c == '.')
        return float(price_digits)
    
