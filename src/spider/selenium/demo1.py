from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':	
    driver=webdriver.Edge(r'C:\Users\william\AppData\Local\Programs\Python\Python38\Scripts\msedgedriver.exe')
    driver.maximize_window()
    driver.get('https://lagou.com/')
    # 1. click element
    btn=driver.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[2]/a')
    btn.click()
    # 2. enter in search box
    search=driver.find_element_by_xpath('//*[@id="search_input"]')
    search.send_keys('python',Keys.ENTER)
    # 3. find <li>
    li_list=driver.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
    print(len(li_list))
    for li in li_list:
        name=li.find_element_by_tag_name('h3').text
        salary=li.find_element_by_xpath("./div/div/div[2]/div/span").text
        company=li.find_element_by_xpath("./div/div[2]/div/a").text
        print(f'name={name},salary={salary},company={company}')