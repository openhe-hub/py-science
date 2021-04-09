from lxml import etree
import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)

    hot_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    city_list = []
    for li in hot_li_list:
        city_list.append(li.xpath('./a/text()')[0])

    ul_list = tree.xpath('//div[@class="bottom"]/ul[@class="unstyled"]')
    for ul in ul_list:
        li_list = ul.xpath('./div[2]/li')
        for li in li_list:
            city_list.append(li.xpath('./a/text()')[0])

    print(city_list)
