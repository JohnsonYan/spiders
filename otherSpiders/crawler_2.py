#coding=utf-8
import requests

url = 'http://www.heibanke.com/lesson/crawler_ex02/'

username = 'hs'

for x in range(1,31):
    print('bursting password...')
    data = {
        'username' : username,
        'password' : x,
    }
    html = requests.post(url,data=data).text
    if not '错误' in html:
        print('password: ', x)
        break
