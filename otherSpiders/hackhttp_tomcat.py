#!/usr/bin/env python
#coding=utf-8
# 这个cnvd网站可能做过防爬或者是防DDoS处理，我如果短时间多次访问，即使带着
# 完整的HTTP信息，也会被发现，之后要么连接不上，要么返回一个完全为空的html
# 页面。等上几分钟再尝试就不会这样了。 神奇的网站。
import hackhttp
from bs4 import BeautifulSoup as BS
import re

url = 'http://www.cnvd.org.cn/flaw/list.htm?flag=true'
raw_body = """
POST /flaw/list.htm?flag=true HTTP/1.1
Host: www.cnvd.org.cn
Proxy-Connection: keep-alive
Content-Length: 417
Cache-Control: max-age=0
Origin: http://www.cnvd.org.cn
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
DNT: 1
Referer: http://www.cnvd.org.cn/flaw/list.htm?flag=true
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6
Cookie: __jsluid=19101cd0fa1a236cd24c29c2f03e4e91; bdshare_firstime=1490102749701; JSESSIONID=12B44D82C073DBFD5B8CB47DF5852044

number=%E8%AF%B7%E8%BE%93%E5%85%A5%E7%B2%BE%E7%A1%AE%E7%BC%96%E5%8F%B7&startDate=&endDate=&manufacturerId=-1&threadIdStr=&causeIdStr=&referenceScope=-1&order=&baseinfoBeanbeginTime=&max=20&baseinfoBeanFlag=0&condition=1&keyword=tomcat&categoryId=-1&keywordFlag=0&refenceInfo=&cnvdId=&field=&cnvdIdFlag=0&flag=%5BLjava.lang.String%3B%4018c08288&serverityIdStr=&editionId=-1&baseinfoBeanendTime=&positionIdStr=&offset="""

def cnvd_tomcat(raw_body):
    for i in range(0,141,20):
        raw = raw_body + str(i)
        hh = hackhttp.hackhttp()
        # status_code, response_head, html, 302etc, log
        code, head, html, redirect, log = hh.http(url=url,raw=raw)
        print(code)
        soup = BS(html,'lxml')
        html_tomcat = soup.tbody
        #print html_tomcat
        title_tomcat = BS(str(html_tomcat),'lxml')
        tomcat = title_tomcat.find_all(name='a',attrs={'href':re.compile('/flaw/show/CNVD.*?')})
        for name in tomcat:
            print name['title']


cnvd_tomcat(raw_body)
