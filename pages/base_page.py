from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from data import TestData

class BasePage:

    LOGOUT = [By. XPATH, './/div[contains(@class, "styles_menu")]/a[text()="Выход"]']
    RECIPES_TAB = [By. XPATH, './/div[contains(@class,"style_nav__container")]/ul/li[1]/a[text() = "Рецепты"]']
    CREATE_RECIPE = [By. XPATH, './/div[contains(@class,"style_nav__container")]/ul/li[3]/a']     
    CARD_OF_RECIPE = [By. XPATH, './/div[contains(@class, "style_cardList")]/div[1]div[contains(@class, "style_card__body")]/a[text() = "{}"]']
    TITLE_OF_RECIPE_CARD =  [By. XPATH, './/div[contains(@class, "style_cardList")]/div[1]/div[contains(@class, "style_card__body")]/a[contains(@class,"style_card__title")]']
    TITLE_OF_RECIPES_TAB = [By. XPATH, './/h1[text() = "Рецепты"]']
    TITLE_OF_RECIPE_PAGE = [By. XPATH, './/h1[contains(@class, "styles_single-card__title")]']
    

    def __init__(self, driver):
        self.driver = driver

    
    def find_element(self, element):
        return self.driver.find_element(*element)
    
    def wait_until_clickable(self, element, time = 20):
        WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(element))

    def wait_until_visible(self, element, time = 20):
        WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(element))
    
    @allure.step('Проверь URL')
    def get_current_page(self):
        return self.driver.current_url
    
    @allure.step('Нажми на вкладку "Создать рецепт"')
    def click_create_recipe(self):
        self.wait_until_clickable(self.CREATE_RECIPE)
        self.find_element(self.CREATE_RECIPE).click()

    @allure.step('Нажми на вкладку "Рецепты"')
    def click_recipe_tab(self):
        self.wait_until_clickable(self.TITLE_OF_RECIPE_PAGE)
        self.find_element(self.RECIPES_TAB).click()

    @allure.step('Проверь название рецепта')
    def check_recipe_name(self):
        self.wait_until_visible(self.TITLE_OF_RECIPE_CARD)
        return self.find_element(self.TITLE_OF_RECIPE_CARD).text

    @allure.step('Проверь карточку рецепта')
    def check_recipe_card(self):
        card_of_recipe = str(self.CARD_OF_RECIPE).format(TestData.recipe_name)
        return card_of_recipe

