from selenium.webdriver.common.by import By


# Локаторы взятые НЕ с оригинального сайта Stellar Burgers

# Локатор, возвращающий список тегов <li>, содержащих номера заказов "В работе"
NUMBERS_IN_JOB_ORDERS = (By.XPATH, "(//div[.//h3[contains(text(),'В работе')]])[last()]//li")
# Локатор счетчика выполненных заказов за сегодня
TODAY_CNT = (By.XPATH, "//h3[text()='Выполнено за сегодня']/following-sibling::p[1]")
# Локатор счетчика выполненных заказов за все время
GENERAL_CNT = (By.XPATH, "//h3[text()='Выполнено за все время']/following-sibling::p[1]")
