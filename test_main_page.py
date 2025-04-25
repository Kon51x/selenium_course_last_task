from .pages.main_page import MainPage
from .pages.login_page import LoginPage


#тут используются методы класса MainPage, чтобы задать последовательность действий для самой проверки
def test_guest_can_go_to_login_page(browser, main_link):
    page = MainPage(browser, main_link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                       # открываем страницу
    page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page() #Проверяет, все ли элементы есть на странице логина

def test_guest_should_see_login_link(browser, main_link):
    page = MainPage(browser, main_link)
    page.open()
    page.should_be_login_link()


    