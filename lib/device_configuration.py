from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Launch Browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()

# Open Application
driver.get("https://networkmangement.netlify.app/")

wait = WebDriverWait(driver, 20)

# ==========================
# Login
# ==========================

username = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Enter username']")
    )
)
username.send_keys("admin")

password = driver.find_element(
    By.XPATH,
    "//input[@placeholder='Enter password']"
)
password.send_keys("admin123")

login_btn = driver.find_element(
    By.XPATH,
    "//button[contains(text(),'Login')]"
)
login_btn.click()

print("Login Successful")

# ==========================
# Dashboard
# ==========================

device_config = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[contains(text(),'Device Config')]")
    )
)

driver.execute_script("arguments[0].click();", device_config)

print("Clicked Device Config")

# ==========================
# Configuration Details
# ==========================

config_name = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='e.g. set_hostname_core']")
    )
)

config_name.clear()
config_name.send_keys("set_hostname_core")

description = wait.until(
    EC.visibility_of_element_located(
        (By.TAG_NAME, "textarea")
    )
)

description.clear()
description.send_keys(
    "Hostname configuration for core router"
)

print("Configuration Details Entered")

# ==========================
# Next
# ==========================

# Scroll to bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(2)

# Find all Next buttons
next_buttons = driver.find_elements(
    By.XPATH,
    "//button[contains(.,'Next')]"
)

print("Next buttons found:", len(next_buttons))

# Click last visible Next button
driver.execute_script(
    "arguments[0].click();",
    next_buttons[-1]
)

print("Moved To Target Device")

print("Moved To Config Script")

driver.switch_to.default_content()

wait.until(
    EC.presence_of_element_located(
        (By.TAG_NAME, "body")
    )
)

time.sleep(2)

wait.until(
    EC.presence_of_element_located(
        (By.TAG_NAME, "body")
    )
)

print("Config Script Page Loaded")

time.sleep(3)

editors = driver.find_elements(
    By.CSS_SELECTOR,
    "[contenteditable='true']"
)

print("Editors Found =", len(editors))

for editor in editors:
    try:
        if editor.is_displayed():

            driver.execute_script(
                "arguments[0].click();",
                editor
            )

            editor.send_keys(Keys.END)
            editor.send_keys(Keys.ENTER)

            editor.send_keys(
                "hostname router-core-01"
            )

            print("Config Command Entered")
            break

    except Exception as e:
        print(e)

# Scroll to device name field

driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);"
)

time.sleep(2)

# Find all text inputs

inputs = driver.find_elements(By.TAG_NAME, "input")

for i in inputs:
    try:
        placeholder = i.get_attribute("placeholder")

        if placeholder and "router-core" in placeholder:

            i.clear()

            i.click()

            i.send_keys("router-core-01")

            print("Placeholder =", placeholder)
            print("Value =", i.get_attribute("value"))


            time.sleep(2)

            break

    except Exception as e:
        print(e)
        print("Entered value =", i.get_attribute("value"))

print("Device Name Entered")
print(driver.page_source)
# Click Next to move to Config Script
# ==========================
# CLICK NEXT
# ==========================

print("Device Name Entered")

buttons = driver.find_elements(By.TAG_NAME, "button")

for btn in buttons:
    try:
        if btn.text.strip() == "Next":
            driver.execute_script(
                "arguments[0].click();",
                btn
            )

            print("Moved To Config Script")
            break

    except Exception as e:
        print(e)
time.sleep(3)

print("Config Script Page Loaded")

# Just click Next on Config Script page
# Scroll to bottom first
driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);"
)

time.sleep(2)

buttons = driver.find_elements(By.TAG_NAME, "button")

print("Buttons Found =", len(buttons))

for btn in buttons:
    try:
        print("Button Text =", btn.text)

        if btn.text.strip() == "Next":

            driver.execute_script(
                "arguments[0].scrollIntoView(true);",
                btn
            )

            time.sleep(1)

            driver.execute_script(
                "arguments[0].click();",
                btn
            )

            print("Moved To Review")
            break

    except Exception as e:
        print(e)

print("Moved To Review")

# ==========================
# REVIEW PAGE
# ==========================

time.sleep(3)

print("Review Page Opened")
print(driver.current_url)
print(driver.page_source)

push_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Push')]")
    )
)

driver.execute_script(
    "arguments[0].click();",
    push_btn
)

print("Push Clicked")

ok_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'OK')]")
    )
)

driver.execute_script(
    "arguments[0].click();",
    ok_btn
)

print("OK Clicked")

jobs_tab = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[contains(text(),'Config Jobs')]")
    )
)

driver.execute_script(
    "arguments[0].click();",
    jobs_tab
)

print("Config Jobs Opened")

time.sleep(3)

rows = driver.find_elements(
    By.XPATH,
    "//table/tbody/tr"
)

print("Rows Found =", len(rows))

if len(rows) > 0:
    cols = rows[0].find_elements(By.TAG_NAME, "td")

    print("Job Name =", cols[0].text)
    print("Device =", cols[1].text)
    print("Status =", cols[2].text)
else:
    print("No Job Found")

driver.quit()