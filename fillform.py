from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://training.qaonlinetraining.com/testPage.php")

driver.find_element(By.NAME,'name').send_keys("ITLearn")
driver.find_element(By.NAME,'email').send_keys("ravi@gmail.com")
driver.find_element(By.NAME,'website').send_keys("www.itlearn360.com")
driver.find_element(By.NAME,'comment').send_keys("The e-learning website")
driver.find_element(By.NAME,'submit').click()