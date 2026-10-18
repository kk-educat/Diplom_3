import allure

from pages.base_page import BasePage
import locators.orders_feed_page_locators as fp_locators


class OrdersFeedPage(BasePage):
    @allure.step('Получаем номера заказов, находящихся "В работе" на странице "Лента заказов"')
    def get_in_job_order_numbers(self):
        # получаем все элементы, соответствующие заданному локатору
        elements = self.get_all_elements(fp_locators.NUMBERS_IN_JOB_ORDERS)
        # формируем список номеров заказов и возвращаем его
        numbers = []
        for element in elements:
              number = element.text
              numbers.append(number)
        return numbers

    @allure.step('Получаем значение счетчика заказов на странице "Лента заказов"')
    def check_counter_orders(self, locators):
        return self.get_element_text(locators)
