import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://google.com')
driver.implicitly_wait(15)

e1 = driver.find_element(By.CLASS_NAME,'gLFyf')
e1.send_keys('chat gpt')
print('success')
e2 = driver.find_element(By.CLASS_NAME,'gNO89b')
e2.click()
print('success')
e3 = driver.find_element(By.CLASS_NAME,'LC20lb')
e3.click()
print('success')
e4 = driver.find_element(By.CLASS_NAME,'btn')
e4.click()
print('success')
e5 = driver.find_element(By.CLASS_NAME,"ctp-checkbox-label")
time.sleep(4)
e5.click()
