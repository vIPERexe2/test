from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

try:
    # Set up the webdriver
    driver = webdriver.Chrome()

    # Open the Gmail signup page
    driver.get("https://accounts.google.com/signup")

    # Fill in the required information
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

    # Submit the form
    confirm_password.send_keys(Keys.RETURN)

except NoSuchElementException as e:
    print("Element not found:", e)

finally:
    # Close the webdriver
    driver.quit()
