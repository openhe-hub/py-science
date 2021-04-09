from lxml import etree
import requests

if __name__ == '__main__':
    url='https://bj.58.com/ershoufang/p1/?PGTID=0d30000c-0000-19ac-7a93-c7a502204e82&ClickID=1'
    path='./src/spider/data_analyze/xpath/house.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
    }
    page_text=requests.get(url=url,headers=headers).text
    with open(path,'w',encoding='utf-8') as fp:
        fp.write(page_text)

    tree=etree.parse('house.html')
    print(tree.xpath('//h3[@class="property-content-title-name"]'))


