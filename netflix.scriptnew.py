
from pydoc import classname
from selenium import webdriver
import time
from selenium.webdriver.common.by import By



driver = webdriver.Chrome ()
driver.get("https://www.netflix.com/in/title/80057281")



cast = driver.find_element("xpath" , "/html/body/div[1]/div/div[2]/section[5]/div[3]/div")

print(cast.text)
time.sleep(3)

description = driver.find_element("xpath" , "/html/body/div[1]/div/div[2]/section[4]/div[3]/div[1]/div/p")
print(description.text)
time.sleep(3)
try:
    play = driver.find_element("xpath" , "/html/body/div[1]/div/div[2]/section[3]/div[2]/ul/li[1]/div/button/span[1]").click()
    print("trailer played succesfully")

except:  
    print("trailer not played")

time.sleep(100)

driver.quit()

















