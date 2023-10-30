import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the Chrome driver options
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = 'com.android.chrome/'  # Replace with the actual path to the Chrome binary

# Set up the browser
browser = webdriver.Chrome(options=chrome_options)

# Enter the desired number of email addresses
email_count = int(input("How many email addresses do you want to create? "))

for i in range(email_count):
    # Generate random strings for first name, last name, and username
    first_name = ''.join(random.choices(string.ascii_lowercase, k=5))
    last_name = ''.join(random.choices(string.ascii_lowercase, k=5))
    username = ''.join(random.choices(string.ascii_lowercase, k=5))
    
    # Generate a random password
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    
    # Enter the first name
    first_name_input = browser.find_element_by_name('firstName')
    first_name_input.send_keys(first_name)
    
    # Enter the last name
    last_name_input = browser.find_element_by_name('lastName')
    last_name_input.send_keys(last_name)
    
    # Enter the username
    username_input = browser.find_element_by_name('username')
    username_input.send_keys(username)
    
    # Enter the password
    password_input = browser.find_element_by_name('Passwd')
    password_input.send_keys(password)
    
    # Confirm the password
    confirm_password_input = browser.find_element_by_name('ConfirmPasswd')
    confirm_password_input.send_keys(password)
    
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
