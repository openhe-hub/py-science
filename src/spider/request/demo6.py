import requests
import json

if __name__ == '__main__':
    # get id
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
    }
    list_id = []
    for i in range(1, 6):
        page = str(i)
        params = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        json_id = requests.post(url=url, headers=headers, params=params).json()
        for dic in json_id['list']:
            list_id.append(dic['ID'])
    # get info
    list_data = []
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in list_id:
        params = {
            'id': id
        }
        detail_json = requests.post(
            url=url, headers=headers, params=params).json()
        list_data.append(detail_json)
    # store
    with open('./src/spider/request/surveillance.json', 'w', encoding='utf-8') as fp:
        json.dump(list_data, fp, ensure_ascii=False)
