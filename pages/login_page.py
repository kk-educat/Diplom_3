import allure

from pages.base_page import BasePage
import locators.login_page_locators as lp_locators


class LoginPage(BasePage):
    @allure.step('Логинимся на сайте')
    def login(self, email, password):
        # заполняем поле E-Mail
        self.driver.find_element(*lp_locators.SIGN_IN_MAIL_FIELD).send_keys(email)
        # заполняем поле Пароль
        self.driver.find_element(*lp_locators.SIGN_IN_PSWD_FIELD).send_keys(password)
        # нажимаем на кнопку Войти
        self.driver.find_element(*lp_locators.SIGN_IN_BUTTON).click()
