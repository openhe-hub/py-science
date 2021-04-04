import requests
import re
import os

if __name__ == '__main__':
    url = 'https://www.qiushibaike.com/imgrank/'
    folder = './src/spider/data_analyze/regex/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
    }
    page_text = requests.get(url=url, headers=headers).text
    with open(folder+'images.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    regex ='<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_src_list=re.findall(regex,page_text,re.S)
    print(img_src_list)

    if not os.path.exists(folder+'pictures'):
        os.makedirs(folder+'pictures')

    for src in img_src_list:
        src='https:'+src
        image_data=requests.get(url=src,headers=headers).content
        image_name=src.split('/')[-1]
        image_path=folder+'pictures/'+image_name
        with open(image_path,'wb') as fp:
            fp.write(image_data)

