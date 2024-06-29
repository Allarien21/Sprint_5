import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from locators import LoginPage
from locators import MainPage

from constants import Constants

fake = Faker()

class TestLogin:

    def test_navigate_on_sections(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*MainPage.ENTER_ACCOUNT_LOCATOR).click()

        driver.find_element(*LoginPage.EMAIL_LOCATOR).send_keys(Constants.EMAIL)
        driver.find_element(*LoginPage.PASSWORD_LOCATOR).send_keys(Constants.PASSWORD)

        driver.find_element(*LoginPage.LOGIN_BUTTON_LOCATOR).click()

        wait.until(EC.url_to_be(Constants.URL))

        driver.find_element(*MainPage.SAUCES_LOCATOR).click()
        wait.until(EC.visibility_of_element_located(MainPage.SAUCES_SECTION_LOCATOR)).is_displayed()

        driver.find_element(*MainPage.TOPPING_LOCATOR).click()
        wait.until(EC.visibility_of_element_located(MainPage.TOPPING_SECTION_LOCATOR)).is_displayed()

        driver.find_element(*MainPage.BREAD_LOCATOR).click()
        wait.until(EC.visibility_of_element_located(MainPage.BREAD_SECTION_LOCATOR)).is_displayed()