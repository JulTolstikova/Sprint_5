from selenium.webdriver.common.by import By
class TestLocators:
    # кнопка Личный кабинет
    PROFILE_BTN = By.XPATH, "//a[@href='/account']"
    # Заголовок Профиль
    PROFILE_TITLE = By.XPATH, "//li[contains(@class, 'Account_listItem')]//a[text()='Профиль']"
    # кнопка Выход
    LOGOUT_BTN = By.XPATH, "//button[@type = 'button']"
    # кнопка Конструктор
    CONSTRUCTION_BTN = By.XPATH, "//p[text()='Конструктор']"
    # заголовок Соберите бургер
    CONSTRUCTION_TITLE = By.XPATH, "//h1"
    # логотип
    LOGO_BURGERS = By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2"
    # ссылка Зарегистрироваться на странице авторизации
    REGISTER_BTN = By.XPATH, "//a[text()= 'Зарегистрироваться']"
    # инпут Имя
    INPUT_NAME = By.XPATH, "//label[text()='Имя']/following::input[@name = 'name']"
    # инпут Email
    INPUT_EMAIL = By.XPATH, "//label[text()='Email']/following::input[@name = 'name']"
    # инпут Пароль
    INPUT_PASSWORD = By.NAME, 'Пароль'
    # кнопка Зарегистрироваться
    REGISTRATION_BTN = By.XPATH, "//button[text()='Зарегистрироваться']"
    # ссылка Восстановить пароль
    RECOVER_PASSWORD_BTN = By.XPATH, "//a[text()='Восстановить пароль']"
    # кнопка Войти на странице авторизации
    MAIN_LOGIN_BTN = By.XPATH, "//button[text()='Войти']"
    # кнопка Войти в других разделах
    LOGIN_BTN = By.XPATH, "//a[text()='Войти']"
    # кнопка Оформить заказ
    PLACE_AN_ORDER_BTN = By.XPATH, "//button[text()='Оформить заказ']"
    # сообщение об ошибке при вводе некорректного пароля
    ERROR_MESSAGE_WRONG_PASSWORD = By.XPATH, "//p[text()='Некорректный пароль']"
    # раздел Начинки
    FILLINGS_SECTIONS = By.XPATH, "//span[text()='Начинки']"
    # заголовок раздела Начинки
    FILLINGS_TITLE = By.XPATH, "//h2[text()='Начинки']"
    # раздел Соусы
    SAUCE_SECTIONS = By.XPATH, "//span[text()='Соусы']"
    # заголовок раздела Соусы
    SAUCE_TITLE = By.XPATH, "//h2[text()='Соусы']"
    # раздел Булки
    BUN_SECTIONS = By.XPATH, "//span[text()='Булки']"
    # заголовок раздела Булки
    BUN_TITLE = By.XPATH, "//h2[text()='Булки']"
