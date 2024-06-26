from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from locators import RegistryPage
from locators import LoginPage
from locators import MainPage


fake = Faker()

class TestRegister:

    def test_successful_registration(self, driver):
        wait = WebDriverWait(driver, 10)
        username = fake.name()
        email = fake.email()
        password = fake.password(length=8)

        driver.find_element(*MainPage.ENTER_ACCOUNT_LOCATOR).click()
        wait.until(EC.element_to_be_clickable(LoginPage.REGISTER_LOCATOR)).click()

        driver.find_element(*RegistryPage.USERNAME_LOCATOR).send_keys(username)
        driver.find_element(*RegistryPage.EMAIL_LOCATOR).send_keys(email)
        driver.find_element(*RegistryPage.PASSWORD_LOCATOR).send_keys(password)
        driver.find_element(*RegistryPage.REGISTER_BUTTON_LOCATOR).click()

        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

        driver.find_element(*LoginPage.EMAIL_LOCATOR).send_keys(email)
        driver.find_element(*LoginPage.PASSWORD_LOCATOR).send_keys(password)

        driver.find_element(*LoginPage.LOGIN_BUTTON_LOCATOR).click()

        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        account_link = wait.until(EC.visibility_of_element_located((MainPage.PERSONAL_ACC_LOCATOR)))
        assert account_link.is_displayed(), "Авторизация после регистрации не удалась"




    def test_invalid_password(self, driver):
        wait = WebDriverWait(driver, 10)

        driver.find_element(*MainPage.ENTER_ACCOUNT_LOCATOR).click()
        wait.until(EC.element_to_be_clickable(LoginPage.REGISTER_LOCATOR)).click()

        driver.find_element(*RegistryPage.USERNAME_LOCATOR).send_keys(fake.name())
        driver.find_element(*RegistryPage.EMAIL_LOCATOR).send_keys(fake.email())
        driver.find_element(*RegistryPage.PASSWORD_LOCATOR).send_keys("12345")
        driver.find_element(*RegistryPage.REGISTER_BUTTON_LOCATOR).click()

        error_message = wait.until(EC.visibility_of_element_located(RegistryPage.ERROR_MESSAGE_LOCATOR)).text
        assert error_message == "Некорректный пароль"





    def test_invalid_email(self, driver):
        wait = WebDriverWait(driver, 10)

        driver.find_element(*MainPage.ENTER_ACCOUNT_LOCATOR).click()
        wait.until(EC.element_to_be_clickable(LoginPage.REGISTER_LOCATOR)).click()

        driver.find_element(*RegistryPage.USERNAME_LOCATOR).send_keys(fake.name())
        driver.find_element(*RegistryPage.EMAIL_LOCATOR).send_keys("test123mail.ru")
        driver.find_element(*RegistryPage.PASSWORD_LOCATOR).send_keys(fake.password(length=8))
        driver.find_element(*RegistryPage.REGISTER_BUTTON_LOCATOR).click()

        register_button = wait.until(EC.visibility_of_element_located((RegistryPage.REGISTER_BUTTON_LOCATOR)))
        assert register_button.is_displayed(), "Кнопка регистрации не отображается"




