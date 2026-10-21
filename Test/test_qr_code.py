#pytest Test/ -v

import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--use-fake-ui-for-media-stream")

    if os.environ.get("CI") == "true":
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=chrome_options)
    browser.get("http://localhost:8000")
    browser.maximize_window()
    try:
        yield browser
    finally:
        browser.quit()

#=============================================================================
# Manual testing
#=============================================================================

#STQC-6 --Valid QR test
@pytest.mark.manual
def test_valid_qr_camera(driver):
    scanner_button = driver.find_element(By.ID, "button")
    assert scanner_button.is_displayed()
    scanner_button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "video"))
    )

    result_is_visible = WebDriverWait(driver, 60).until(
        lambda browser: (
            browser.find_element(By.ID, "resultText").is_displayed()
            or browser.find_element(By.ID, "resultLink").is_displayed()
        )
    )
    assert result_is_visible


#STQC‑7 Invalid QR test
@pytest.mark.manual
def test_invalid_qr_camera(driver):
    scanner_button = driver.find_element(By.ID, "button")
    assert scanner_button.is_displayed()
    scanner_button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "video"))
    )

    input(
        "Hold a non-QR or unreadable image in front of the camera for a few seconds, "
        "then press Enter here."
    )

    assert not driver.find_element(By.ID, "resultText").is_displayed()
    assert not driver.find_element(By.ID, "resultLink").is_displayed()
    assert driver.find_element(By.ID, "resultPlaceholder").is_displayed()



#STQC‑8 Empty request QR test
@pytest.mark.manual
def test_empty_qr_camera(driver):
    scanner_button = driver.find_element(By.ID, "button")
    assert scanner_button.is_displayed()
    scanner_button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "video"))
    )

    input(
        "Show a blank sheet or cover the camera for a few seconds, "
        "then press Enter here."
    )

    assert not driver.find_element(By.ID, "resultText").is_displayed()
    assert not driver.find_element(By.ID, "resultLink").is_displayed()
    assert driver.find_element(By.ID, "resultPlaceholder").is_displayed()


#=============================================================================
#Automated UI & State assertions for QR Code Scanner
#=============================================================================
#STQC‑9 UI validation
def test_ui_validation(driver):

    # Check page title
    assert "QR Code Scanner" in driver.title, "Page title does not match"

    # Check scanner button
    scanner_button = driver.find_element(By.ID, "button")
    assert scanner_button.is_displayed(), "Scanner button is not displayed"
    assert scanner_button.is_enabled(), "Scanner button is not enabled"

    # Check video element
    video_feed = driver.find_element(By.ID, "video")
    assert video_feed is not None, "Video feed element is not present"

    # Check result box elements
    result_placeholder = driver.find_element(By.ID, "resultPlaceholder")
    assert result_placeholder.text == "No result yet"
    result_text = driver.find_element(By.ID, "resultText")
    result_link = driver.find_element(By.ID, "resultLink")
    assert result_placeholder is not None, "Result placeholder element is not present"
    assert result_placeholder.is_displayed(), "Result placeholder is not displayed"
    assert result_text is not None
    assert not result_text.is_displayed()
    assert result_link is not None
    assert not result_link.is_displayed()

    # Check status message element
    status_box = driver.find_element(By.ID, "status")
    assert status_box is not None, "Status message element is not present"  
