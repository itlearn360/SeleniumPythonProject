

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://demo.itlearn360.com/")
driver.implicitly_wait(10)
driver.manage().window().maximize();
driver.find_element(By.ID,'loginlabel').click()
driver.find_element(By.NAME,'log').send_keys("Demo12")
driver.find_element(By.NAME,'pwd').send_keys("Test123456$")

driver.find_element(By.NAME,'wp-submit').click()


