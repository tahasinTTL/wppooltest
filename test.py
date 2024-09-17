import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import re

options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)
# options.add_argument("--no-sandbox")  # Bypass OS security model
# options.add_argument("--headless")  # Runs Chrome in headless mode.
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--disable-gpu")  # applicable to windows os only
# options.add_argument("start-maximized")  #
# options.add_argument("disable-infobars")
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--log-level=3")

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
# driver.set_window_size(1920, 1080)
driver.get("http://localhost/wppool/wp-admin/")
# print(driver.title)
username = "Tahasin"
password = "aq0EIwLxib1XS%QfeR"

driver.find_element(By.ID, "user_login").send_keys(username)
driver.find_element(By.ID, "user_pass").send_keys(password)
driver.find_element(By.ID, "wp-submit").click()

print("logged in")
driver.get("http://localhost/wppool/wp-admin/plugins.php")
try:
    driver.find_element(By.ID, "activate-wp-dark-mode").click()
    print("activated")
except:
    print("not found activate")

driver.get("http://localhost/wppool/wp-admin/admin.php?page=wp-dark-mode#/admin")

try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.CLASS_NAME, "relative w-10 h-full rounded-full transition duration-100 bg-slate-200"))
    driver.find_element(By.CLASS_NAME, "relative w-10 h-full rounded-full transition duration-100 bg-slate-200").click()
    print("Enabled")
except:
    print("Not enabled")