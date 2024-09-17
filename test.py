import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import re

options = Options()
# options.add_argument("--no-sandbox")  # Bypass OS security model
# options.add_argument("--headless")  # Runs Chrome in headless mode.
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--disable-gpu")  # applicable to windows os only
# options.add_argument("start-maximized")  #
# options.add_argument("disable-infobars")
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--log-level=3")

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)
driver.get("http://localhost/wppool/wp-admin/")