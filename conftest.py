import pytest
from selenium import webdriver

import data as d
from helpers import User
from helpers import ClientAPI


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.get(d.MAIN_PAGE_LINK)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.get(d.MAIN_PAGE_LINK)
    yield driver
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
