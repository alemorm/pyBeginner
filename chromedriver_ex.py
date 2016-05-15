import os
from selenium import webdriver

chromedriver = "/Users/Alejandro/Documents/Chromedriver/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://stackoverflow.com")
driver.quit()