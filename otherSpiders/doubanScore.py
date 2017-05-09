import re
import urllib
L=[]
for i in range(0,7):
    url='http://movie.douban.com/top250?start=%s'%(i*25)
    page=urllib.urlopen(url)
    html=page.read()
    reg=r'<span class="rating_num" property="v:average">([\d]+.[\d]+)'
    htmlre=re.compile(reg)
    htmllist=re.findall(htmlre,html)
    L.extend(htmllist)
sum=0
M=L[:166]
for i in M:
    sum=sum + float(i)

print sum

