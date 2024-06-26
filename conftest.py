import pytest
from selenium import webdriver
from constants import Constants
from locators import MainPage, LoginPage


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(Constants.URL)
    browser.maximize_window()
    yield browser
    
    browser.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*MainPage.PERSONAL_ACC_LOCATOR).click()
    driver.find_element(*LoginPage.EMAIL_LOCATOR).send_keys(Constants.EMAIL)
    driver.find_element(*LoginPage.PASSWORD_LOCATOR).send_keys(Constants.PASSWORD)
    driver.find_element(*LoginPage.LOGIN_BUTTON_LOCATOR).click()
    return driver


