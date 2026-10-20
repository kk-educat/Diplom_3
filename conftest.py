import pytest
from selenium import webdriver

import data as d
from helpers import User
from helpers import ClientAPI


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    # ожидание ответа от тестируемого сайта не более 10 сек
    driver.set_page_load_timeout(10)
    try:
        # если сайт не ответит за 10 сек, тут будет исключение
        driver.get(d.MAIN_PAGE_LINK)
        yield driver
    finally:
        # этот блок кода сработает даже в случае возникновения исключения
        driver.quit()

@pytest.fixture
def user_data():
    payload = User().get_new_user_data()
    response = ClientAPI().create_user(payload)
    data = {
        "email": payload["email"],
        "password": payload["password"],
        "name": payload["name"],
        "accessToken": response.json()["accessToken"]
    }
    yield data
    ClientAPI().delete_user(data["accessToken"])

@pytest.fixture
def ingredients_data():
    response = ClientAPI().get_ingredients()
    response_data = response.json()
    ingredient_0 = response_data['data'][0]['_id']
    ingredient_1 = response_data['data'][1]['_id']
    data = {'ingredients': [ingredient_0, ingredient_1]}
    return data
