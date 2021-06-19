from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':	
    driver=webdriver.Edge(r'C:\Users\william\AppData\Local\Programs\Python\Python38\Scripts\msedgedriver.exe')
    driver.maximize_window()
    driver.get('https://lagou.com/')
    # click element
    btn=driver.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[2]/a')
    btn.click()
    # enter in search box
    search=driver.find_element_by_xpath('//*[@id="search_input"]')
    search.send_keys('python',Keys.ENTER)