from selenium.common.exceptions import NoSuchElementException

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
    
