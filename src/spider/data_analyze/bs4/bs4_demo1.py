#%%
from bs4 import BeautifulSoup
import requests
# %%
# build instance of Beautiful Soup
# html from remote or local
# type I
fp=open('./test.html','r',encoding='utf-8')
soup1= BeautifulSoup(fp,'lxml')
print(soup1)
    
# %%
# type II
page_text=requests.get('http://www.baidu.com').text
soup2= BeautifulSoup(page_text,'lxml')
print(soup2)
# %%
# soup.tagName : return first exist tag
print(soup1.a)
print(soup1.div)
# %%
# soup.find(tagName) : return first exist tag
print(soup1.find('a'))
# class_ : return first exist tag with class
# or id
print(soup1.find('div',class_='next'))
# %%
print(soup1.findAll('div'))
# %%
# select('selector(css style)')
print(soup1.select('.story'))
print(soup1.select('.title>b')[1])
# %%
# get attr and text data 
# text,get_text() get all text,string get pure string
print(soup1.a.text)
print(soup1.find('p',class_='story').string)
print(soup1.a['href'])
# %%
