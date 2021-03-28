#%%
# how to use:
# -url
# -request 
# -get response data
# -data store

# target:crawl www.sougou.com

# %%
import requests
# %%
# step 1:get url
url='https://www.sogou.com/'
# step 2:send request
response=requests.get(url=url)
# step 3:get response data
text=response.text
print(text)
# step 4:store data
with open('./data1.html','w',encoding='utf-8') as f:
    f.write(text)
print('finished.')
# %%
