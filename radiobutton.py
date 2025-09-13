from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://training.qaonlinetraining.com/testPage.php")

radio_button=driver.find_element(By.XPATH,'/html/body/form/input[4]')
radio_button.click()

if(radio_button.is_selected()):
    print("The test passed ")
else:
    print("The test failed")