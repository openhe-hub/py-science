from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':	
    driver=webdriver.Edge(r'C:\Users\william\AppData\Local\Programs\Python\Python38\Scripts\msedgedriver.exe')
    driver.get('https://www.91kanju.com/vod-play/541-2-1.html')
    #handle <iframe>
    iframe=driver.find_element_by_xpath('//*[@id="player_iframe"]')
    driver.switch_to.frame(iframe)
    #switch out
    driver.switch_to.default_content()
