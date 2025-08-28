import os
import allure
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
    allure.attach(
        driver.get_screenshot_as_png(),
        name="Google Home Screenshot",
        attachment_type=allure.attachment_type.PNG
    )
    assert "Google" in driver.title
    driver.quit()

# add 5 more tests as per above pattern for google

def test_google_search_box():
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor=SELENIUM_GRID_URL,
        options=options
    )
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    assert search_box is not None
    allure.attach(
        driver.get_screenshot_as_png(),
        name="Google Search Box Screenshot",
        attachment_type=allure.attachment_type.PNG
    )
    driver.quit()

def test_google_search_functionality():
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor=SELENIUM_GRID_URL,
        options=options
    )
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("OpenAI")
    search_box.submit()
    assert "OpenAI" in driver.title
    allure.attach(
        driver.get_screenshot_as_png(),
        name="Google Search Functionality Screenshot",
        attachment_type=allure.attachment_type.PNG
    )
    driver.quit()

def test_google_images_link():
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor=SELENIUM_GRID_URL,
        options=options
    )
    driver.get("https://www.google.com")
    images_link = driver.find_element(By.LINK_TEXT, "Images")
    assert images_link is not None
    allure.attach(
        driver.get_screenshot_as_png(),
        name="Google Images Link Screenshot",
        attachment_type=allure.attachment_type.PNG
    )
    driver.quit()

def test_google_privacy_link():
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor=SELENIUM_GRID_URL,
        options=options
    )
    driver.get("https://www.google.com")
    privacy_link = driver.find_element(By.LINK_TEXT, "Privacy")
    assert privacy_link is not None
    allure.attach(
        driver.get_screenshot_as_png(),
        name="Google Privacy Link Screenshot",
        attachment_type=allure.attachment_type.PNG
    )
    driver.quit()

def test_google_terms_link():
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor=SELENIUM_GRID_URL,
        options=options
    )
    driver.get("https://www.google.com")
    terms_link = driver.find_element(By.LINK_TEXT, "Terms")
    assert terms_link is not None
    allure.attach(
        driver.get_screenshot_as_png(),
        name="Google Terms Link Screenshot",
        attachment_type=allure.attachment_type.PNG
    )
    driver.quit()
    
def test_google_about_link():
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor=SELENIUM_GRID_URL,
        options=options
    )
    driver.get("https://www.google.com")
    about_link = driver.find_element(By.LINK_TEXT, "About")
    assert about_link is not None
    allure.attach(
        driver.get_screenshot_as_png(),
        name="Google About Link Screenshot",
        attachment_type=allure.attachment_type.PNG
    )
    driver.quit()
