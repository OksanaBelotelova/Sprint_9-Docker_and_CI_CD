from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from data import TestData

class BasePage:

    LOGOUT = [By. XPATH, './/div[contains(@class, "styles_menu")]/a[text()="Выход"]']
    RECIPE = [By. XPATH, './/div[contains(@class,"style_nav__container")]/ul/li[1]/a']
    CREATE_RECIPE = [By. XPATH, './/div[contains(@class,"style_nav__container")]/ul/li[3]/a']     
    CARD_OF_RECIPE = [By. XPATH, './/div[contains(@class, "style_cardList")]/div[1]div[contains(@class, "style_card__body")]/a[text() = "{}"]']
    RECIPE_TITLE =  [By. XPATH, './/div[contains(@class, "style_cardList")]/div[1]/div[contains(@class, "style_card__body")]/a[contains(@class,"style_card__title")]']
    
    def __init__(self, driver):
        self.driver = driver

    
    def find_element(self, element):
        return self.driver.find_element(*element)
    
    def wait_until_clickable(self, element, time=10):
        WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(element))

    def wait_until_visible(self, element, time=10):
        WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(element))
    
    @allure.step('Проверь URL')
    def get_current_page(self):
        self.wait_until_clickable(self.RECIPE, 15)
        return self.driver.current_url
    
    @allure.step('Нажми на создать рецепт')
    def click_create_recipe(self):
        self.wait_until_clickable(self.CREATE_RECIPE)
        self.find_element(self.CREATE_RECIPE).click()

    @allure.step('Нажми на вкладку рецепты')
    def click_recipe_tab(self):
        self.find_element(self.RECIPE).click()

    @allure.step('Проверь название рецепта')
    def check_recipe_name(self):
        return self.find_element(self.RECIPE_TITLE).text

    @allure.step('Проверь карточку рецепта')
    def check_recipe_card(self):
        card_of_recipe = str(self.CARD_OF_RECIPE).format(TestData.recipe_name)
        return card_of_recipe

