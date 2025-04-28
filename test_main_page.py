import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage


#тут используются методы класса MainPage, чтобы задать последовательность действий для самой проверки
@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser, main_link):
        page = MainPage(browser, main_link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                       # открываем страницу
        page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page() #Проверяет, все ли элементы есть на странице логина

    def test_guest_should_see_login_link(self, browser, main_link):
        page = MainPage(browser, main_link)
        page.open()
        page.should_be_login_link()

# просто пример из курса - как использовать is_not_element_present, чтобы убедиться, что элемента нет
# def should_not_be_success_message(self):
#     assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
#        "Success message is presented, but should not be"

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, main_link):
    page = MainPage(browser, main_link)
    page.open()
    page.go_to_view_basket()
    page.basket_should_not_contain_items()
    page.should_be_basket_empty_message()
    



    