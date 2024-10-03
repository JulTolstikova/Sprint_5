from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators

class Test_Logout:
    def test_logout_from_profile(self, driver, register_user):
        # Ожидаем появления кнопки входа в личный кабинет после успешной регистрации
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_LOGIN_BTN))
        # Используем зарегистрированного пользователя для входа
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(register_user["email"])
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(register_user["password"])

        # Нажимаем кнопку "Войти"
        driver.find_element(*TestLocators.MAIN_LOGIN_BTN).click()

        # Нажимаем на кнопку Личный кабинет
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_BTN))
        driver.find_element(*TestLocators.PROFILE_BTN).click()

        # Нажимаем кнопку выхода
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.LOGOUT_BTN))
        driver.find_element(*TestLocators.LOGOUT_BTN).click()
        # Проверяем, что отображается страница авторизации
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAIN_LOGIN_BTN))