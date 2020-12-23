from selenium import webdriver

DRIVER_PATH = "/'Program Files (x86)'/ChromeDriver/"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.wsj.com/market-data/stocks/us/indexes')
