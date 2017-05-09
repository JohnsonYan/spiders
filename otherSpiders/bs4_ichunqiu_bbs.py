#!/usr/bin/env python3
#coding=utf-8

import requests
from bs4 import BeautifulSoup

url = 'http://bbs.ichunqiu.com/portal.php'

r= requests.get(url=url)

soup = BeautifulSoup(r.content,'lxml')

#print(soup.title)
#print(soup.title.string)
bbs_news = soup.findAll(name='a',attrs={'class':'ui_colorG'})
for news in bbs_news:
    print(news.string)
#万金油用法
#soup.findAll(name='xxx',attrs={'xxx':re.compile('re_xxx')}
