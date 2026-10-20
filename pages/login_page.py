import allure

from pages.base_page import BasePage
import locators.login_page_locators as lp_locators


class LoginPage(BasePage):
    @allure.step('Логинимся на сайте')
    def login(self, email, password):
        # заполняем поле E-Mail
        self.send_keys_in_field(lp_locators.SIGN_IN_MAIL_FIELD, email)
        # заполняем поле Пароль
        self.send_keys_in_field(lp_locators.SIGN_IN_PSWD_FIELD, password)
        # нажимаем на кнопку Войти
        self.element_click(lp_locators.SIGN_IN_BUTTON)
