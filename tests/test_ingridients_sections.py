from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators

class Test_Ingridients_Sections:
    def test_transition_to_ingridients_sections(self, driver, register_user):
        # Ожидаем появления кнопки входа в личный кабинет после успешной регистрации
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_LOGIN_BTN))
        # Используем зарегистрированного пользователя для входа
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(register_user["email"])
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(register_user["password"])
        # Нажимаем кнопку "Войти"
        driver.find_element(*TestLocators.MAIN_LOGIN_BTN).click()
        # Нажимаем на секцию Начинки
        driver.find_element(*TestLocators.FILLINGS_SECTIONS).click()
        # Проверяем, что отображается заголовок Начинки
        assert driver.find_element(*TestLocators.FILLINGS_TITLE).is_displayed()
        # Нажимаем на секуию Соусы
        driver.find_element(*TestLocators.SAUCE_SECTIONS).click()
        # Проверяем, что отображается заголовок Соусы
        assert driver.find_element(*TestLocators.SAUCE_TITLE).is_displayed()
        # Нажимаем на секцию Булки
        driver.find_element(*TestLocators.BUN_SECTIONS).click()
        # Проверяем, что отображается заголовок Булки
        assert driver.find_element(*TestLocators.BUN_TITLE).is_displayed()