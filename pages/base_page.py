import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import locators.base_page_locators as bp_locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик по ссылке "Конструктор" в хедере')
    def click_constructor_lnk(self):
        self.driver.find_element(*bp_locators.CONSTRUCTOR_LINK).click()

    @allure.step('Клик по ссылке "Лента заказов" в хедере')
    def click_feed_lnk(self):
        self.driver.find_element(*bp_locators.ORDERS_FEED_LINK).click()

    @allure.step('Клик по ссылке "Личный Кабинет" в хедере')
    def click_personal_cabinet_lnk(self):
        self.driver.find_element(*bp_locators.PERSONAL_CABINET_LINK).click()

    @allure.step('Ожидаем появление элемента')
    def wait_element_visibility(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))

    @allure.step('Ожидаем, когда элемент станет кликабельным')
    def wait_element_clickability(self, locator):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))

    # Проверочный метод: возвращает элемент в случае его появления (это может служить признаком успеха для assert)
    @allure.step('Проверяем появление элемента')
    def check_element(self, locator):
        return self.wait_element_visibility(locator)

    # Проверочный метод: возвращает элемент в случае его исчезновения (это может служить признаком успеха для assert)
    @allure.step('Проверяем исчезновение элемента')
    def check_element_not_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.invisibility_of_element_located(locator))

    @allure.step('Получаем текстовое содержимое элемента')
    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
        return element.text

    @allure.step('Получаем все элементы, соответствующие локатору')
    def get_all_elements(self, locator):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step('Обновляем текущую веб-страницу')
    def update_page(self):
        self.driver.refresh()
