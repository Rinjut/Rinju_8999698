# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the facebook homepage
driver.get("https://www.facebook.com/")
time.sleep(15)

email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "email"))
)
# Entering email
email_field.send_keys("rinjut83@gmail.com")

# Entering password
password_field = driver.find_element(By.ID, "pass")
password_field.send_keys("Rinju@123")

# Clicking the login button
login_button = driver.find_element(By.NAME, "login")
login_button.click()

# Waiting for the search results page to load
time.sleep(8)



messenger_link = driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/div[3]/span/span/div/div[1]")
messenger_link.click()
# Waiting for the details page to load
time.sleep(2)

# find messenger icon
messenger_link = driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[3]/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div/div/div")
messenger_link.click()
# Waiting
time.sleep(2)

# close messenger box
message_input = driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div/div[1]/div/div[2]/span[2]/div/div")
message_input.click()
time.sleep(2)

#clicking profile icon
profile_input = driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/span/div/div[1]/div")
profile_input.click()
time.sleep(2)

#clicking logout button
logout_input = driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[5]/div/div[1]/div[2]/div/div/div/div")
logout_input.click()
time.sleep(2)

# Closing the webdriver
driver.close()
