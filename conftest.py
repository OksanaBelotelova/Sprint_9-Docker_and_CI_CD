import pytest
from selenium import webdriver
from data import URL


@pytest.fixture
def driver():
    url = URL().test_url
    driver = webdriver.Chrome()
    driver.get(url)
    yield driver
    driver.quit()