import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver import ActionChains

import locators.base_page_locators as bp_locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # сохраняем в переменную имя текущего браузера
        self.browser_name = driver.capabilities['browserName']

    @allure.step('Клик по ссылке "Конструктор" в хедере')
    def click_constructor_lnk(self):
        self.element_click(bp_locators.CONSTRUCTOR_LINK)

    @allure.step('Клик по ссылке "Лента заказов" в хедере')
    def click_feed_lnk(self):
        self.element_click(bp_locators.ORDERS_FEED_LINK)

    @allure.step('Клик по ссылке "Личный Кабинет" в хедере')
    def click_personal_cabinet_lnk(self):
        self.element_click(bp_locators.PERSONAL_CABINET_LINK)

    @allure.step('Ожидаем появление элемента')
    def wait_element_visibility(self, locator):
        return WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(locator))

    @allure.step('Ожидаем, когда элемент станет кликабельным')
    def wait_element_clickability(self, locator):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable(locator))

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

    @allure.step('Получаем URL текущей веб-страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Находим поле по заданному локатору и заполняем его значением {key}')
    def send_keys_in_field(self, locator, key):
        self.driver.find_element(*locator).send_keys(key)

    @allure.step('Находим элемент по заданному локатору и кликаем по нему')
    def element_click(self, locator):
        # если тестируем в браузере firefox, то приходится кликать через js из-за наличия модального окна на странице
        if self.browser_name == "Firefox":
            elmt = self.wait_element_clickability(locator)
            self.driver.execute_script("arguments[0].click();", elmt)
        else:
            self.wait_element_clickability(locator).click()

    @allure.step('Перетаскиваем заданный локатором элемент в заданное место страницы')
    def drag_and_drop(self, drag_elmt_locator, drop_position_locator):
        # ожидаем, когда перетаскиваемый элемент будет кликабельным
        self.wait_element_clickability(drag_elmt_locator)
        # находим при помощи локаторов перетаскиваемый элемент и место страницы, куда его нужно перетащить
        drag_elmt = self.driver.find_element(*drag_elmt_locator)
        drop_position = self.driver.find_element(*drop_position_locator)
        # для перетаскивания выполняем скрипт
        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, drag_elmt, drop_position)
