#!/usr/bin/env python
"""
糗事百科图片下载

"""

from __future__ import print_function
import re
import os
import sys
import requests


HEADERS = {'user-agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
URL = 'https://www.qiushibaike.com/imgrank/page/%d/'
ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'

if not os.path.exists('qiushi'):
        os.mkdir('qiushi')
# 总个数
num = 0
for i in range(1,36):
    new_url = format(URL%i)
    respones = requests.get(url=new_url, headers=HEADERS)
    page_text = respones.text
    img_url_list = re.findall(ex, page_text, re.S)
    num += len(img_url_list)
    for src in img_url_list:
        src = 'https:' + src
        img_data = requests.get(src, headers=HEADERS).content
        with open(os.path.join('qiushi', src.split('/')[-1]), 'wb') as f:
            f.write(img_data)
        print(src + '下载完成')
print('共下载%d张图片' % num)
