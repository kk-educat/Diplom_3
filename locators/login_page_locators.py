from selenium.webdriver.common.by import By

# Локаторы, взятые из проекта 5 спринта автоматизации
SIGN_IN_MAIL_FIELD = (By.XPATH, "//input[@name='name']")
SIGN_IN_PSWD_FIELD = (By.XPATH, "//input[@name='Пароль']")
SIGN_IN_BUTTON = (By.XPATH, "//button[text()='Войти']")
