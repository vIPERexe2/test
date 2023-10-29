import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Määritä selain
browser = webdriver.Chrome()

# Avaa Google-sivusto
browser.get('https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp')

# Syötä haluttu määrä sähköpostiosoitteita
email_count = int(input("Kuinka monta sähköpostiosoitetta haluat luoda? "))

for i in range(email_count):
    # Syötä etunimi
    first_name = browser.find_element_by_name('firstName')
    first_name.send_keys(''.join(random.choices(string.ascii_lowercase, k=5)))
    
    # Syötä sukunimi
    last_name = browser.find_element_by_name('lastName')
    last_name.send_keys(''.join(random.choices(string.ascii_lowercase, k=5)))
    
    # Syötä käyttäjänimi
    username = browser.find_element_by_name('Username')
    username.send_keys(''.join(random.choices(string.ascii_lowercase, k=5)))
    
    # Syötä salasana
    password = browser.find_element_by_name('Passwd')
    password.send_keys(''.join(random.choices(string.ascii_letters + string.digits, k=8)))
    
    # Syötä salasana uudelleen
    confirm_password = browser.find_element_by_name('ConfirmPasswd')
    confirm_password.send_keys(password.get_attribute('value'))
    
    # Paina "Seuraava" -painiketta
    next_button = browser.find_element_by_xpath('//*[@id="accountDetailsNext"]/div/button/span')
    next_button.click()
    
    # Odota 2 sekuntia
    time.sleep(2)
    
    # Paina "Vahvista puhelinnumero" -painiketta
    phone_button = browser.find_element_by_xpath('//*[@id="view_container"]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div/div/button/span')
    phone_button.click()
    
    # Odota 2 sekuntia
    time.sleep(2)
    
    # Paina "Seuraava" -painiketta
    next_button2 = browser.find_element_by_xpath('//*[@id="view_container"]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/button/span')
    next_button2.click()
    
    # Odota 2 sekuntia
    time.sleep(2)
    
    # Paina "Seuraava" -painiketta
    next_button3 = browser.find_element_by_xpath('//*[@id="view_container"]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/button/span')
    next_button3.click()
    
    # Odota 2 sekuntia
    time.sleep(2)
    
    # Paina "Hyväksy" -painiketta
    accept_button = browser.find_element_by_xpath('//*[@id="view_container"]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/button/span')
    accept_button.click()
    
    # Odota 2 sekuntia
    time.sleep(2)
    
    # Paina "Seuraava" -painiketta
    next_button4 = browser.find_element_by_xpath('//*[@id="view_container"]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/button/span')
    next_button4.click()
    
    # Odota 2 sekuntia
    time.sleep(2)
    
    # Paina "Valmis" -painiketta
    done_button = browser.find_element_by_xpath('//*[@id="view_container"]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/button/span')
    done_button.click()
    
    # Odota 2 sekuntia
    time.sleep(2)
    
    # Avaa uusi välilehti
    browser.execute_script("window.open('https://www.google.com/')")
    
# Sulje selain
browser.quit()
