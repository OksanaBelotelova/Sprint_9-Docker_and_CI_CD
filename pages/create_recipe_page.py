from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage
from data import TestData
from app_dir import APP_DIR


class CreateRecipe(BasePage):
    PAGE_HEADER = [By. XPATH, './/h1[text()="Создание рецепта"]']
    RECIPE_NAME_INPUT = [By. XPATH, './/label[contains(@class, "styles_inputLabel")]/div[text() ="Название рецепта"]/following-sibling::input']
    INGREDIENTS_FIELD = [By. XPATH, './/input[contains(@class, "styles_ingredientsInput")]']
    INGREDIENTS_DROPDOWN= [By. XPATH, './/div[contains(@class,"styles_ingredientsInputs")]/div[contains(@class,"styles_container")]']
    ADD_INGREDIENT = [By. XPATH,'.//div[text()= "Добавить ингредиент"]']
    INGREDIENT = [By. XPATH,'.//div[contains(@class, "styles_ingredientsInputs")]/div[last()]/div[1]']
    WEIGHT_FIELD = [By. XPATH,'.//input[contains(@class,"styles_ingredientsAmountValue")]']
    TIME_FIELD = [By. XPATH,'.//label[contains(@class,"styles_inputLabel")]/div[text() ="Время приготовления"]/following-sibling::input']
    DESCRIPTION_FIELD = [By. XPATH, './/label[contains(@class,"styles_textareaLabel")]/textarea']
    SELECT_FILE = [By. XPATH, './/input[@type = "file"]']
    SUBMIT_RECIPE_BUTTON = [By. XPATH, './/button[text() = "Создать рецепт"]']
    FILE_UPLOAD = str(APP_DIR / 'assets' / 'toast.jpeg')
    
    
    def __init__(self, driver):
        super().__init__(driver)
    

    @allure.step('Введи название рецепта')
    def input_recipe_name(self):
        self.wait_until_visible(self.PAGE_HEADER)
        self.find_element(self.RECIPE_NAME_INPUT).send_keys(TestData.recipe_name)

    @allure.step('Добавь ингрeдиент')
    def add_ingredient(self):
        for key, value in TestData.ingredients.items():
            self.find_element(self.INGREDIENTS_FIELD).send_keys(key)
            self.wait_until_visible(self.INGREDIENTS_DROPDOWN)
            self.find_element(self.INGREDIENT).click()
            self.find_element(self.WEIGHT_FIELD).send_keys(value)
            self.find_element(self.ADD_INGREDIENT).click()
            
    @allure.step('Укажи время приготовления')
    def add_time(self):
        self.find_element(self.TIME_FIELD).send_keys(TestData.time)

    @allure.step('Добавь описание рецепта')
    def add_recipe_description(self):
        self.find_element(self.DESCRIPTION_FIELD).send_keys(TestData.description)

    @allure.step('Добавь изображение')
    def add_image(self):
        file_input = self.find_element(self.SELECT_FILE)
        file_input.send_keys(self.FILE_UPLOAD)

    @allure.step('Нажми на "Создать рецепт"')
    def submit_recipe(self):
        self.find_element(self.SUBMIT_RECIPE_BUTTON).click()

    


    
    
