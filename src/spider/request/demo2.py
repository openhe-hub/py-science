# %%
import requests
# case 2:simple page collector

# UA disguise:User-Agent, the identification of request
# server may check the User-Agent,if User-Agent is the browser,OK
# %%
# UA disguise
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
}
search_text = input("Search for:")
param = {
    'query': search_text
}
url = 'https://www.sogou.com/web'
response = requests.get(url=url, params=param, headers=headers)
text = response.text
with open(f'./result_{search_text}.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('spider finished')

# %%
