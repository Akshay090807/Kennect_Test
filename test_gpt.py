from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Firefox driver (you can use other drivers like Chrome as well)
service_obj = Service()
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Find the name field and enter a name
name_field = driver.find_element(By.CSS_SELECTOR, "[data-test='name']")
name_field.send_keys("John Doe")

# Find the gender radio button and select it
gender_radio = driver.find_element(By.ID, "exampleFormControlSelect1")
gender_radio.click()

# Find the submit button and click it
submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
submit_button.click()

# Verify that the success message is displayed
success_message = driver.find_element(By.CSS_SELECTOR, ".alert-success")
assert success_message.text == "Success! The Form has been submitted successfully!"

print("Test passed successfully!")

driver.quit()
