from selenium import webdriver
from msedge.selenium_tools import EdgeOptions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

target_url = 'https://www.jiumodiary.com/'
chrome_driver_path = r'C:\Users\william\AppData\Local\Programs\Python\Python38\Scripts\msedgedriver.exe'

if __name__ == '__main__':
    print("Welcome to py-book-spider(copyright:openhe).")
    print("This spider software targets to search books on web(powered",
    " by selenium),and collects the direct link,currently using JiuMo Search Site.")
    key = input("Please input the name of the book:")


    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument('log-level=3')
    driver=webdriver.Chrome(chrome_driver_path,options=options)
    driver.get(target_url)

    search_box = driver.find_element_by_xpath('//*[@id="SearchWord"]')
    search_box.send_keys(key, Keys.ENTER)

    # get link
    time.sleep(4) # wait for loading
    ul = driver.find_element_by_xpath('//*[@id="result-ul"]')
    link_list = ul.find_elements_by_xpath('div/a')
    info_list=ul.find_elements_by_xpath('div/a/span')
    href_list,detail_list=[],[]
    for i in range(len(link_list)):
        href=link_list[i].get_attribute('data-href')
        info=info_list[i].text if info_list[i].text!='' else 'lack info' 
        if(href!=None): 
            href_list.append(href)
            detail_list.append(info)
    print(f'{len(detail_list)} results found.')
    for i in range(len(href_list)):
        print(f'{i}.\n\tname:{detail_list[i]}\n\tlink:{href_list[i]}')
