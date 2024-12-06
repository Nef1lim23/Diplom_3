import pytest
from selenium import webdriver

from data import URLs


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
    else:
        driver = webdriver.Firefox()
    driver.get(URLs.BASE_URL)
    yield driver
    driver.quit()