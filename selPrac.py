from selenium import webdriver

driver = webdriver.Chrome(r'C:/ChromeDriver/chromedriver.exe')
driver.get('https://www.wsj.com/market-data/stocks/us/indexes')
