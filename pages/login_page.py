from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage
from helpers import RandomUserData
from data import TestData


class LoginPage(BasePage):
    CREATE_ACCOUNT = [By. XPATH, './/div[contains(@class,"styles_menu")]/a[text()="Создать аккаунт"]']
    NAME_FIELD = [By. XPATH,'.//input[@name = "first_name"]']
    LAST_NAME_FIELD = [By. XPATH,'.//input[@name = "last_name"]']
    USERNAME_FIELD = [By. XPATH,'.//input[@name = "username"]']
    EMAIL_ADDRESS_FIELD = [By. XPATH,'.//input[@name = "email"]']
    PASSWORD_FIELD = [By. XPATH,'.//input[@name = "password"]']
    SUBMIT_ACCOUNT = [By. XPATH, './/button[text() = "Создать аккаунт"]']
    LOGIN_FORM = [By. XPATH, './/form[contains(@class, "styles_form")]'] 
    INPUT_EMAIl = [By. XPATH,'.//input[@name = "last_name"]']
    SUBMIT_LOGIN = [By. XPATH, './/button[contains(@class,"style_button")]']
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажми на ""Создать аккаунт')
    def click_create_account(self):
        self.wait_until_clickable(self.CREATE_ACCOUNT)
        self.find_element(self.CREATE_ACCOUNT).click()

    @allure.step('Введи имя')
    def input_name(self):
        self.find_element(self.NAME_FIELD).send_keys(RandomUserData.random_string(self, 7))

    @allure.step('Введи фамилию')
    def input_last_name(self):
        self.find_element(self.LAST_NAME_FIELD).send_keys(RandomUserData.random_string(self, 10))

    @allure.step('Введи имя пользователя')
    def input_username(self):
        self.find_element(self.USERNAME_FIELD).send_keys(RandomUserData.random_string(self, 7))

    @allure.step('Введи имя пользователя')
    def input_email_address(self):
        self.find_element(self.EMAIL_ADDRESS_FIELD).send_keys(RandomUserData.generate_email(self))

    @allure.step('Введи пароль')
    def input_password(self):
        self.find_element(self.PASSWORD_FIELD).send_keys(RandomUserData.random_string(self, 10))

    @allure.step('Нажми "Создать аккаунт"')
    def submit_account_form(self):
        self.find_element(self.SUBMIT_ACCOUNT).click()

    @allure.step('Подожди пока загрузится страница')
    def wait_until_page_loaded(self):
        self.wait_until_clickable(self.SUBMIT_LOGIN, time=50)

    @allure.step('Проверь форму авторизации')
    def check_login_form(self):
        self.wait_until_visible(self.LOGIN_FORM)
        return self.find_element(self.LOGIN_FORM)
    
    @allure.step('заполни форму аторизации')
    def submit_login_form(self):
        self.find_element(self.EMAIL_ADDRESS_FIELD).send_keys(TestData.username)
        self.find_element(self.PASSWORD_FIELD).send_keys(TestData.password)
        self.find_element(self.SUBMIT_LOGIN).click()

    @allure.step('Проверь кнопку "Выход"')
    def check_logout_button(self):
        self.wait_until_clickable(self.LOGOUT)
        return self.find_element(self.LOGOUT)