import requests
from lxml import etree


HEADERS = {'user-agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
URL = 'https://www.pearvideo.com/category_5'

se = requests.Session()

page_text = se.get(URL, headers=HEADERS).text

tree = etree.HTML(page_text)

li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
video_list = []
for li in li_list:
    # video_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
    video_contid = li.xpath('./div/a/@href')[0].split('_')[-1]
    
    print(video_contid)
    video_name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
    video_dict = {'video_name':video_name, 'video_contid':video_contid}
    video_list.append(video_dict)

def get_video(dic):
    video_url = 'https://www.pearvideo.com/videoStatus.jsp'
    data = {
        'contId': dic['video_contid']
    }
    detail_url = se.get(video_url, params=data, headers=HEADERS).content
    print(detail_url)

for dic in video_list:
    get_video(dic)