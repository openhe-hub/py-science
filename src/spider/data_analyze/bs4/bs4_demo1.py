#%%
from bs4 import BeautifulSoup
import requests
# %%
# build instance of Beautiful Soup
# html from remote or local
# type I
fp=open('./test.html','r',encoding='utf-8')
soup= BeautifulSoup(fp,'lxml')
print(soup)
    
# %%
# type II
page_text=requests.get('http://www.baidu.com').text
soup= BeautifulSoup(page_text,'lxml')
print(soup)
# %%
