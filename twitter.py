from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
PATH = r'C:\Users\JSDev\Documents\chromedriver.exe'


options = webdriver.ChromeOptions()

driver = webdriver.Chrome(PATH)

driver.get('https://twitter.com')

time.sleep(2)

twit = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')

time.sleep(2)

twit.click()

