from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators

class Test_Registration:
    def test_sucess_registration(self, driver, register_user):
        # Ожидаем появления кнопки входа в личный кабинет после успешной регистрации
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_LOGIN_BTN))
        # Используем зарегистрированного пользователя для входа
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(register_user["email"])
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(register_user["password"])

        # Нажимаем кнопку "Войти"
        driver.find_element(*TestLocators.MAIN_LOGIN_BTN).click()

        # Ожидаем появления кнопки Оформить заказ, что указывает на успешный вход
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BTN))

    def test_unsucess_registration_short_password(self, driver, test_user):
        # Меняем пароль на короткий
        test_user["password"] = "123"
        # Нажимаем на кнопку регистрации
        driver.find_element(*TestLocators.REGISTER_BTN).click()

        # Ожидаем появление поля ввода имени
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.INPUT_NAME))

        # Вводим данные для регистрации
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(test_user["name"])
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(test_user["email"])
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(test_user["password"])

        # Нажимаем на кнопку регистрации
        driver.find_element(*TestLocators.REGISTRATION_BTN).click()

        #Проверяем, что отображается сообщение об ошибке
        assert driver.find_element(*TestLocators.ERROR_MESSAGE_WRONG_PASSWORD).text == "Некорректный пароль"