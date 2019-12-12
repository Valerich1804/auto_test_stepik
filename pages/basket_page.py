from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def cart_should_be_empty(self):
        self.shouldnt_be_any_product_in_a_basket()
        self.should_be_empty_basket_text_on_basket_page()

    def shouldnt_be_any_product_in_a_basket(self):
        substring = BasketPageLocators.SUBSTRING_BASKET_EN_GB
# проверка, что на странице присутствует строчка о пустой корзине
        assert substring in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text, "No message of empty basket!"

    def should_be_empty_basket_text_on_basket_page(self):
# проверка, что на странице не появляется товаров, добавленных в корзину
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), "Basket is not empty, but it should!"

    def should_be_not_basket_text_on_basket_page(self):
# проверка, что на странице появляется товар, добавленный в корзину
        assert self.is_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), "Basket is empty, but it shouldn't!"
