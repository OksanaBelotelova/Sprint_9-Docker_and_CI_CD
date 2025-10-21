from pages.login_page import LoginPage
from data import URL
import allure


class TestLoginPage:

    @allure.title("Создание аккаунта")
    @allure.description("После заполнения формы юзер переходит на страницу авторизации")
    def test_create_account(self, driver):
        login = LoginPage(driver)

        login.click_create_account()
        login.input_name()
        login.input_last_name()
        login.input_username()
        login.input_email_address()
        login.input_password()
        login.submit_account_form()
        login.wait_until_page_loaded()

        login_form = login.check_login_form()
        expected_page = URL.login_page_url
        current_page = login.get_current_page()
        
        
        assert login_form.is_displayed()
        assert current_page == expected_page

    
    @allure.title("Авторизация")
    @allure.description("После заполнения формы авторизации и нажатия кнопки 'Войти' юзер перходит на главную страницу")    
    def test_user_login(self, driver):
        login = LoginPage(driver)

        login.submit_login_form()
        
        logout_button = login.check_logout_button()
        current_page = login.get_current_page()
        expected_page = URL.home_page_url
       

        assert current_page == expected_page
        assert logout_button.is_displayed()

