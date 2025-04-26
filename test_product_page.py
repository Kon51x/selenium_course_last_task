import pytest
from .pages.main_page import MainPage # тут это не надо, потому что создается объект страницы продукта, а не гл. страницы
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage



# @pytest.mark.skip(reason="Temporary skipping this test")
def test_guest_can_add_product_to_basket(browser, product_link):
    page = ProductPage(browser, product_link)
    page.open()
    page.product_has_info()
    page.guest_should_see_add_product_to_basket_button()
    page.add_product_to_basket()
    page.get_success_message_product_name()
    page.success_message_has_close_button()
    # page.solve_quiz_and_get_code()

def test_guest_can_select_language(browser, product_link):
    page = ProductPage(browser, product_link)
    page.open()
    page.select_language("fr")
    page.apply_selected_language()
    page.selected_language_should_appear_in_url("fr")

def test_product_should_have_image(browser, product_link):
    page = ProductPage(browser, product_link)
    page.open()
    page.product_has_image()


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

