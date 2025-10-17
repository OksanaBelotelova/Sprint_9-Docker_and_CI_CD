from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage


class LoginPage(BasePage):
    CREATE_ACCOUNT = [By. XPATH, './/а[text() = "Создать аккаунт"]']
    NAME_FIELD = [By. XPATH,'.//input[@name = "first_name"]']
    LAST_NAME_FIELD = [By. XPATH,'.//input[@name = "last_name"]']
    USERNAME_FIELD = [By. XPATH,'.//input[@name = "username"]']
    EMAIL_ADDRESS_FIELD = [By. XPATH,'.//input[@name = "email"]']
    PASSWORD_FIELD = [By. XPATH,'.//input[@name = "password"]']
    SUBMIT_ACCOUNT = [By. XPATH, './/button[text() = "Создать аккаунт"]']
    LOGIN_FORM = [By. XPATH, './/form[@class = "styles_form"]']
    INPUT_EMAIl = [By. XPATH,'.//input[@name = "last_name"]']
    SUBMIT_LOGIN = [By. XPATH, './/button[text() = "Войти"]']
    
    def __init__(self, driver):
        super().__init__(driver)