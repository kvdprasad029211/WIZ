from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome(executable_path="C:\\Users\\prasad\\Downloads\\Application\\chrome.exe")
    # driver.get('http://localhost:8000')
    return driver