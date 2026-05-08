from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open website
driver.get("https://practicetestautomation.com/practice-test-login/")

# Maximize browser
driver.maximize_window()

# Enter correct username
driver.find_element(By.ID, "username").send_keys("student")

# Enter correct password
driver.find_element(By.ID, "password").send_keys("wrongpassword")

# Click login
driver.find_element(By.ID, "submit").click()

# Wait for page load
time.sleep(3)

# Validate successful login
current_url = driver.current_url

if "logged-in-successfully" in current_url:
    print("TEST PASSED ✅")
else:
    print("TEST FAILED ❌")
    driver.save_screenshot("validation_failure.png")

# Wait before closing
time.sleep(3)

# Close browser
driver.quit()