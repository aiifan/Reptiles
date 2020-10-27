"""
彼岸4k美女图片下载，比老师讲的多了一步点开大图页，下载大图。
共下载了3382张图片。
"""
import os
import requests
from lxml import etree

def get_url():
    """
    下载剩余所有页
    """
    for i in range(2,171):
        meinv_index(meinv_url_index, num='index_{}.html'.format(i))
        print('第%d页下载完成' % i)

def meinv_index(local_url, num=''):
    """
    打开单页
    """
    meinv_url = local_url + num
    page = requests.get(meinv_url, headers=HEADERS).text
    tree = etree.HTML(page)
    one_url_list = tree.xpath('//div[@class="slist"]/ul/li/a/@href')
    for one_url in one_url_list:
        p_url = url + one_url
        reptile_meinv(p_url)

def reptile_meinv(to_url):
    """
    打开大图页，下载大图
    """
    reponse = requests.get(to_url, headers=HEADERS)
    reponse.encoding = 'gbk'
    meinv_page = reponse.text
    tree = etree.HTML(meinv_page)
    img_src = tree.xpath('//div[@class="photo-pic"]/a/img/@src')[0]
    img_title = tree.xpath('//div[@class="photo-pic"]/a/img/@title')[0]
    img_url = url + img_src
    img_data = requests.get(img_url, headers=HEADERS).content
    with open(os.path.join('彼岸','{}.jpg'.format(img_title)), 'wb') as f:
        f.write(img_data)

if __name__ == "__main__":
    url = 'http://pic.netbian.com/'
    HEADERS = {'user-agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    meinv_url_index = url + '4kmeinv/'
    if not os.path.exists('彼岸/'):
        os.mkdir('彼岸/')
    # 下载第一页
    meinv_index(meinv_url_index)
    print('第1页下载完成')
    #下载剩余所有页
    get_url()
