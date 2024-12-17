
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

file = open("log.txt", "w")

driver = webdriver.Chrome()

driver.get('http://www.saucedemo.com/')
driver.maximize_window()

def login():
    user_name = driver.find_element(By.ID, "user-name")
    user_name.send_keys("standard_user")
    file.write("Success write login\n")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    file.write("Success write password\n")

    login_button = driver.find_element(By.XPATH,'//input[@id="login-button"]')
    login_button.click()

    file.write("Success click enter\n")
    sleep(5)
login()
file.close()
driver.quit()
