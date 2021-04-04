# get image
import requests

if __name__ == '__main__':
    url='https://bkimg.cdn.bcebos.com/pic/63d9f2d3572c11dfe4175154632762d0f603c287?x-bce-process=image/watermark,image_d2F0ZXIvYmFpa2U5Mg==,g_7,xp_5,yp_5/format,f_auto'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
    }
    img_data=requests.get(url=url,headers=headers).content
    with open('./src/spider/data_analyze/regex/sakura.jpg','wb') as fp:  #wb write in binary mode
        fp.write(img_data)