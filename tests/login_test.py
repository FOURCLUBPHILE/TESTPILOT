from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time



from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Open test website
driver.get("https://practicetestautomation.com/practice-test-login/")

# Maximize browser
driver.maximize_window()

# Enter username
driver.find_element(By.ID, "username").send_keys("student")

# Enter password
driver.find_element(By.ID, "password").send_keys("Password123")

# Click login button
driver.find_element(By.ID, "submit").click()

# Wait 5 seconds
time.sleep(10)

# Print success message
print("Login Test Passed")

# Close browser
driver.quit()
