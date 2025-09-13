

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
#driver.implicitly_wait(10)

wait=WebDriverWait(driver,10)


element=wait.until(Ec.element_to_be_clickable(By.ID,'loginlabel'))

driver.find_element(By.NAME,'log').send_keys("Demo12")
driver.find_element(By.NAME,'pwd').send_keys("Test123456$")
driver.find_element(By.NAME,'wp-submit').click()