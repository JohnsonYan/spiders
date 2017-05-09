#coding=utf-8
import requests

url = 'http://www.heibanke.com/lesson/crawler_ex02/'
login_url = 'http://www.heibanke.com/lesson/crawler_ex02/'

username = 'hshs'
password = '123456'
data = {
    'username' : username,
    'password' : password,
    'csrfmiddlewaretoken' : 'PkcCn7PWbK9cAVAMnGYxwYmIrxKqYdqy',
}

headers = {
    'Cookie' : 'sessionid=2bkhkftt1c3lwz5dqnsh5sftuvy5ytjd;csrftoken=PkcCn7PWbK9cAVAMnGYxwYmIrxKqYdqy',
}

s = requests.Session()
s.headers.update(headers)
html = s.post(login_url,data = data).text
for x in range(1,31):
    data = {
        'username':username,
        'password':x,
        'csrfmiddlewaretoken':'PkcCn7PWbK9cAVAMnGYxwYmIrxKqYdqy',
    }

    html = s.post(login_url,data = data).text
    print('...')
    if not '错误' in html:
        print('password', x)
        break
