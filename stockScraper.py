'''
Author: Geoffrey Bonnanzio
Last Updated: 12/22/2020

Script written to scrape stock values off of the Wall Street Journal website
'''
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

url = 'https://www.wsj.com/market-data/stocks/us/indexes'
#hdr = {'User-Agent': 'Mozilla/5.0'}
req = requests.get(url,headers)
soup = BeautifulSoup(req.content,'html.parser')

body = soup.find('body')
div = body.find('div',id='root') 
div2 = div.find('div',class_='style--grid--SxS2So51')
div3 = div2.find('div')
div4 = div3.find_all('div')
div5 = div4[-3].find_all('div')
#,class_='WSJBASE--clearfix--3Mtqek7G '
print(div5)
#print(body.prettify())
#div = body.find('div',id='root') 
#div2 = div.find('div',class_='style--grid--SxS2So51')
#div3 = div2.find('div')
#div4 = div3.find_all('div')
#div5 = div4[-3].find('div')



#for i in range(0,len(div4)):
#	print(div4[i])

#print("WOOOOOOOOOOP\n\n\n\n")
#div4 = div3.find('div')
#div5 = div4.find_all('div')
#print(div4)
#print(div.find_all('tbody',class_='WSJTables--table__body--3Y0p0d6H'))
