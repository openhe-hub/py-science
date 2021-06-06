# login demo: https://user.17k.com/www/
import requests


if __name__ == '__main__':
    #1.login
    session = requests.session()
    data={
        "loginName": "16602105188",
        "password": "5f6e778dx"
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
    }
    url="https://passport.17k.com/ck/user/login"
    resp=session.post(url=url,data=data,headers=headers)
    # print(resp.text)
    # print(resp.cookies)

    #2.get page
    resp=session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
    print(resp.text)
