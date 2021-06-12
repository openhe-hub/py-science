from concurrent.futures import ThreadPoolExecutor
import requests
from lxml import etree
import csv

# url:http://xinfadi.com.cn/marketanalysis/0/list/1.shtml

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
}
file_path = './src/spider/thread/data.csv'
csv_reader = csv.writer(open(file_path, 'w', encoding='utf-8'))


def download(url):
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    dom = etree.HTML(resp.text)

    table = dom.xpath('/html/body/div[2]/div[4]/div[1]/table')[0]
    trs = table.xpath('./tr')[1:]
    for tr in trs:
        text = tr.xpath('./td/text()')
        csv_reader.writerow(text)
    print(f'Download {url} done.')


if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 200):
            t.submit(
                download, url=f"http://xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")

    print("Download finished.")
