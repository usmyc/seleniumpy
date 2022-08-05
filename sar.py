from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
PATH = r'C:\Users\JSDev\Documents\chromedriver.exe'


options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\JSDev\AppData\Local\Google\Chrome\User Data\Default')
driver = webdriver.Chrome(PATH, options=options)

driver.get('https://rembrandtblog.vercel.app/')

time.sleep(2)

twit = driver.find_element(
    By.XPATH, '//*[@id="__next"]/div/div/div/div[1]/div[2]/div[2]/a')
twit.click()

time.sleep(5)

driver.quit()
