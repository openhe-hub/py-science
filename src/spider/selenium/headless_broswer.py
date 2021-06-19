from selenium import webdriver
from msedge.selenium_tools import EdgeOptions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

if __name__ == '__main__':
    # options
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver=webdriver.Chrome(r'C:\Users\william\AppData\Local\Programs\Python\Python38\Scripts\msedgedriver.exe',options=options)
    driver.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')

    # handle <select>
    selector=driver.find_element_by_xpath('//*[@id="OptionDate"]')
    select_element=Select(selector)
    for i in range(len(select_element.options)):
        select_element.select_by_index(i)
        time.sleep(1)
        scripts=f"console.log(\"crawling {2020-i} year's data\")"
        driver.execute_script(scripts)
        table=driver.find_element_by_xpath('//*[@id="TableList"]')
        print(table.text)
        print("================================")
    
