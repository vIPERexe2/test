import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Luo satunnaisen sähköpostiosoitteen
def generate_email():
    letters = string.ascii_lowercase
    email = ''.join(random.choice(letters) for i in range(10))
    email += "@gmail.com"
    return email

# Luo satunnaisen salasanan
def generate_password():
    letters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(letters) for i in range(15))
    return password

# Avaa selainikkunan
driver = webdriver.Chrome()
driver.get("https://accounts.google.com/signup")

# Täytä lomake
time.sleep(2)
first_name = driver.find_element_by_name("firstName")
first_name.send_keys("Etunimi")
last_name = driver.find_element_by_name("lastName")
last_name.send_keys("Sukunimi")
email = driver.find_element_by_name("Username")
email.send_keys(generate_email())
password = driver.find_element_by_name("Passwd")
password.send_keys(generate_password())
confirm_password = driver.find_element_by_name("ConfirmPasswd")
confirm_password.send_keys(generate_password())
time.sleep(2)

# Lähetä lomake
submit_button = driver.find_element_by_id("accountDetailsNext")
submit_button.click()
time.sleep(2)

# Näytä käyttäjän sähköpostiosoite ja salasana
print("Sähköpostiosoite:", email.get_attribute("value"))
print("Salasana:", password.get_attribute("value"))

# Sulje selainikkuna
driver.quit()
