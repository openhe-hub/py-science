import requests
import json
# using : Baidu Translation


def info():
    print("Welcome to PyTranslation(Copyright (c) openhe,driven by Baidu Translation).")


def translate(keyword):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
    }

    data = {
        'kw': keyword
    }
    url = "https://fanyi.baidu.com/sug"
    response = requests.post(url=url, data=data, headers=headers)
    result = response.json()
    analyze(result, keyword)


def analyze(obj, keyword):
    data = obj['data']
    if len(data) == 0:
        print(f'Err:{keyword} not found.')
    else:
        print(f'{len(data)}  results found:')
        for i in range(len(data)):
            print(
                f'{i+1}.\n\tKeyword:{data[i]["k"]}\n\tMeaning:{data[i]["v"]}')


if __name__ == '__main__':
    info()
    while(True):
        keyword = input('Enter Keyword:(# for exit)')
        if keyword == '#':
            break
        else:
            translate(keyword)
    print('Bye.')
