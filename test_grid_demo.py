import os
from selenium import webdriver
from selenium.webdriver.common.by import By

SELENIUM_GRID_URL = os.getenv("SELENIUM_GRID_URL", "http://selenium-hub:4444/wd/hub")

def test_google_title():
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor=SELENIUM_GRID_URL,
        options=options
    )
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()