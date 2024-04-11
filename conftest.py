import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
@pytest.fixture()
def driver():
    chrome_options = Options()
    page = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield page
    page.quit()
