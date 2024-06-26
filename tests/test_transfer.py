from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from locators import MainPage
from locators import PersonalAccountPage

from constants import Constants

fake = Faker()

class TestTransfer:

    def test_transfer_into_personal_account(self, login):
        driver = login
        wait = WebDriverWait(driver, 10)

        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        driver.find_element(*MainPage.PERSONAL_ACC_LOCATOR).click()

        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))

        exit_btn = wait.until(EC.visibility_of_element_located(PersonalAccountPage.EXIT_BTN_LOCATOR))
        assert exit_btn.is_displayed(), "Переход в Личный кабинет не удался"




    def test_transfer_from_personal_account_to_constructor(self, login):
        driver = login
        wait = WebDriverWait(driver, 10)

        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        driver.find_element(*MainPage.PERSONAL_ACC_LOCATOR).click()

        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))

        driver.find_element(*MainPage.CONSTRUCTOR_LOCATOR).click()

        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        order_btn = wait.until(EC.visibility_of_element_located(MainPage.PLACE_ORDER_LOCATOR))
        assert order_btn.is_displayed(), "Переход на страницу Конструктор не удался"



    def test_transfer_from_personal_account_to_main_logo(self, login):
        driver = login
        wait = WebDriverWait(driver, 10)


        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        driver.find_element(*MainPage.PERSONAL_ACC_LOCATOR).click()

        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))

        driver.find_element(By.XPATH, '//header/nav[1]/div[1]/a[1]/*[1]').click()

        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        order_btn = wait.until(EC.visibility_of_element_located(MainPage.PLACE_ORDER_LOCATOR))
        assert order_btn.is_displayed(), "Авторизация после регистрации не удалась"

