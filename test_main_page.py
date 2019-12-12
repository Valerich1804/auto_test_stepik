import pytest
from .pages.main_page import MainPage
from .pages.locators import MainPageLocators
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    def test_guest_should_see_login_link(self, browser):
        link = MainPageLocators.MAIN_PAGE_LINK
# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, link)
# открываем нужную страницу
        page.open()
# выполняем метод страницы: ищем переход на страницу логина
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = MainPageLocators.MAIN_PAGE_LINK
# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, link)
# открываем нужную страницу
        page.open()
# выполняем метод страницы: переходим на страницу логина
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
# проверка, что попали именно на страницу логина
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_cart_opened_from_main_page(self, browser):
        link = MainPageLocators.MAIN_PAGE_LINK
# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, link)
# открываем нужную страницу
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
# проверка, что корзина пустая
        basket_page.Basket_should_be_empty()
