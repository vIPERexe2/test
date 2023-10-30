# Importing the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Setting up the Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Setting up the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# Opening the Gmail signup page
driver.get("https://accounts.google.com/signup")

# Filling in the required information
first_name = driver.find_element_by_id("firstName")
first_name.send_keys("John")

last_name = driver.find_element_by_id("lastName")
last_name.send_keys("Doe")

username = driver.find_element_by_id("username")
username.send_keys("johndoe123")

password = driver.find_element_by_name("Passwd")
password.send_keys("password123")

confirm_password = driver.find_element_by_name("ConfirmPasswd")
confirm_password.send_keys("password123")

# Submitting the form
submit_button = driver.find_element_by_id("accountDetailsNext")
submit_button.click()

# Closing the browser
driver.quit()
