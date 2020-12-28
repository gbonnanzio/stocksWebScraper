from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:/ChromeDriver/chromedriver.exe')
driver.get('https://www.wsj.com/market-data/stocks/us/indexes')
#assert "Python" in driver.title
table = driver.find_element_by_tag_name('table')
tbody = table.find_element_by_tag_name('tbody')
td_list = tbody.find_elements_by_tag_name('td')
#elem = tbody.find_element_by_class_name('WSJTables--table__cell--2u6629rx WSJTheme--table__cell--3njwWeaF ')
at = td_list[0].getAttribute()
print(at)

#elem = driver.find_element_by_class_name('WSJTables--table__row--2VdwxeeP')
driver.close()
#print(elem)