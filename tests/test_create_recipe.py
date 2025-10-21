import allure
from pages.create_recipe_page import CreateRecipe
from pages.login_page import LoginPage
from data import TestData


class TestCreateRecipe:

    @allure.title("Создание рецепта")
    @allure.description("После создания рецепта, отображается карточка созданного рецепта с названием, которое заполняли при создании")
    def test_create_recipe(self, driver):
        login =LoginPage(driver)
        recipe = CreateRecipe(driver)

        login.submit_login_form()
        recipe.click_create_recipe()
        recipe.input_recipe_name()
        #recipe.select_checkbox_dinner()
        recipe.add_ingredient()
        recipe.add_time()
        recipe.add_recipe_description()
        recipe.add_image()
        recipe.submit_recipe()
        recipe.click_recipe_tab()
        
        card_of_recipe = recipe.check_recipe_card()
        current_recipe_name = recipe.check_recipe_name()
        expected_recipe_name = TestData.recipe_name

        assert card_of_recipe
        assert current_recipe_name == expected_recipe_name
