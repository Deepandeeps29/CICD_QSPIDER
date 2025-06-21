import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_form_submission():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://demoapps.qspiders.com/ui?scenario=1")

    time.sleep(2)

    name_field = driver.find_element(By.ID, "name")
    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")

    name_field.send_keys("John Doe")
    email_field.send_keys("john@example.com")
    password_field.send_keys("john@example.com")
    submit_btn.click()

    time.sleep(2)

    # Example: capture success or validation text
    # success_msg = driver.find_element(By.ID, "successMessage")
    # assert "successfully" in success_msg.text.lower()

    driver.quit()
