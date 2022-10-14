# Registration_Patients .
#https://medisquare.com.bd/register

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


serv_obj=Service("C:\\Drivers\chromeDriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://medisquare.com.bd/register")
#implicity must dite hobe
driver.implicitly_wait(10)


# first_name
driver.find_element(By.CSS_SELECTOR,"input[placeholder='First Name']").send_keys('Imran')
# last_name
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Last Name']").send_keys('Fakir')
#Phone_Number
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Ex: 01XXXXXXXXX']").send_keys('01747247678')

# drop down menu
#Gender Xpath = //select[@class='block w-full px-4 py-
find_element_click = driver.find_element(By.CSS_SELECTOR,"select[class='block w-full px-4 py-[22px] pr-8 cursor-pointer text-gray-500 text-lg leading-tight bg-white border-2 border-gray-200 rounded-lg appearance-none focus:outline-none']")
find_element_click = Select(find_element_click)
find_element_click.select_by_visible_text("Male")

# #password CSS =input[placeholder='Enter Password']
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter Password']").send_keys('01747247678')
#Confirm password CSS = input[placeholder='Confirm Password']
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Confirm Password']").send_keys('01747247678')

#click term & conditin css = input[type='checkbox']
driver.find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()

#Registration Button Xpath = //button[normalize-space()='Register']
driver.find_element(By.XPATH,"//button[normalize-space()='Register']").click()

time.sleep(20)

print(driver.title)
print(driver.current_url)

act_title = driver.title
exp_title = "Patient Register-Medisquare"

if act_title == exp_title:
    print("Login Page Passed")
else:
    print("Login Page failed")

driver.delete_all_cookies()
driver.close()
