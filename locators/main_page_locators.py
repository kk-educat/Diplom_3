from selenium.webdriver.common.by import By


BUN_RD_D3_INGREDIENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
BUN_RD_D3_INGREDIENT_COUNTER = (
    By.XPATH,
    "//a[.//p[contains(@class, 'BurgerIngredient_ingredient__text')"
    "and text()='Флюоресцентная булка R2-D3']]"
    "//p[contains(@class, 'counter_counter__num')]"
)
INGREDIENTS_FORM_HEADER = (By.XPATH, "//h2[text()= 'Детали ингредиента']")
INGREDIENTS_FORM_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button//*[name()='path']")
CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
# локатор позиции в корзине, куда пользователь добавляет верхнюю булочку
CONSTRUCTOR_BASKET_TOP_BUN_POSITION = (By.XPATH, "//div[contains(@class, 'constructor-element_pos_top')]")
