from selenium import webdriver

def main():
    
    driver = webdriver.Chrome(executable_path=r'C:/ChromeDriver/chromedriver.exe')
    driver.get('https://www.wsj.com/market-data/stocks/us/indexes')
    indexes_needed = ['Industrial Average','500 Index','Nasdaq 100','Russell 2000']
    vals_found = []
    table = driver.find_element_by_tag_name('table')
    tbody_list = table.find_elements_by_tag_name('tbody')
    for tbody in tbody_list:
        tr_list = tbody.find_elements_by_tag_name('tr')
        for tr in tr_list:
            td_list = tr.find_elements_by_tag_name('td')
            href = td_list[0].find_element_by_tag_name('a')
            indexName = href.get_attribute("innerHTML")
            if(indexName in indexes_needed):
                curr_td_val = td_list[3].get_attribute("innerHTML")
                vals_found.append(float(curr_td_val))
                break
                
            
    print(vals_found)


    driver.close()

main()