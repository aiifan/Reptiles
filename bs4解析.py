"""
爬取三国演义全文
"""


import requests
from bs4 import BeautifulSoup


HEADERS = {'user-agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}


# url = "https://www.shicimingju.com/book/sanguoyanyi.html"

# page_text = requests.get(url, headers=HEADERS).text

# soup = BeautifulSoup(page_text, 'lxml')

# tag_list = soup.select('.book-mulu > ul > li > a')

# for tag in tag_list:
#     telti = tag.text


def connent():
    url = 'https://www.shicimingju.com/book/sanguoyanyi/%d.html'
    with open('三国演义.txt', 'a', encoding='utf-8') as f:
        for i in range(1,121):
            new_url = format(url%i)
            page_text = requests.get(new_url, headers=HEADERS).text
            soup = BeautifulSoup(page_text, 'lxml')
            title = soup.select_one('.bookmark-list > h1').text
            con_list = soup.select('.chapter_content > p')
            f.write(title + '\n')
            for con in con_list:
                conn = ''.join(con)
                f.write(conn + '\n')
    return 'ok'
connent()