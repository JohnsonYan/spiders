#coding=utf-8
# 用来爬过黑板客第一关的爬虫
import requests
import re

url = 'http://www.heibanke.com/lesson/crawler_ex00/'
nextNumber = '43396'

while(nextNumber):
    r = requests.get(url=url+nextNumber)
    pattern = re.compile('是[0-9]{5}')
    a = pattern.findall(r.text)
    print(a)
    nextNumber = a[0][1:]
