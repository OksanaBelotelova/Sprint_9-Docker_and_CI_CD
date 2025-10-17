from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage


class CreateRecipe(BasePage):

    RECIPE_NAME = [By. XPATH, './/input[@class = "styles_inputField"]']