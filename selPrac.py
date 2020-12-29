import tkinter as tk
from selenium import webdriver

def create_error_window(error_message,width,height):
    # create root window
    root = tk.Tk()
    # width and height of user scree
    screenW = root.winfo_screenwidth()
    screenH = root.winfo_screenheight()
    # x and y coords of center of screen
    x = (screenW/2) - (width/2)    
    y = (screenH/2) - (height/2)
    # set root starting position and size
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    # not resizable
    root.resizable(0,0)
    # title
    root.title('Error')
    text = tk.Text(root)
    text.pack()
    # error message
    text.insert(tk.END,error_message)
    # launch window
    root.mainloop() 


def main():
    # get chromedriver app from the local machine 
    try:
        driver_path = r'C:/ChromeDriver/chromedriver.exe'
        driver = webdriver.Chrome(executable_path=driver_path)
    except:
        driver_error = "An error has occurred.\n\nchromedriver.exe not found in file path given:\n" + driver_path
        create_error_window(driver_error,400,100)
        return
    # try to get the necessary values from the table on the website
    try:
        # go to this website
        driver.get('https://www.wsj.com/market-data/stocks/us/indexes')
        # indexes needed from table and empty array to store floats
        indexes_needed = ['Industrial Average','500 Index','Nasdaq 100','Russell 2000']
        vals_found = []
        # iterate through values in table until found
        table = driver.find_element_by_tag_name('table')
        tbody_list = table.find_elements_by_tag_name('tbody')
        for tbody in tbody_list:
            tr_list = tbody.find_elements_by_tag_name('tr')
            for tr in tr_list:
                td_list = tr.find_elements_by_tag_name('td')
                href = td_list[0].find_element_by_tag_name('a')
                indexName = href.get_attribute("innerHTML")
                # found one of the values, break to go to next one
                if(indexName in indexes_needed):
                    curr_td_val = td_list[3].get_attribute("innerHTML")
                    vals_found.append(float(curr_td_val))
                    break
    # error parsing data in the table
    except:
        general_error = "An error has occurred.\n\nIt is suggested you collect data manually for\nthe time-being.\n\nIt is likely that the format of the WSJ website \nhas changed or you exited the application early."
        create_error_window(general_error,400,150)
    # close driver
    driver.close() 
    
main()