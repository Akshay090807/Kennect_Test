from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

service_obj = Service()
driver = webdriver.Chrome()
driver.get("https://gor-pathology.web.app/")
driver.implicitly_wait(10)
driver.maximize_window()
# Enter Login details
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("test@kennect.io")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Qwerty@1234")
driver.find_element(By.CSS_SELECTOR, "button[type='submit'] span[class='MuiButton-label']").click()
# Enter data in Cost Calculator for blood test
driver.find_element(By.XPATH, "//input[@id='patient-test']").send_keys("VITAMIN B12, SERUM")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "VITAMIN B12, SERUM")))

