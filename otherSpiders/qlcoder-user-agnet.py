#!/usr/bin/env python3
#coding=utf-8

import requests

url = 'http://www.qlcoder.com/train/secret'
headers = {'user-agent':'qlcoder spider'}
r = requests.get(url, headers=headers)
print(r.text)
