from selenium.webdriver.common.by import By

class RegistryPage:
    USERNAME_LOCATOR = (By.XPATH, "(//input[@type='text'])[1]") # Поле ввода Имени для регистрации
    EMAIL_LOCATOR = (By.XPATH, "(//input[@type='text'])[2]") # Поле ввода Емайла для регистрации
    PASSWORD_LOCATOR = (By.XPATH, "//input[@type='password']") # Поле ввода пароля для регистрации
    REGISTER_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0')]") # Кнопка регистрации
    ERROR_MESSAGE_LOCATOR = (By.XPATH, "//p[contains(@class, 'error')]") # Поле отображение ошибки
    ENTER_BTN_LOCATOR = (By.XPATH, "//a[@href='/login']")

class LoginPage:
    EMAIL_LOCATOR = (By.XPATH, "//input[@type='text']") # Поле ввода Имени для авторизации
    PASSWORD_LOCATOR = (By.XPATH, "//input[contains(@type, 'password')]") # Поле ввода пароля для авторизации
    LOGIN_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'button')]") # Кнопка авторизации
    REGISTER_LOCATOR = (By.XPATH, "//a[@href= '/register']") # Кнопка зарегистрироваться
    RESTORE_PASSWORD_LOCATOR = (By.XPATH, "//a[@href= '/forgot-password']") # Кнопка восстановление пароля


class MainPage:
    PERSONAL_ACC_LOCATOR = (By.XPATH, "//a[@href='/account']") # Кнопка Личного кабинета
    CONSTRUCTOR_LOCATOR = (By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a") # Кнопка Конструктора
    ORDER_FEED_LOCATOR = (By.XPATH, "//a[@href='/feed']") # Кнопка Лента заказов
    MAIN_LOGO_LOCATOR = (By.XPATH, "//a[@class='active']") # Кнопка Логотипа сайта
    ENTER_ACCOUNT_LOCATOR = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка Войти в акаунт
    PLACE_ORDER_LOCATOR = (By.XPATH, "//button[contains(@class, 'button')]") # Кнопка Оформление заказа

    BREAD_LOCATOR = (By.XPATH, "(//span[@class= 'text text_type_main-default'])[1]") # Кнопка скрола на Булки
    SAUCES_LOCATOR = (By.XPATH, "(//span[@class= 'text text_type_main-default'])[2]") # Кнопка скрола на Соусы
    TOPPING_LOCATOR = (By.XPATH, "(//span[@class= 'text text_type_main-default'])[3]") # Кнопка скрола на Начинки

    BREAD_SECTION_LOCATOR = (By.XPATH, "//h2[contains(text(),'Булки')]") # Поле с Названием Булки
    SAUCES_SECTION_LOCATOR = (By.XPATH, "//h2[contains(text(),'Соусы')]") # Поле с Названием Соусы
    TOPPING_SECTION_LOCATOR = (By.XPATH, "//h2[contains(text(),'Начинки')]") # Поле с Названием Начинки



class PersonalAccountPage:

    EXIT_BTN_LOCATOR = (By.XPATH, "//button[contains(@class, 'text')]") # Кнопка выхда в Личном кабинете
    ORDER_HISTORY_BTN_LOCATOR = (By.XPATH, "//a[@href='/account/order-history']") # Кнопка Истории заказов в личном кабинете
    PROFILE_BTN_LOCATOR = (By.XPATH, "//a[@href='/account/profile']") # Кнопка Профиль в личном кабинете
    SAVE_BTN_LOCATOR = (By.XPATH, "//button[contains(@class, 'primary')]") # Кнопка сохранить в личном кабинете
    CANCEL_BTN_LOCATOR = (By.XPATH, "//button[contains(@class, 'ts')]") # Кнопка отменя в личном кабинете

    NAME_INPUT_LOCATOR = (By.XPATH, "//input[@name='Name']") # Поле Имя в личном кабинете
    LOGIN_INPUT_LOCATOR = (By.XPATH, "(//input[contains(@name, 'name')])[1]") # Поле логин в личном кабинете
    PASSWORD_INPUT_LOCATOR = (By.XPATH, "//input[contains(@type, 'password')]") # Поле паролья в личном кабинете

class RestorePasswordPage:
    ENTER_BTN_LOCATOR = (By.XPATH, "//a[@href='/login']") # Кнопка Войти из блока восстановление пароля