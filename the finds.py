# Importing the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def fill_signup_form(first_name, last_name, username, password):
    # Setting up the Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode

    # Setting up the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    # Opening the Gmail signup page
    driver.get("https://accounts.google.com/signup")

    # Filling in the required information
    first_name_input = driver.find_element_by_id("firstName")
    first_name_input.send_keys(first_name)

    last_name_input = driver.find_element_by_id("lastName")
    last_name_input.send_keys(last_name)

    username_input = driver.find_element_by_id("username")
    username_input.send_keys(username)

    password_input = driver.find_element_by_name("Passwd")
    password_input.send_keys(password)

    confirm_password_input = driver.find_element_by_name("ConfirmPasswd")
    confirm_password_input.send_keys(password)

    # Submitting the form
    submit_button = driver.find_element_by_id("accountDetailsNext")
    submit_button.click()

    # Closing the browser
    driver.quit()

# Example usage
fill_signup_form("John", "Doe", "johndoe123", "password123")
