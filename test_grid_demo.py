import os
import pytest
from selenium import webdriver
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

# Helper to attach screenshot
def attach_screenshot(driver, name="screenshot"):
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)

# 1. Open Google homepage
@allure.feature("Google Homepage")
@allure.story("Check title")
def test_google_homepage_title(driver):
    with allure.step("Open Google"):
        driver.get("https://www.google.com")
        attach_screenshot(driver, "homepage")
    with allure.step("Verify title contains 'Google'"):
        assert "Google" in driver.title

# 2. Search for a keyword
@allure.feature("Google Search")
@allure.story("Search Selenium Grid")
def test_google_search_keyword(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    with allure.step("Enter search query 'Selenium Grid'"):
        search_box.send_keys("Selenium Grid")
        search_box.send_keys(Keys.RETURN)
        attach_screenshot(driver, "search_results")
    with allure.step("Verify search results contain 'Selenium Grid'"):
        assert "Selenium Grid" in driver.page_source or "Selenium Grid" in driver.title

# 3. Check Google logo visibility
@allure.feature("Google Homepage")
@allure.story("Check logo")
def test_google_logo_displayed(driver):
    driver.get("https://www.google.com")
    logo = driver.find_element(By.ID, "hplogo")
    with allure.step("Verify Google logo is displayed"):
        attach_screenshot(driver, "logo_display")
        assert logo.is_displayed()

# 4. Search suggestions appear
@allure.feature("Google Search")
@allure.story("Check suggestions")
def test_google_search_suggestions(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Python")
    suggestions = driver.find_elements(By.CSS_SELECTOR, "ul[role='listbox'] li")
    with allure.step("Verify search suggestions appear"):
        attach_screenshot(driver, "search_suggestions")
        assert len(suggestions) > 0

# 5. Navigate to Images tab
@allure.feature("Google Navigation")
@allure.story("Images tab")
def test_google_images_tab(driver):
    driver.get("https://www.google.com")
    images_link = driver.find_element(By.LINK_TEXT, "Images")
    images_link.click()
    with allure.step("Verify Images tab URL"):
        attach_screenshot(driver, "images_tab")
        assert "images" in driver.current_url

# 6. Navigate to Gmail
@allure.feature("Google Navigation")
@allure.story("Gmail link")
def test_google_gmail_link(driver):
    driver.get("https://www.google.com")
    gmail_link = driver.find_element(By.LINK_TEXT, "Gmail")
    gmail_link.click()
    with allure.step("Verify Gmail page opened"):
        attach_screenshot(driver, "gmail_page")
        assert "mail.google.com" in driver.current_url or "Gmail" in driver.title

# 7. Check footer text presence
@allure.feature("Google Homepage")
@allure.story("Footer text")
def test_google_footer_text(driver):
    driver.get("https://www.google.com")
    footer = driver.find_element(By.ID, "fsl")
    with allure.step("Verify footer is displayed"):
        attach_screenshot(driver, "footer")
        assert footer.is_displayed()
