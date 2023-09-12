from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.webdriver.common.keys import Keys

# get into amazon
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
driver.get("https://www.amazon.fr/")

# bypass cookies notif
cookies = driver.find_element(By.ID, 'sp-cc-accept')
cookies.click()

# choose the products you are looking for 
search_bar = driver.find_element(By.ID, 'twotabsearchtextbox')
search_bar.send_keys("perfume")
search_bar.send_keys(Keys.ENTER)
time.sleep(2)

# get the products
products = driver.find_elements(By.XPATH, "//div[@class='sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20']")

# get each product's name and price 
for i in range(0,5):
    product_name = products[i].find_element(By.XPATH, ".//span[@class='a-size-base-plus a-color-base a-text-normal']")
    print(product_name.text)
    rubbish = products[i].find_elements(By.XPATH, ".//div[@class='a-row a-size-base a-color-secondary']")
    price = rubbish[-1].find_element(By.TAG_NAME, "span")
    print(price.text)
    print("-----------------------------------------------")



