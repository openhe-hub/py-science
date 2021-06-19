from selenium import webdriver

if __name__ == '__main__':	
    driver=webdriver.Edge(r'C:\Users\william\AppData\Local\Programs\Python\Python38\Scripts\msedgedriver.exe')
    driver.maximize_window()
    driver.get('https://www.qingpufdfz.cn/')
    
    