import requests

if __name__ == '__main__':
    proxy={
        "https":"https://218.60.8.83:3129"
    }

    resp=requests.get("https://www.baidu.com",proxies=proxy)
    resp.encoding='utf-8'
    print(resp.text)