#!/usr/bin/env python
#coding=utf-8

import hackhttp
import re

url_to_get_id = 'http://www.ichunqiu.com/qad/course/57477'

raw_to_get_id = """
GET /qad/course/57477 HTTP/1.1
Host: www.ichunqiu.com
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
DNT: 1
Referer: http://www.ichunqiu.com/qad/courses
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6
Cookie: danmuSet={"size":"1","position":"0","color":"#ffffff","opacity":"100","shieldFly":false,"shieldTop":false,"shieldBottom":false}; __jsluid=85a9ed8a785c5e63fdc6036b55faa35e; pgv_pvi=825744384; uid=NcjxYpxhOpDigcxhKujnkq4ieumR2NGs3; chkphone=acWxNpxhQpDiAchhNuSnEqyiQuDIO0O0O; Hm_lvt_9104989ce242a8e03049eaceca950328=1489560638,1490788543,1490879876,1491398751; Hm_lpvt_9104989ce242a8e03049eaceca950328=1491398751; __jsl_clearance=1491400728.298|0|BukO7HsBbqvR5OTf1ENA%2FTLqKEU%3D; browse=CFlZTxUYU0BeU1BCVQJTRFBZSkdeQF5YWVdFRVhRW0dTU1lPX0dLThQ; Hm_lvt_1a32f7c660491887db0960e9c314b022=1489560621,1490788511,1490879873,1491397123; Hm_lpvt_1a32f7c660491887db0960e9c314b022=1491400926; ci_session=c8897c059ed771b0d5e556beaf3429afc44928b4
Connection: close"""
hh = hackhttp.hackhttp()
code, head, html, redirect, log = hh.http(url=url_to_get_id,raw=raw_to_get_id)
print "test:",code

p3 = re.compile('<a href="//www.ichunqiu.com/qad/course/(\d*?)"')


course_id = p3.findall(html)

for i in course_id:
    url = 'http://www.ichunqiu.com/qad/course/'+i
    raw_body = """
GET /qad/course/"""+i+""" HTTP/1.1
Host: www.ichunqiu.com
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
DNT: 1
Referer: http://www.ichunqiu.com/qad/courses
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6
Cookie: danmuSet={"size":"1","position":"0","color":"#ffffff","opacity":"100","shieldFly":false,"shieldTop":false,"shieldBottom":false}; __jsluid=85a9ed8a785c5e63fdc6036b55faa35e; pgv_pvi=825744384; uid=NcjxYpxhOpDigcxhKujnkq4ieumR2NGs3; chkphone=acWxNpxhQpDiAchhNuSnEqyiQuDIO0O0O; Hm_lvt_9104989ce242a8e03049eaceca950328=1489560638,1490788543,1490879876,1491398751; Hm_lpvt_9104989ce242a8e03049eaceca950328=1491398751; __jsl_clearance=1491400728.298|0|BukO7HsBbqvR5OTf1ENA%2FTLqKEU%3D; browse=CFlZTxUYU0BeU1BCVQJTRFBZSkdeQF5YWVdFRVhRW0dTU1lPX0dLThQ; Hm_lvt_1a32f7c660491887db0960e9c314b022=1489560621,1490788511,1490879873,1491397123; Hm_lpvt_1a32f7c660491887db0960e9c314b022=1491400926; ci_session=c8897c059ed771b0d5e556beaf3429afc44928b4
Connection: close"""
    every_page = hackhttp.hackhttp()
    code, head, html, redirect, log = every_page.http(url=url,raw=raw_body)
    #print code
    p1 = re.compile("var vid = '(\d*)';")
    v_id = p1.findall(html)

    raw_record = """POST /qad/course/recordVideoPlay HTTP/1.1
Host: www.ichunqiu.com
Content-Length: 82
Accept: */*
Origin: http://www.ichunqiu.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
DNT: 1
Referer: http://www.ichunqiu.com/qad/course/57615
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6
Cookie: danmuSet={"size":"1","position":"0","color":"#ffffff","opacity":"100","shieldFly":false,"shieldTop":false,"shieldBottom":false}; __jsluid=85a9ed8a785c5e63fdc6036b55faa35e; pgv_pvi=825744384; uid=NcjxYpxhOpDigcxhKujnkq4ieumR2NGs3; chkphone=acWxNpxhQpDiAchhNuSnEqyiQuDIO0O0O; Hm_lvt_9104989ce242a8e03049eaceca950328=1489560638,1490788543,1490879876,1491398751; Hm_lpvt_9104989ce242a8e03049eaceca950328=1491398751; __jsl_clearance=1491400728.298|0|BukO7HsBbqvR5OTf1ENA%2FTLqKEU%3D; browse=CFlZTxUYU0BeVVlAVQJTRFBZSkdeQF5YWVdFRVhRW0dTU1tPWkdLThQ; Hm_lvt_1a32f7c660491887db0960e9c314b022=1489560621,1490788511,1490879873,1491397123; Hm_lpvt_1a32f7c660491887db0960e9c314b022=1491401031; ci_session=c8897c059ed771b0d5e556beaf3429afc44928b4
Connection: close

courseID="""+i+"""&videoID="""+v_id[0]+"""&duration=8000.766&careerID=1&viewPoint=8000.0743189213995"""

    record_post = hackhttp.hackhttp()
    code, head, html, redirect, log = record_post.http(url='http://www.ichunqiu.com/qad/course/recordVideoPlay',raw=raw_record)
    #print head
    #print code
    print "courseID:%s  videoID:%s  status_code:%d" % (i,str(v_id),code)
