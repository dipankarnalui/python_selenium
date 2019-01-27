from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()
#Open URL
driver.get("https://mail.google.com/") 
#Enter username
driver.find_element_by_id("identifierId").send_keys("dipankarnalui@gmail.com") 
#click next button in username page
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/content/span").click()
sleep(4) 
#Enter password
password_xpath="/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/content/form/div[1]/div/div[1]/div/div[1]/input"
driver.find_element_by_xpath(password_xpath).send_keys("password")
#click next button in password page
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/content/span").click()
sleep(2) 
#Compose new mail
compose_button_xpath="/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div"
driver.find_element_by_xpath(compose_button_xpath).click()
sleep(10)
#Wait 20 seconds for compose window. It depends upon network speed
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, ":zo")))
#The following code is to enter the Recipient's email address in Compose Window
driver.find_element_by_xpath("//*[@id=':125']").send_keys("receiver@gmail.com,")
#Type Subject
driver.find_element_by_name("subjectbox").send_keys("Subject123")
#Type Content
driver.find_element_by_xpath("//*[@id=':12s']").send_keys("Content")
#Click Send button
driver.find_element_by_xpath("//*[@id=':11d']").click()
