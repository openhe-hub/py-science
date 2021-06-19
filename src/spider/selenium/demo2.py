from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':	
    driver=webdriver.Edge(r'C:\Users\william\AppData\Local\Programs\Python\Python38\Scripts\msedgedriver.exe')
    driver.get('https://lagou.com/')
    btn=driver.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[2]/a')
    btn.click()
    search=driver.find_element_by_xpath('//*[@id="search_input"]')
    search.send_keys('python',Keys.ENTER)

    # selenium switch windows(not default to new tab)
    driver.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').click()
    driver.switch_to.window(driver.window_handles[-1])
    job_details=driver.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text
    print(job_details)

    # close and switch back
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    company=driver.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[2]/div[1]/a').text
    print(company)