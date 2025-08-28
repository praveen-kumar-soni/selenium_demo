
import os
import pytest
from selenium import webdriver
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Selenium Grid URL
SELENIUM_GRID_URL = os.getenv("SELENIUM_GRID_URL", "http://selenium-hub:4444/wd/hub")
BROWSERS = ["firefox"]

@pytest.fixture(params=BROWSERS)
def driver(request):
    browser = request.param

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL, options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(30)
    yield driver
    driver.quit()

def test_google_title(driver):
    driver.get("https://www.google.com")
    allure.attach(driver.get_screenshot_as_png(), name="Google Home Screenshot", attachment_type=allure.attachment_type.PNG)
    assert "Google" in driver.title

def test_google_search_box(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    assert search_box is not None
    allure.attach(driver.get_screenshot_as_png(), name="Google Search Box Screenshot", attachment_type=allure.attachment_type.PNG)

def test_google_search_functionality(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("OpenAI")
    search_box.submit()
    assert "OpenAI" in driver.title
    allure.attach(driver.get_screenshot_as_png(), name="Google Search Functionality Screenshot", attachment_type=allure.attachment_type.PNG)

def test_google_images_link(driver):
    driver.get("https://www.google.com")
    images_link = driver.find_element(By.LINK_TEXT, "Images")
    assert images_link is not None
    allure.attach(driver.get_screenshot_as_png(), name="Google Images Link Screenshot", attachment_type=allure.attachment_type.PNG)

def test_google_privacy_link(driver):
    driver.get("https://www.google.com")
    privacy_link = driver.find_element(By.LINK_TEXT, "Privacy")
    assert privacy_link is not None
    allure.attach(driver.get_screenshot_as_png(), name="Google Privacy Link Screenshot", attachment_type=allure.attachment_type.PNG)

def test_google_terms_link(driver):
    driver.get("https://www.google.com")
    terms_link = driver.find_element(By.LINK_TEXT, "Terms")
    assert terms_link is not None
    allure.attach(driver.get_screenshot_as_png(), name="Google Terms Link Screenshot", attachment_type=allure.attachment_type.PNG)

def test_google_about_link(driver):
    driver.get("https://www.google.com")
    about_link = driver.find_element(By.LINK_TEXT, "About")
    assert about_link is not None
    allure.attach(driver.get_screenshot_as_png(), name="Google About Link Screenshot", attachment_type=allure.attachment_type.PNG)