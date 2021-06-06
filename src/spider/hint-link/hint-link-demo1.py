import requests

if __name__ == '__main__':
    url = 'https://www.pearvideo.com/video_1731256'
    file_path='./src/spider/hint-link/result.mp4'
    contId=url.split('_')[1]
    video_url =f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.665111719005099'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63',
        'Referer':'https://www.pearvideo.com/video_1731256' #anti-stealing-link : by getting the original request
    }

    resp=requests.get(url=video_url,headers=headers)
    dict=resp.json()
    srcUrl=dict['videoInfo']['videos']['srcUrl']
    systemTime=dict['systemTime']
    srcUrl=srcUrl.replace(systemTime,f'cont-{contId}')
    
    resp=requests.get(srcUrl)
    with open(file_path,'wb') as f:
        f.write(resp.content)

