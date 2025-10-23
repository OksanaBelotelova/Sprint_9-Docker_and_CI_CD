import pytest
from selenium import webdriver
from data import URL


def pytest_addoption(parser):
    parser.addoption(
        "--selenoid-uri", action="store", default="http://localhost:4444", help="Selenoid url"
    )


def get_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless=new")
    return options


@pytest.fixture
def driver(request):
    url = URL().test_url

    # TODO selenoid-uri
    selenoid_uri = request.config.getoption("--selenoid-uri")
    driver = webdriver.Remote(
        command_executor=f'{selenoid_uri}/wd/hub', options=get_chrome_options())
    driver.get(url)
    yield driver
    driver.quit()
