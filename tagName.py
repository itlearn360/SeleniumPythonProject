from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://demo.itlearn360.com/")

allinks=driver.find_elements(By.TAG_NAME,'a')
print(len(allinks))

for link in allinks:
    url=link.get_attribute("href")
    print(url)
