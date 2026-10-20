from selenium.webdriver.common.by import By


# Локаторы, взятые из проекта 5 спринта автоматизации, в то же время работающие и с НЕ оригинальным сайтом Stellar Burgers
CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
ORDERS_FEED_LINK = (By.XPATH, "//p[text()='Лента заказов']")
PERSONAL_CABINET_LINK = (By.XPATH, "//p[text()='Личный кабинет']")
