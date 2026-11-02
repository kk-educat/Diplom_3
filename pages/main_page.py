import allure

from pages.base_page import BasePage
import locators.main_page_locators as mp_locators


class MainPage(BasePage):
    @allure.step('Кликаем ингредиент в Конструкторе')
    def click_ingredient(self):
        self.wait_element_clickability(mp_locators.BUN_RD_D3_INGREDIENT)
        self.element_click(mp_locators.BUN_RD_D3_INGREDIENT)

    @allure.step('Проверяем появление всплывающего окна с деталями ингредиента')
    def check_ingredients_details(self):
        return self.check_element(mp_locators.INGREDIENTS_FORM_HEADER)

    @allure.step('Закрываем всплывающее окно с деталями ингредиента')
    def close_ingredients_details(self):
        self.element_click(mp_locators.INGREDIENTS_FORM_CLOSE_BUTTON)

    @allure.step('Проверяем закрытие всплывающего окна с деталями ингредиента')
    def check_close_ingredients_details(self):
        return self.check_element_not_visible(mp_locators.INGREDIENTS_FORM_HEADER)

    @allure.step('Перетаскиваем ингредиент в корзину')
    def add_ingredient(self):
        self.drag_and_drop(mp_locators.BUN_RD_D3_INGREDIENT, mp_locators.CONSTRUCTOR_BASKET_TOP_BUN_POSITION)

    @allure.step('Получаем значение счетчика ингредиента')
    def get_ingredient_counter(self):
        return self.get_element_text(mp_locators.BUN_RD_D3_INGREDIENT_COUNTER)

    @allure.step('Ожидаем появление элементов главной страницы')
    def wait_load_main_page(self):
        self.wait_element_visibility(mp_locators.CREATE_ORDER_BUTTON)
