from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from locators import RegistryPage
from locators import LoginPage
from locators import MainPage
from locators import RestorePasswordPage

from constants import Constants

fake = Faker()

class TestLogin:

    def test_auth_by_account_btn(self, driver):
        wait = WebDriverWait(driver, 10)

        driver.find_element(*MainPage.ENTER_ACCOUNT_LOCATOR).click()

        driver.find_element(*LoginPage.EMAIL_LOCATOR).send_keys(Constants.EMAIL)
        driver.find_element(*LoginPage.PASSWORD_LOCATOR).send_keys(Constants.PASSWORD)

        driver.find_element(*LoginPage.LOGIN_BUTTON_LOCATOR).click()

        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        personal_account = wait.until(EC.visibility_of_element_located(MainPage.PERSONAL_ACC_LOCATOR))
        assert personal_account.is_displayed(), "Авторизация не удалась"



    def test_auth_by_personal_account_btn(self, login):
        driver = login
        wait = WebDriverWait(driver, 10)

        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        personal_account = wait.until(EC.visibility_of_element_located(MainPage.PERSONAL_ACC_LOCATOR))
        assert personal_account.is_displayed(), "Авторизация не удалась"





    def test_auth_by_registry_enter_btn(self, driver):
        wait = WebDriverWait(driver, 10)

        driver.find_element(*MainPage.ENTER_ACCOUNT_LOCATOR).click()
        wait.until(EC.element_to_be_clickable(*LoginPage.REGISTER_LOCATOR)).click()

        driver.find_element(*RegistryPage.ENTER_BTN_LOCATOR).click()

        driver.find_element(*LoginPage.EMAIL_LOCATOR).send_keys(Constants.EMAIL)
        driver.find_element(*LoginPage.PASSWORD_LOCATOR).send_keys(Constants.PASSWORD)

        driver.find_element(*LoginPage.LOGIN_BUTTON_LOCATOR).click()

        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        personal_account = wait.until(EC.visibility_of_element_located(MainPage.PERSONAL_ACC_LOCATOR))
        assert personal_account.is_displayed(), "Авторизация не удалась"


    def test_auth_by_registry_enter_btn(self, driver):
        wait = WebDriverWait(driver, 10)

        driver.find_element(*MainPage.ENTER_ACCOUNT_LOCATOR).click()
        wait.until(EC.element_to_be_clickable(LoginPage.RESTORE_PASSWORD_LOCATOR)).click()

        wait.until(EC.element_to_be_clickable(RestorePasswordPage.ENTER_BTN_LOCATOR)).click()

        driver.find_element(*LoginPage.EMAIL_LOCATOR).send_keys(Constants.EMAIL)
        driver.find_element(*LoginPage.PASSWORD_LOCATOR).send_keys(Constants.PASSWORD)

        driver.find_element(*LoginPage.LOGIN_BUTTON_LOCATOR).click()

        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        personal_account = wait.until(EC.visibility_of_element_located(MainPage.PERSONAL_ACC_LOCATOR))
        assert personal_account.is_displayed(), "Авторизация не удалась"