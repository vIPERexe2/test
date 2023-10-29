import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Define the browser
chrome_driver_path = 'system/app/Chrome/Chrome.apk'  # Replace with the actual path to the Chrome driver
browser = webdriver.Chrome(executable_path=chrome_driver_path)

# Open the Google website
browser.get('https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp')

# Enter the desired number of email addresses
email_count = int(input("How many email addresses do you want to create? "))

for i in range(email_count):
    # Enter the first name
    first_name = browser.find_element_by_name('firstName')
    first_name.send_keys(''.join(random.choices(string.ascii_lowercase, k=5)))
    
    # Enter the last name
    last_name = browser.find_element_by_name('lastName')
    last_name.send_keys(''.join(random.choices(string.ascii_lowercase, k=5)))
    
    # Enter the username
    username = browser.find_element_by_name('Username')
    username.send_keys(''.join(random.choices(string.ascii_lowercase, k=5)))
    
    # Enter the password
    password = browser.find_element_by_name('Passwd')
    password.send_keys(''.join(random.choices(string.ascii_letters + string.digits, k=8)))
    
    # Confirm the password
    confirm_password = browser.find_element_by_name('ConfirmPasswd')
    confirm_password.send_keys(password.get_attribute('value'))
    
    # Click the "Next" button
    next_button = browser.find_element_by_xpath('//*[@id="accountDetailsNext"]/div/button/span')
    next_button.click()
    
    # Wait for 2 seconds
    time.sleep(2)
    
    # Click the "Verify phone number" button
    phone_button = browser.find_element_by_xpath('//*[@id="view_container"]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div/div/button/span')
    phone_button.click()
    
    # Wait for 2 seconds
    time.sleep(2)
    
    # Click the "Next" button
    next_button2 = browser.find_element_by_xpath('//*[@id="view_container"]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/button/span')
    next_button2.click()
    
    # Wait for 2 seconds
    time.sleep(2)
    
    # Click the "Next" button
    next_button3 = browser.find_element_by_xpath('//*[@id="view_container"]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/button/span')
    next_button3.click()
    
    # Wait for 2 seconds
    time.sleep(2)
    
    # Click the "Accept" button
    accept_button = browser.find_element_by_xpath('//*[@id="view_container"]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/button/span')
    accept_button.click()
    
    # Wait for 2 seconds
    time.sleep(2)
    
    # Click the "Next" button
    next_button4 = browser.find_element_by_xpath('//*[@id="view_container"]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/button/span')
    next_button4.click()
    
    # Wait for 2 seconds
    time.sleep(2)
    
    # Click the "Done" button
    done_button = browser.find_element_by_xpath('//*[@id="view_container"]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/button/span')
    done_button.click()
    
    # Wait for 2 seconds
    time.sleep(2)
    
    # Open a new tab
    browser.execute_script("window.open('https://www.google.com/')")
    
# Close the browser
browser.quit()
