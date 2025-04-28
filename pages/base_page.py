from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from .locators import BasePageLocators

import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


#Самый 'верхний' класс, задает базовые действия, ОБЩИЕ для всех страниц сайта

class BasePage():
    def __init__(self, browser, url, timeout=10):#вызывается при создании объекта base page, то есть при попытке создать
        self.browser = browser                   #создает объект страницы с неявным ожиданием 10с, которое будет
        self.url = url                           #работать на всей проверяемой странице
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):     #вызывается в других классах вместо find_element, так он проверяет 
        try:                                     #наличие элемента и по сути возвращает этот элемент, если он найден
            self.browser.find_element(how, what) #иначе assert в вызываемом методе другого класса вызовет ошибку
        except (NoSuchElementException):
            return False
        return True
    
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
    
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"
    
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_view_basket(self):
        basket = self.browser.find_element(*BasePageLocators.VIEW_BASKET)
        basket.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
    

    #Если же мы хотим проверить, что какой-то элемент исчезает, то следует воспользоваться явным ожиданием 
    #вместе с функцией until_not, в зависимости от того, какой результат мы ожидаем
    #будет ждать до тех пор, пока элемент не исчезнет
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
    
    def select_language(self, selected_language):
        print(f"Attempting to select language: {selected_language}")
        assert self.is_element_present(*BasePageLocators.SELECT_LANGUAGE), "selector for select_language was not found"
        select_element = self.browser.find_element(*BasePageLocators.SELECT_LANGUAGE)
        select_language_button = Select(select_element)
        select_language_button.select_by_value(selected_language)

    def apply_selected_language(self):
        assert self.is_element_present(*BasePageLocators.LANGUAGE_GO), "selector for apply_selected_language was not found"
        GO_BUTTON = self.browser.find_element(*BasePageLocators.LANGUAGE_GO)
        GO_BUTTON.click()

    def selected_language_should_appear_in_url(self, selected_language):
        link = self.browser.current_url
        assert f"/{selected_language}/" in link, "selected language might not have changed"
    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert                      # Переключаемся на всплывающее окно (alert)
        x = alert.text.split(" ")[2]                              # Извлекаем значение x из текста алерта (третье слово)
        answer = str(math.log(abs((12 * math.sin(float(x))))))    # Вычисляем математическую формулу по заданию
        alert.send_keys(answer)                                   # Вводим ответ в поле алерта
        alert.accept()                                            # Подтверждаем алерт (нажимаем OK)

        try:
            alert = self.browser.switch_to.alert       # Пытаемся снова переключиться на алерт (вдруг есть второй)
            alert_text = alert.text                    # Сохраняем текст второго алерта (в нём код)
            print(f"Your code: {alert_text}")          # Выводим код из второго алерта в консоль
            alert.accept()                             # Подтверждаем второй алерт
        except NoAlertPresentException:                # Если второго алерта нет — ловим исключение
            print("No second alert presented")         # Сообщаем, что второго алерта не было
