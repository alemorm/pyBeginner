import os
from bs4 import BeautifulSoup
import requests
import re
import urllib
from selenium import webdriver

chromedriver = '/Users/Alejandro/Documents/Chromedriver/chromedriver'
os.environ['webdriver.chrome.driver'] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get('http://ipilab.org/BAAweb/')

RaceVal = ["'ASI'", "'BLK'", "'CAU'", "'HIS'"]
GenderVal = ["'F'", "'M'"]
AgeVal = ["'00'", "'01'", "'02'", "'03'", "'04'", "'05'", "'06'", "'07'", "'08'", "'09'", "'10'", "'11'", "'12'", "'13'", "'14'", "'15'", "'16'", "'17'", "'18'"]
for x in RaceVal:
	if x == "'CAU'":
		driver.find_element_by_xpath("//select[@name='Race']/option[@vaule="+ x +"]").click()
	else:
		driver.find_element_by_xpath("//select[@name='Race']/option[@value="+ x +"]").click()
		for y in GenderVal:
			driver.find_element_by_xpath("//select[@name='Gender']/option[@value="+ y +"]").click()
			for z in AgeVal:
				driver.find_element_by_xpath("//select[@name='Age']/option[@value="+ z +"]").click()
				driver.find_element_by_name('Submit').click()
				
				soupObject = BeautifulSoup(driver.page_source, 'html.parser')
				pagesrc = str(soupObject)
				n = 1
				strt = 1
				while strt > 0:
					strt = pagesrc.find('JPEG', n)
					end = pagesrc.find('.jpg', n)
					print strt
					print end
					newurl = 'http://ipilab.org/BAAweb/' + pagesrc[strt:(end+4)]
					print newurl
					picname = x.replace("'","") + y.replace("'","") + z.replace("'","") + '_' + pagesrc[(end-4):end]
					urllib.urlretrieve(newurl, 'C:/Users/Alejandro/Documents/Python Images/' + picname + '.jpg')
					n = strt + 100
				
driver.close()