from bs4 import BeautifulSoup
import requests
import re
import os

os.system('cls')
# choice = 'y'

# while choice == 'y':
print 'Finance Crawler'
print '~~~~~~~~~\n'
company_original = raw_input('Name of the company acronym: ')
company_edit = company_original.replace(' ', '+')

url = 'http://finance.yahoo.com/q;_ylt=AjSev5USVeC8JC3HULKk2Asnv7gF?uhb=uhb2&fr=uh3_finance_vert_gs_ctrl1_e&type=2button&s=' + company_edit	
element = requests.get(url)
plain_text = element.text
soupObject = BeautifulSoup(plain_text, 'html.parser')
company_lower = company_original.lower()
for quote in soupObject.findAll('span',{'id':'yfs_l84_' + company_lower}):
	# timer = str(time.strftime("%I:%M:%S"))	
	print quote.string
	#print('\n' + company_original + ' Stock Price: ' + number_quote)	
	# number_quote = int(number_seats)
	# seat_list.insert(i,number_seats)
	# i += 1
		#print("\n**Finish**")
	# for band_name in soupObject.findAll('a'):
	# 	band_name = (band_name.get_text())
	# 	if band_name == 'Music-Map':
	# 		continue
	# 	elif band_name == '?':
	# 		continue
	# 	elif band_name == band_original.title():
	# 		print ''
	# 	else:
	# 		print (band_name.encode("utf-8"))
		#if '.html' in band_name['href']:
		#	name = band_name['href']
		#	if bool(re.search('http', name)):
		#		name = ''
		#	name = name.replace('.html','')
		#	name = name.replace('+', ' ')	
		#	name = name.title()		
		#	print name
			
	# choice = raw_input('\nWould you like to make another search? \n(y/n): ')
	# if choice == 'n':
	# 	os.system('exit')
	# elif choice == 'y':
	# 	os.system('cls')