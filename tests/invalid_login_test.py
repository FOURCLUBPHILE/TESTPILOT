from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Maximize window
driver.maximize_window()

# Enter WRONG username
driver.find_element(By.ID, "username").send_keys("wronguser")

# Enter WRONG password
driver.find_element(By.ID, "password").send_keys("wrongpassword")

# Click login button
driver.find_element(By.ID, "submit").click()

# Wait for result
time.sleep(6)

# Capture screenshot
driver.save_screenshot("failed_login.png")

# Print message
print("Invalid Login Test Completed")
print("Screenshot Captured")

# Wait before closing
time.sleep(3)

# Close browser
driver.quit()