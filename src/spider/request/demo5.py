import requests
import json


def get(keyword):
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
    }
    params = {
        'cname': '',
        'pid': '',
        'keyword': keyword,
        'pageIndex': 1,
        'pageSize': 10
    }

    json_text = requests.post(url=url, headers=headers, params=params).json()
    size = json_text['Table'][0]['rowcount']
    print(size)

    params['pageSize'] = size

    json_text = requests.post(url=url, headers=headers, params=params).json()
    return json_text


def record(json_text):
    fp=open('./src/spider/request/kfc.json','w',encoding='utf-8')
    json.dump(json_text,fp,ensure_ascii=False)
    print('spider finished.')

if __name__ == '__main__':
    keyword = input('Enter a keyword(city name).')
    json_text = get(keyword)
    record(json_text)
