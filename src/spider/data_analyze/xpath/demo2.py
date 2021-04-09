# 解析下载图片数据
from lxml import etree
import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
    }
    folder_path='./src/spider/data_analyze/xpath/beauty/'
    url='https://pic.netbian.com/4kmeinv/'
    prefix='https://pic.netbian.com'

    response = requests.get(url=url, headers=headers)
    response.encoding='gbk'
    page_text=response.text

    tree=etree.HTML(page_text)
    li_list=tree.xpath('//ul[@class="clearfix"]/li')

    for li in li_list:
        src=prefix+li.xpath('./a/img/@src')[0]
        title=li.xpath('./a/img/@alt')[0]
        print(f'src={src},title={title}')
        picture=requests.get(url=src, headers=headers).content
        with open(folder_path+title+'.jpg','wb') as fp:
            fp.write(picture)


