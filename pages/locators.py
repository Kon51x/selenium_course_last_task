from selenium.webdriver.common.by import By


class BasePageLocators():
    SELECT_LANGUAGE = (By.CSS_SELECTOR, "select.form-control")
    LANGUAGE_GO = (By.CSS_SELECTOR, "#language_selector > button[type='submit']")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    L = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(): 
    LOGIN_EMAIL_ADRESS = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")

    REGISTRATION_EMAIL_ADRESS = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")

    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_form > button[name='login_submit']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    PRODUCT_STOCK = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.instock.availability")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, ".item.active img")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1)")
    SUCCESS_MESSAGE_CLOSE_BUTTON = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > a.close")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs")
    SEARCHBAR = (By.CSS_SELECTOR, "#id_q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "div.navbar-collapse.primary-collapse.collapse > form > input")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items .row h3 a")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p > a")