# 需求： 爬取三国演义所有章节标题
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    prefix ='https://www.shicimingju.com'
    url='https://bj.58.com/ershoufang/p1/'
    file_path='./src/spider/data_analyze/bs4/chapter.txt'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
    }
    response=requests.get(url=url, headers=headers)
    response.encoding='UTF-8-SIG'
    page_text=response.text

    soup=BeautifulSoup(page_text,'lxml')
    
    catalog=soup.select('div.book-mulu>ul>li')

    with open(file_path,'w',encoding='utf-8') as fp:
        for item in catalog:
            text=item.text+'\t'+prefix+item.a['href']+'\n'
            fp.write(text)


