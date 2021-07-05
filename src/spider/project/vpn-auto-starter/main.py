from selenium import webdriver
from msedge.selenium_tools import EdgeOptions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

url='http://localhost:54889/H3vVfzjXgD138GJrASpzHyhoESgQ2xUv/connect'

if __name__ == '__main__':	
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver=webdriver.Chrome(r'C:\Users\william\AppData\Local\Programs\Python\Python38\Scripts\msedgedriver.exe',options=options)
    driver.get(url)
    driver.implicitly_wait(20)
    close_btn=driver.find_element_by_xpath('//*[@id="renew-pane-free"]/div[1]')
    close_btn.click()
    time.sleep(5)
    driver.execute_script('toggle_connect()')

