import allure
import pytest

from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage
from pages.login_page import LoginPage
from helpers import ClientAPI
import locators.orders_feed_page_locators as fp_locators

class TestOrdersFeed:
    @allure.title('Тест-кейс: после оформления заказа его номер появляется в разделе "В работе"')
    def test_user_order_appearance_in_job_section(self, driver, user_data, ingredients_data):
        main_page = MainPage(driver)
        feed_page = OrdersFeedPage(driver)
        login_page = LoginPage(driver)
        # логиним пользователя (который был создан в фикстуре)
        main_page.click_personal_cabinet_lnk()
        login_page.login(user_data["email"], user_data["password"])
        main_page.wait_load_main_page()
        # отправляем запрос на создание заказа
        ClientAPI().create_order(ingredients_data, user_data["accessToken"])
        # переходим на страницу Лента заказов
        main_page.click_feed_lnk()
        # получаем список номеров заказов "В работе"
        in_job_order_numbers = feed_page.get_in_job_order_numbers()
        # так как пользователь создал заказ один раз, можем получить номер первого заказа в его списке заказов
        user_order_number = str(ClientAPI().get_user_first_order_number(user_data["accessToken"]))
        # проверяем, что номер заказа, сделанного пользователем присутствует среди заказов "В работе"
        assert user_order_number in in_job_order_numbers

    @allure.title('Тест-кейс: при создании нового заказа счетчик "Выполнено за всё время" / "Выполнено за сегодня" увеличивается')
    @pytest.mark.parametrize('counter', [fp_locators.TODAY_CNT, fp_locators.GENERAL_CNT])
    def test_orders_counter_increase(self, driver, user_data, ingredients_data, counter):
        main_page = MainPage(driver)
        feed_page = OrdersFeedPage(driver)
        login_page = LoginPage(driver)
        # логиним пользователя (который был создан в фикстуре)
        main_page.click_personal_cabinet_lnk()
        login_page.login(user_data["email"], user_data["password"])
        main_page.wait_load_main_page()
        # переходим на страницу Лента заказов
        main_page.click_feed_lnk()
        # считываем текущее значение счетчика
        current_cnt = int(feed_page.check_counter_orders(counter))
        # отправляем запрос на создание заказа
        ClientAPI().create_order(ingredients_data, user_data["accessToken"])
        # обновляем страницу
        feed_page.update_page()
        # считываем значение счетчика после создания заказа
        new_cnt = int(feed_page.check_counter_orders(counter))
        # проверяем, что значение счетчика увеличилось
        assert new_cnt > current_cnt
