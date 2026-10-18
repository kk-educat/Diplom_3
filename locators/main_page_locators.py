from selenium.webdriver.common.by import By


# Локаторы взятые НЕ с оригинального сайта Stellar Burgers
BUN_RD_D3_INGREDIENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']") 
INGREDIENTS_FORM_HEADER = (By.XPATH, "//h3[text()= 'Детали ингредиента']")
INGREDIENTS_FORM_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'modal-module__button')]")
INGREDIENT_ADD_BUTTON = (By.XPATH, "//li[.//p[text()='Флюоресцентная булка R2-D3']]//button[contains(@class, 'addButton')]")
INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class, 'counter__num')]")
# Локаторы, взятые из проекта 5 спринта автоматизации, в то же время работающие и с НЕ оригинальным сайтом Stellar Burgers
CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
