'''
Author: Geoffrey Bonnanzio
Last Updated: 12/22/2020

Script written to scrape stock values off of the Wall Street Journal website
'''
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests



url = 'https://www.wsj.com/market-data/stocks/us/indexes'
hdr = {'User-Agent': 'Mozilla/5.0'}
req = requests.Session()
page_raw = req.get(url,headers = hdr)
page_text = page_raw.text
soup = BeautifulSoup(page_text,'lxml')
body = soup.find('body')
#print(body.prettify())
div = body.find('div',id='root') 
div2 = div.find('div',class_='style--grid--SxS2So51')
div3 = div2.find('div')
div4 = div3.find_all('div')
div5 = div4[-3].find('div')
div6 = div5.find('div')
print(div6.prettify())


#for i in range(0,len(div4)):
#	print(div4[i])

#print("WOOOOOOOOOOP\n\n\n\n")
#div4 = div3.find('div')
#div5 = div4.find_all('div')
#print(div4)
#print(div.find_all('tbody',class_='WSJTables--table__body--3Y0p0d6H'))
