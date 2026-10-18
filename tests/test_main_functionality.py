import allure

from pages.main_page import MainPage
import data as d


class TestMainFunctionality:
    @allure.title('Тест-кейс: переход по клику на "Конструктор"')
    def test_constructor_access_through_link(self, driver):
        main_page = MainPage(driver)
        main_page.click_personal_cabinet_lnk()
        main_page.click_constructor_lnk()
        assert driver.current_url == d.MAIN_PAGE_LINK

    @allure.title('Тест-кейс: переход по клику на раздел "Лента заказов"')
    def test_feed_access_through_link(self, driver):
        main_page = MainPage(driver)
        main_page.click_feed_lnk()
        assert driver.current_url == d.FEED_PAGE_PATH

    @allure.title('Тест-кейс: если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_ingredient_details_appearance(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.check_ingredients_details()

    @allure.title('Тест-кейс: всплывающее окно закрывается кликом по крестику')
    def test_ingredient_details_closing(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.close_ingredients_details()
        assert main_page.check_close_ingredients_details()

    @allure.title('Тест-кейс: при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        main_page.add_ingredient()
        assert int(main_page.get_ingredient_counter()) > 0
