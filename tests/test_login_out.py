from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from locators import LoginPage
from locators import MainPage
from locators import PersonalAccountPage

from constants import Constants

fake = Faker()

class TestLogin:

    def test_logging_out_by_personal_account(self, driver):
        wait = WebDriverWait(driver, 10)

        driver.find_element(*MainPage.ENTER_ACCOUNT_LOCATOR).click()

        driver.find_element(*LoginPage.EMAIL_LOCATOR).send_keys(Constants.EMAIL)
        driver.find_element(*LoginPage.PASSWORD_LOCATOR).send_keys(Constants.PASSWORD)

        driver.find_element(*LoginPage.LOGIN_BUTTON_LOCATOR).click()

        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        driver.find_element(*MainPage.PERSONAL_ACC_LOCATOR).click()

        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))

        driver.find_element(*PersonalAccountPage.EXIT_BTN_LOCATOR).click()

        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

        email_locator = wait.until(EC.visibility_of_element_located(LoginPage.EMAIL_LOCATOR))
        assert email_locator.is_displayed(), "Выход из аккаунта не удался"
