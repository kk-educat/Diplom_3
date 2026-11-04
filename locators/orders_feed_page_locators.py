from selenium.webdriver.common.by import By


# Локатор, возвращающий список тегов <li>, содержащих номера заказов "В работе"
NUMBERS_IN_JOB_ORDERS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li")
# Локатор счетчика выполненных заказов за сегодня
TODAY_CNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
# Локатор счетчика выполненных заказов за все время
GENERAL_CNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
