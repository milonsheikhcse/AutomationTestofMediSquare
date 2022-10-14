#https://medisquare.com.bd/doctor/login
# next page = Dashboard|Patient-Medisquare
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\\Drivers\chromeDriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)


driver.get("https://medisquare.com.bd/doctor/login")

#implicity_must privide otherwise it not work
driver.implicitly_wait(10)
#phone num
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Ex: 01XXXXXXXXX']").send_keys('01717754602')
#password
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter Password']").send_keys('01717754602')
#button click
driver.find_element(By.XPATH,"//button[normalize-space()='Log In']").click()

time.sleep(10)

print(driver.title)
print(driver.current_url)

act_title = driver.title
exp_title = "Dashboard|Patient-Medisquare"

if act_title == exp_title:
    print("Login Page Passed")
else:
    print("Login Page failed")

driver.delete_all_cookies()
# only one page close
driver.close()
#all page close
driver.quit()
