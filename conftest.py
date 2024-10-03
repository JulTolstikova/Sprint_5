import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from selenium.webdriver.chrome.options import Options
import random

@pytest.fixture
def base_url():
    return "https://stellarburgers.nomoreparties.site/login"

# Фикстура для инициализации драйвера
@pytest.fixture(scope="function")
def driver(base_url):
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.get(base_url)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def generate_email():
    random_digits = ''.join([str(random.randint(0, 9)) for _ in range(4)])
    email = f"jul_tolstikova_14{random_digits}@yandex.ru"
    return email

@pytest.fixture
def test_user():
    user = {
        "name": "Julia",
        "email": generate_email(),
        "password": "password123"
    }
    return user

# Фикстура для регистрации пользователя
@pytest.fixture(scope="function")
def register_user(driver, test_user):

    # Нажимаем на кнопку регистрации
    driver.find_element(*TestLocators.REGISTER_BTN).click()

    # Ожидаем появление поля ввода имени
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.INPUT_NAME))

    # Вводим данные для регистрации
    driver.find_element(*TestLocators.INPUT_NAME).send_keys(test_user["name"])
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(test_user["email"])
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(test_user["password"])

    # Нажимаем на кнопку регистрации
    driver.find_element(*TestLocators.REGISTRATION_BTN).click()
    return test_user
