import requests
import json
# case 4: crawling DOUBAN Top 250 science fiction films.

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
    }
    params = {
        'type': 17,
        'interval_id': '100:90',
        'action':'',
        'start':'0',
        'limit':'250'
    }

    response =requests.get(url=url, params=params,headers=headers)
    list=response.json()
    print(list)

    fp=open('./src/spider/request/films.json','w',encoding='utf-8')
    json.dump(list,fp,ensure_ascii=False)
    print('over')
