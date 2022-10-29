from pydoc import classname
from selenium import webdriver
import time
from Credentials import LoginID, password
from selenium.webdriver.common.by import By


driver = webdriver.Chrome ()
driver.get("https://www.netflix.com/in/login")
time.sleep(3)

emailId = driver.find_element("xpath" , '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div/div/label/input')
emailId.send_keys(LoginID)

passwordInput = driver.find_element("xpath" , '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div[1]/div/label/input')
passwordInput.send_keys(password)

signInButton = driver.find_element("xpath" , "/html/body/div[1]/div/div[3]/div/div/div[1]/form/button").click()
time.sleep(3)

driver.get("https://www.netflix.com/SwitchProfile?tkn=MRPC7FT7UVF4LF5RUWM34UA4CE")
time.sleep(3)

driver.find_element(By.CLASS_NAME , 'ltr-j0gpa2').click()
driver.__exit__








