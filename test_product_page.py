import pytest
import time
from .pages.login_page import LoginPage
from .pages.main_page import MainPage # тут это не надо, потому что создается объект страницы продукта, а не гл. страницы
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage



# @pytest.mark.skip(reason="Temporary skipping this test")
# @pytest.mark.run_this
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, product_link):
    page = ProductPage(browser, product_link)
    page.open()
    page.product_has_info()
    page.guest_should_see_add_product_to_basket_button()
    page.add_product_to_basket()
    # page.solve_quiz_and_get_code()
    page.get_success_message_product_name()
    page.success_message_has_close_button()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, main_link):
    page = MainPage(browser, main_link)
    page.open()
    page.go_to_view_basket()
    page.basket_should_not_contain_items()
    page.should_be_basket_empty_message()

#пример с курса, на всякий случай

# @pytest.mark.parametrize('product_link', [
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
# ])

# def test_guest_can_add_product_to_basket(browser, product_link):
#     page = ProductPage(browser, product_link)
#     page.open()
#     page.product_has_info()
#     page.guest_should_see_add_product_to_basket_button()
#     page.add_product_to_basket()
#     page.solve_quiz_and_get_code()

#     # Получаем название продукта на странице
#     product_name = page.browser.find_element(By.CSS_SELECTOR, "div.product_main h1").text

#     # Получаем название продукта в success-сообщении (только жирный текст)
#     success_message_product_name = page.browser.find_element(By.CSS_SELECTOR, "div.alert-success div.alertinner strong").text

#     # Проверяем название товара
#     assert product_name == success_message_product_name, f"Product name mismatch on page {product_link}"

#     # Дополнительно можешь проверить цену, если хочешь:
#     product_price = page.browser.find_element(By.CSS_SELECTOR, "div.product_main p.price_color").text
#     success_message_product_price = page.browser.find_element(By.CSS_SELECTOR, "div.alert-info div.alertinner strong").text

#     assert product_price == success_message_product_price, f"Product price mismatch on page {product_link}"

def test_guest_can_select_language(browser, product_link):
    page = ProductPage(browser, product_link)
    page.open()
    page.select_language("fr")
    page.apply_selected_language()
    page.selected_language_should_appear_in_url("fr")

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser, product_link):
    page = ProductPage(browser, product_link)  
    page.open()                                
    page.go_to_login_page()                    
    login_page = LoginPage(browser, browser.current_url)  
    login_page.should_be_login_page()    

def test_product_should_have_image(browser, product_link):
    page = ProductPage(browser, product_link)
    page.open()
    page.product_has_image()

def test_guest_should_see_search_bar(browser, product_link):
    page = ProductPage(browser, product_link)
    page.open()
    page.navbar_has_search()

@pytest.mark.xfail
def test_guest_cant_see_success_message(browser, product_link):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, product_link):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, product_link):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_basket()
    page.success_message_is_disappeared()

product_links = ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/",
"http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
]

def test_add_multiple_items_to_the_basket(browser):
    total_expected_price = 0.0
    added_product_names = []

    for link in product_links:
        page = ProductPage(browser, link)
        page.open()
        product_name = page.get_product_name()
        product_price = page.get_product_price_as_float()
        page.add_product_to_basket()
        total_expected_price += product_price
        added_product_names.append(product_name)

    total_actual_price = page.get_basket_total_price()
    
    assert round(total_expected_price, 2) == round(total_actual_price, 2), "prices do not match"

    page.go_to_view_basket()
    basket_page = BasketPage(browser, browser.current_url)

    basket_product_names = basket_page.get_items_in_basket()

    assert added_product_names == basket_product_names, "Products in basket do not match added products"


@pytest.mark.user_tests
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, product_link):
        link = product_link
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)
        email = str(time.time()) + "@fakemail.org"
        password = "strongpassword123"
        login_page.register_new_user(email, password)
        login_page.press_registration()
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, product_link):
        page = ProductPage(browser, product_link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, product_link):
        page = ProductPage(browser, product_link)
        page.open()
        page.product_has_info()
        page.guest_should_see_add_product_to_basket_button()
        page.add_product_to_basket()
        page.get_success_message_product_name()
        page.success_message_has_close_button()