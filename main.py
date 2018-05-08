#! python3

import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time


def main():
    email = sys.argv[1]                            # Takes email address from command line

    driver = webdriver.Chrome()                   # Chooses webdriver
    driver.get('http://www.accounts.google.com')  # Fetching your email account site (here it's gmail)

    wait = WebDriverWait(driver, 2)               # Declares waiting time for browser to load elements
    presence = ec.presence_of_element_located     # Locates presence of desired element

    loginElem = driver.find_element_by_id('identifierId')  # Identifies the field in which user types login
    loginElem.send_keys('my_login')      # Input your email address login here

    nButton = driver.find_element_by_id('identifierNext')  # Finds 'Next' button on site
    nButton.click()

    time.sleep(3)
    passwrdElem = driver.find_element_by_name('password') # Identifies field to type password
    passwrdElem.send_keys('my_pass')              # Sends password to password field

    nPassButton = driver.find_element_by_id('passwordNext') # Identifies 'Next' button on password site
    nPassButton.click()

    time.sleep(3)
    newMessage = driver.find_element_by_xpath('//*[@id=":4g"]/div/div') # Find 'New message' button
    newMessage.click()                           # Clicks the button

    wait.until(presence((By.ID, ':96')))         # Waits for receiver field to appear
    receiverElem = browser.find_element_by_id(':9j') #Finds receiver field in new message
    receiverElem.send_keys(email)                # Sends email address typed in cmd to the receiver field

    topicElem = browser.find_element_by_id(':91') # Finds topic field in new message
    topicElem.send_keys(sys.argv[2])              # Sends topic typed as third argument in command line

    messageElem = browser.find_element_by_id(':a6') # Finds textfield to type your message in
    messageElem.send_keys(sys.argv[3:])            # Sends your message typed in command line

    sendButton = browser.find_element_by_id(":8r") # Finds 'Send' button
    sendButton.click()                             # Clicks 'Send' button

