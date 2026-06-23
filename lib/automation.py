from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


# Launch Chrome Browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)
# Maximize Browser
driver.maximize_window()

# Open URL
driver.get("https://networkmangement.netlify.app/app.html#dashboard")

# Wait for page to load
time.sleep(2)

# Enter Username
driver.find_element(By.XPATH, "//input[@placeholder='Enter username']").send_keys("admin")

# Enter Password
driver.find_element(By.XPATH, "//input[@placeholder='Enter password']").send_keys("admin123")

# Click Login Button
driver.find_element(By.XPATH, "//button[text()='Login']").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Software Update").click()

# Wait to see result
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def upload_image(self, file_path):
    self.driver.find_element(*self.FILE_UPLOAD).send_keys(file_path)
time.sleep(10)

driver.find_element(By.XPATH, "//button[text()='Next']").click()
time.sleep(5)

wait = WebDriverWait(driver, 30)

element = wait.until(
    EC.element_to_be_clickable((By.ID, "selectAllDevices"))
)

print("Element found")
element.click()

time.sleep(5)
wait.until(
    EC.element_to_be_clickable((By.ID, "nextStep2"))
).click()

driver.find_element(By.ID,"jobName").send_keys("venkat_router")

driver.find_element(By.ID,"runNow").click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID,"startJob"))
).click()


time.sleep(5)
driver.close()