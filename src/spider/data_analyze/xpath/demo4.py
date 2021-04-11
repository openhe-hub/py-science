from lxml import etree
import requests

if __name__ == '__main__':
    url = 'https://sc.chinaz.com/jianli/free.html'
    folder_path = './src/spider/data_analyze/xpath/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text
    with open(folder_path+'demo4.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    tree = etree.HTML(page_text)
    div_list = tree.xpath('//div[@class="box col3 ws_block"]')

    href_list = []
    name_list = []
    for div in div_list:
        href_list.append('https:'+div.xpath('./a/@href')[0])
        name_list.append(div.xpath('./a/img/@alt')[0])

    for href, name in zip(href_list, name_list):
        response = requests.get(url=href, headers=headers)
        response.encoding = 'utf-8'
        page_text = response.text
        tree = etree.HTML(page_text)
        res_url = tree.xpath('//ul[@class="clearfix"]/li[1]/a/@href')[0]
        print(f'downloading {res_url}...')
        rar_file = requests.get(url=res_url, headers=headers).content
        with open(folder_path+'cv/'+name+'.rar','wb') as fp:
            fp.write(rar_file)
        print(f'{name} downloading Done.')
 