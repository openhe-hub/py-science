#%%
import requests
import json
# case 3:Baidu Translation
# -post request
# -json response data 
# %%
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
}
keyword=input('Enter Keyword:')
data ={
    'kw':keyword
}
url="https://fanyi.baidu.com/sug"
response=requests.post(url=url,data=data,headers=headers)
result=response.json()
print(result)
fp=open(f'./result_{keyword}.json','w',encoding='utf-8')
json.dump(result,fp,ensure_ascii=False)
print('done')
# %%

# %%
