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

    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# 1. Open Google homepage
def test_google_homepage_title(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title

# 2. Search for a keyword
def test_google_search_keyword(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Grid")
    search_box.send_keys(Keys.RETURN)
    assert "Selenium Grid" in driver.page_source or "Selenium Grid" in driver.title

# 3. Check Google logo visibility
def test_google_logo_displayed(driver):
    driver.get("https://www.google.com")
    logo = driver.find_element(By.ID, "hplogo")  # may vary by region
    assert logo.is_displayed()

# 4. Search suggestions appear
def test_google_search_suggestions(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Python")
    suggestions = driver.find_elements(By.CSS_SELECTOR, "ul[role='listbox'] li")
    assert len(suggestions) > 0

# 5. Navigate to Images tab
def test_google_images_tab(driver):
    driver.get("https://www.google.com")
    images_link = driver.find_element(By.LINK_TEXT, "Images")
    images_link.click()
    assert "images" in driver.current_url

# 6. Navigate to Gmail
def test_google_gmail_link(driver):
    driver.get("https://www.google.com")
    gmail_link = driver.find_element(By.LINK_TEXT, "Gmail")
    gmail_link.click()
    assert "mail.google.com" in driver.current_url or "Gmail" in driver.title

# 7. Check footer text presence
def test_google_footer_text(driver):
    driver.get("https://www.google.com")
    footer = driver.find_element(By.ID, "fsl")
    assert footer.is_displayed()
