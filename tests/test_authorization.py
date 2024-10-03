from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators

class Test_Authorization:
    def test_login_on_registration_form(self, driver, register_user):
        driver.find_element(*TestLocators.REGISTER_BTN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BTN))
        driver.find_element(*TestLocators.LOGIN_BTN).click()
        # Ожидаем появления кнопки входа в личный кабинет после успешной регистрации
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_LOGIN_BTN))
        # Используем зарегистрированного пользователя для входа
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(register_user["email"])
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(register_user["password"])
        # Нажимаем кнопку "Войти"
        driver.find_element(*TestLocators.MAIN_LOGIN_BTN).click()
        # Ожидаем появления кнопки Оформить заказ, что указывает на успешный вход
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BTN))

    def test_login_on_recover_password_form(self, driver, register_user):
        driver.find_element(*TestLocators.RECOVER_PASSWORD_BTN).click()
        driver.find_element(*TestLocators.LOGIN_BTN).click()
        # Ожидаем появления кнопки входа в личный кабинет после успешной регистрации
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_LOGIN_BTN))
        # Используем зарегистрированного пользователя для входа
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(register_user["email"])
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(register_user["password"])
        # Нажимаем кнопку "Войти"
        driver.find_element(*TestLocators.MAIN_LOGIN_BTN).click()
        # Ожидаем появления кнопки Оформить заказ, что указывает на успешный вход
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BTN))

    def test_login_from_profile(self, driver, register_user):
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver,5).until(expected_conditions.element_to_be_clickable(TestLocators.PROFILE_BTN))
        driver.find_element(*TestLocators.PROFILE_BTN).click()
        # Ожидаем появления кнопки входа в личный кабинет после успешной регистрации
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_LOGIN_BTN))
        # Используем зарегистрированного пользователя для входа
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(register_user["email"])
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(register_user["password"])
        # Нажимаем кнопку "Войти"
        driver.find_element(*TestLocators.MAIN_LOGIN_BTN).click()
        # Ожидаем появления кнопки Оформить заказ, что указывает на успешный вход
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BTN))