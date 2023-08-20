import pytest
from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

path_picture = os.path.abspath(os.path.join(os.path.dirname(__file__), '../resources'))

@pytest.fixture()
def browser_management():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="114.0.5735.90").install()))
    browser.config.driver = driver


@pytest.fixture()
def browser_open(browser_management):
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'
